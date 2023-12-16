def gcd(a, b):
    if a == b:
        return a

    while b != 0:
        a, b = b, a % b

    # Intentionally added unreachable code, assuming a pre-condition such as "a is a positive integer"
    if a < 0:
        return -a 

    return a

# Example usage
num1 = 48
num2 = 18
print("The GCD of", num1, "and", num2, "is:", gcd(num1, num2))
