import csv
from csv import DictWriter as dw
from csv import DictReader as dr
from correct_input import correct_value


def change_headers(headers):
    action = correct_value('\nВыберете действие:\n1. Добавить поле\n2. Удалить поле\nВыбор: ')
    print()
    print(', '.join(headers))
    length = len(headers) + 1
    if action == '2':
        length = len(headers)    
    position = correct_value(f'Введите номер позиции от 1 до {length}: ', length)
    if action == '1':
        headers.insert(int(position) - 1,(input('Введите название поля: ').capitalize()))
    else:
        headers.pop(int(position) - 1)
    print(f'\nРезультат:')
    print(', '.join(headers))
    complite = correct_value('\nСохранить изменения?\n1. Да\n2. Вернуть стандартные\n3. Изменить текущие\nВыбор: ', 3)
    return complite
        

with open('phonebook.csv', 'r+', encoding='utf8',  newline='') as file:
    headers = dr(file)
    writer = dw(file, fieldnames=headers.fieldnames, restval='Нет')
    next_row = {}
    print('Добавление новой записи')
    for field in headers.fieldnames:
        next_row[field] = input(f'{field}: ')
        
    writer.writerow(next_row)
        
    # writer.writerow({'Фамилия': 'Бойков', 'Имя': 'Александр', 'dada': 'netnet'})
    # writer_1.writerow({'Фамилия': 'Кругов', 'Имя': 'Дмитрий'})    
    # writer_1.writerow({'Фамилия': 'Игнатьева', 'Имя': 'Олеся'})