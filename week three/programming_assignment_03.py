# Download the following text file: https://d18ky98rnyall9.cloudfront.net/_6ec67df2804ff4b58ab21c12edcb21f8_Median.txt?Expires=1513900800&Signature=Wj6eGPh9a6m-qwCPCdKVuodRT9txqIT1s4awRhR0x3D~lLMEQmdQGKjPZBXGU5BHeiTydyxg6xkfEg2uxE9YSKBDGhIcl55vGA0ud8RmR4APlFXbJzQhdpd4bc--tuR9LNXeLOi4HP4LveqWkP8gWCLrVQQ410FkddkeF3vjPng_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A

# The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 3 lecture on heap applications). The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one. Letting xi denote the ith number of the file, the kth median mk is defined as the median of the numbers x1,…,xk. (So, if k is odd, then mk is ((k+1)/2)th smallest number among x1,…,xk; if k is even, then mk is the (k/2)th smallest number among x1,…,xk.)

# In the box below you should type the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). That is, you should compute (m1+m2+m3+⋯+m10000)mod10000.

# OPTIONAL EXERCISE: Compare the performance achieved by heap-based and search-tree-based implementations of the algorithm.

# @author: Hunter1706

#!/usr/bin/python

import bisect

fileName = "_6ec67df2804ff4b58ab21c12edcb21f8_Median.txt"
with open(fileName, "r") as fInput:
	lines = fInput.readlines()

incomingStream = [int(x) for x in lines]
medianList = []
ceiling = 10000
flag = True

medSum = incomingStream[0]
medianList.append(incomingStream[0])

def returnValidMedian():

	index = len(medianList)/2
	if flag:
		return medianList[index - 1]
	else:
		return medianList[index]

for x in range(2, 1 + ceiling):

	bisect.insort(medianList, incomingStream[x - 1])
	medSum = medSum + returnValidMedian()
	flag = not flag

print medSum % ceiling
