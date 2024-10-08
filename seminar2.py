##1. Напишите программу, которая получает целое число и возвращает его
##шестнадцатеричное строковое представление.
##Функцию hex используйте для проверки своего результата.

hex_number = '0123456789ABCDEF'

n = int(input())
number = ''

print('Функция hex: ', hex(n))


if n < 16:
    number = hex_number[n]
else:
    while n > 0:
        number = hex_number[n % 16] + number
        n = n // 16

print('Ваше число в 16-чной системе равно: ', number)

##2. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
##Программа должна возвращать сумму и произведение* дробей.
##Для проверки своего кода используйте модуль fractions

str1 = input()
str2 = input()


a, b = (int(num) for num in str1.split('/'))
c, d = (int(num) for num in str2.split('/'))

# сокращение дроби 
def gcd(a, b): 
    if b == 0: 
        return a 
    else: 
        return gcd(b, a % b) 

# сумма дробей
numerator_sum = a * d + b * c
denominator_sum = b * d
nod = gcd(numerator_sum, denominator_sum)
numerator_sum //= nod 
denominator_sum //= nod

# произведения дробей 
numerator_div = a * c 
denominator_div = b * d 

divisor = gcd(numerator_div, denominator_div) 
numerator_div //= divisor 
denominator_div //= divisor 

# вывод результата
print("Сумма дробей равно:", numerator_sum, "/", denominator_sum)
print("Произведение дробей равно:", numerator_div, "/", denominator_div)
