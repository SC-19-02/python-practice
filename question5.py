# function to calculate the factorial of a number (recursive)
def factorial_recursive(num):
    # base case: the factorial of 0 or 1 is 1
    if num == 0 or num == 1:
        return 1
    # checks if num is less than 0 as factorial does not exist for negative numbers
    elif num < 0:
        print("Factorial does not exist for negative numbers")
        return
    # recursive case: n * factorial of (n - 1)
    else:
        return num * factorial_recursive(num - 1)

# function call
print(factorial_recursive(5))
