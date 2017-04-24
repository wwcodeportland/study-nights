#!/usr/bin/python

import sys, os
import queue
import time

"""
input: argv[1]
first line: number of commands
following lines: commands to be issued
"""

tasks = 0
q = queue.Queue()
with open(sys.argv[1], 'r') as inputtxt:
	tasks = int(inputtxt.readline())
	for line in inputtxt:
		q.put(line.strip())

while not q.empty():
	print(q.get())
	time.sleep(5)