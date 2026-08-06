def generate_primes(n):
    if n < 2:
        return []
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
                
    return [i for i in range(2, n + 1) if is_prime[i]]

print(generate_primes(10))  # Output: [2, 3, 5, 7]
print(generate_primes(20))  # Output: [2, 3, 5, 7, 11, 13, 17, 19]
print(generate_primes(1))   # Output: []
print(generate_primes(2))   # Output: [2]