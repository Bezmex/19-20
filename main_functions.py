from array import array
from functions_for_work import *

def input_numbers_mas_for_compare(array1, array2):
    """
    Функция для ввода двух массивов чисел, для сравнения
    :param array1: Массив 1
    :param array2: Массив 2
    """
    print("\nВыберите опцию 1-2:\n"
          "1. Ввести массивы самостоятельно\n"
          "2. Сгенерировать массивы случайным образом\n")
    option = input()
    if is_int(option):
        option = int(option)

    option_handlers = {
        1: lambda: (input_array(), input_array()),
        2: lambda: (random_array(int(input("Введите количество цифр в случайном массиве 1: "))),
                    random_array(int(input("Введите количество цифр в случайном массиве 2: "))))
    }

    array1, array2 = option_handlers.get(option, lambda: ([], []))()

    if not array1 and not array2:
        print('error')

    print("\nПервый массив:", array1)
    print("Второй массив:", array2)
    return array1, array2

def count_same_numbers(array1, array2):
    """
    Алгоритм поиска одинаковых чисел в двух массивах
    :param array1: Массив 1
    :param array2: Массив 2
    """
    result = 0
    for i in array1:
        for j in array2:
            if i == j or str(i)[::-1] == str(j):
                result += 1
    print("\nАлгоритм выполнен\n")
    return result

def input_big_numbers_mas(array1, array2):
    """
    Функция для ввода двух массивов, представляющих большие числа
    :param array1: Массив 1
    :param array2: Массив 2
    """
    print("\nВыберите опцию 1-2:\n"
          "1. Ввести массивы самостоятельно\n"
          "2. Сгенерировать массивы \n")
    option = input()
    if is_int(option):
        option = int(option)

    option_handlers = {
        1: lambda: (input_large_number_for_arr(), input_large_number_for_arr()),
        2: lambda: (generate_random_number_for_arr(int(input("Введите количество цифр в случайном массиве: "))),
                    generate_random_number_for_arr(int(input("Введите количество цифр в случайном массиве: "))))
    }

    array1, array2 = option_handlers.get(option, lambda: ([], []))()

    if not array1 and not array2:
        print('error')

    print("Первый массив цифр:", array1)
    print("Второй массив цифр:", array2)
    return array1, array2

def sum_or_dif_of_array(array1, array2):
    """
    Алгоритм сложения/вычитания двух массивов, который возвращает полученное значение
    :param array1: Массив 1
    :param array2: Массив 2
    """
    print("\nВыберите находить сумму или разность массивов:\n"
          "1. Сумму\n"
          "2. Разность")
    operation_choice = input()
    if is_int(operation_choice):
        operation_choice = int(operation_choice)

    operation_handlers = {
        1: lambda: sum(number for number in array1) + sum(number for number in array2),
        2: lambda: sum(number for number in array1) - sum(number for number in array2)
    }

    result = operation_handlers.get(operation_choice, lambda: None)()

    if result is None:
        print("Ошибка выбора")

    print("\nАлгоритм выполнен\n")
    return result

def input_points_array(array1, array2):
    """
    Алгоритм задания значений массивов точек
    :param array1: Массив 1
    :param array2: Массив 2
    """
    print("\nВыберите опцию 1-2:\n"
          "1. Ввести массивы самостоятельно\n"
          "2. Сгенерировать массивы \n")
    option = input()
    if is_int(option):
        option = int(option)

    option_handlers = {
        1: lambda: (input_points(), input_points()),
        2: lambda: (generate_random_points(int(input("Введите количество цифр в случайном массиве: "))),
                    generate_random_points(int(input("Введите количество цифр в случайном массиве: "))))
    }

    array1, array2 = option_handlers.get(option, lambda: ([], []))()

    if not array1 and not array2:
        print('error')

    print("Первый массив цифр:", array1)
    print("Второй массив цифр:", array2)
    return array1, array2

def find_points_bigger_distance(array1, array2):
    """
    Алгоритм сравнения расстояний между точками с заданным числом
    :param array1: Массив 1
    :param array2: Массив 2
    """
    number_for_compare = int(input("Введите число для сравнения: "))
    points_array = []
    for point1, point2 in zip(array1, array2):
        if distance(point1, point2) > number_for_compare:
            points_array.append((point1, point2))
    print("\nАлгоритм выполнен\n")
    return points_array
