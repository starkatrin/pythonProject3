#Задача 1 Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#*Пример:*

#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

def make_list():
    array = [random.randint(0, 20) for _ in range(random.randrange(1, 10))]
    return array

def sum_of_elem(array):
    summa = 0
    for i in range(len(array)):
        if i % 2 != 0:
            summa = summa + array[i]
    return summa

array = make_list()
print(array)
print(sum_of_elem(array))







