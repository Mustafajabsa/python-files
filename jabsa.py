# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
selected1 = ''
selected2 = ''
selected3 = ''
sel = ''
final = ''
for letter in range(nr_letters):
    choice1 = random.choice(letters)
    selected1 += choice1
for symbol in range(nr_symbols):
    choice2 = random.choice(symbols)
    selected2 += choice2
for number in range(nr_numbers):
    choice3 = random.choice(numbers)
    selected3 += choice3
all = (selected1+selected2+selected3).split()
all = list(map(list, all))
for one in range(len(all[0])):
    sel = random.choice(all[0])
    final += sel
print(final)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
