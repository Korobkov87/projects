num = int(input('Введите число '))
oper1 = (num % 100 // 10) ** (num % 10) # первая операция
oper2 = oper1 * (num % 1000 // 100) # вторая операция
oper3 = oper2 / ((num % 100000 // 10000) - num % 10000 // 1000) # третья операция
print(oper3)