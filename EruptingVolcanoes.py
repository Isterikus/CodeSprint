#!/bin/python

import sys

n = int(raw_input().strip())
m = int(raw_input().strip())
area = [[0 for i in range(n)] for j in range(n)]

def print_area():
	mx = max(area[0])
	for i in range(n):
		# print(area[i])
		temp = max(area[i])
		if temp > mx:
			mx = temp
	print(mx)

def add_val(i, j, w, h, val):
	# print('i =', i, 'j = ', j, ' | w = ', w, ' | h = ', h, 'val = ', val)
	for k in range(h):
		for l in range(w):
			if (k == 0 or k == h - 1) or (l == 0 or l == w - 1):
				if (i - k) >= 0 and (i - k) < n and (j + l) >= 0 and (j + l) < n:
					area[i - k][j + l] += val

def go_squares(i, j, val):
	w, h = 1, 1
	while (val > 0):
		add_val(i, j, w, h, val)
		i = i + 1
		j = j - 1
		w,h = w+2,h+2
		val -= 1

for a0 in xrange(m):
	x, y, w = raw_input().strip().split(' ')
	x, y, w = [int(x), int(y), int(w)]
	go_squares(x, y, w)

print_area()