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


def problem8():
    str_num = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    idx = 0
    str_len = len(str_num)
    prods = []

    while idx + 13 < str_len:
        str_slice = str_num[idx:idx + 13]
        curr_prod = reduce(lambda a, b: a * b, [int(x) for x in str_slice])
        prods.append(curr_prod)
        idx += 1

    print "Greatest prod is", max(prods)


problem8()
