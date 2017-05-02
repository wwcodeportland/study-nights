#!/usr/bin/python

import sys
import re
import queue

"""
input: argv[1]
first line: number of cases

- skill of players
- max number of consecutive wins a player can have
- which game number to inspect
"""

cases = 0
tables = []
numbers = re.compile('\d+(?:\.\d+)?')
with open(sys.argv[1], 'r') as inputtxt:
	cases = int(inputtxt.readline())
	for i in range(0, cases):
		skills = numbers.findall(inputtxt.readline())
		maxwins = int(inputtxt.readline())
		gamenum = int(inputtxt.readline())
		tables.append((skills, maxwins, gamenum))

for table in tables:
	skills = table[0]
	maxwins = table[1]
	gamenum = table[2]
	q = queue.Queue()
	for skill in skills:
		q.put(int(skill))
	leader = 0
	challenger = 0
	wins = 0
	players = []
	for i in range(0, gamenum):
		challenger = q.get()
		if leader == 0:
			leader = q.get()
		players = [leader, challenger]
		if leader > challenger:
			q.put(challenger)
			challenger = 0
			wins += 1
			
			if wins == maxwins:
				q.put(leader)
				leader = 0
				wins = 0
		elif challenger > leader:
			q.put(leader)
			leader = challenger
			challenger = 0
			win = 1
	players.sort()
	print(players)

	""" todo: format output correctly [, ] -> {, } """
	""" for some reason, solution for case 3 is incorrect... """
