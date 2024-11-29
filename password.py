import random
import string

def generate_password(length):
    """Generates a random password with the given length."""
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None

    # Ensure the password contains at least one character from each category
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    # Fill the rest of the password length with random choices from all categories
    remaining = random.choices(string.ascii_letters + string.digits + string.punctuation, k=length-4)

    # Combine all characters and shuffle them
    password_list = list(lower + upper + digit + special + ''.join(remaining))
    random.shuffle(password_list)

    return ''.join(password_list)

def main():
    print("Password Generator")
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 4): "))
            password = generate_password(length)
            if password:
                print(f"Generated Password: {password}")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()