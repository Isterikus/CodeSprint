#!/bin/python

import sys

n = int(raw_input().strip())
d = raw_input().strip()
x, y = raw_input().strip().split(' ')
x, y = [int(y), int(x)]
# Write Your Code Here
area = [[0 for i in range(n)] for j in range(n)]

def get_way(corner, primary):
	i = 0 if (corner == 2 or corner == 3) else n - 1
	j = 0 if (corner < 3) else n - 1
	i_iterator = 1 if (corner == 2 or corner == 3) else -1
	j_iterator = 1 if (corner < 3) else -1
	val = 1
	if primary == 'i':
		while i < n and i >= 0:
			if val > 1:
				j = 0 if (j == -1) else n - 1
				j_iterator = -1 if (j_iterator == 1) else 1
			while j < n and j >= 0:
				area[i][j] = val
				val += 1
				j += j_iterator
			i += i_iterator
	else:
		while j < n and j >= 0:
			if val > 1:
				i = 0 if (i == -1) else n - 1
				i_iterator = -1 if (i_iterator == 1) else 1
			while i < n and i >= 0:
				area[i][j] = val
				val += 1
				i += i_iterator
			j += j_iterator

def print_area():
	# print('---------------------------------')
	for i in range(n):
		for j in range(n):
			sys.stdout.write(str(area[i][j]) + ' ')
		sys.stdout.write('\n')

def choose_way():
	# print('x = ', x, 'y = ', y)
	if x == 0:
		corner = 2 if (y == 0) else 1
	else:
		corner = 3 if (y == 0) else 4
	if d == 's' or d == 'n':
		primary = 'i'
	else:
		primary = 'j'
	if ((corner == 1 or corner == 4) and (d == 'n')) or ((corner == 2 or corner == 3) and (d == 's')):
		primary = 'j'
	if ((corner < 3) and (d == 'e')) or ((corner > 2) and (d == 'w')):
		primary = 'i'
	get_way(corner, primary)
	print_area()

choose_way()