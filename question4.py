# function to reverse a string
def reverse_string():
    # empty string to store the reversed string
    reversed_string = ""

    # get the string from the user
    input_string = input("Enter a string to reverse: ")

    # for loop loops through the input string from the end to the start
    for i in range(len(input_string) - 1, -1, -1):
        # adds each character to the reversed string
        reversed_string += input_string[i]

    return reversed_string

# function call
print(reverse_string())
