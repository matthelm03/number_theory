import numpy as np

def is_prime(x):
    """Shows if a number is prime or not"""
    if x < 2:
        return False
    for i in range(2, int(np.floor(np.sqrt(x))) + 1):
        if x % i == 0:
            return False

    return True


def legendre(num,prime):
    """This function calculates the legendre symbol of a number relative to a prime"""

    if num % prime == 0:
        return 0

    if prime % 2 == 0:
        return "invalid input"

    if is_prime(prime) is not True:
        return "invalid input"
        
    leg_symbol = (num**((prime-1)/2)) % prime   #(a/p) = a^((p-1)/2)mod p

    return -1 + 2*(leg_symbol == 1)  #Convert to -1 if 4 mod  etc





#Testing
print(legendre(2,7))
        