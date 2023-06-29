# Определить индексы элементов массива (списка), значения
# которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше
#  заданного максимума)1.1

num_max = int(input())
num_min = int(input())

import random
list = [random.randint(1, 100) for _ in range(10)]
print(list)


print([ind for ind, val in enumerate(list) if num_min <= val <= num_max])


