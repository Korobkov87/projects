# положительное чётное число    +
# положительное нечётное число  
# отрицательное чётное число    +
# отрицательное нечётное число
# нулевое число
num = int(input('Введите число '))
if num > 0 and num % 2 == 0: 
    print('Положительное чётное число')
elif num < 0 and num % 2 == 0:
    print('Отрицательное чётное число')
elif num > 0 and num % 2 != 0:
    print('Положительное нечётное число') 
elif num < 0 and num % 2 !=0:
    print('Отрицательное нечётное число')             
else:
    print('Нулевое число')