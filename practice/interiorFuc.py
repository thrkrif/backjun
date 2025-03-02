# 파이썬 내장 함수
# 이전에 배운 모듈과 다르게 import로 불러올 필요 없이 바로 사용 가능하다.

# all : iterable한 인자를 받는다. 하나라도 거짓이면 거짓
# print(all([1, 2, 3]))
# print(all([1, 2, 3, 0]))  # 0은 False이다.

# any : all과 마찬가지로 반복 가능한 인자를 받는다. 하나라도 참이면 참
# print("any :",  any([1, 2, 3, 0]))


# print(ord('0'))

# divmod
# a = 1, # 튜플
# b = 1,2 # 튜플
# print(a)
# print(b)
# print(b[1])

# result = divmod(7,3)
# print(result[0]) # 몫
# print(result[1]) # 나머지

# dir() : ()안에 들어있는 객체의 변수나 메서드를 보여준다.
# print(dir([1,2])) # 리스트에 대한 메서드를 보여준다.

# filter의 반환값은 filter 참조값
# filter의 첫번째 인수 : 메서드, 두번째 인수: 반복가능한 객체
# 반복 가능한 객체의 요소 중 메서드에 참인 값들만 반환한다.
# def positive(x):
#     return x > 0
# print(list(filter(positive, [1,-2,3,-5,8])))
#
# print(positive(1))
# print(positive(-2))

# map의 매개변수는 filter와 같다. 첫번째 인수 : 메서드 , 두번째 인수: 반복 가능한 객체
# 두번째 인수의 요소들을 첫번째 인수인 메서드를 적용시켜 반환한다.
# def two_times(x):
#     return x ** 2
# print(list(map(two_times, [1,-2,3,-5,8])))


# print(list(filter(lambda x: x > 0, [1, -2, 3, -5])))
# print((lambda a,b: a+b)(4,5))

# enumerate , 첫번째 인자 : 인덱스, 두번째 인자: 반복 가능한 객체
# lst = [1,2,3,4,5]
# for i, value in enumerate(lst):
#     print(f'index: {i}, value: {value}')

# int() 사용하면 n진수를 10진수로 바꿀 수 있다.
# print(int('111',2))

# sort, sorted
# lst = [2,100,29,30,1,-5]
# sorted_list = sorted(lst) # 기존의 리스트를 유지하고 싶으면 sorted() 메서드를 이용할 것!
# print(sorted_list)
# # sorted_list2 = lst.sort() , (x) sort()는 반환값이 없다. 리스트 그 자체를 변경시킨다.
# lst.sort()
# print(lst)

