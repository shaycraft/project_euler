# https://projecteuler.net


def problem1():
    total = 0
    for x in range(1, 1000):
        if (x % 3) == 0 or (x % 5 == 0):
            total += x
    print "Sum is", total


def problem2():
    fib = list({1, 2})

    total = + fib[1]
    isgood = True
    while isgood:
        currfib = fib[0] + fib[1]
        if currfib > 4e6:
            isgood = False
        else:
            if currfib % 2 == 0:
                total += currfib
            fib[0] = fib[1]
            fib[1] = currfib

    print "Sum is ", total


def isPalindrome(x, y):
    return str(x) + str(y) == str(y) + str(x)


def problem4():
    largest_pal = 0
    for i in range(1, 1000):
        for j in range(1, 1000):
            if isPalindrome(i, j):
                palnum = int(str(i) + str(j))
                if palnum > largest_pal:
                    largest_pal = palnum

    print "Largest palindrome is", largest_pal

problem4()
