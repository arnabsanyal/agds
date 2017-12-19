# Code Documentation

###### Please <span style="color:red"> _ABIDE BY_ </span> [coursera honor code](https://learner.coursera.help/hc/en-us/articles/209818863-Coursera-Honor-Code "coursera honor code") if you are currently taking a coursera course

* I have used the python library ProgressBar in this code implementation. You can comment out the ProgressBar parts of the code, if it suits you better. I used the library only to estimate progress as individual parts of this code can take up some time to fully execute owing to the huge size of the data-set.

* This is a very straight-forward problem where we calculate the Dijkstra's shortest path algorithm to a graph with 200 nodes.I read the graph data from the file, as an adjacency list, into a python _list of dictionaries_ (in the first for loop).
```python
for singleLine in lines:
	singleLine = singleLine.split()
	d1 = {}
	for strTok in singleLine[1 : ]:
		strTok = strTok.split(",")
		d1[int(strTok[0])] = int(strTok[1])
	graphData.append(d1)
	del d1
``` 

* In the next for loop, I run Dijkstra's algorithm,
```python
for x in range(1, nodeNumber):
	k1 = graphData[currentNode].keys()
	for y in range(len(graphData[currentNode])):
		shortestPath[k1[y] - 1] = min(shortestPath[k1[y] - 1], graphData[currentNode][k1[y]] + shortestPath[currentNode])
	currentNode = unvisited[0] - 1
	for allUnvisited in unvisited[1 : ]:
		currentNode = currentNode if (shortestPath[currentNode] < shortestPath[allUnvisited - 1]) else allUnvisited - 1
	unvisited.remove(1 + currentNode)
	bar.update(1 + x)
```

* In the end, I print the final output - which is the shortest paths from the source node labeled as 1 to the ten nodes of interest given in the problem statement.