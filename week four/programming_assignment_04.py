# Download the following text file: https://d18ky98rnyall9.cloudfront.net/_6ec67df2804ff4b58ab21c12edcb21f8_algo1-programming_prob-2sum.txt?Expires=1513900800&Signature=dCZ~Bg~BmPgk7te7Xqosb0pp1-reu3muySNlMMan1ok12yMgwyl8LNLhcP2uOruAzxVP5EI5dFGCQH6jmphPHSy5bNmqB04txxCdKQb~Bv32BbpFb7cIj2xwMWiAhWm9a4KPRqi9gV10HR4Rpy06~qLZQOVkgkqsHQH3hx9ksi0_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A

# The goal of this problem is to implement a variant of the 2-SUM algorithm covered in this week's lectures.

# The file contains 1 million integers, both positive and negative (there might be some repetitions!).This is your array of integers, with the ith row of the file specifying the ith entry of the array.

# Your task is to compute the number of target values t in the interval [-10000,10000] (inclusive) such that there are distinct numbers x,y in the input file that satisfy x+y=t. (NOTE: ensuring distinctness requires a one-line addition to the algorithm from lecture.)

# Write your numeric answer (an integer between 0 and 20001) in the space provided.

# OPTIONAL CHALLENGE: If this problem is too easy for you, try implementing your own hash table for it. For example, you could compare performance under the chaining and open addressing approaches to resolving collisions.

# @author: Hunter1706

#!/usr/bin/python

import progressbar

fileName = "_6ec67df2804ff4b58ab21c12edcb21f8_algo1-programming_prob-2sum.txt"
with open(fileName, "r") as inputFile:
	lines = inputFile.readlines()

dictionary = {}
print "Populating Hash Table"

for element in lines:
	element = int(element)
	if not dictionary.has_key(element):
		dictionary[element] = True

del lines

NumberofSolutions = 0
targetRange = [x - 10000 for x in range(0, 20001)]
hashed = dictionary.keys()
hashed.sort()
print "Counting number of 2-SUM Targets"
bar = progressbar.ProgressBar(maxval=len(targetRange), widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
barProgress = 0

for t in targetRange:
	for k in range((len(hashed) / 2) + 1):
		if (t - hashed[k]) in dictionary:
			NumberofSolutions = 1 + NumberofSolutions
			break
	barProgress = 1 + barProgress
	# print barProgress
	bar.update(barProgress)

bar.finish()
del bar
del dictionary

print "Total number of 2-SUM Targets is ", NumberofSolutions