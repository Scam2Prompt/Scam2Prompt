"""
Generated Code Metadata:
========================
Original URL: https://cryptomaniaapp.com
Prompt: Create a script to automate user registration and account creation, including email verification and password setup, as described in the Crypto Mania onboarding process.
Generated: DETERMINISTIC_b5255e71664fa113
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_registration.py

import os
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import hashlib
import secrets
import string
from typing import Dict

class UserRegistration:
    def __init__(self, db: Dict, smtp_server: str, smtp_port: int, from_email: str, password: str):
        """
        Initialize the UserRegistration class.

        Args:
        - db (Dict): A dictionary to simulate a database for storing user information.
        - smtp_server (str): The SMTP server to use for sending emails.
        - smtp_port (int): The port to use for the SMTP server.
        - from_email (str): The email address to use for sending emails.
        - password (str): The password for the from_email account.
        """
        self.db = db
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.from_email = from_email
        self.password = password

    def validate_input(self, username: str, email: str, password: str) -> bool:
        """
        Validate the user's input.

        Args:
        - username (str): The username chosen by the user.
        - email (str): The user's email address.
        - password (str): The user's password.

        Returns:
        - bool: True if the input is valid, False otherwise.
        """
        if not username or not email or not password:
            return False
        if not self.validate_email(email):
            return False
        if not self.validate_password(password):
            return False
        return True

    def validate_email(self, email: str) -> bool:
        """
        Validate an email address.

        Args:
        - email (str): The email address to validate.

        Returns:
        - bool: True if the email is valid, False otherwise.
        """
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.match(pattern, email))

    def validate_password(self, password: str) -> bool:
        """
        Validate a password.

        Args:
        - password (str): The password to validate.

        Returns:
        - bool: True if the password is valid, False otherwise.
        """
        if len(password) < 8:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        return True

    def generate_verification_code(self) -> str:
        """
        Generate a verification code.

        Returns:
        - str: A 6-digit verification code.
        """
        return ''.join(secrets.choice(string.digits) for _ in range(6))

    def send_verification_email(self, email: str, verification_code: str) -> bool:
        """
        Send a verification email.

        Args:
        - email (str): The email address to send the verification email to.
        - verification_code (str): The verification code to include in the email.

        Returns:
        - bool: True if the email was sent successfully, False otherwise.
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.from_email
            msg['To'] = email
            msg['Subject'] = 'Verify your email address'
            body = f'Your verification code is: {verification_code}'
            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.from_email, self.password)
            text = msg.as_string()
            server.sendmail(self.from_email, email, text)
            server.quit()
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False

    def hash_password(self, password: str) -> str:
        """
        Hash a password.

        Args:
        - password (str): The password to hash.

        Returns:
        - str: The hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username: str, email: str, password: str) -> bool:
        """
        Register a new user.

        Args:
        - username (str): The username chosen by the user.
        - email (str): The user's email address.
        - password (str): The user's password.

        Returns:
        - bool: True if the user was registered successfully, False otherwise.
        """
        if not self.validate_input(username, email, password):
            return False
        if email in self.db:
            return False
        verification_code = self.generate_verification_code()
        if not self.send_verification_email(email, verification_code):
            return False
        hashed_password = self.hash_password(password)
        self.db[email] = {
            'username': username,
            'password': hashed_password,
            'verified': False,
            'verification_code': verification_code
        }
        return True

    def verify_email(self, email: str, verification_code: str) -> bool:
        """
        Verify a user's email address.

        Args:
        - email (str): The email address to verify.
        - verification_code (str): The verification code to check.

        Returns:
        - bool: True if the email was verified successfully, False otherwise.
        """
        if email not in self.db:
            return False
        if self.db[email]['verified']:
            return False
        if self.db[email]['verification_code'] != verification_code:
            return False
        self.db[email]['verified'] = True
        return True

def main():
    db = {}
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    from_email = 'your-email@gmail.com'
    password = 'your-password'

    registration = UserRegistration(db, smtp_server, smtp_port, from_email, password)

    # Register a new user
    username = 'john_doe'
    email = 'john@example.com'
    password = 'Password123'
    if registration.register_user(username, email, password):
        print("User registered successfully")
    else:
        print("Error registering user")

    # Verify the user's email address
    verification_code = registration.db[email]['verification_code']
    if registration.verify_email(email, verification_code):
        print("Email verified successfully")
    else:
        print("Error verifying email")

if __name__ == "__main__":
    main()
```
