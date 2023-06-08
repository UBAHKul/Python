# ; Найдите сумму цифр трехзначного числа.

# ; *Пример:*

# ; 123 -> 6 (1 + 2 + 3)
# ; 100 -> 1 (1 + 0 + 0) |

n = int(input())
n_sum = 0

while n:
    n_sum += n % 10
    n //= 10

print(n_sum)

# while n:
#     n_sum += n % 10
#     n //= 10

# print(n_sum)