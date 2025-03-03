# 2587
import sys
# lst = [int(input()) for i in range(5)]
# result = sorted(lst)
# print(sum(result)//5)
# print(result[2])

# 11651 좌표 정렬하기 2
# 1. y좌표로 정렬, 2. y좌표가 같으면 x좌표로 정렬

# 기본적으로 2차원 배열에서 sort하면 x좌표로 정렬 된다.
# prc = [[3,1], [2,5], [7,8]]
# prc.sort()
# print(prc)

# lambda를 쓰면 y좌표로 정렬이 가능하다.
import sys
a = int(input())
lst = []
for i in range(a):
    lst.append(list(map(int, sys.stdin.readline().strip().split())))

result = sorted(lst) # x좌표로 먼저 정렬시킨다.
result = sorted(result, key=lambda x: x[1]) # 그 이후 y 좌표로 정렬
