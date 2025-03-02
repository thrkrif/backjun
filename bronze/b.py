# 10987 모음의 개수
# 1. set으로 중복을 제거시키고 다시 리스트로 만든다.
# 그 다음 count 이용
# 2. for문으로 전체 돌면서 모음이 있는 경우 count += 1 증가시킨다.
# str = input()
# count = 0
# for i in str:
#     if i in 'aeiou':
#         count += 1
# print(count)
# 집합이 어떤식으로 나오는지 확인해 봄
# voewls = set('aeiou')
# print(voewls) # {'i', 'a', 'o', 'e', 'u'}
# print(1 if 'i' in voewls else 0) # 1
# print(1 if 'd' in voewls else 0) # 0

# 4470 줄 번호 :  입력 값 맨 앞에 순서를 추가하여 출력
# a = int(input())
# for i in range(a):
#     str = input()
#     print(f'{i+1}. {str}')

# # 4299 억지로 만든 정답률 낮은 문제인듯 쓸모 없음. 얻을게 없음
# a, b = map(int, input().split())
# win = (a+b) // 2
# lose = (a-b) // 2
# print(-1 if win == lose else win,lose)

# 15873
# 공백 없는 두 수 더하기, 102 인 경우 10+2 로 한다. 한 숫자의 최댓값은 10이다.
# 이것도 틀렸다고 나왔는데 왜 틀린지 모르겠음
# str = input()
# result = 0
# if len(str) == 4:
#     result = 20
# if len(str) == 3:
#     result = 10 + int(str[2])
# if len(str) == 2:
#     result = int(str[0]) + int(str[1])
# print(result)

# 15726 세 수 중에 가장 큰 값과 가장 작은 값을 구한다.
# * 세 수의 순서를 변화시키면 안된다. 이래서 오답인듯 + 소수점 아래는 버린다
# a, b, c = map(int, input().split())
# a, c = max(a,b,c), min(a,b,c)
# print(a*b/c)

# 15726
# a, b, c = map(int, input().split())
# print(int(a * b / c) if a * b / c >= a / b * c else int(a / b * c))

# 13136
# CCTV 몇개 설치할 수 있는가
# a, b, c = map(int, input().split())
# import math
# print(math.ceil(a/c) * math.ceil(b/c))

# 2577 0~9 가 몇개 들어있는지 개수 세기
# a = int(input())
# b = int(input())
# c = int(input())
# result = str(a*b*c)
# for i in range(10):
#     print(result.count(str(i)))

# 1110
# while문을 쓰는게 나을듯?
# a = input()
# # a가 한 자릿수면 루프는 항상 1인듯? a = 1 이면, a = 10 = 1 + 0 = 1 (1), 0 + 1 = 1 (2), 1 + 1 = 11(3)
# loop = 1 if int(a) < 10 else 0
# result = ''
# while(a != result):
#     new = int(a[0]) +


# # 2750 수 정렬하기 : 오랜만에 sort 메서드 써 봄
# lst = []
# num = int(input())
# for _ in range(num):
#     lst.append(int(input()))
# lst.sort()
# for i in range(len(lst)):
#     print(lst[i])

# 10872 팩토리얼 : 재귀함수
# a = int(input())
# def factorial(num):
#     if num == 0:
#         return 1
#     return num * factorial(num-1)
# print(factorial(a))

# 10870 피보나치 수 : 수열 문제
# def pibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return pibo(n-1) + pibo(n-2)
# n = int(input())
# print(pibo(n))

# 15596 함수 구현
# def solve(a: list) -> int , 타입 힌트란?
#
# def solve(a: list) -> int

# 2292 벌집
# 첫번째는 1, 그 다음부터 6의 배수만큼 갯수 증가
# search = int(input())
# def solve(search):
#     distance = 1
#     start = 1
#     end = 1
#
#     while not(start <= search <= end):
#         start = end + 1
#         end = start + 6 * distance - 1
#         distance += 1
#
#     return distance
#
# print(solve(search))

# 2501 약수 구하기
# import sys
# a, b = map(int, sys.stdin.readline().split())
# lst = [i for i in range(1, a+1) if a % i == 0] # 약수들 담긴 리스트
# print(lst[b-1] if b-1 < len(lst) else 0)


# 5086 배수와 약수
# import sys
#
# while True:
#     a, b = map(int, sys.stdin.readline().split())
#
#     if a == 0 and b == 0:
#         break
#     if b % a == 0:
#         print('factor')
#     elif a % b == 0:
#         print('multiple')
#     else:
#         print('neither')

# 9506 약수들의 합
# import sys
#
# while True:
#     a = int(sys.stdin.readline())
#     lst = [i for i in range(1, a) if a % i == 0] # 약수 보관함.
#
#     if a == -1:
#         break
#
#     if a == sum(lst):
#         result = ' + '.join(map(str, lst))
#         print(f"{a} = {result}")
#     else:
#         print(f"{a} is NOT perfect.")

# 1978 소수 찾기
# 소수란? 1과 자기 자신만 약수로 가지는 수 -> 약수가 2개여야 한다.
# import sys
# n = int(sys.stdin.readline())
# lst = list(map(int, sys.stdin.readline().split()))
# result = []
# for i in lst:
#     count = 0
#     for j in range(1,i+1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         result.append(i)
# print(len(result))

# 2581 소수 : 실행 속도가 4.8초나 나옴.
# m = int(input())
# n = int(input())
# result = []
# for i in range(m, n+1):
#     count = 0
#     for j in range(1, i+1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         result.append(i)
#
# if len(result) == 0:
#     print(-1)
# else:
#     print(sum(result))
#     print(min(result))

# 2581 소수 문제는 제곱근을 사용하여 풀어라. 시간 복잡도가 제곱근 만큼 줄음.
# import sys
# import math
#
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(math.sqrt(num)) + 1):  # 제곱근까지만 확인
#         if num % i == 0:
#             return False
#     return True
#
# m = int(sys.stdin.readline())
# n = int(sys.stdin.readline())
#
# result = [i for i in range(m, n+1) if is_prime(i)]
#
# if not result:
#     print(-1)
# else:
#     print(sum(result))
#     print(min(result))

# 11653 소인수 분해 : 결과가 소수가 될 때 까지 계속 소수들로 나누는 거임.
# 지금 푼거 거의 다 맞았는데 마지막 수가 print가 안된다.
# import math
# a = int(input())
#
# # 소수 판별하는 함수
# def prime(x):
#     if x < 2:
#         return False
#     for i in range(2,int(math.sqrt(x)) + 1):
#         if x % i == 0:
#             return False
#     return True
# def prime_fac(x):
#
#     if prime(x):
#         print(int(x))
#     for i in range(2,int(math.sqrt(x)) + 1):
#         if x % i == 0:
#             print(i)
#             x = x / i
#             return prime_fac(x)
#
# prime_fac(a)

# 11653 더 나은 버전
# import math
#
# def prime_fac(x):
#     for i in range(2, int(math.sqrt(x)) + 1):
#         while x % i == 0:  # i로 나누어 떨어지면 계속 나눔
#             print(i)
#             x //= i  # 정수 나눗셈
#
#     if x > 1:  # 남아있는 값이 1보다 크면 소수임
#         print(x)
#
# a = int(input())
# prime_fac(a)

# 24263 알고리즘 수업 2
# for문을 한 번 돈다. O(n) 이므로 차수는 1차이다.
# n = int(input())
# print(n)
# print(1)

# 24264
# n = int(input())
# print(n**2)
# print(2)

# 24265
# n = int(input())
# print(n * (n-1) // 2)
# print(2)

# 24266
# n = int(input())
# print(n ** 3)
# print(3)

