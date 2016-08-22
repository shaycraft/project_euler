import math

x = math.factorial(100)
dsum = 0
while x > 0:
    digit = x % 10
    dsum += digit
    x /= 10

print dsum

