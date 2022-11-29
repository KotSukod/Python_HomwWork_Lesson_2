# Реализуйте алгоритм перемешивания списка.
import random
ls = list(range(1,10))
print("Было")
print(ls, end = ' ')
for i in range(len(ls)):
    help = 0
    k = random.randint(1, (len(ls)-1))
    help = ls[k]
    ls[k] = ls[i]
    ls[i] = help
print()
print("Стало")
print(ls, end = ' ')

    