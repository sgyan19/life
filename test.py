import sys
import input
import pickle
 
originalCode = open('life.py', 'r').read()
globals = {}
local_vars = {'s' : originalCode}
 
source = '''
import math
import random
result = math.sqrt(16)
ran = random.randint(0, 999999999)
'''
 

 
 
exec(originalCode, globals, local_vars)
# print(globals)
print(local_vars['result'])
 
# value = timeoutInput.user_input("请输入内容（5秒内）: ", "默认值", 5)
# print(f"您输入的值是: {value}")
 
class Context:
    loopTimes = 99
    loopIndex = 0
    parentIndex = 1
    lifeIndex = 1
    parent = []
    children = []
 
    def __str__(self):
        return str(loopIndex)
 
def dump():
    pickle.dump(ctx, open('ctx.pkl','wb'))
 
def load():
    newCtx = pickle.load(open('ctx.pkl','rb'))
    print(str(newCtx.loopIndex))
 
load()