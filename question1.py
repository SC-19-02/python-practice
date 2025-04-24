# function that sums all the elements in a list
def sum_elements(numbers):
    # total is set to 0 at the start
    total = 0
    # for loop loops through each number in the list
    for number in numbers:
        # adds the current number to the total
        total += number
    # total is returned at the end
    return total

# function call
print(sum_elements([1, 2, 3, 4, 5]))