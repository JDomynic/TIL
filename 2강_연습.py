# 진법 변경 (10진수 -> n진수)
# print(bin(12))
# print(oct(12))
# print(hex(12))

# f-string
# bugs = 'roaches'
# counts = 13
# area = 'living room'
# print(f'Debugging {bugs} {counts} {area}')
# print(f'{bugs:^30}')


# # 불변과 가변
# # my_str = 'hello'
# # my_str[0] = 'z'

# my_list = [1, 2, 3]
# my_list[0] = 100
# print(my_list)

# 불변 타입
# x = 10
# y = x

# x = 20
# print(x)
# print(y)

# # 가변 타입
# list_1 = [1, 2, 3]
# list_2 = list_1

# list_1[0] = 100
# print(list_1) # [100, 2, 3]
# print(list_2) # [100, 2, 3] 같은 주소로 할당



## 실습
# decimal = 10
# # 1. 2진수로 출력해보세요
# print(bin(decimal)[2:])
# # 2. 8진수로 출력해보세요
# print(oct(decimal)[2:])
# # 3. 16진수로 출력해보세요
# print(hex(decimal)[2:])

# a = 3.2 - 3.1
# b = 1.2 - 1.1

# 부동 소수점 값을 출력 할 때 f-string 을 활용하여 부동소수점의 정확도를 제어 할 수 있습니다.
# print(f'{a:.1f}')
# print(f'{b:.1f}')

# print(314e-2)
# print(314 * 10 ** -2)

# greeting = 'hi'
# print(f'{greeting:<10}')
# print(f'{greeting:^10}')
# print(f'{greeting:>10}')

# * 중요 * 알고리즘 테스트는 무조건 Sequence 자료형
# im형 1개, a형 2개 3시간 안에 풀기

greeting = 'hello world' # 공백도 포함

# 1. 인덱싱 -> 알파벳 w를 출력해 보세요.
print(greeting[6])
# 2-1. 슬라이싱 -> hello를 출력해 보세요.
print(greeting[:5])
# 2-2. 슬라이싱 -> world를 출력해 보세요.
print(greeting[6:])
# 2-3. 슬라이싱 -> 거꾸로 출력해보세요. #  [start:end:step], step > 0 end -1까지, step < 0 end +1까지
print(greeting[::-1])
# 3. 내장함수를 사용해서 문자열의 길이를 출력해 보세요.
print(len(greeting))
# 4. for 문을 활용하여 hello world를 출력해 보세요.(2가지 방법)
for i in greeting:
    print(i, end = '')
print()    

for i in range(len(greeting)):
    print(greeting[i], end = '')