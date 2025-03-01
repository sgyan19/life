import sys
import select
 
def input_with_timeout(prompt, default, timeout):
    print(prompt, end='', flush=True)
    # 使用select来监视标准输入
    rlist, _, _ = select.select([sys.stdin], [], [], timeout)
    if rlist:
        # 如果用户输入了内容，读取并返回
        return sys.stdin.readline().strip()
    else:
        # 如果超时，返回默认值
        print() # 换行
        return default