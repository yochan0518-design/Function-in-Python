# Python program for checking if it is a armstrong number or not 
num = int(input("Enter a number: "))

# Convert number to string to easily count digits and iterate through them
num_str = str(num)
num_digits = len(num_str)

# Calculate sum of digits raised to the power of num_digits
sum_of_powers = 0
for digit in num_str:
    sum_of_powers += int(digit) ** num_digits

# Check if the sum is equal to the original number
if num == sum_of_powers:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")