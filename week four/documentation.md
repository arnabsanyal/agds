# Code Documentation

###### Please <span style="color:red"> _ABIDE BY_ </span> [coursera honor code](https://learner.coursera.help/hc/en-us/articles/209818863-Coursera-Honor-Code "coursera honor code") if you are currently taking a coursera course

* I have used the python library ProgressBar in this code implementation. You can comment out the ProgressBar parts of the code, if it suits you better. I used the library only to estimate progress as individual parts of this code can take up some time to fully execute owing to the huge size of the data-set.

* Reading a file that has a million numbers and inserting all of them in a dictionary is the first order of things to be done and is exactly what happens in code as well.
```python
for element in lines:
	element = int(element)
	if not dictionary.has_key(element):
		dictionary[element] = True
```

* Now we procure the huge number of keys and sort them
```python
hashed = dictionary.keys()
hashed.sort()
```
* The idea behind this being that every time I search only half the keys, as a match if exists will definitely exist in the other half, making the extra work redundant in searching through all keys.
```python
for t in targetRange:
	for k in range((len(hashed) / 2) + 1):
		if (t - hashed[k]) in dictionary:
			NumberofSolutions = 1 + NumberofSolutions
			break
	barProgress = 1 + barProgress
	bar.update(barProgress)
```

* If a hit is found then we mark that target as viable and increment the counter by one.