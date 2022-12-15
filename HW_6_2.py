# Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

list1 = [12,'sadf',5643]
list_w = []
list_d = []
list_w = list(filter(lambda x: type(x) == str, list1))
list_d = list(filter(lambda x: type(x) == int, list1))

print('Список букв из списка: ', list_w)
print('Список цифр из списка: ', list_d)