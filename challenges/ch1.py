# Create a method that tests whether the result of taking the power of one number to another number provides an answer which is greater than 5000. We will use a conditional statement to return True if the result is greater than 5000 or return False if it is not. In order to accomplish this, we will need the following steps:

# Define the function to accept two input parameters called base and exponent
# Calculate the result of base to the power of exponent
# Use an if statement to test if the result is greater than 5000. If it is then return True. Otherwise, return False




# Coding Question

# Create a function named large_power() that takes two parameters named base and exponent.

# If base raised to the exponent is greater than 5000, return True, otherwise return False

def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False

# Example usage
print(large_power(2, 10))  # True (1024)
print(large_power(3, 5))   # False (243)
print(large_power(10, 4))  # True (10000)
