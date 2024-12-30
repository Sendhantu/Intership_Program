import random
import string

uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
special_characters = "@#$%&*"
password = ""
try:
    length = int(input("Enter the desired password length (minimum 4): "))
except ValueError:
    print("Invalid input. Please enter a valid number.")

all_characters = uppercase_letters + lowercase_letters + digits + special_characters
random_password = random.choices(all_characters, k=length)
for i in random_password:
    password += i

print("The Password Generated is :",password)
