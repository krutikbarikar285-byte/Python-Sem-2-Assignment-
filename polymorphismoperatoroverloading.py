class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value
A = float(input("Enter first number: "))
B = float(input("Enter second number: "))
print("Addition is:", A+B)