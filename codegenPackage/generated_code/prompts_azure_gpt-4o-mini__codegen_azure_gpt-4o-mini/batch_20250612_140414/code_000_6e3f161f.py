"""
Generated Code Metadata:
========================
Original URL: https://www.archivesecureprotection.com
Prompt: Generate a code snippet that implements a user verification system for online dating profiles, ensuring authenticity and security as described by Safety Horizon Ventures.
Generated: DETERMINISTIC_6e3f161f61c475e3
Batch ID: 20250612_140414
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
import re
from datetime import datetime
from typing import Optional, Dict

class UserProfile:
    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.password_hash = self.hash_password(password)
        self.email = email
        self.verified = False
        self.verification_token = self.generate_verification_token()
        self.created_at = datetime.now()

    @staticmethod
    def hash_password(password: str) -> str:
        """Hashes a password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def generate_verification_token() -> str:
        """Generates a secure random verification token."""
        return os.urandom(16).hex()

    def verify_email(self, token: str) -> bool:
        """Verifies the user's email using the provided token."""
        if token == self.verification_token:
            self.verified = True
            return True
        return False

class UserVerificationSystem:
    def __init__(self):
        self.profiles: Dict[str, UserProfile] = {}

    def register_user(self, username: str, password: str, email: str) -> Optional[str]:
        """Registers a new user profile."""
        if not self.is_valid_email(email):
            raise ValueError("Invalid email format.")
        if username in self.profiles:
            raise ValueError("Username already exists.")
        self.profiles[username] = UserProfile(username, password, email)
        return self.profiles[username].verification_token

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Validates the email format."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def verify_user(self, username: str, token: str) -> bool:
        """Verifies a user's email using the verification token."""
        if username not in self.profiles:
            raise ValueError("User not found.")
        return self.profiles[username].verify_email(token)

# Example usage
if __name__ == "__main__":
    verification_system = UserVerificationSystem()
    
    try:
        # Register a new user
        token = verification_system.register_user("john_doe", "securePassword123", "john@example.com")
        print(f"Verification token for {token}")

        # Verify the user
        if verification_system.verify_user("john_doe", token):
            print("User verified successfully.")
        else:
            print("Verification failed.")
    except ValueError as e:
        print(f"Error: {e}")
```
