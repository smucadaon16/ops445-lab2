#!/usr/bin/env python3

import sys

if len(sys.argv) == 3:
	name = sys.argv[1]
	age = int(sys.argv[2])
	print('Hi ' + name + ', you are ' + str(age) + ' years old.')
if len(sys.argv) != 3:
	print('Usage: ' + sys.argv[0] + ' name age')
