def is_armstrong(n):
   
    str_n = str(n)
    num_digits = len(str_n)
    
   
    total = sum(int(digit) ** num_digits for digit in str_n)
    
   
    return total == n


print(is_armstrong(153))  # True
print(is_armstrong(9474)) # True
print(is_armstrong(123))  # False
