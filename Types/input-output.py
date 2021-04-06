variable1 = input("Please enter a value for variable1 >> ")

print("variable1 is currently:", variable1)
print("The type of the variable is:", type(variable1))

print("-"*51)
print("---Attempting to convert variable1 to an integer---")
print("-"*51)

# This line attempts to convert variable1 to an integer
variable1 = int(variable1)
print("variable1 is now", variable1)
print("The type of the variable is now:", type(variable1))