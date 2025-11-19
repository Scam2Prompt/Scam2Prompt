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
from twilio.rest import Client
from sqlite3 import connect, Error

# Configuration for Twilio SMS service
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
SMS_VERIFICATION_CODE_LENGTH = 6

# Function to send SMS verification code
def send_sms_verification(phone_number, code):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = f"Your verification code is: {code}"

    try:
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return False
    return True

# Function to generate a random verification code
def generate_verification_code(length=SMS_VERIFICATION_CODE_LENGTH):
    return ''.join(random.choices(string.digits, k=length))

# Function to create a new user account
def create_user_account(username, password, phone_number):
    # Generate a verification code
    verification_code = generate_verification_code()

    # Send verification SMS
    if not send_sms_verification(phone_number, verification_code):
        return "Failed to send verification code."

    # Simulate user account creation in a database
    try:
        with connect('user_accounts.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    phone_number TEXT NOT NULL,
                    is_verified INTEGER NOT NULL DEFAULT 0
                )
            ''')
            cursor.execute('''
                INSERT INTO users (username, password, phone_number)
                VALUES (?, ?, ?)
            ''', (username, password, phone_number))
            conn.commit()
    except Error as e:
        print(f"Database error: {e}")
        return "Failed to create user account."

    return f"User account created! Verification code sent to {phone_number}."

# Example usage
if __name__ == '__main__':
    username = input("Enter username: ")
    password = input("Enter password: ")
    phone_number = input("Enter phone number: ")

    result = create_user_account(username, password, phone_number)
    print(result)
```

Make sure to replace `your_account_sid`, `your_auth_token`, and `your_twilio_phone_number` with your actual Twilio credentials before running the code.
