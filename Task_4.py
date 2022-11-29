# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.

n = int(input("Введите число: "))
ls = list()
ls1 = list()
result = 1
i = -n
while i <= n:
    ls.append(i)
    i += 1
index = str(input("Введите индексы через пробел: "))
for elements in index:
    if elements == " ":
        continue
    else:
        ls1.append(int(elements))
for k in ls1:
    result = result * ls[k]
print (result)
