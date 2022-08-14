from csv import DictWriter as dw
from correct_input import correct_value
from csv import DictReader as dr

        
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
        

with open('phonebook.csv', 'w', encoding='utf8',  newline='') as file:
    headers = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    print('\nСтандартные поля для заполнения:')
    print(', '.join(headers))
    choice = correct_value('\nЖелаете их изменить?\n1. Да\n2. Нет\nВыбор: ')
    if choice == '1':
        complite = change_headers(headers)
        while complite == '3':
            complite = change_headers(headers)
        if complite == '2':
            headers = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    print('\nСоздан телефонный справочник с полями: ')
    print(', '.join(headers))
    writer = dw(file, fieldnames=headers, restval='Нет')
    writer.writeheader()   
    
   
   
   
   
   
   
   
   
   
   
   
   
# with open('phonebook.csv', 'r', encoding='utf8',  newline='') as file:
#     reader = dr(file)
#     for n, row in enumerate(reader, 1):
#         print(n, '; '.join(list(row.values())))

