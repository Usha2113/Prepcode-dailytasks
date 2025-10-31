# Find the number of digits in a given integer

def count_digits(num):
    # Convert the number to a string and find its length
    return len(str(abs(num)))

# Example usage
num = int(input("Enter an interger: "))
print("Number of digits:", count_digits(num))

