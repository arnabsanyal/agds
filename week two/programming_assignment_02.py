# Download the following text file: https://d18ky98rnyall9.cloudfront.net/_dcf1d02570e57d23ab526b1e33ba6f12_dijkstraData.txt?Expires=1513814400&Signature=UZ-f57BP62qD1mOyOxh0cwvNAwbseb4gOrq9xa2ihCx08u9QkrSDbxLOH5qGkno5VFfdWwHjUgU5T1U4Wg2Z5ga36yBquj0xr073JAMLC1zLjISXu1DgSZ6Noim~niibpsEbhC62Vhh2sA9roSb6yTGxypnONZzhoGQbUK2QnfY_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A

# The file contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200. Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge. For example, the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6. The next entry of this row "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length 8200. The rest of the pairs of this row indicate the other vertices adjacent to vertex 6 and the lengths of the corresponding edges.

# Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source vertex, and to compute the shortest-path distances between 1 and every other vertex of the graph. If there is no path between a vertex v and vertex 1, we'll define the shortest-path distance between 1 and v to be 1000000.

# You should report the shortest-path distances to the following ten vertices, in order: 7,37,59,82,99,115,133,165,188,197. You should encode the distances as a comma-separated string of integers. So if you find that all ten of these vertices except 115 are at distance 1000 away from vertex 1 and 115 is 2000 distance away, then your answer should be 1000,1000,1000,1000,1000,2000,1000,1000,1000,1000. Remember the order of reporting DOES MATTER, and the string should be in the same order in which the above ten vertices are given. The string should not contain any spaces. Please type your answer in the space provided.

# IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Dijkstra's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing the heap-based version. Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.

# @author: Hunter1706

#!/usr/bin/python

import sys
import progressbar

with open("_dcf1d02570e57d23ab526b1e33ba6f12_dijkstraData.txt", "r") as inF:
	lines = inF.readlines()

nodeNumber = len(lines)
bar = progressbar.ProgressBar(maxval=nodeNumber, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
print "\nProgress Status\n"
bar.start()

graphData = []
maxVal = 1000000
for singleLine in lines:
	singleLine = singleLine.split()
	d1 = {}
	for strTok in singleLine[1 : ]:
		strTok = strTok.split(",")
		d1[int(strTok[0])] = int(strTok[1])
	graphData.append(d1)
	del d1

shortestPath = nodeNumber * [maxVal]
unvisited = range(1, nodeNumber + 1)

shortestPath[0] = 0
currentNode = 0
unvisited.remove(1 + currentNode)

bar.update(1)

for x in range(1, nodeNumber):
	k1 = graphData[currentNode].keys()
	for y in range(len(graphData[currentNode])):
		shortestPath[k1[y] - 1] = min(shortestPath[k1[y] - 1], graphData[currentNode][k1[y]] + shortestPath[currentNode])
	currentNode = unvisited[0] - 1
	for allUnvisited in unvisited[1 : ]:
		currentNode = currentNode if (shortestPath[currentNode] < shortestPath[allUnvisited - 1]) else allUnvisited - 1
	unvisited.remove(1 + currentNode)
	bar.update(1 + x)

#print shortestPath
#print unvisited

bar.finish()

print "\nYour Output\n"
verticesOfInterest = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
sys.stdout.write(str(shortestPath[verticesOfInterest[0] - 1]))
for aVertex in verticesOfInterest[1 : ]:
	sys.stdout.write(',' + str(shortestPath[aVertex - 1]))
print "\n"