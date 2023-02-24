# Вывод на экран одной строки с номером num_line
def view_entry(num_line):
    with open("db.csv", "r", encoding="UTF8") as file:
        count = 0
        for line in file:
            if count == num_line:
                print(f'Заметка №{num_line + 1}:\n{line}\n')
            count += 1
    del count


# Вывод на экран всех строк в базе
def view_entry_all():
    with open("db.csv", "r", encoding="UTF8") as file:
        # счетчик строк для вывода на экран
        count = 1
        # Выводим на экран все строки, построчно
        for line in file:
            print(f'Заметка №{count:4d}: {line}', end="")
            count += 1
    del count
