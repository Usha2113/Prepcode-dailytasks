# Find the largest number in a list of integers.

def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Get input from user and convert to list of integers
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("The largest number is:", find_largest(numbers))
