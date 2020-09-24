'''
In mathematics, the notation n! represents the factorial of the
nonnegative integer n. The factorial of n is the product of all the
nonnegative integers from 1 to n. For example,
	4!=1×2×3×4=24
	7!=1×2×3×4×5×6×7=5040
Write a program that lets the user enter a nonnegative integer then
uses a loop to calculate the factorial of that number. Display the
factorial.
'''

num = int(input('Enter an integer: '))
fact = 1

for i in range(1, num+1, 1):
    fact *= i

print(fact)