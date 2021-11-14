def rot(num):
    str_num = str(num)  # перевод числа в строку для сравненения
    length = len(str_num)  # количество разрядов числа
    for i in range(0, length):
        if str_num[i] == '6':
            num = num - 6 * (10 ** (length - i - 1)) + 9 * (10 ** (length - i - 1))
            return num
    return num
