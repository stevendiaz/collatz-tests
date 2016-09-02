
# **** ACCEPTANCE TEST SPEC ****
# - The input will consist of a series of pairs of integers i and j,
# one pair of integers per line.
# - All integers will be less than 1,000,000 and greater than 0.
# - You should process all pairs of integers and for each pair determine the
#  maximum cycle length over all integers between and including i and j.
# - You can assume that no operation overflows a 32-bit integer.

import sys
import random
collatz_in = open('RunCollatz.in', 'w')
collatz_out = open('RunCollatz.out', 'w')
overflows_file = open('overflow', 'r')
overflow_numbers = []
upper_limit = 1000000
lower_limit = 0

def read_overflow_numbers():
    for line in overflows_file:
        overflow_numbers.append(int(line))

def collatz_solve(n):
    cycles = 1
    while(n > 1):
        if n % 2 == 0:
            n = n / 2
            cycles = cycles + 1
        else:
            n = (3 * n) + 1
            cycles = cycles + 1
    return cycles

def validate_range(i, j):
    result = (0,0)
    if(i < j):
        result = (i, j)
    elif(j > i):
        result = (j, i)

    for n in range(result[0], result[1]):
        if(n in overflow_numbers):
            print('### NUMBER IN RANGE WILL OVERFLOW ###')
    return result

def collatz_range(i, j):
    a = 0
    b = 0
    if(i < j):
        a = i
        b = j
    elif(j < i):
        a = j
        b = i
    for n in range(a, b + 1):
        if(n in overflow_numbers):
            return -1
    if(i == j):
        return collatz_solve(i)

    largest_cycle = 1
    for n in range(a, b + 1):
        cycle_length = collatz_solve(n)
        if(cycle_length > largest_cycle):
            largest_cycle = cycle_length
    return largest_cycle


def run():
    num_tests = input("Enter how many tests to generate: ")
    n = 0
    while(n < num_tests):
        i = random.randint(lower_limit, upper_limit)
        j = random.randint(lower_limit, upper_limit)
        res = collatz_range(i,j)
        if(res == -1):
            print('### TEST %d: NUMBER IN RANGE WILL OVERFLOW. Reattempting... ###' % n)
        elif(res is not None):
            collatz_in.write("%d %d\n" % (i, j))
            collatz_out.write("%d %d %d\n" % (i, j, res))
            n = n + 1


if __name__ == "__main__":
    read_overflow_numbers()
    run()
