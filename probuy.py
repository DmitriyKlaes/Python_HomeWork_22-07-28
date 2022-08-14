import csv

with open('telephones.csv', 'w', encoding='utf8',  newline='') as csvfile:
# with open('telephones.csv', 'w', encoding='utf8') as csvfile:
    fieldnames = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    writer_1 = csv.DictWriter(csvfile, fieldnames=fieldnames, restval='Нет', extrasaction='ignore')

    writer_1.writeheader()
    writer_1.writerow({'Фамилия': 'Бойков', 'Имя': 'Александр', 'dada': 'netnet'})
    writer_1.writerow({'Фамилия': 'Кругов', 'Имя': 'Дмитрий'})    
    writer_1.writerow({'Фамилия': 'Игнатьева', 'Имя': 'Олеся'})

with open('telephones.csv', encoding='utf8') as f:
    resder = csv.reader(f)
    for i in resder:
        if 'Бойков' in i:
            print('; '.join(i))
        
# with open('telephones.csv', encoding='utf8', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         row['Телефон'] = '895545121'
#         print(row['Фамилия'], row['Имя'], row['Телефон'])
#         print(row)

# with open('telephones.csv', encoding='utf8', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         row['Телефон'] = '895545121'
#         print(row['Фамилия'], row['Имя'], row['Телефон'])
#         print(row)
#         key = str.title(input('Введите имя для редактирования: '))
#         if key in row['Фамилия']:
#             print('DA')
#         else:
#             print('NO')        
            
# with open('telephones.csv', 'a', encoding='utf8') as f:
    
#     for data in f:
#         if '(отсутствует)' in data:
#             print(f'Заполните {data[0]}')

# with open("classmates.csv", encoding='utf-8') as r_file:
#     # Создаем объект reader, указываем символ-разделитель ","
#     file_reader = csv.reader(r_file, delimiter = ",")
#     # Счетчик для подсчета количества строк и вывода заголовков столбцов
#     count = 0
#     # Считывание данных из CSV файла
#     for row in file_reader:
#         if count == 0:
#             # Вывод строки, содержащей заголовки для столбцов
#             print(f'Файл содержит столбцы: {", ".join(row)}')
#         else:
#             # Вывод строк
#             print(f'    {row[0]} - {row[1]} и он родился в {row[2]} году.')
#         count += 1
#     print(f'Всего в файле {count} строк.')
    

# with open("classmates.csv", encoding='utf-8') as r_file:
#     # Создаем объект DictReader, указываем символ-разделитель ","
#     file_reader = csv.DictReader(r_file, delimiter = ",")
#     # Счетчик для подсчета количества строк и вывода заголовков столбцов
#     count = 0
#     # Считывание данных из CSV файла
#     for row in file_reader:
#         if count == 0:
#             # Вывод строки, содержащей заголовки для столбцов
#             print(f'Файл содержит столбцы: {", ".join(row)}')
#         # Вывод строк
#         print(f' {row["Имя"]} - {row["Успеваемость"]}', end='')
#         print(f' и он родился в {row["Год рождения"]} году.')
#         count += 1
#     print(f'Всего в файле {count + 1} строк.')