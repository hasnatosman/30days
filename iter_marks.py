"""
marks = input('Enter a number: ')
marks = int(marks)
"""
marks = int(input('Enter a number: '))

if marks >= 80:
    grade = 'Good'
    print('WOW!')
elif marks >= 50:
    grade = 'Average'
    print('NICE!!')
else:
    grade = 'Normal'
    print('BAD!')
print('Your level is:', grade)
