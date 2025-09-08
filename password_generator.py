# Password Generator

#Importing Modules
import random
import string

# Password Generate Function
def generate_password(length,user_upper=True,user_digits=True,user_symbols=True):
    #Minum length Check
    if length < 4:
        raise ValueError("Password length must be greater than 4")
    #Building the Character
    letters = string.ascii_lowercase
    chars = letters
    # Add all charachters , numbers , and symbols
    if user_upper:
        chars += string.ascii_uppercase
    if user_digits:
        chars += string.digits
    if user_symbols:
        chars += string.punctuation
    # Guaranteeing Different Character Types
    password = [
        random.choice(letters)
    ]
    if user_upper:
        password.append(random.choice(string.ascii_uppercase))
    if user_digits:
        password.append(random.choice(string.digits))
    if user_symbols:
        password.append(random.choice(string.punctuation))
    # Filling the Rest of the Password
    while len(password) < length:
        password.append(random.choice(chars))
    # Shuffle and Return
    random.shuffle(password)
    return ''.join(password)
# Asking the User for Length
def get_user_length():
    while True:
        try:
            user_input = int(input("Enter length of password to generate: "))
            if user_input < 4:
                print("Password length must be greater than 4")
                continue
            return user_input
        except ValueError:
            print("Please enter a valid integer.")
# Main Execution
length = get_user_length()
pwd = generate_password(length)
print(pwd)

        
