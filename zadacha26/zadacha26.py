# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

a = int(input('Введите число: '))
b = int(input('Введите степень: '))

def degree_number(a, b):
    if b == 0:
        return 1
    else:
        return a * degree_number(a, b-1)

print(f'Число {a} в {b} степени равно: {degree_number(a, b)}')
