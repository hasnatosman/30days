numbers = [1, 3, 8, 22, 66, 77, 96, 33, 31, 75, 66]
even = []
odd = []

while len(numbers) > 0:
    print('Numbers are:', numbers)
    number = numbers.pop()
    print('Popped number to check :', number)
    if number % 2 == 0:
        even.append(number)
        print('Even number list :', even)
    else:
        odd.append(number)
        print('Odd number list :', odd)
        
print()
print('*******************************')
print('*******************************')
print()
print('Final Even List is: ', even)
print('Final Odd List is: ', odd)
print('Program terminated.!!')