# If statements
is_hot = True
is_cold = False
if is_hot: # Take care of indentations
    print("It's a hot day") # Press shift + tab to exit one condition
elif is_cold :
    print("It's a cold day")
else:
    print("It's a rainy day")
print("Enjoy your day")

c = False
if c:
    d = 0.1 * 1000000
else:
    d = 0.2 * 1000000
print(f'Down payment is : ${d}')

# Logical operators
# AND - and , OR - or , NOT - not (WHAT HOW SIMPLE :0)
is_good = False
is_kind = False
if is_kind and is_good:
    print('Nice person')
elif is_kind or is_good:
    print('Can do better')
else:
    print('YOU ARE GOING TO HELL')
is_racist = True
if not is_racist:
    print('Good going')
else:
    print('Satan is already sharpening his knives')