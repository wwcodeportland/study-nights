#!/usr/bin/python

import sys
import math

def isPalindrome(n):
    string = str(n)
    for i, char in enumerate(string):
        if char != string[-i-1]:
            return False
        return True

def isSquare(n):
    if math.sqrt(n) % 1 == 0:
        return True
    return False

def getSquare(n):
    return int(math.sqrt(n))

cases = 0
ranges = []
with open(sys.argv[1], 'r') as inputtxt:
    cases = int(inputtxt.readline())
    for line in inputtxt:
        string = line.split()
        ranges.append(string)

filename = sys.argv[1].split('.')[0] + '.out'
outputtxt = open(filename, 'w')
for i in range(0, cases):
    outputtxt.write("Case #" + str(i+1) + ': ')
    fairandsquare = 0
    for j in range(int(ranges[i][0]), int(ranges[i][1])+1):
        if isPalindrome(j) and isSquare(j):
            squareRoot = getSquare(j)
            if isPalindrome(squareRoot):
                fairandsquare += 1
    outputtxt.write(str(fairandsquare) + '\n')
outputtxt.close()