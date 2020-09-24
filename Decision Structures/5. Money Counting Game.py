'''
Create a change-counting game that gets the user to enter the
number of coins required to make exactly one dollar. The program
should prompt the user to enter the number of pennies, nickels,
dimes, and quarters. If the total value of the coins entered is equal
to one dollar, the program should congratulate the user for winning
the game. Otherwise, the program should display a message
indicating whether the amount entered was more than or less than
one dollar.
'''

pennies_val = 1/100
nickels_val = 1/20
dimes_val = 1/10
quarters_val = 1/4

pennies = int(input('Enter pennies: '))
nickels = int(input('Enter nickels: '))
dimes = int(input('Enter dimes: '))
quarters = int(input('Enter quarters: '))

total = pennies * pennies_val + nickels * nickels_val + dimes * dimes_val + quarters * quarters_val

if total == 1:
    print('Congratulations!')
elif total > 1:
    print('The amount entered is more than than one dollar')
else:
    print('The amount entered is less than than one dollar')
