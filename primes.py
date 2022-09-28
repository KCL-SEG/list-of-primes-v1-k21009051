"""List of prime numbers generator."""

def primes(number_of_primes):
    list = []
    n = 2
    
    while len(list) < number_of_primes:
        prime = True

        for i in range(2,(n//2)+1):
            if n % i == 0:
                prime = False
                break
        
        if prime == True:
            list.append(n)
        n += 1

    return list
