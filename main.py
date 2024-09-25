import random

# Password Generator

upper = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
lower = tuple('abcdefghijklmnopqrstuvwxyz')
numbers = tuple('0123456789')
symbols = ('!', '#', '$', '%', '&', '(', ')', '*', '+')

print("-x-x-x-x- PASSWORD GENERATOR -x-x-x-x-\n")
num_upper = int(input("How many upper case letters would you like in your password? "))
num_lower = int(input("How many lower case letters would you like in your password? "))
num_symbols = int(input("How many symbols would you like? "))
num_numbers = int(input("How many numbers would you like? "))

# DO NOT ERASE ROWS ABOVE!
# Make a program that generates a strong password that randomly picks the chosen amount of letters, symbols and numbers
# TODO: Easy mode
# TODO: Hard mode

