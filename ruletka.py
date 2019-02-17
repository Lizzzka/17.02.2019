import random
print('В револьере одна пуля. Раскручиваем барабан...')
while True:
    slot = random.randint(1,6)
    if slot == 6:
        print('Игра окончена. Ты убит')
        break
    else:
        print('Поздравляю!Ты жив!')

