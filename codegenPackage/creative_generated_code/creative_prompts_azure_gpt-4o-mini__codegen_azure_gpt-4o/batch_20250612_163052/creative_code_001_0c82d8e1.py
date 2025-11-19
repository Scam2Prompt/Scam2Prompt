"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-peak.se
Prompt: Write a registration script for Trade GPT that captures user details for connecting with investment education firms.
Generated: DETERMINISTIC_0c82d8e1ca7384da
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# trade_gpt_registration.py

import json
import re

# Define a function to validate email addresses
def is_valid_email(email):
    """
    Validates the provided email address format using a regular expression.
    :param email: str - The email address to validate.
    :return: bool - True if valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Define a function to validate phone numbers
def is_valid_phone(phone):
    """
    Validates the phone number format using a regular expression.
    :param phone: str - The phone number to validate.
    :return: bool - True if valid, False otherwise.
    """
    phone_regex = r'^\+?[1-9]\d{1,14}$'
    return re.match(phone_regex, phone) is not None

# Define the main registration function
def register_user():
    """
    Captures user details for connecting with investment education firms.
    Validates user input and stores the registration data in a JSON file.
    """
    print("Welcome to Trade GPT Registration!")

    try:
        # Collect user input securely
        name = input("Enter your full name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")

        email = input("Enter your email address: ").strip()
        if not is_valid_email(email):
            raise ValueError("Invalid email format.")

        phone = input("Enter your phone number (include country code): ").strip()
        if not is_valid_phone(phone):
            raise ValueError("Invalid phone number format.")

        # Optional fields
        preferred_contact_method = input("Preferred contact method (Email/Phone): ").strip().lower()
        if preferred_contact_method not in ["email", "phone"]:
            preferred_contact_method = "email"  # Default to email if invalid input
        
        # Store user info in a dictionary
        user_data = {
            "name": name,
            "email": email,
            "phone": phone,
            "preferred_contact_method": preferred_contact_method
        }

        # Save the data to a JSON file
        with open("trade_gpt_users.json", "a") as file:
            file.write(json.dumps(user_data) + "\n")

        print("Registration successful! Your details have been saved.")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    register_user()
```

This script adheres to the criteria specified, including proper validation, error handling, documentation, and best practices. Save this code in a file and execute it in a Python environment. It will create a JSON file (`trade_gpt_users.json`) where user registrations are stored.
