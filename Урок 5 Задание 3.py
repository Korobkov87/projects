invest = int(input('Введите минималную сумму инвестиций '))
michail = int(input('Введите инвестиции Майкла '))
ivan = int(input('Введите инвестиции Ивана '))
if michail >= invest and ivan >= invest:
    print('2')
elif michail < invest and ivan >= invest:
    print('1')
elif michail >= invest and ivan < invest:
    print('1')
else:
    print('0')