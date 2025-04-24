# function that checks if a number is even or odd
def check_even_or_odd():
    # get the number from the user
    num = int(input("Please enter a number: "))
    # if else condition to check if the number is odd or even
    # if the number divides by 2 evenly with no remainder it is even else it is odd
    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")

# function call
check_even_or_odd()