# 함수
# lambda는 return을 직접 입력하지 않아도 값을 돌려준다.

# add = lambda a, b: a + b
# cal1 = add(3,4)
# print(cal1)
# cal2 = add(5,10)
# print(cal2)


# 사용자 입출력
# name = input("문자를 입력하세요: ")
# print(name)

# 큰 따옴표 이용
# print("life" "is" "too short") # 문자열 중간에 +를 굳이 작성 안해도 된다.
# print('life' 'is' 'too short') # 문자열 중간에 +를 굳이 작성 안해도 된다. -> 작은 따옴표도 가능하네
# print(",이용하여 띄어쓰기 : life","is","too short") # , 가 있으면 띄어쓰기 해줌

# 한 줄에 결괏값 출력하기 매개변수 =end 이용
# for i in range(1,11):
#     print(i, end=' ') # 이렇게 사용하면 마지막 맨 끝에도 띄어쓰기가 되어있음. 유의하셈

# 클래스

# 사칙연산 클래스 만들어보기
# 클래스에서 self는 자신이 어떤 객체인지 알 수 있도록 하는 매개변수이다.
# self 말고 이름을 다르게 해도 상관은 없는데 관례적으로 self라고 쓰는게 형식상 보기 좋다.
# class FourCal:
#
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#
#     def add(self):
#         return self.first + self.second
#
#     def sub(self):
#         return self.first - self.second
#
#     def mul(self):
#         return self.first * self.second
#
#     def div(self):
#         return self.first / self.second
#
#
# # 아래 두가지 방식은 똑같은 방식임. 단 클래스명.메서드를 이용하면 어떤 객체인지 모르기 때문에 첫번째 인자를 반드시 등록해야함
# a = FourCal(7,2)
# # a.setdata(5, 2)
# print(a.div())
#
# # 이전 클래스에서는 setdata메서드를 호출 하지 않으면 계산기를 사용할 수 없었음.
# # 생성자란? 객체를 생성할 때 자동으로 객체 변수들을 초기화 해줌.
#
# # 상속
# class MoreFourCal(FourCal):
#     def pow(self):
#         return self.first ** self.second
#
# b = MoreFourCal(4,2)
# print(b.add())
# print(b.pow())

# import sys
# print(sys.path)

# 에외 처리
#
# try:
#     4 / 0
# except ZeroDivisionError as e:
#     print(e)

#  두 개 이상의 오류를 회피하고 싶다면 ()를 사용하면 된다.
# try:
#     a = [1,2]
#     print(a[2])
#     print(4/0)
# except (IndexError, ZeroDivisionError) as e:
#     print(e)

# 내가 예외를 직접 만들 수 있음 : Exception을 상속 받기
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError() # 예외를 터트릴 수 있음.
    print(nick)

# 예외를 잡을 수 있음
try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")

