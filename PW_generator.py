import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if length < 1:
        print("Password length should be at least 1 character.")
        return None
    password = ''.join(random.choice(characters) for i in range(length))
    return password 

def main():
    print("Welcome to the Password Generator!")
    
    # Ask for user input about their dream password
    print("Please provide the following details about your dream password:")
    try:
        length = int(input("Enter the desired password length (minimum 1 character): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'
    
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    if password:
        print("Generated password:", password)

if __name__ == "__main__":
    main()