# Code Documentation

###### Please <span style="color:red"> _ABIDE BY_ </span> [coursera honor code](https://learner.coursera.help/hc/en-us/articles/209818863-Coursera-Honor-Code "coursera honor code") if you are currently taking a coursera course

* I have used the python library ProgressBar in this code implementation. You can comment out the ProgressBar parts of the code, if it suits you better. I used the library only to estimate progress as individual parts of this code can take up some time to fully execute owing to the huge size of the data-set.

* Upto line 54, 
```python
print "\nData downloaded"
```
the program basically reads the graph data file and creates two adjacency lists - one forward and one reverse for the two passes of Kosaraju's algorithm

* The main body of the algorithm is implemented in between line 55 and 143. 
```python
sys.stdout.flush()
```
* The last few lines after that basically counts the various Strongly Connected Component's sizes, and prints out the top five after sorting those sizes in descending order.

* The size of the huge data-set ensured that I had to use my own DFS stack, instead of the recursion stack as I couldn't use a recursive implementation of DFS. Using recursive DFS on this huge data-set would surely make the program hit the recursion depth limit.

* The dummy data-set is a small graph data file that I used to test my code. Basically it is the same graph that Professor Roughgarden uses in his videos.

