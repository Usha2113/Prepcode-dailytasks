# Find the sum of first n natural numbers.

def sum_of_natural_numbers(n):
    total = 0
    for i in range(1,n+1):
        total+=i
    return total
n=int(input("Enter a positive interger: "))
print("The sum of first ",n,"natural numbers is : ",sum_of_natural_numbers(n))
