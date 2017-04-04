#!/usr/bin/python

import sys
import math

def isPalindrome(n):
    string = str(n)
    return string == string[::-1]

def enumPalindromes(n, m):
    for i in range(n, m):
        if isPalindrome(i):
            yield i

def getSquare(n):
    if n == 0:
        return 0
    lg = (n.bit_length() + 1)//2
    x = 1 << lg
    while True:
        y = (x + n//x)//2
        if y >= x:
            break
        x = y
    return x


cases = 0
ranges = []
with open(sys.argv[1], 'r') as inputtxt:
    cases = int(inputtxt.readline())
    for line in inputtxt:
        string = line.split()
        ranges.append(string)

filename = sys.argv[1].split('.')[0] + '.out'
outputtxt = open(filename, 'w')
for i in range(cases):
    outputtxt.write("Case #" + str(i) + ': ')
    fairandsquare = 0
    lower = int(ranges[i][0])
    upper = int(ranges[i][1])
    print i
    n = getSquare(lower-1)+1
    m = getSquare(upper)
    print upper
    for j in enumPalindromes(n, m+1):
        if isPalindrome(j*j):
            fairandsquare += 1
    print i
    print str(fairandsquare)
    outputtxt.write(str(fairandsquare) + '\n')
outputtxt.close()