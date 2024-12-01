num1 = int(input("숫자 입력 :"))
num2 = int(input("숫자 입력 :"))

if num1 < num2:
    print(num2)
    print(" 이가 두 숫자 중 큰 숫자는 입니다.")
elif num1 == num2:
    print(num1, num2)
    print("모두 두 숫자는 동일합니다.")
else:
    print(num1)
    print(" 이가 두 숫자 중 큰 숫자는 입니다.")

num3 = int(input("숫자 입력 :"))

if num3%2 == 0:
    print(num3)
    print(" 는 짝수 입니다.")
else:
    print(num3)
    print(" 는 홀수 입니다.")

total = 0
for i in range(1, 11):
    total += i
print(total)

print(type(None))