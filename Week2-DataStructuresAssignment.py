#  empty list creation
my_list = []

# Append of elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting 15 at the second position
my_list.insert(1, 15)

# Extending the list with [50, 60, 70]
my_list.extend([50, 60, 70])

# Removing last element
my_list.pop()

# Sorting list in ascending order
my_list.sort()

# Finding and printing the index of value 30
index_of_30 = my_list.index(30)
print("Sorted List:", my_list)
print("Index of 30:", index_of_30)
