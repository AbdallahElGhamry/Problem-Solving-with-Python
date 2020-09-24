'''
A software company sells a package that retails for $99. Quantity
discounts are given according to the following table:
	Quantity 	Discount
	10–19 		10%
	20–49 		20%
	50–99 		30%
	100 or more 	40%
Write a program that asks the user to enter the number of
packages purchased. The program should then display the
amount of the discount (if any) and the total amount of the
purchase after the discount.
'''

qnt = int(input('Enter the quantity: '))
disc = 0.0

if qnt >= 100:
    disc = 40/100
elif qnt >= 50 and qnt <= 99:
    disc = 30/100
elif qnt >= 20 and qnt <= 49:
    disc = 20/100
elif qnt >= 10 and qnt <= 19:
    disc = 10/100

print('Discount Percentage:', disc)
print('Discount Value:', disc * qnt)
print('Total Amount:', qnt + disc * qnt )



