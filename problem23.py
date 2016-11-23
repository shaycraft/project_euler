import math


def get_divisors(n):
    divisors = []
    for i in range(1, int(math.floor(math.sqrt(n))) + 1):
        if n % i == 0:
            divisors.append(i)
            quotient = n / i
            if quotient != i and quotient != n:
                divisors.append(quotient)
    return divisors


def is_abundant(n):
    if math.fsum(get_divisors(n)) > n:
        return True
    else:
        return False


MAX_LIMIT = 28123
abundant_numbers = []
for i in range(1, MAX_LIMIT):
    if is_abundant(i):
        abundant_numbers.append(i)

# calculate all numbers which are sums of abundant numbers
abundant_sums = []
for i in abundant_numbers:
    for j in abundant_numbers:
        if i <= j:
            abundant_sums.append(i + j)

allnums = range(MAX_LIMIT + 1)
results = list(set(allnums) - set(abundant_sums))
print sum(results)
