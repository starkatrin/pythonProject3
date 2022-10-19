#Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#*Пример:*
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

import random

def make_list():
    array = [random.randint(0, 20) for _ in range(random.randrange(1, 10))]
    return array

def middle_of_list(array):
    if len(array) % 2 == 0:
        n = int(len(array) / 2)
    else:
        n = int((len(array) + 1) / 2)
    return n

def list_sum(array, n):
    list_of_sum = []
    for i in range(n):
        summa = array[i] + array[-(i+1)]
        list_of_sum.append(summa)
    return list_of_sum

array = make_list()
n = middle_of_list(array)
print(array)
print(n)
print(list_sum(array, n))