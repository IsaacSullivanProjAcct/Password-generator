import random
import string

#input for length of password
length = int(input('Please insert the length of password you want: '))

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
    print("Generated Passcode:", generate_passcode(length, use_digits=True, use_letters=True, use_symbols=True))