"""
Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""

def calc_the_progression(n):
    if n == 1:
        return 1
    else:
        return n + calc_the_progression(n - 1)

try:
    x = int(input("Введите натуральное число: "))
except ValueError:
    print("Неверный символ")

func = x * (x + 1)/2
print("Разультаты равны") if func == calc_the_progression(x) else print("Результаты различаются")
