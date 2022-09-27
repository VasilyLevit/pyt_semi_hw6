# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# Пример: [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]
# Сделать с помощью функций ускоренной обработки

# def unique_num(list_in):
#         list_out = []
#         for i in list_in:
#                 if (list_in.count(i)) == 1:
#                         list_out.append(i)
#         return list_out

# list = [1, 1, 2, 3, 4, 5, 5]
# print(unique_num(list))

# Варианты преобразования списка
list_in = [1, 1, 2, 3, 4, 5, 5]
# list_in = list(map(int, list_in))
# если лист состоит из строковых переменных
# list_in = [int(i) for i in list_in if i.isdigit()]
# если хотим выделить числовые значени и перевести их в инт
# list_in = ['412', '+', '123', '*', '45']
# list_in = list(map(lambda x: int(x) if x.isdigit() else x, list_in))

# print(list_in)

# Вариант решения с помощью Comprehansion
out_lst2 = [i for i in list_in if list_in.count(i) == 1]


# Вариант решения с помощью filter
out_lst2 = list(filter(lambda x: list_in.count(x) == 1, list_in))
print(out_lst2)