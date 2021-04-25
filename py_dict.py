name = {'name': 'Hasnat', 'number': 12345, 'city': 'Dhaka'}
print(name)
print(name.keys())
print(name.values())

print(name.get('name'))
print(name.get('number'))
print(name['city'])


print(len(name))
print(list(name.keys()))
print(list(name.values()))

name['email'] = 'x@gmail.com'
print(name['email'])


name.pop('email')
print(name)