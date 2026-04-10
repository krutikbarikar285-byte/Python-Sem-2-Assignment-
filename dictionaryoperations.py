student = {"Name": "Aarav", "Age": 18, "City": "Delhi"}

print("Original Dictionary:", student)

# Update values
student["Age"] = 22
student["City"] = "Pune"

print("After Update:", student)

# Dictionary info
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Length:", len(student))

# Remove a key
student.pop("City")
print("After Removing City:", student)