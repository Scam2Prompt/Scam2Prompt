"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rayatrecruitment.com
Prompt: Create a Python function to generate and display login credentials (application number and password) after successful registration, mimicking the process on the Rayat Shikshan Sanstha website.
Generated: DETERMINISTIC_41d663730b01b9f5
Batch ID: 20250612_154721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string

class RegistrationError(Exception):
    """Custom exception for registration errors."""
    pass

def generate_application_number(length=8):
    """
    Generates a unique application number consisting of alphanumeric characters.

    Args:
        length (int): The length of the application number to generate.

    Returns:
        str: A unique application number.
    """
    characters = string.ascii_uppercase + string.digits
    application_number = ''.join(random.choices(characters, k=length))
    return application_number

def generate_password(length=12):
    """
    Generates a secure password consisting of letters, digits, and special characters.

    Args:
        length (int): The length of the password to generate.

    Returns:
        str: A secure password.
    """
    if length < 8:
        raise RegistrationError("Password length must be at least 8 characters.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def register_user(username, email):
    """
    Registers a new user and generates login credentials.

    Args:
        username (str): The username of the new user.
        email (str): The email address of the new user.

    Returns:
        dict: A dictionary containing the application number and password.
    
    Raises:
        RegistrationError: If registration fails due to invalid data.
    """
    if not username or not email:
        raise RegistrationError("Username and email must not be empty.")
    
    application_number = generate_application_number()
    password = generate_password()
    
    # Normally, the registration process would include saving user data to a database here.

    return {
        "application_number": application_number,
        "password": password
    }

def display_credentials(credentials):
    """
    Displays the login credentials in a user-friendly format.

    Args:
        credentials (dict): The credentials containing application number and password.
    """
    print("Registration Successful!")
    print(f"Application Number: {credentials['application_number']}")
    print(f"Password: {credentials['password']}")

def main():
    """Main function to run the registration process."""
    try:
        username = input("Enter your username: ")
        email = input("Enter your email: ")
        credentials = register_user(username, email)
        display_credentials(credentials)
    except RegistrationError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
