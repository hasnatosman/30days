if True:
    print('Hello, Hasnat!!')
if not False:
    print('Nothing there!!!')
print()
print('...............................')

name = input('Input a name: ')
age = int(input('Enter an age: '))
country = input('Enter a country name: ')

if name == "HASNAT" or 'Hasnat' or 'hasnat':
    print('He is ', name, '. His age is ', age, ' years old and from', country)
else:
    print('SORRY!!!')
    print('Please. Try Again!')