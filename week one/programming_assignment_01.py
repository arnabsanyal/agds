# Download the following text file: https://d18ky98rnyall9.cloudfront.net/_410e934e6553ac56409b2cb7096a44aa_SCC.txt?Expires=1513814400&Signature=D3e41CyQU1WBG5GF-NXqHvPOM6lGC~VD1zAPFbD1NG5pfBtZbezyjUF1FDt2lNAPKsyKYYe4-nz5X676k6syrSfwc6NQX7m41F8VMZxDzlS4isvb3Y4LBws4PMXHqDHlCJb6NF9lClzv~obS-GxWkGS9i4d56Pig1ZP88oncPHA_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A

# The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex). So for example, the 11th row looks liks : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646

# Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph.

# Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes, separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100" (without the quotes). If your algorithm finds less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your answer should be "400,300,100,0,0" (without the quotes). (Note also that your answer should not have any spaces in it.)

# WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may have to manage memory carefully. The best way to do this depends on your programming language and environment, and we strongly suggest that you exchange tips for doing this on the discussion forums.

# @author: Hunter1706

#!/usr/bin/python

import progressbar
import sys

fileName = "_410e934e6553ac56409b2cb7096a44aa_SCC.txt"
#fileName = "dummy.txt"

with open(fileName, 'r') as inFile:
	lines = inFile.readlines()

bar = progressbar.ProgressBar(maxval=len(lines), widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
barProgress = 0
numberOfNodes = 875714
#numberOfNodes = 9

forwardGraphData = {}
reverseGraphData = {}

print "Downloading Forward Edge-list and Reverse Edge-list"
bar.start()

for aLine in lines:
	aLine = aLine.split()
	aLine = [int(x) for x in aLine]
	if forwardGraphData.has_key(aLine[0]):
		forwardGraphData[aLine[0]].append(aLine[1])
	else:
		forwardGraphData[aLine[0]] = [aLine[1]]

	if reverseGraphData.has_key(aLine[1]):
		reverseGraphData[aLine[1]].append(aLine[0])
	else:
		reverseGraphData[aLine[1]] = [aLine[0]]

	barProgress = barProgress + 1
	bar.update(barProgress)

bar.finish()

del(bar)
print "\nData downloaded"

alreadyVisited = [False] * numberOfNodes
completionTimeList = [-1] * numberOfNodes
relabelList = [-1] * numberOfNodes
globalCompletionVar = 0;
DFS_stack = []

def DFS_Subroutine(SourceNode, isForward):

	global globalCompletionVar
	global DFS_stack
	flag = True
	if isForward:
		while len(DFS_stack):
			if forwardGraphData.has_key(SourceNode):
				for node in forwardGraphData[SourceNode]:
					if not alreadyVisited[node - 1]:
						alreadyVisited[node - 1] = True
						DFS_stack.append(node)
						SourceNode = node
						flag = False
						break

				if flag:
					completionTimeList[DFS_stack.pop() - 1] = globalCompletionVar
					if len(DFS_stack):
						SourceNode = DFS_stack[-1]
				else:
					flag = True

			else:
				completionTimeList[DFS_stack.pop() - 1] = globalCompletionVar
				if len(DFS_stack):
					SourceNode = DFS_stack[-1]

	else:
		while len(DFS_stack):
			if reverseGraphData.has_key(SourceNode):
				for node in reverseGraphData[SourceNode]:
					if not alreadyVisited[node - 1]:
						alreadyVisited[node - 1] = True
						DFS_stack.append(node)
						SourceNode = node
						flag = False
						break

				if flag:
					completionTimeList[DFS_stack.pop() - 1] = globalCompletionVar
					globalCompletionVar = 1 + globalCompletionVar
					if len(DFS_stack):
						SourceNode = DFS_stack[-1]
				else:
					flag = True

			else:
				completionTimeList[DFS_stack.pop() - 1] = globalCompletionVar
				globalCompletionVar = 1 + globalCompletionVar
				if len(DFS_stack):
					SourceNode = DFS_stack[-1]

for aNode in list(reversed(range(numberOfNodes))):
	if not alreadyVisited[aNode]:
		alreadyVisited[aNode] = True
		DFS_stack.append(1 + aNode)
		DFS_Subroutine(1 + aNode, False)

for var in range(numberOfNodes):
	relabelList[completionTimeList[var]] = var

sys.stdout.write("Finished Kosaraju's 1st pass (Blazingly Fast) ;)")
sys.stdout.flush()

alreadyVisited = [False] * numberOfNodes
globalCompletionVar = 0;
completionTimeList = [-1] * numberOfNodes
relabelList.reverse()

for aNode in relabelList:
	if not alreadyVisited[aNode]:
		alreadyVisited[aNode] = True
		DFS_stack.append(1 + aNode)
		DFS_Subroutine(1 + aNode, True)
		globalCompletionVar = 1 + globalCompletionVar

numberOfSCC = 1 + max(completionTimeList)

sys.stdout.write("\r")
sys.stdout.write("Finished Kosaraju's 2nd Pass (Bet you didn't even notice the previous update) :p\n")
sys.stdout.flush()
print "Counting Size of Strongly Connected Components"

bar = progressbar.ProgressBar(maxval=numberOfNodes, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
sccArray = [0] * numberOfSCC
bar.start()
barProgress = 0

for var in completionTimeList:
	sccArray[var] = 1 + sccArray[var]
	barProgress = 1 + barProgress
	bar.update(barProgress)

sccArray.sort()
sccArray.reverse()
bar.finish()
del(bar)

print "Finished sizing\nTop five SCC =>", sccArray[0 : 5]
