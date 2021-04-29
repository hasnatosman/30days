year = int(input('Enter a year : '))

if year % 400 == 0:
    print('It is a leaf year.')
elif year % 100 == 0:
    print('It is not a leaf year.')
elif year % 4 == 0:
    print('It is a leaf year.')
else:
    print(' It is not a leaf year.')