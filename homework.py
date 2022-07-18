# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def find_odd_indexes(arr):
    odd_i_elements = []
    for i in arr:
        if (arr.index(i) % 2 != 0):
            odd_i_elements.append(i)
    return odd_i_elements


numbers = [2, 3, 4, 5, 6]
print(sum(find_odd_indexes(numbers)))

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.


def mult_list(arr):
    result = []
    i = 0
    while i < len(arr) / 2:
        result.append(arr[i] * arr[-i - 1])
        i += 1
    return result


numbers = [2, 3, 4, 5, 6]
print((mult_list(numbers)))

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


def float_min_max_diff(arr):
    min = 1.0
    max = 0.0
    for i in arr:
        if i - int(i) != 0:
            a = float('0.' + str(i).split('.')[1])
            if a < min:
                min = a
            if a > max:
                max = a
    return(max - min)


numbers = [1.1, 1.2, 3.1, 5, 10.01]
print((float_min_max_diff(numbers)))

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def dec_to_bin(number):
    bin = ''
    while number > 2:
        bin = str(number % 2) + bin
        number //= 2
    bin = str(number // 2) + str(number % 2) + bin
    return bin


n = int(input())
print(dec_to_bin(n))


# *5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fibonaci(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f


def add_nega(arr: list):
    nega = []
    for i in range(1, len(arr)):
        nega = [pow(-1, i + 1) * arr[i]] + nega
    return nega


n = int(input())
print(add_nega(fibonaci(n)) + (fibonaci(n)))