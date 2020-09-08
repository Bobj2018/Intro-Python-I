def prime_numbers(number):
    total = []
    for i in range (2,  number + 1):
        if(i % 2 != 0 or i == 2):
            total.append(i)
    return total

def is_prime(number):
    primes = prime_numbers(number)
    if number in primes:
        print(f'{number} is a prime!')
    else:
        print(f'{number} is not a prime!')

is_prime(200)
