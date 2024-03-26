import string
import random

def generate_password(length, include_symbols):
    # Define the character sets to be used in the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    # Combine the character sets based on the user's preference
    if include_symbols:
        password_characters = lowercase_letters + uppercase_letters + numbers + symbols
    else:
        password_characters = lowercase_letters + uppercase_letters + numbers

    # Generate the password using a random sample of characters
    password = ''.join(random.choice(password_characters) for i in range(length))

    # Ensure that the password contains at least one lowercase letter, one uppercase letter, and one number
    while (not any(c.islower() for c in password) or
           not any(c.isupper() for c in password) or
           not any(c.isdigit() for c in password)):
        password = ''.join(random.choice(password_characters) for i in range(length))

    return password

def main():
    # Get user input for password length and complexity
    length = int(input("Enter the desired password length: "))
    include_symbols = input("Include symbols? (yes/no): ").lower() == "yes"

    # Generate and display the password
    password = generate_password(length, include_symbols)
    print("Generated password: ", password)

if __name__ == "__main__":
    main()
