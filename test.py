import csv
# with open('eggs.csv', 'r', newline='') as csvfile:
#      spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#      for row in spamreader:
#          print(row)
# Spam, Spam, Spam, Spam, Spam, Baked Beans
# Spam, Lovely Spam, Wonderful Spam

with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

# with open('names.csv', 'r', newline='') as csvfile:
#      reader = csv.DictReader(csvfile)
#      reader = csv.field_size_limit(10)
#      for row in reader:
#          print(row['first_name'], row['last_name'])
#          print(row)

# Eric Idle
# John Cleese

# print(row)
# {'first_name': 'John', 'last_name': 'Cleese'}

# with open('names.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
# #     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]

# with open('names.csv', 'w') as f:
#     writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
#     for row in data:
#         writer.writerow(row)
        
# with open('names.csv') as f:
#     print(f.read())