# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

num = int(input("Введите число: "))
i = 1
sum = 0
ls = list()
while i <= num:
    if i == 0:
        continue
    help = (1+1/i)**i
    ls.append(help)
    sum = sum + (1+1/i)**i
    i += 1
print (sum)