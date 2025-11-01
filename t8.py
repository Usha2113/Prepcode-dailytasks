# Second Largest Element in List

def second_largest(numbers):
    if len(numbers) < 2:
        return None
    first = second = float('-inf')
    for n in numbers:
        if n > first:
            second = first
            first = n
        elif first > n > second:
            second = n
    return second if second != float('-inf') else None

# get the input from the user 
numbers = list(map(int,input("Enter numbers separated by space: ").split()))
print("The second largest number is:", second_largest(numbers))
