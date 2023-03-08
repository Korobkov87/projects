# не разобрался как сделать только с if
s = input("Введите строку:")
count = 0
vowels = set("aeiou")
for letter in s:
    if letter in vowels: # подсмотрел в гугле
        count += 1
print("Количество гласных равно:")
print(count)