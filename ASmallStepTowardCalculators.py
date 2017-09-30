#!/bin/python

import sys

def solve(opr):
	a,sign,b = int(opr[0]), opr[1], int(opr[2])
	if sign == '-':
		return a - b
	else:
		return a + b
    # Complete this function

if __name__ == "__main__":
    opr = raw_input().strip()
    result = solve(opr)
    print(result)