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
    # 내가 만든 오류를 확인하고 싶으면 __str__ 메서드를 작성해주어야 함.
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError() # 예외를 터트릴 수 있음.
    print(nick)

# 예외를 잡을 수 있음
# try:
#     say_nick("천사")
#     say_nick("바보")
# except MyError:
#     print("허용되지 않는 별명입니다.")

# as를 이용하여 어떤 오류인지 확인하고픈 경우에는 내가 만든 오류에 __str__ 메서드를 추가해줘야함.
try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)