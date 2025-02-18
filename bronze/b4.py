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

# 4299
a, b = map(int, input().split())
win = (a+b) // 2
lose = (a-b) // 2
print(-1 if win == lose else win,lose)