#!/bin/python

import sys

n = int(raw_input().strip())
d = raw_input().strip()
x, y = raw_input().strip().split(' ')
x, y = [int(x), int(y)]
# Write Your Code Here
area = [[0 for i in range(n)] for j in range(n)]
mx = pow(n, 2)

def go_to(i, j, val):
	if val > mx:
		return
	if d == 'e' or d == 'w':
		temp_j = j + 1 if (d == 'e') else j - 1
		if temp_j >= 0 and temp_j < n and not area[i][temp_j]:
			area[i][temp_j] = val
			go_to(i, temp_j, val + 1)
		elif i - 1 >= 0 and not area[i - 1][j]:
			area[i - 1][j] = val
			go_to(i - 1, j, val + 1)
		elif i + 1 < n and not area[i + 1][j]:
			area[i + 1][j] = val
			go_to(i + 1, j, val + 1)
		else:
			temp_j = j - 1 if (temp_j == j + 1) else j + 1
			if temp_j >= 0 and temp_j < n and not area[i][temp_j]:
				area[i][temp_j] = val
				go_to(i, temp_j, val + 1)
			else:
				return
		return
	else:
		temp_i = i + 1 if (d == 's') else i - 1
		if temp_i >= 0 and temp_i < n and not area[temp_i][j]:
			area[temp_i][j] = val
			go_to(temp_i, j, val + 1)
		elif j - 1 >= 0 and not area[i][j - 1]:
			area[i][j - 1] = val
			go_to(i, j - 1, val + 1)
		elif j + 1 < n and not area[i][j + 1]:
			area[i][j + 1] = val
			go_to(i, j + 1, val + 1)
		else:
			temp_i = i - 1 if (temp_i == i + 1) else i + 1
			if temp_i >= 0 and temp_i < n and not area[temp_i][j]:
				area[temp_i][j] = val
				go_to(temp_i, j, val + 1)
			else:
				return
		return
	return

def print_area():
	# print('---------------------------------')
	for i in range(n):
		for j in range(n):
			sys.stdout.write(str(area[i][j]) + ' ')
		sys.stdout.write('\n')
area[x][y] = 1
go_to(x, y, 2)
print_area()