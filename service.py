import os

from viewer import view_entry


# Функция очистки экрана для терминала, должна работать на Win и на MAC
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Функция паузы для терминала, должна работать на Win и на MAC
def pause():
    os.system('pause' if os.name == 'nt' else 'read -s -n 1 -p "Для продолжения нажмите любую клавишу..."')


# Запись строки str_data в файл
def file_write(str_data):
    with open("db.csv", "a", encoding="UTF8") as fp:
        fp.writelines(str_data)
    fp.close()


# Определение количества строк в файле
def count_lines_file():
    with open("db.csv", "r", encoding="UTF8") as fp:
        len_file = len(fp.readlines())
        return len_file
    fp.close()


# Удаление строки с номером num_line из файла
def del_line_file(num_line):
    with open("db.csv", 'r') as fp:
        lines = fp.readlines()
    fp.close()

    with open("db.csv", 'w') as fp:
        for number, line in enumerate(lines):
            if number not in [num_line]:
                fp.write(line)
    fp.close()


# Изменение строки с номером num из файла
def edit_line_file(num):
    with open('db.csv', 'r', encoding="UTF8") as fp:
        lines = fp.readlines()
    # Для образца выводим строку до редактирования
    view_entry(num)
    fp.close()
    with open("db.csv", 'w', encoding="UTF8") as fp:
        count = 0
        for number, line in enumerate(lines):
            # Если строка не с нужным номером то записываем
            if number not in [num]:
                fp.write(line)
                count += 1
            # Если строка нужная
            else:
                view_entry(num)  # Для образца выводим строку до редактирования
                # то запрашиваем новые данные
                new_text = input('Введите новый текст для замены:\n')
                # и записываем их в файл
                fp.write(f'{new_text}\n')
                count += 1
        del count
    fp.close()
