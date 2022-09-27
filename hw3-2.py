# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример: - [2, 3, 4, 5, 6] => [12, 15, 16];  - [2, 3, 5, 6] => [12, 15]

input_list = [2, 3, 4, 5, 6]
# result = []
# len_list = len(input_list)
# for i in range(len_list - len_list // 2):
#     result.append(input_list[i] * input_list[-i-1])
# print(result)

result = []
len_list = len(input_list)
# result = [input_list[i] * input_list[-i-1] for i in range(len_list - len_list // 2)]
# print(result)
print(list(input_list[i] * input_list[-i-1] for i in range(len_list - len_list // 2)))