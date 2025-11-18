"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wlfin.org
Prompt: Provide code examples for implementing two-factor authentication (2FA) in a cryptocurrency wallet application, as recommended by WLFI for securing user accounts.
Generated: DETERMINISTIC_39dbd3242475236b
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import smtplib
from email.mime.text import MIMEText
import hashlib

# Constants for 2FA
CODE_EXPIRY_SECONDS = 300  # 5 minutes
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_USERNAME = "your_email@example.com"
EMAIL_PASSWORD = "your_email_password"

# Dictionary to store 2FA codes and their expiry timestamps
two_fa_store = {}

def generate_2fa_code():
    """
    Generate a random 6-digit code for 2FA.
    """
    return str(random.randint(100000, 999999))

def send_email(to_email, subject, body):
    """
    Send an email with the 2FA code.
    :param to_email: Recipient's email address.
    :param subject: Subject of the email.
    :param body: Body of the email.
    """
    try:
        msg = MIMEText(body)
        msg['From'] = EMAIL_USERNAME
        msg['To'] = to_email
        msg['Subject'] = subject

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")
        raise

def request_2fa(user_id, email):
    """
    Generate and send a 2FA code to the user's email and store it.
    :param user_id: Unique identifier for the user.
    :param email: Email address of the user.
    """
    code = generate_2fa_code()
    hashed_code = hashlib.sha256(code.encode()).hexdigest()
    expiry_time = time.time() + CODE_EXPIRY_SECONDS

    # Save the hashed 2FA code and expiry time for the user
    two_fa_store[user_id] = {"code": hashed_code, "expires_at": expiry_time}

    email_body = f"Your 2FA code is: {code}\n\nThis code will expire in 5 minutes."
    send_email(email, "Your 2FA Code", email_body)
    print("2FA code sent successfully.")

def verify_2fa(user_id, input_code):
    """
    Verify the 2FA code entered by the user.
    :param user_id: Unique identifier for the user.
    :param input_code: Code entered by the user.
    :return: True if the code is valid, False otherwise.
    """
    try:
        if user_id not in two_fa_store:
            print("No 2FA code found for user.")
            return False

        data = two_fa_store[user_id]
        hashed_input_code = hashlib.sha256(input_code.encode()).hexdigest()

        # Check if the code has expired
        if time.time() > data["expires_at"]:
            print("2FA code has expired.")
            del two_fa_store[user_id]  # Clean up expired code
            return False

        # Check if the entered code matches the stored hashed code
        if hashed_input_code == data["code"]:
            print("2FA code verified successfully.")
            del two_fa_store[user_id]  # Clean up after successful verification
            return True
        else:
            print("Invalid 2FA code.")
            return False
    except Exception as e:
        print(f"Error verifying 2FA code: {e}")
        return False

# Example Usage:

import time

# Simulated user data
user_id = "user123"
user_email = "user123@example.com"

# Request 2FA code
request_2fa(user_id, user_email)

# Simulate user entering the code
time.sleep(2)  # Wait for 2 seconds before verification (for demonstration)
user_input_code = input("Enter the 2FA code sent to your email: ")

# Verify the 2FA code
is_verified = verify_2fa(user_id, user_input_code)
print(f"2FA verification result: {is_verified}")
```
