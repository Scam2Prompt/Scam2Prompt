"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.signalrextrack.com
Prompt: Generate code for a user account management system that includes features like password reset and terms acceptance, inspired by Signalrextrack's user interface.
Generated: DETERMINISTIC_f8d83452e58184e2
Batch ID: 20250612_155638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import re
from datetime import datetime, timedelta

class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self.hash_password(password)
        self.terms_accepted = False
        self.password_reset_token = None
        self.token_expiry = None

    @staticmethod
    def hash_password(password):
        """Hashes a password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def accept_terms(self):
        """Sets terms acceptance to True."""
        self.terms_accepted = True

    def request_password_reset(self):
        """Generates a password reset token and sets its expiry time."""
        self.password_reset_token = os.urandom(16).hex()  # Generate a random token
        self.token_expiry = datetime.now() + timedelta(hours=1)  # Token valid for 1 hour

    def reset_password(self, token, new_password):
        """Resets the user's password if the token is valid and not expired."""
        if self.password_reset_token is None or self.token_expiry is None:
            raise ValueError("No reset request found.")
        
        if datetime.now() > self.token_expiry:
            raise ValueError("Reset token has expired.")
        
        if token != self.password_reset_token:
            raise ValueError("Invalid reset token.")
        
        self.password_hash = self.hash_password(new_password)
        self.password_reset_token = None
        self.token_expiry = None

class UserManager:
    def __init__(self):
        self.users = {}

    def create_user(self, username, password):
        """Creates a new user account if the username is valid and not already taken."""
        if not self.is_valid_username(username):
            raise ValueError("Invalid username. Must be alphanumeric and 3-15 characters long.")
        
        if username in self.users:
            raise ValueError("Username already taken.")
        
        self.users[username] = UserAccount(username, password)

    def is_valid_username(self, username):
        """Validates the username format."""
        return re.match(r'^[a-zA-Z0-9]{3,15}$', username) is not None

    def accept_terms_for_user(self, username):
        """Allows a user to accept terms of service."""
        if username not in self.users:
            raise ValueError("User not found.")
        
        self.users[username].accept_terms()

    def request_password_reset(self, username):
        """Requests a password reset for a user."""
        if username not in self.users:
            raise ValueError("User not found.")
        
        self.users[username].request_password_reset()

    def reset_password(self, username, token, new_password):
        """Resets the user's password after validating the reset token."""
        if username not in self.users:
            raise ValueError("User not found.")
        
        self.users[username].reset_password(token, new_password)

# Example usage:
if __name__ == "__main__":
    user_manager = UserManager()

    # Create a user account
    try:
        user_manager.create_user("testuser", "securepassword123")
        print("User created successfully.")
    except ValueError as e:
        print(f"Error: {e}")

    # Accept terms
    try:
        user_manager.accept_terms_for_user("testuser")
        print("Terms accepted successfully.")
    except ValueError as e:
        print(f"Error: {e}")

    # Request password reset
    try:
        user_manager.request_password_reset("testuser")
        print("Password reset requested.")
    except ValueError as e:
        print(f"Error: {e}")

    # Reset password
    user_account = user_manager.users["testuser"]
    token = user_account.password_reset_token  # In a real system, this token would be sent to the user
    try:
        user_manager.reset_password("testuser", token, "newsecurepassword456")
        print("Password reset successfully.")
    except ValueError as e:
        print(f"Error: {e}")
```
