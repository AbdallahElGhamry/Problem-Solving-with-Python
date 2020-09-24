'''
Running on a particular treadmill you burn 4.2 calories per minute.
Write a program that uses a loop to display the number of calories
burned after 10, 15, 20, 25, and 30 minutes.
'''

i = 10

print('minutes', '\t', 'calories')
while i <= 30:
    print(i, '\t\t\t', i * 4.2)
    i += 5
