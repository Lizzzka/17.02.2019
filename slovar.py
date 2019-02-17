names = {}

for number in range(2):
    key = input('Введите имя:\n')
    value = input('\nВведите возраст\n')
    names[key]=value
print(names)
for name in names:
    if value>str(18):
        print('Старше 18: + name')
