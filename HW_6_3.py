# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def sum_numbers(numb):
    return sum(map(int, numb.replace('.','').replace('-','').replace(',','')))
    
numb = input('Введите вещественное число: ')
print(f'Сумма цифр числа = {sum_numbers(numb)}')
