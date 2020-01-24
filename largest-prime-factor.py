# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def get_largest_prime_factor(number):
    largest = 0
    factor = 2

    while factor * factor <= number:
        while number % factor == 0:
            largest = factor
            number /= factor
        factor += 1
    if (number > 1):
        return number
    return largest


print(get_largest_prime_factor(600851475143))
