# Creating a set
my_set = {5, 15, 'B', 'Car'}
print("Original Set:", my_set)

# Adding elements
my_set.add('Mango')
print("After add:", my_set)

my_set.update([100, 200])
print("After update:", my_set)

# Removing elements
my_set.remove('B')
print("After remove:", my_set)

my_set.discard(5)
print("After discard:", my_set)

# Set operations
set1 = {1, 3, 5}
set2 = {3, 5, 7}

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))