"""
 Дана последовательность: 1111<40 нулей>1111.

 1. Необходимо прогнать данную последовательность через стандартный скремблер и дескремблер.

 2. Придумать свой скремблер, который покажет лучшее значение, чем стандартный, с исходной последовательностью.

"""


def count(array: list) -> int:
    """
    Подсчитывает количество подряд идущих одинаковых битов.
    :param array: list - список битов двоичной последовательности после скремблинга
    :return: int
    """
    max_count = 1
    cur_count = 1
    for i in range(47):
        if array[i] == array[i + 1]:
            cur_count += 1
        else:
            if cur_count > max_count:
                max_count = cur_count
            cur_count = 1
    return max_count


def print_results(array1: list, array2: list, array3: list) -> None:
    """
    Выводит результаты работы скремблера и дескремблера.
    :param array1: list - список битов исходной двоичной последовательности
    :param array2: list - список битов двоичной последовательности после скремблинга
    :param array3: list - список битов двоичной последовательности после дескремблинга
    :return: None
    """
    print('Исходная последовательность:\t\n', ''.join(map(str, array1)))
    print('\nПоследовательность после скремблирования:\t\n', ''.join(map(str, array2)))
    print('\nПоследовательность после дескремблирования:\t\n', ''.join(map(str, array3)))
    print("\nМаксимальное количество подряд идущих одинаковых битов:", count(array2))


def standard(a: list, b: list, c: list) -> None:
    """
    Прогоняет исходную последовательность через стандартные скремблер и дескремблер.
    :param a: list - список битов исходной двоичной последовательности
    :param b: list - список для хранения битов двоичной последовательности после скремблинга
    :param c: list - список для хранения битов двоичной последовательности после дескремблинга
    :return: None
    """
    for i in range(48):  # скремблирование
        if i >= 5:
            b[i] = a[i] ^ b[i - 3] ^ b[i - 5]
        elif i >= 3:
            b[i] = a[i] ^ b[i - 3]
        else:
            b[i] = a[i]

    for i in range(48):  # дескремблирование
        if i >= 5:
            c[i] = b[i] ^ b[i - 3] ^ b[i - 5]
        elif i >= 3:
            c[i] = b[i] ^ b[i - 3]
        else:
            c[i] = b[i]

    print_results(a, b, c)


def new(a: list, b: list, c: list) -> None:
    """
    Прогоняет исходную последовательность через придуманные скремблер и дескремблер.
    :param a: list - список битов исходной двоичной последовательности
    :param b: list - список для хранения битов двоичной последовательности после скремблинга
    :param c: list - список для хранения битов двоичной последовательности после дескремблинга
    :return: None
    """
    for i in range(48):  # скремблирование
        if i >= 4:
            b[i] = a[i] ^ b[i - 1] ^ b[i - 3] ^ b[i - 4]
        elif i >= 3:
            b[i] = a[i] ^ b[i - 1] ^ b[i - 3]
        elif i >= 1:
            b[i] = a[i] ^ b[i - 1]
        else:
            b[i] = a[i]

    for i in range(48):  # дескремблирование
        if i >= 4:
            c[i] = b[i] ^ b[i - 1] ^ b[i - 3] ^ b[i - 4]
        elif i >= 3:
            c[i] = b[i] ^ b[i - 1] ^ b[i - 3]
        elif i >= 1:
            c[i] = b[i] ^ b[i - 1]
        else:
            c[i] = b[i]

    print_results(a, b, c)


initial = [1] * 4 + [0] * 40 + [1] * 4
encrypted, decrypted = [0] * 48, [0] * 48
new(initial, encrypted, decrypted)
