square = []
for number in range(1, 11):
    if number % 2 == 0:
        formula = number ** 2
        print(number, '=', formula)
        square.append(formula)

print(square)