import sys
def isPrime(num):
    div = 2
    while num % div != 0:
        div += 1
    return div == num
print("Введите число")
number = input()
if not number.isdigit():
    sys.exit("Не число")
number = int(number)
flag = isPrime(number)
if (flag == True):
    print("Простое число")
else:
    print("Не простое число")