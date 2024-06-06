import random
import string

def password_generator():
    print("Password Generator")

    # Prompt the user to specify the desired length of the password
    password_length = int(input("Enter the desired length of the password: "))

    # Define the characters that can be used to generate the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password of the specified length using random characters
    password = ''.join(random.choice(all_characters) for i in range(password_length))

    # Display the generated password on the screen
    print("Generated Password: ", password)

    # Reappear every time it gives a password
    password_generator()

if __name__ == "__main__":
    password_generator()