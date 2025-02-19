# 10828 스택 직접 구현
# 구현은 됐는데 시간 초과 났음
# input() 써서 그런듯 sys.stdin.readline() 쓰니까 해결 됐음
def push(lst, num):
    lst.append(num)

def pop(lst):
    if len(lst) == 0:
        return print(-1)
    oldValue = lst[-1]
    del lst[-1]
    return print(oldValue)

def size(lst):
    return print(len(lst))

def empty(lst):
    return print(1) if len(lst) == 0 else print(0)

def top(lst):
    if len(lst) == 0:
        return print(-1)
    return print(lst[-1])

import sys
lst = []
a = int(sys.stdin.readline())

for _ in range(a):
    str = sys.stdin.readline().strip()
    if str.startswith('push'):
        num = int(str.split()[1])
        push(lst, num)
    if str == 'top':
        top(lst)
    if str == 'empty':
        empty(lst)
    if str == 'size':
        size(lst)
    if str == 'pop':
        pop(lst)