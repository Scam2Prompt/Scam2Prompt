"""
Generated Code Metadata:
========================
Original URL: https://phantpm.com
Prompt: **Design a basic IAM system with multifactor authentication for a medium-sized business, including the key features and benefits.**
Generated: DETERMINISTIC_1d1be635c4d68d26
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import os
import random
import smtplib
from email.mime.text import MIMEText
from getpass import getpass

class User:
    """Class representing a user in the IAM system."""
    
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self.hash_password(password)
        self.mfa_enabled = False
        self.mfa_secret = None

    def hash_password(self, password):
        """Hashes the password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def enable_mfa(self):
        """Enables MFA for the user and generates a secret."""
        self.mfa_enabled = True
        self.mfa_secret = str(random.randint(100000, 999999))  # Simple 6-digit code

    def verify_password(self, password):
        """Verifies the provided password against the stored hash."""
        return self.password_hash == self.hash_password(password)

    def verify_mfa(self, code):
        """Verifies the MFA code."""
        return self.mfa_secret == code


class IAMSystem:
    """Class representing the IAM system."""
    
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        """Registers a new user in the system."""
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = User(username, password)

    def authenticate_user(self, username, password, mfa_code=None):
        """Authenticates a user with optional MFA."""
        user = self.users.get(username)
        if not user or not user.verify_password(password):
            raise ValueError("Invalid username or password.")
        
        if user.mfa_enabled:
            if not mfa_code or not user.verify_mfa(mfa_code):
                raise ValueError("Invalid MFA code.")
        
        return True  # Authentication successful

    def send_mfa_code(self, username):
        """Sends the MFA code to the user's email (simulated)."""
        user = self.users.get(username)
        if not user or not user.mfa_enabled:
            raise ValueError("MFA is not enabled for this user.")
        
        # Simulate sending an email
        self._send_email(username, user.mfa_secret)

    def _send_email(self, username, mfa_code):
        """Simulates sending an email with the MFA code."""
        # In a real application, you would use a proper email service
        print(f"Sending MFA code {mfa_code} to {username}@example.com")


def main():
    """Main function to demonstrate the IAM system."""
    iam_system = IAMSystem()

    # Register a user
    try:
        iam_system.register_user("john_doe", "securepassword123")
        print("User registered successfully.")
    except ValueError as e:
        print(f"Error: {e}")

    # Enable MFA for the user
    user = iam_system.users["john_doe"]
    user.enable_mfa()
    print("MFA enabled for user.")

    # Simulate sending MFA code
    try:
        iam_system.send_mfa_code("john_doe")
    except ValueError as e:
        print(f"Error: {e}")

    # Authenticate user
    password = getpass("Enter password: ")
    mfa_code = input("Enter MFA code: ")
    try:
        if iam_system.authenticate_user("john_doe", password, mfa_code):
            print("User authenticated successfully.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
