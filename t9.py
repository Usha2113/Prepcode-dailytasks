# List Rotation

def rotate_list(list, k):
    n=len(list)
    k%=n
    return list[-k:]+list[:-k]

# get the input from the user
numbers = list(map(int,input("Enter numbers separated by space: ").split()))
k = int(input("Enter the number of positions to rotate: "))
rotated_list = rotate_list(numbers, k)
print("The rotated list is:", rotated_list)
