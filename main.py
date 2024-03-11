import random

print('Welcome to who pays the bill Game !')
names_list = input('Enter the names separated by comma : ')
names = names_list.split(',')
result = random.randint(0, len(names))
print(f'{names[result]} will pay the bill ')
