# https://projecteuler.net
import helpers


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


def problem4():
    largest_pal = 0
    for i in range(1, 1000):
        for j in range(1, 1000):
            prod = i * j
            strProd = str(prod)
            if strProd == strProd[::-1]:
                if prod > largest_pal:
                    largest_pal = prod

    print "Largest palindrome is", largest_pal


def isDivisibleByAll(num, start, stop):
    for x in range(start, stop + 1):
        if num % x != 0:
            return False
    return True


def problem5():
    currNum = 20
    found = False
    while not found:
        if isDivisibleByAll(currNum, 1, 20):
            print "Found smallest of", currNum
            found = True
        currNum += 20


def problem6():
    sum_squares = 0
    sum_nums = 0
    for x in range(1, 101):
        sum_squares += x*x
        sum_nums += x

    diff = sum_nums * sum_nums - sum_squares
    print "Different is", diff


def problem7():
    num_found = 2
    is_found = False
    curr_num = 5

    while not is_found:
        if helpers.miller_rabin(curr_num, 20):
            num_found += 1
            if num_found == 10001:
                is_found = True
                print "Found 10,001st prime of", curr_num
        curr_num += 2


problem7()