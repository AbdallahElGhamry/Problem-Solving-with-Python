'''
Write a program that displays a table of the Celsius temperatures
0 through 20 and their Fahrenheit equivalents. The formula for
converting a temperature from Celsius to Fahrenheit is
			F = 95C + 32
where F is the Fahrenheit temperature, and C is the Celsius
temperature. Your program must use a loop to display the table.
'''


print('C', '\t', 'F')

for c in range(0, 20+1, 1):
    f = (9/5)*c + 32
    print(c,'\t', f)
