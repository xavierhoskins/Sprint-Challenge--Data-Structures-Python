import time
import sys
from binary_search_tree import BSTNode
sys.path.append('./binary_search_tree')

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Return the list of duplicates in this data structure
duplicates = []

# Replace the nested for loops below with your improvements
#Creates the new tree
new_BST = BSTNode(names_1[0])
for name_1 in names_1:
    #inserted tree to go through lists
    new_BST.insert(name_1)
    #runtime is: 0.14099597930908203 seconds
for name in names_2:
    if new_BST.contains(name):
            duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.