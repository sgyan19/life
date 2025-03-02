import input
import pickle
import log
 
class Context:
    eraYears = 99
    years = 0
    parentIndex = 1
    lifeIndex = 1
    parents = []
    children = []
    populationLimit = 10000
 
ctx = Context()
 
class Life:
    parent = None
    version = 0
    origin = '1'
    age = 1
    childrenCount = 0
    code = ''
    def __init__(self, p, v, o, c):
        self.parent = p
        self.version = v
        self.origin = o
        self.code = c
    def partite(self):
        globals = {}
        self.age = self.age + 1
        local_vars = {'s': self.code}
        exec(self.code, globals, local_vars)
        global ctx
        if self.version == 0:
            ctx.parentIndex = ctx.parentIndex + 1
            version = ctx.parentIndex
 
        ctx.lifeIndex = ctx.lifeIndex + 1
        return Life(0, self, self.origin +'-'+ str(self.version), local_vars['result'])
    def __str__(self):
        return '[version={},origin={}]'.format(self.version, self.origin)
 
    def detail(self):
        return '[version={},origin={},age={},childrenCount={},fertility={}\n{}]'.format(self.version, self.origin, self.age, self.childrenCount, self.fertility(), self.code)
    
    def fertility(self):
        return self.childrenCount / self.age
 
 
def dump():
    printOverview()
    pickle.dump(ctx, open('ctx.pkl','wb'))
def load():
    try:
        global ctx
        ctx = pickle.load(open('ctx.pkl','rb'))
        return True
    except Exception as e:
        print('load failed', e)
    return False
 
 
def partite():
    for p in ctx.parents:
        ctx.children.append(p.partite())
    nl = ctx.children.copy()
    newParent = False
    for c in nl:
        try:
            newChild = c.partite()
            newChild.childrenCount = newChild.childrenCount + 1
            ctx.children.append(newChild)
            ctx.parents.append(c)
            newParent = True
        except Exception as e:
             pass
        ctx.children.remove(c)
    return newParent

def parentCmp(a, b):
    return a.fertility() - b.fertility()

def survivalOfFittest():
    dep = len(ctx.parents) - ctx.populationLimit
    if dep > 0:
        log.warning('parents:{}, parentMaxLimit:{} do obsolete')
        oldParents = ctx.parents.sort(cmp = parentCmp)
        for i in range(0, dep):
            ctx.parents.remove(oldParents[i])
 
def printOverview():
    log.info('years:{} parents:{} children:{} parentIndex:{} lifeIndex:{}'.format(ctx.years, len(ctx.parents),
                                                                                  len(ctx.children), ctx.parentIndex,
                                                                                  ctx.lifeIndex))
def printOverviewCtx(ctx):
    log.info('years:{} parents:{} children:{} parentIndex:{} lifeIndex:{}'.format(ctx.loopIndex, len(ctx.parent),
                                                                                  len(ctx.children), ctx.parentIndex,
                                                                                  ctx.lifeIndex))
 
 
if not load() or len(ctx.parents) == 0 :
     originalLife = Life(1, None, '1', open('life.py', 'r').read())
     ctx.parents.append(originalLife)

log.info('Evolution start')
while(True):
    r = input.input_with_timeout("3秒内输入命令，g=继续，q=停止，p=暂停(默认 g):", 'g', 3)
    if r == 'q':
        break
    elif r == 'p':
        r2 = 'p'
        while r2 != 'g':
            r2 = input.input_with_timeout('''输入命令(默认 p)
                                          g=恢复
                                          o=打印概览
                                          p=暂停
                                          parent=打印父节点
                                          children=打印子节点
                                          era=修改纪元年数
                                          limit=种群上限
                                          :''', 'p', 200)
            if r2 == 'o':
                printOverview()
            elif r2 == 'parent':
                r3 = input.input_with_timeout('5秒内输入父节点索引，0～{}:'.format(len(ctx.parents) - 1), 'p', 5)
                log.info(ctx.parents[int(r3)].detail())
                r2 = 'p'
            elif r2 == 'children':
                r3 = input.input_with_timeout('5秒内输入父节点索引，0～{}:'.format(len(ctx.children) - 1), 'p', 5)
                log.info(ctx.children[int(r3)].detail())
                r2 = 'p'
            elif r2 == 'era':
                r3 = input.input_with_timeout('5秒内输入新的循环次数，现值{}:'.format(ctx.eraYears), 'p', 5)
                ctx.eraYears = int(r3)
                r2 = 'p'
            elif r2 == 'limit':
                r3 = input.input_with_timeout('5秒内输入新的种群上限，现值{}:'.format(ctx.populationLimit), 'p', 5)
                ctx.populationLimit = int(r3)
                r2 = 'p'
            else:
                 pass
    else:
        pass
    for i in range(0, ctx.eraYears):
        if partite():
            dump()
            log.info("新生命诞生! 已经保存")
    printOverview()
    ctx.lifeIndex = 0
    ctx.years = ctx.years + 1
dump()
log.info('Evolution stopped')