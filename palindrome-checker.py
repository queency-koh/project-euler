# Original String
# Get the Reverse String
# Check if Original and Reverse String are same


def palindrome_checker(palindrome):

    # Check Data Type
    if type(palindrome) == int:
        # Convert to String
        palindrome = str(palindrome)

    if palindrome == palindrome[::-1]:
        return True
    else:
        return False


print(palindrome_checker('12344321'))
