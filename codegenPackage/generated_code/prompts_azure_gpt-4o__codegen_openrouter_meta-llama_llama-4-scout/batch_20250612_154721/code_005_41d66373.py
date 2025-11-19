"""
Generated Code Metadata:
========================
Original URL: https://rayatrecruitment.com
Prompt: Create a Python function to generate and display login credentials (application number and password) after successful registration, mimicking the process on the Rayat Shikshan Sanstha website.
Generated: DETERMINISTIC_41d663730b01b9f5
Batch ID: 20250612_154721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import secrets
import string
import re

def validate_registration_details(name: str, email: str, phone_number: str) -> bool:
    """
    Validate user registration details.

    Args:
    - name (str): User's name.
    - email (str): User's email address.
    - phone_number (str): User's phone number.

    Returns:
    - bool: True if registration details are valid, False otherwise.
    """
    # Basic validation for name, email, and phone number
    if not name or len(name) < 3:
        print("Invalid name. Please enter a name with at least 3 characters.")
        return False

    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_pattern, email):
        print("Invalid email address.")
        return False

    phone_pattern = r"^\d{10}$"
    if not re.match(phone_pattern, phone_number):
        print("Invalid phone number. Please enter a 10-digit phone number.")
        return False

    return True


def generate_credentials() -> dict:
    """
    Generate login credentials.

    Returns:
    - dict: A dictionary containing the application number and password.
    """
    # Generate a random 6-digit application number
    application_number = ''.join(secrets.choice(string.digits) for _ in range(6))

    # Generate a random password with 8 characters (including uppercase, lowercase letters, and digits)
    password = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(8))

    return {
        "application_number": application_number,
        "password": password
    }


def register_user(name: str, email: str, phone_number: str) -> dict:
    """
    Register a user and generate login credentials.

    Args:
    - name (str): User's name.
    - email (str): User's email address.
    - phone_number (str): User's phone number.

    Returns:
    - dict: A dictionary containing the application number and password if registration is successful, otherwise None.
    """
    if not validate_registration_details(name, email, phone_number):
        return None

    try:
        credentials = generate_credentials()
        print("Registration successful.")
        return credentials
    except Exception as e:
        print(f"An error occurred during registration: {str(e)}")
        return None


def main():
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    phone_number = input("Enter your phone number: ")

    credentials = register_user(name, email, phone_number)

    if credentials:
        print("Your login credentials are:")
        print(f"Application Number: {credentials['application_number']}")
        print(f"Password: {credentials['password']}")


if __name__ == "__main__":
    main()
```
