# Creating list
my_list = [5, 15, 25, 35]
print("Original List:", my_list)

# Accessing elements
print("First element:", my_list[0])
print("Sliced list:", my_list[:3])

# Modifying elements
my_list[0] = 50
print("After modification:", my_list)

# Adding elements
my_list.append(60)
print("After append:", my_list)

my_list.insert(2, 100)
print("After insert:", my_list)

# Removing elements
my_list.pop()
print("After pop:", my_list)

my_list.remove(15)
print("After remove:", my_list)