def clone(s):
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 \r\n"
    l = len(s)
    r = []
    for num in range(0, l):
        import random
        a = random.randint(0, 99)
        if a in range(0,9):
            r.append(char[random.randint(0,len(char) - 1)])
            r.append(s[num])
        elif a in range(10, 14):
            r.append(char[random.randint(0,len(char) - 1)])
        elif a in range(15,18):
            pass
        else:
            r.append(s[num])
    return ''.join(r)
 
result = clone(s)
