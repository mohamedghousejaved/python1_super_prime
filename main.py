def is_prime(num):
    if num<= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def SUPERPRIME(prime_list, N):
    super_prime = {}

    for i in range(len(prime_list) - 1):
        if is_prime(prime_list[i + 1]):
            super_prime[prime_list[i]] = prime_list[i + 1]

    return super_prime



prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]  # Add more prime numbers until the desired limit.
N = 9 # Replace with the desired limit of the prime numbers.
super_prime_dict = SUPERPRIME(prime_numbers, N)
print(super_prime_dict)
