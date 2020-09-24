'''
Assuming the ocean’s level is currently rising at about 1.6
millimeters per year, create an application that displays the
number of millimeters that the ocean will have risen each year for
the next 25 years.
'''


print('Year', '\t', 'Level')

for i in range(1, 25+1, 1):
    print(i, '\t\t', i*1.6)