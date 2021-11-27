def merge(*lists):
    new_line = [] # формируем новый список
    temporary_list = []

    for i in range(len(lists[0]) - 1, -1, -1):  # объединяем списки
        temporary_list = temporary_list + lists[0][i]

    while temporary_list:
        sort_num = min(temporary_list) # ищем минимальные значения в списке
        while sort_num in temporary_list: # добавляем минимальное значение в новый список
            new_line.append(sort_num)
            temporary_list.remove(sort_num)
            
    return new_line
