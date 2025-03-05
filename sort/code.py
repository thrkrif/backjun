# 2587
import sys
# lst = [int(input()) for i in range(5)]
# result = sorted(lst)
# print(sum(result)//5)
# print(result[2])

# 11650 좌표 정렬하기 1
# 이번엔 x좌표로 정렬 후 y좌표로 정렬이다.
# import sys
#
# a = int(input())
# lst = []
# for i in range(a):
#     lst.append(list(map(int, sys.stdin.readline().strip().split())))
#
# result = sorted(lst, key=lambda x: (x[0], x[1]))
# for x, y in result:
#     print(x, y)

# 11651 좌표 정렬하기 2
# 1. y좌표로 정렬, 2. y좌표가 같으면 x좌표로 정렬

# 기본적으로 2차원 배열에서 sort하면 x좌표로 정렬 된다.
# prc = [[3,1], [2,5], [7,8]]
# prc.sort()
# print(prc)

# lambda를 쓰면 y좌표로 정렬이 가능하다.
# import sys
#
# a = int(input())
# lst = []
# for i in range(a):
#     lst.append(list(map(int, sys.stdin.readline().strip().split())))
#
# result = sorted(lst, key=lambda x: (x[1], x[0]))
# for x, y in result:
#     print(x, y)


# 25305번 커트라인
# import sys
# a, b = map(int, sys.stdin.readline().strip().split())
# score = list(map(int, sys.stdin.readline().strip().split()))
#
# result = sorted(score, reverse=True)
# print(result[b-1])

# 문자열 정렬하기
# 1. 길이가 짧은 순 2. 길이가 같으면 사전 순
# 중복된 단어들은 제거 -> 집합 이용하면 될듯?
# import sys
# a = int(sys.stdin.readline().strip())
# myset = set(sys.stdin.readline().strip() for i in range(a)) # 중복된 단어들을 제거
# mylist = list(myset) # 리스트로 변환
# result = []
# for i in mylist:
#     min = len(i)
#     for j in (i+1, len(mylist) + 1):
#         if min > len(mylist[j]):
#           min = len(mylist[j])
#     result.append(i)
# print(result)

# 2751 수 정렬하기2 : 이게 왜 정답률 31퍼?
# import sys
# a = int(sys.stdin.readline().strip())
# lst = [int(sys.stdin.readline().strip()) for i in range(a)]
# result = sorted(lst)
# for i in result:
#     print(i)

# 10814 나이순 정렬 2개 다 맞음. 어차피 split()쓰면 리스트로 반환된다.
# import sys
# a = int(sys.stdin.readline().strip())
# lst = [list(map(str, sys.stdin.readline().strip().split())) for i in range(a)]
# result = sorted(lst, key=lambda x: int(x[0]))
# for x,y in result:
#     print(x,y)

# import sys
# a = int(sys.stdin.readline().strip())
# lst = [sys.stdin.readline().strip().split() for i in range(a)]
# result = sorted(lst, key=lambda x: int(x[0]))
# for x,y in result:
#     print(x,y)