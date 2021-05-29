import timeit
import random
import cProfile

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
        sequence = random.randint(n ** 1000, (n + n) ** 1000)
        find_value = random.randint(1, 9)
        print(timeit.timeit('count_numbers(sequence, find_value)',
              number=10000,
              globals=globals()))
        cProfile.run('count_numbers(sequence, find_value)')
        # Достигла максимальной глубины рекурсии на первом вызове
        # print(timeit.timeit('count_numbers_v2(sequence, find_value)',
        #                     number=10000,
        #                     globals=globals()))
        # cProfile.run('count_numbers_v2(sequence, find_value)')
        # 15.7692046
        # 19.8396082
        # 25.006816
        # print(timeit.timeit('count_numbers_v3(sequence, find_value)',
        #                     number=10000,
        #                     globals=globals()))
        # cProfile.run('count_numbers_v3(sequence, find_value)')
        # 145.72374720000002
        # 197.0959995
        # 252.80085820000005
        n *= 10

"""
n1 = 1 000 000
n2 = 10 000 000
n3 = 100 000 000
Каждое n дополнительно возводится в степень 1000.
Рекурсивная функция оказалась самой длительной по времени выполнения, что видно уже на относительно небольших n.
К тому же, при некоторых n достигается максимальная глубина рекурсии и вызов функции завершается ошибкой.
Реализации с циклами for и while выполняются в разы быстрее, чем рекурсивная функция. 
Решение с циклом for является оптимальным, т.к. происходит только перебор значений, без каких-либо дополнительных
вычислений(в отличии от варианта с циклом while"""
