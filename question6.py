# function to calculate the sum of digits of a number
def sum_of_digits(num):
    # total is set to 0 at the start
    total = 0
    # while loop which runs until all digits are finished
    while num > 0:
        # gets the last digit
        digit = num % 10
        # adds it to the total
        total += digit
        # removes the last digit
        num = num // 10
    return total

# function call
print(sum_of_digits(123456))
