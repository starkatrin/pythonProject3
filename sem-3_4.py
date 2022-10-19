#Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Нельзя использовать готовые функции.
#*Пример:*
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

def dec_to_bin(num_dec):
    bin_list = []
    while num_dec != 0:
        num_bin = num_dec % 2
        num_dec = num_dec // 2
        bin_list.append(num_bin)
    bin_list = bin_list[::-1]
    return ''.join(str(elem) for elem in bin_list)

try:
    num_dec = int(input('Введите целое число: '))
except ValueError:
    num_dec = int(input('Нужно ввести целое число: '))
print(dec_to_bin(num_dec))