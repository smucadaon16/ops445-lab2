#!/usr/bin/env python3

# Author: Sheila Mae Cadaon
# Author ID: 152944229
# Date Created: 2025/02/01

import sys

if len(sys.argv) != 1:
	timer = int(sys.argv[1])
else:
	timer = 3

while timer != 0:
	print(timer)
	timer = timer - 1
print('blast off!')
