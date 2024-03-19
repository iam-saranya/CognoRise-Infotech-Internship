import random
import string

def generate_password(length=12):
    # Define character sets for password generation
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure the password length is at least 4 characters
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")

    # Generate a password with at least one character from each set
    password = random.choice(uppercase_letters) + random.choice(lowercase_letters) + random.choice(digits) + random.choice(special_characters)

    # Fill the remaining length with random characters from all sets
    for _ in range(length - 4):
        password += random.choice(all_characters)

    # Shuffle the password to mix characters
    password_list = list(password)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)

    return shuffled_password

def password_generator():
    while True:
        try:
            length = int(input("Enter the length of the password (at least 4 characters): "))
            if length < 4:
                print("Password length must be at least 4 characters.")
                continue
            password = generate_password(length)
            print("Generated Password:", password)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        
        another_generation = input("Do you want to generate another password? (yes/no): ")
        if another_generation.lower() != 'yes':
            break

if __name__ == "__main__":
    password_generator()
