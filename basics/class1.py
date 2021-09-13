# First Python program simple print you can use either '' or ""
print("Ananya Thomas")
print('Hello world!')
# lol here you go a dog
print('o----')
print(' ||||')
# python interpreter runs line by line from top
print('*' *10) # expression
# basically the string gets multiplied by 10
print('Hey', 10) # can print 10 
# print('Hello' + 10) will cause error as 10 is int and + means concatenate so write (str)10

price = 10 # definition of variable
price = price +1
print(price)
r = 4.76
print(r)
b = True # Python is case-sensitive

name= 'John Smith'
age = 20
is_new = True
print (name , ' ', age ,' ', is_new)

# How to receive input
name = input('What is your name? ')
colour = input('What is your favourite color? ')
print(name+ ' likes '+colour)

# Type conversion
year =input('Birth year? ') # Here year is a string as '2002' not 2002 so type conversion needed
print(type(year))
age = 2021 - int(year)
print(type(age))
print(age)
weight =input('Weight ')
kg= float(weight) * 0.454
print(kg)

# Strings
# If you need to use apostrophe or double quotes in the string and have multiple lines then we use triple quotes
print('''Python's course for "Beginnners"
so thanks bye
:)
''')
course = 'Python for beginners'
print(course[0]) # first character from front
print(course[-1]) # first character from last
print(course[0:6]) # default index is [0,n] n-last index
print(course[1:-1])

# Formatted Strings
first = 'Ananya'
last = 'Thomas'
message =first + ' ['+ last +'] is a coder' # not formatted
print(message)
msg =f'{first} [{last}] is a coder' # formatted
print(msg)

# String Methods
c = 'Ananya Thomas'
print(len(c)) # len is a general purpose function NOT a method
print(c.upper()) # a method
# upper, lower , find(returns first of that character)
print(c.find('T')) # -1 if element not found
# replace(replaces a value with another
print(c.replace('Ananya', 'The Queen Ananya'))
print('Ananya' in c) # returns boolean value checks if it is present

# Arithmetic operations
print(10/3) # Prints floating number
print(10//3) # Prints integer
print(10 % 3) # remainder
print(10 ** 3) # Exponent operator returns 10^3
x = 10
x = x +3
x += 3 # same output as up known as augmented assignment operator

# Operator Precedence - parenthesis > Exponent > Mul or divide > add or sub

# Math Functions
x = 2.9
print(round(x))
print(abs(-3.5))
import math # Import math module to perform complex mathematical functions
print(math.ceil(3.5))
print(math.sin(0.524)) # sine of x RADIANS all trigonometric functions are in radians
