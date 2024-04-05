import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Please enter a valid length greater than 0.")
            return
        num_passwords = int(input("Enter the number of passwords to generate: "))
        if num_passwords <= 0:
            print("Please enter a valid number greater than 0.")
            return

        passwords = [generate_password(length) for _ in range(num_passwords)]

        print("\nGenerated Passwords:")
        for password in passwords:
            print(password)

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
