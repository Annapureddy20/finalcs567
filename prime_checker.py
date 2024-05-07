def is_prime(number):
    # Check if the number is less than or equal to 1.
    if number <= 1:
        return False  # If the number is less than or equal to 1, it's not prime, so return False.
    
    # Iterate through numbers from 2 to the square root of the given number.
    for i in range(2, int(number**0.5) + 1):
        # Check if the number is divisible by any number between 2 and its square root (inclusive).
        if number % i == 0:
            return False  # If the number is divisible by any of these numbers, it's not prime, so return False.
    
    # If the number is not divisible by any number between 2 and its square root, it's prime, so return True.
    return True
