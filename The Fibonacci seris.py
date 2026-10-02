# Fibonacci series using recursion
def recur_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recur_fibonacci(n-1) + recur_fibonacci(n-2)

nterms = int(input("Enter the number of terms: "))

# Check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibonacci(i))