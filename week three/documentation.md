# Code Documentation

###### Please <span style="color:red"> _ABIDE BY_ </span> [coursera honor code](https://learner.coursera.help/hc/en-us/articles/209818863-Coursera-Honor-Code "coursera honor code") if you are currently taking a coursera course

* I used a python library **Bisect** in this code implementation. Bisect has a function *insort* which makes coding the problem trivial. Initially I read off one number at a time from the file treating it as an input-stream. The *insort* functions inserts the incoming number at it's correct position.
```python
for x in range(2, 1 + ceiling):
	bisect.insort(medianList, incomingStream[x - 1])
	medSum = medSum + returnValidMedian()
	flag = not flag
```

* *flag* is toggled every time as it is a global variable that determines whether list has even or odd element and which element is returned as median by *returnValidMedian()* accordingly.
```python
def returnValidMedian():
	index = len(medianList)/2
	if flag:
		return medianList[index - 1]
	else:
		return medianList[index]
```

Rest is plain addition and modulus.