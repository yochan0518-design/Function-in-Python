# This Function adds two numbers
def add(x, y):
    return x + y

# This Function Subtracts the two numbers 
def subtract(x, y):
    return x - y

# This Function Multiplies the two numbers 
def multiply(x, y):
    return x * y

# This Function Divides the two numbers 
def divide(x, y):
    return x / y

num1 = int(input("Enter Number 1"))
num2 = int(input("Enter Number 2"))

print("sum :", add(num1, num2))
print("difference :", subtract(num1, num2))
print("product :", multiply(num1, num2))
print("quotient :", divide(num1, num2))