"""
Generated Code Metadata:
========================
Original URL: https://financeinvestmentslimited.org
Prompt: Write Python code to simulate a digital asset management system with two-factor authentication, inspired by Finance Investment Limited's security features.
Generated: DETERMINISTIC_68f22bfc37091c9a
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import random
import smtplib
import string
import time
from getpass import getpass
from email.mime.text import MIMEText

# Constants for the email configuration
EMAIL_HOST = 'smtp.example.com'  # Replace with your SMTP server
EMAIL_PORT = 587  # Common SMTP port for TLS
EMAIL_USER = 'your_email@example.com'  # Replace with your email
EMAIL_PASSWORD = 'your_email_password'  # Replace with your email password

# User database simulation
user_db = {
    'user@example.com': {
        'password': 'securepassword',  # In production, use hashed passwords
        'two_factor_code': None,
        'is_authenticated': False
    }
}

def send_two_factor_code(email, code):
    """Send the two-factor authentication code to the user's email."""
    msg = MIMEText(f'Your two-factor authentication code is: {code}')
    msg['Subject'] = 'Your Two-Factor Authentication Code'
    msg['From'] = EMAIL_USER
    msg['To'] = email

    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.send_message(msg)
            print("Two-factor code sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

def generate_two_factor_code():
    """Generate a random 6-digit two-factor authentication code."""
    return ''.join(random.choices(string.digits, k=6))

def authenticate_user(email, password):
    """Authenticate the user with email and password."""
    user = user_db.get(email)
    if user and user['password'] == password:
        return True
    return False

def verify_two_factor_code(email, code):
    """Verify the two-factor authentication code."""
    user = user_db.get(email)
    if user and user['two_factor_code'] == code:
        user['is_authenticated'] = True
        user['two_factor_code'] = None  # Clear the code after verification
        return True
    return False

def main():
    """Main function to run the digital asset management system."""
    print("Welcome to the Digital Asset Management System")

    # Step 1: User login
    email = input("Enter your email: ")
    password = getpass("Enter your password: ")

    if authenticate_user(email, password):
        print("User authenticated. Sending two-factor code...")
        
        # Step 2: Generate and send two-factor code
        code = generate_two_factor_code()
        user_db[email]['two_factor_code'] = code
        send_two_factor_code(email, code)

        # Step 3: Verify two-factor code
        user_input_code = input("Enter the two-factor authentication code sent to your email: ")
        if verify_two_factor_code(email, user_input_code):
            print("Authentication successful! You are now logged in.")
            # Proceed with the digital asset management functionalities
        else:
            print("Invalid two-factor authentication code. Access denied.")
    else:
        print("Invalid email or password. Access denied.")

if __name__ == "__main__":
    main()
```

**Note:** Replace the email configuration constants with your actual SMTP server details and credentials. In a production environment, ensure to use secure password storage methods (e.g., hashing) and handle sensitive information appropriately.
