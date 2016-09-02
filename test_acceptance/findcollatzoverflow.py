# 2 147 483 647
import sys
file_object = open('overflow', 'w')
maxint = 2147483647


def findcollatz(max):
    itr = 0
    while(itr <= max):
        current_start = itr
        print('Testing %s ' % itr)
        result = collatz(itr, current_start)
        itr += 1

def collatz(i, orig):
    assert (i == orig)
    while(i > 1):
        if i % 2 == 0:
            i = i / 2
        else:
            i = 3*i + 1
            if(i > maxint):
                file_object.write('%d \n' % orig)
                return False
    return True

if __name__ == "__main__":
    findcollatz(1000000)
