import timeit
import random

"""Проанализировать скорость и сложность одного любого алгоритма из разработанных
в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему."""

"""Посчитать, сколько раз встречается определенная цифра в введенной
последовательности чисел. Количество вводимых чисел и цифра, которую
необходимо посчитать, задаются вводом с клавиатуры."""


def count_numbers(a, b):
    if a // b == 0:
        if a == b:
            return 1
        else:
            return 0
    if a % 10 == b:
        return 1 + count_numbers(a // 10, b)
    else:
        return count_numbers(a // 10, b)


def count_numbers_v2(a, b):
    counter = 0
    for i in str(a):
        if i == str(b):
            counter += 1
    return counter


def count_numbers_v3(a, b):
    counter = 0
    while a > 10:
        if a % 10 == b:
            counter += 1
        a = a // 10
    if a == b:
        counter += 1
    return counter


if __name__ == '__main__':
    n = 1_000_000
    while n != 1_000_000_000:
        sequence = random.randint(n ** 100, (n + n) ** 100)
        find_value = random.randint(1, 9)
        # print(timeit.timeit('count_numbers(sequence, find_value)',
        #       number=10000,
        #       globals=globals()))
        # 4.7858973
        # 6.1776559
        # 7.8821136
        # Достигла максимальной глубины рекурсии
        # print(timeit.timeit('count_numbers_v2(sequence, find_value)',
        #                     number=10000,
        #                     globals=globals()))
        # 0.9514739
        # 1.1330882
        # 1.3398004000000001
        print(timeit.timeit('count_numbers_v3(sequence, find_value)',
                            number=10000,
                            globals=globals()))
        # 1.9443685
        # 2.4268754999999995
        # 3.1367898999999992
        n *= 10

"""
n1 = 1 000 000
n2 = 10 000 000
n3 = 100 000 000
Каждое n дополнительно возводится в степень 100.
Рекурсивная функция оказалась самой длительной по времени выполнения.
К тому же, при некоторых n достигается максимальная глубина рекурсии и вызов функции завершается ошибкой.
Реализации с циклами for и while выполняются в разы быстрее, чем рекурсивная функция. 
Решение с циклом for является оптимальным, т.к. происходит только перебор значений, без каких-либо дополнительных
вычислений(в отличии от варианта с циклом while"""
