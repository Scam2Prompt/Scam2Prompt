"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patenteimpresa.it
Prompt: Generate a Python script that automates the registration process for the "Patente d'impresa" course, including fields for name, email, and phone number.
Generated: DETERMINISTIC_d2e0282a8d7b48b7
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import re

def validate_email(email):
    """
    Validates the format of an email address.
    :param email: str, the email address to validate
    :return: bool, True if valid, False otherwise
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def validate_phone(phone):
    """
    Validates the format of a phone number.
    :param phone: str, the phone number to validate
    :return: bool, True if valid, False otherwise
    """
    phone_regex = r'^\+?[0-9]{7,15}$'
    return re.match(phone_regex, phone) is not None

def register_user(name, email, phone):
    """
    Registers a user for the "Patente d'impresa" course.
    :param name: str, name of the user
    :param email: str, email address of the user
    :param phone: str, phone number of the user
    :return: dict, confirmation data of the registration
    """
    # Validate input
    if not name.strip():
        raise ValueError("Name cannot be empty.")
    if not validate_email(email):
        raise ValueError("Invalid email format.")
    if not validate_phone(phone):
        raise ValueError("Invalid phone number format.")
    
    # Registration process (mocked)
    registration_data = {
        "name": name,
        "email": email,
        "phone": phone,
        "course": "Patente d'impresa",
        "status": "Registered successfully"
    }

    # Save registration data to a file
    with open('registrations.json', 'a') as f:
        f.write(json.dumps(registration_data) + '\n')

    return registration_data

def main():
    """
    Main function to handle user input and automate registration process.
    """
    print("Welcome to the 'Patente d'impresa' course registration system.")
    
    try:
        # Collect user input
        name = input("Enter your name: ").strip()
        email = input("Enter your email: ").strip()
        phone = input("Enter your phone number: ").strip()

        # Register the user
        result = register_user(name, email, phone)
        print("\nRegistration successful!")
        print(json.dumps(result, indent=4))

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
