# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Aaron'
age = 22

# Concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position
print('Hello, my name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (Python 3.6 and above)
print(f'Hello, my name is {name} and I am {age}')

# String Methods

s = 'hello world'

print('Capitalize string:\t' + s.capitalize())
print('Make all uppercase:\t' + s.upper())
print('Make all lowercase:\t' + s.lower())
print('Swap case:\t\t' + s.swapcase())
print('Get length:\t\t' + str(len(s)))
print('Replace:\t\t' + s.replace('world', 'everyone'))

sub ='h'
print('Count:\t\t\t' + str(s.count(sub)))

print(s.startswith('hello'))
print(s.endswith('d'))
print(s.split())
print(s.find('r'))
print(s.isalnum())
print(s.isalpha())
print(s.isnumeric())