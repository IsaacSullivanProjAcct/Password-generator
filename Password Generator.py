import random
import string

#Prints statement asking user if they want to use digits, ascii letters, or punctuation
def get_boolean_input(prompt):
    while True:
        response = input(prompt + " (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


#input for length of password, updated to have a catch
while True:
    try:
        length = int(input('Please insert the length of password you want: '))
        if length <= 0:
            print("Error: Password length must be a positive integer.")
        else:
            break
    except ValueError:
        print("Error: Please enter a valid integer.")

use_digits = get_boolean_input("Include digits?")
use_letters = get_boolean_input("Include letters?")
use_symbols = get_boolean_input("Include symbols?")

#Generates the passcode from random using string of digits, letters, and symbols
def generate_passcode(length, use_digits=True, use_letters=True, use_symbols=False):
    characters = ''
    if use_digits:
        characters += string.digits
    if use_letters:
        characters += string.ascii_letters
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    passcode = ''.join(random.choice(characters) for _ in range(length))
    return passcode

#Driver
if __name__ == "__main__":
    try:
        print("Generated Passcode:", generate_passcode(length, use_digits, use_letters, use_symbols))
    except ValueError as ve:
        print(ve)