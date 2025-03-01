import input
import pickle
 
 
class Context:
    loopTimes = 99
    loopIndex = 0
    parentIndex = 1
    lifeIndex = 1
    parent = []
    children = []
 
ctx = Context()
 
class Life:
    version = 0
    origin = '1'
    childrenCount = 0
    code = ''
    def __init__(self, v, o, c):
        self.version = v
        self.origin = o
        self.code = c
    def partite(self):
        globals = {}
        local_vars = {'s': self.code}
        exec(self.code, globals, local_vars)
        global ctx
        if self.version == 0:
            ctx.parentIndex = ctx.parentIndex + 1
            version = ctx.parentIndex
 
        ctx.lifeIndex = ctx.lifeIndex + 1
        return Life(0, self.origin +'-'+ str(self.version), local_vars['result'])
    def __str__(self):
        return '[version={},origin={}]'.format(self.version, self.origin)
 
    def detail(self):
        return '[version={},origin={}\n{}]'.format(self.version, self.origin, self.code)
 
 
def dump():
    printOverview()
    pickle.dump(ctx, open('ctx.pkl','wb'))
def load():
    try:
        newctx = pickle.load(open('ctx.pkl','rb'))
        printOverviewCtx(newctx)
        return True
    except Exception as e:
        print('load failed')
    return False
 
 
def partite():
    for p in ctx.parent:
        ctx.children.append(p.partite())
    nl = ctx.children.copy()
    for c in nl:
        try:
            newChild = c.partite()
            ctx.children.append(newChild)
            ctx.parent.append(c)
        except Exception as e:
             pass
        ctx.children.remove(c)
 
 
def printOverview():
     print('loopIndex:{} parent:{} children:{} parentIndex:{} lifeIndex:{}'.format(ctx.loopIndex, len(ctx.parent),
                                                                                  len(ctx.children), ctx.parentIndex,
                                                                                  ctx.lifeIndex))
def printOverviewCtx(ctx):
     print('loopIndex:{} parent:{} children:{} parentIndex:{} lifeIndex:{}'.format(ctx.loopIndex, len(ctx.parent),
                                                                                  len(ctx.children), ctx.parentIndex,
                                                                                  ctx.lifeIndex))
 
 
if not load() or len(ctx.parent) == 0 :
     originalLife = Life(1, '1', open('life.py', 'r').read())
     ctx.parent.append(originalLife)
 
while(True):
    r = timeoutInput.input_with_timeout("3秒内输入命令，g=继续，q=停止，p=暂停:", 'g', 3)
    if r == 'q':
        break
    elif r == 'p':
        r2 = 'p'
        while r2 != 'g':
            r2 = input.input_with_timeout("输入命令，g=恢复,o=打印概览,parent=打印父节点，children=打印子节点，p=暂停, x=修改循环次数:", 'p', 20)
            if r2 == 'o':
                printOverview()
            elif r2 == 'parent':
                r3 = input.input_with_timeout('5秒内输入父节点索引，0～{}:'.format(len(ctx.parent) - 1), 'p', 5)
                print(ctx.parent[int(r3)].detail())
            elif r2 == 'children':
                r3 = input.input_with_timeout('5秒内输入父节点索引，0～{}:'.format(len(ctx.children) - 1), 'p', 5)
                print(ctx.children[int(r3)].detail())
            elif r2 == 'x':
                 r3 = input.input_with_timeout('5秒内输入新的循环次数，现值{}:'.format(ctx.loopTimes), 'p', 5)
                 ctx.loopTimes = int(r3)
            else:
                 pass
    else:
        pass
    for i in range(0, ctx.loopTimes):
        partite()
        printOverview()
    ctx.lifeIndex = 0
    ctx.loopIndex = ctx.loopIndex + 1
dump()