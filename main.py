"""
Upper and Lower
"""
# Provide your solution here
#
i = 0
l = 0
input_string = input("Please enter a string: ")
def count_upper_lower():
    for i in range(0, len(input_string)):
        if input_string.islower():
            print("lower", end="")
        elif input_string.isupper():
            print("upper", end="")


count_upper_lower()

### Überlegungen

#     while i > len(word):
#         print("a")
#         i += 1
#     # while index < len(input_string):
#     #     print(input_string[index])
#     #     index += 1
#       #  if i ==
#
#     # print(word)
# length = len(word)
#
# count_upper_lower("This is at least PrINTing SoMEthing.")






"""
Check 33
"""
# Provide your solution here

listing = input("Please enter a list of integers: ")
def has_33(list):
    if "3" in listing:
        print(listing, "\n", ("3" in listing))
    else:
        print(listing), "\n", print("3" in listing)
#    print(listing.find("3"))
    return



has_33([1, 2, 3])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

