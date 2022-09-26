# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

import random
n = 10
# input_list = []
# for i in range(0, n):
#     input_list.append(random.randint(0,10))
# print(input_list)
# summ = 0
# for i in input_list[1::2]:
#     summ += i
# print('Сумма: ', summ)

# Вариант 2
input_list = [random.randint(0,10) for i in range(0, n)]

print(input_list)
print('Сумма: ', sum(i for i in input_list[1::2]))