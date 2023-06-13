# Даны два неупорядоченных набора
# целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания
# все те числа, которые встречаются в обоих наборах.
#1111
# Пользователь вводит 2 числа.
# n - кол-во элементов первого множества.1
# m - кол-во элементов второго множества.1
# Затем пользователь вводит сами элементы множеств.1



n, m = input().split()
first = [int(i) for i in input().split()]
second = [int(j) for j in input().split()]

print(*sorted(set(first).intersection(second)))

