'''
Write a program with a loop that asks the user to enter a series of
positive numbers. The user should enter a negative number to
signal the end of the series. After all the positive numbers have
been entered, the program should display their sum.
'''


sum = 0

while(True):
    num = int(input('Enter a number: '))
    if num < 0:
        break
    sum += num

print(sum)