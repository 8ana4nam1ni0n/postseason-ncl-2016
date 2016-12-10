import re
import sys

dictionary = []

with open("dictionary.txt", "r") as d:
	dictionary = [x.strip('\n') for x in d.readlines()]

for d in dictionary:
	d.strip('\r')
	d.replace("a", "4", 1)
	d.replace("o", "0")
	d.replace('e', '3')
	print d
