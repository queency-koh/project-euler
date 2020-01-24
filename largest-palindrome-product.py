# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def get_largest_palindrome():

    palindromes = []

    for x in range(100, 999):
        for i in range(100, 999):
            palindrome = str(i * x)
            if len(palindrome) == 6:
                if palindrome == palindrome[::-1]:
                    palindromes.append(i * x)

    return max(palindromes)


print(get_largest_palindrome())
# 906609
