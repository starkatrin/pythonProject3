#Задача 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
#*Пример:*
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def make_list():
    array = [round(random.uniform(0, 20), 2) for _ in range(random.randrange(2, 10))]
    return array

def list_of_fractions(array):
    frac_list = [round(array[i]%1, 2) for i in range(len(array))]
    return frac_list

def max_min_sub(frac_list):
    min_frac = frac_list[0]
    max_frac = frac_list[0]
    for i in range(1, len(frac_list)):
        if frac_list[i] < min_frac:
            min_frac = frac_list[i]
        if frac_list[i] > max_frac:
            max_frac = frac_list[i]
    sub = max_frac - min_frac
    return round(sub, 2)

array = make_list()
print(array)
frac_list = list_of_fractions(array)
print(frac_list)
print(max_min_sub(frac_list))