# Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
# [1,2,3,4,22,234,24] ----> [22, 24]

def double_numers():
    numbers = list(map(int, input('Введите последовательность целых чисел через пробел:\n').split()))
    return ' '.join(map(str, filter(lambda i: 9 < abs(i) < 100, numbers)))

print(f'[{double_numers()}]')