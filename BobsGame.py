#!/bin/python

import sys

q = int(raw_input().strip())
for a0 in xrange(q):
	n = int(raw_input().strip())
	board = []
	board_i = 0
	for board_i in xrange(n):
		board_t = [i for i in raw_input().strip()]
		board.append(board_t)
	# Write Your Code Here
	
