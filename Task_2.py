# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input("Введите число: "))

def f(x):
    result = 1
    for i in range(x + 1):
        if i == 0:
            continue
        result = result * i
        i += 1
    return result

for i in range(n + 1):
    if i == 0:
        continue
    print(f(i))