# function to calculate the factorial of a number
def factorial():
    # get the number from the user
    num = int(input("Enter a number: "))

    # checks if number is less than 0 as factorial does not exist for negative numbers
    if num < 0:
        print("Factorial does not exist for negative numbers")
        return
    # sets the variable result to 1 (starting point for multiplication)
    result = 1
    # for loop loops from 1 to the number entered
    for i in range(1, num + 1):
        # multiply the result by the current number
        result *= i
    return result

# function call
print(factorial())
