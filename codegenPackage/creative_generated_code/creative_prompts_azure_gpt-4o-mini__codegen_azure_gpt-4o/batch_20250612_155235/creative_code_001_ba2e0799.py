"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pixels-dashboard.pages.dev
Prompt: Write a code snippet for creating a new user account in a system like Pixels, utilizing SMS verification for phone numbers.
Generated: DETERMINISTIC_ba2e0799acb77194
Batch ID: 20250612_155235
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
import re
from twilio.rest import Client

# User database (for example purposes, using a dictionary)
user_database = {}

# Twilio credentials (replace with your actual credentials)
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = '+1234567890'

# Function to send SMS verification
def send_sms_verification(phone_number, code):
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=f"Your verification code is: {code}",
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        print(f"Verification code sent to {phone_number}. SID: {message.sid}")
    except Exception as e:
        raise Exception(f"Failed to send SMS: {str(e)}")

# Function to generate a random verification code
def generate_verification_code(length=6):
    return ''.join(random.choices(string.digits, k=length))

# Function to validate phone number format (basic validation for example purposes)
def validate_phone_number(phone_number):
    pattern = r'^\+\d{10,15}$'
    return re.match(pattern, phone_number)

# Function to create a new user account
def create_user_account(username, phone_number):
    try:
        # Validate phone number
        if not validate_phone_number(phone_number):
            raise ValueError("Invalid phone number format. Must be in the form +1234567890.")

        # Check if username already exists
        if username in user_database:
            raise ValueError("Username already exists. Please choose another.")

        # Generate verification code
        verification_code = generate_verification_code()

        # Send SMS verification code
        send_sms_verification(phone_number, verification_code)

        # Simulate verification process (prompt user for code)
        user_input_code = input("Enter the verification code sent to your phone: ")
        if user_input_code != verification_code:
            raise ValueError("Incorrect verification code. Account creation failed.")

        # Create user account
        user_database[username] = {"phone_number": phone_number}
        print(f"Account successfully created for user: {username}")

    except ValueError as ve:
        print(f"Error: {str(ve)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

# Example usage
if __name__ == "__main__":
    print("=== Create New User Account ===")
    username = input("Enter a username: ")
    phone_number = input("Enter your phone number (e.g., +1234567890): ")
    create_user_account(username, phone_number)
```
