# Задача 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +, -, /, *. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - добавить возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;

# Вариант (семинар)
string = '1 + 2 * 3'.split()
# переоводим числа в инт
for i in range(len(string)):
    if string[i].isdigit():
        string[i] = int(string[i])
# составляем словарь операций
op_1 = {'+': lambda x, y: x + y,
        '-': lambda x, y: x - y}
op_2 = {'*': lambda x, y: x * y,
        '/': lambda x, y: x / y}
index = 0
while ('*' in string) or ('/' in string):
    if string[index] in op_2:
        temp = op_2[string[index]](string[index-1], string[index+1]) 
        del string[index-1:index+2]
        string.insert(index-1,temp)
        index = 0
    else:
        index += 1

index = 0
while ('+' in string) or ('-' in string):
    if string[index] in op_1:
        temp = op_1[string[index]](string[index-1], string[index+1]) 
        del string[index-1:index+2]
        string.insert(index-1,temp)
        index = 0
    else:
        index += 1

print(string)
print(eval('1 + 2 * 3'))
