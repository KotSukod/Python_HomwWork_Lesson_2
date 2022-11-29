# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = float(input("Введите число:"))
help = str(num)
result = 0
for i in help:
     a = list
     if i == '.' or i == ',':
          continue
     else:
          result = result + int(i)
print(result)
