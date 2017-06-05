#!/usr/bin/python

import sys
import re

"""
input: argv[1]
first line: number of cases

- students enter either at beginning of queue (b) or end of queue (e)
- annoyance factor of student
"""

cases = 0
lunchlines = {}
numbers = re.compile('\d+(?:\.\d+)?')
with open(sys.argv[1], 'r') as inputtxt:
	cases = int(inputtxt.readline())
	for i in range(0, cases):
		lineup = inputtxt.readline().strip()
		annoyance = numbers.findall(inputtxt.readline())
		lunchlines[lineup] = annoyance

for key, value in lunchlines.items():
	q = []
	annoyfactor = 0
	for idx, c in enumerate(key):
		if c == 'b':
			for pos in q:
				annoyfactor += int(value[pos])
			q.insert(0, idx)
		elif c == 'e':
			q.append(idx)
	print(annoyfactor)
	
	""" todo: output to file, annoyfactor """
	""" important: change dictionary to list of tuples """