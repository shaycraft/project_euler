import math


def sum_divisors(n):
    divisors = []
    for i in range(1, int(math.floor(math.sqrt(n)))):
        if n % i == 0:
            divisors.append(i)
            quotient = n / i
            if quotient != i and quotient != n:
                divisors.append(quotient)
    return int(math.fsum(divisors))


asum = 0
testnums = []
for i in range(10000):
    a = sum_divisors(i)
    b = sum_divisors(a)
    if b == i and i != a:
        if not i in testnums:
            testnums.append(i)
        if not a in testnums:
            testnums.append(a)
print testnums
print math.fsum(testnums)
