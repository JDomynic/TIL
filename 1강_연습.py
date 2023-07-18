"""
a1 = 1
a2 = 2.3
a3 = 2 + 3j
a4 = "Hello World"
a5 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # 알고리즘문제에서 많이 사용
a6 = (1, 2, 3, 4)
a7 = {1, 2, 3}
a8 = {'one' : 1, 'two' : 2, 'three' : 3} # 웹에서 많이 사용
a9 = True
a10 = None
a11 = lambda x, y : x + y
a12 = range(10)
a13 = {"a1" : [1, 2, 3], "a2" : [4, 5, 6]}

for i in range(1, 14):
    var = f'a{i}'
    var = eval(var)
    print(type(var))"""
    

# print("7 / 3 : ", 7 / 3, "\n7 // 3 : ", 7 // 3, "\n7 % 3 : ", 7 % 3)


# print(-2 ** 4)
# print(-(2 ** 4))
# print((-2) ** 4)


# degrees = 36.5
# print(id(degrees))

# degrees = 37.5
# print(id(degrees))


# num = 10
# double = 2 * num
# print(double)

# num = 5
# print(double)

# name = "min"
# age = 33
# is_student = False
# SECOND = 60
# MAX_VALUE = 100
# PI = 3.14159

# person_name = "Alice"

# def calculate_sum(x, y):
#     return x + y


# def calculate_sub(x, y):
#     return x - y


## PEP8

# char = input()
# char = input("문자 한개를 입력하세요!!")

# num = int(input())

# char1, char2 = input().split()

# num1, num2 = map(int, input().split())


# year, month, day = map(int, input().split(','))
# print(f"{year}년 {month}월 {day}일")

name = input("이름 : ")
age = int(input("나이 : "))
height = float(input("키 : "))
# 1. 포맷 코드
# print("저의 이름은 %s, 나이는 %d, 키는 %.2f" %(name, age, height)) # 소숫점 2자리까지 반올림, 기본은 6자리

# 2. f-string
# print(f"저의 이름은 {name}, 나이는 {age}, 키는 {height:.2f}") # 기본이 적은만큼만 나온다 ### 이 방법을 많이 쓴다 !!!

# 3. .format()
print("저의 이름은 {}, 나이는 {}, 키는 {}".format(name, age, height))