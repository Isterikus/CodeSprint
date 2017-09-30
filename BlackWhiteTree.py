#!/bin/python

import sys

n = int(input().strip())
c = list(map(int, input().strip().split(' ')))
main_tree = {i: {'col': c[i], 'conn': []} for i in range(n)}
rez = main_tree
diff = 0

for a0 in range(n-1):
	x, y = input().strip().split(' ')
	x, y = [int(x) - 1, int(y) - 1]
	# Write Your Code Here
	main_tree[x]['conn'].append(y)
	main_tree[y]['conn'].append(x)

def calc_diff(tree):
	black = 0
	white = 0
	for key in tree:
		if tree[key]['col'] == 1:
			black += 1
		else:
			white += 1
	return abs(white - black)

diff = calc_diff(main_tree)

def find_range(tree):
	rng = []
	for i in range(len(tree)):
		if len(tree[i]['conn']) == 1:
			rng.append(i)
	return rng

def find_close(tree):
	rng = find_range(tree)
	close = []
	for key in rng:
		if tree[key]['conn'][0] not in close:
			close.append(key)
	return close

def try_sub(tree, keys):
	global diff
	for i in range(2):
		tmp_tree = tree
		for key in keys:
			if tmp_tree[key]['col'] == i:
				del tmp_tree[key]
		tmp_diff = calc_diff(tmp_tree)
		print(tmp_tree)
		if tmp_diff > diff:
			diff = tmp_diff
			rez = tmp_tree

# def recursion(tree):
	# rng = find_range(tmp_tree)
	# for key in rng:

tmp_tree = main_tree
rng = find_range(tmp_tree)
# print(rng)
diff = calc_diff(main_tree)
try_sub(main_tree, rng)
print(diff)
print(len(rez))
print(rez)