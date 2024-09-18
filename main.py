import random

# Password Generator

upper = list('abcdefghijklmnopqrstuvwxyz')
lower = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("-x-x-x-x- PASSWORD GENERATOR -x-x-x-x-\n")
num_upper = int(input("How many upper caseletters would you like in your password? "))
num_lower = int(input("How many lower case letters would you like in your password? "))
num_symbols = int(input("How many symbols would you like? "))
num_numbers = int(input("How many numbers would you like? "))

# DO NOT ERASE ROWS ABOVE!
# TODO: Make a program that generates a strong password that randomly picks the chosen amount of letters, symbols and numbers
