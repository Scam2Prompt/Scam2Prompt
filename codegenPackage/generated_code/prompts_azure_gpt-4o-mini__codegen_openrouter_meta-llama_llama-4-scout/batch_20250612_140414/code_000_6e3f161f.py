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
# user_verification_system.py

import hashlib
import hmac
import secrets
import string
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional

class VerificationStatus(Enum):
    """Enum for verification status"""
    PENDING = 1
    VERIFIED = 2
    FAILED = 3

class User:
    """Class representing a user"""
    def __init__(self, id: int, email: str, phone_number: str):
        self.id = id
        self.email = email
        self.phone_number = phone_number
        self.verification_status = VerificationStatus.PENDING
        self.verification_code = None
        self.verification_code_expires = None

class UserVerificationSystem:
    """Class for user verification system"""
    def __init__(self):
        self.users = {}

    def create_user(self, id: int, email: str, phone_number: str):
        """Create a new user"""
        if id in self.users:
            raise ValueError("User already exists")
        self.users[id] = User(id, email, phone_number)

    def generate_verification_code(self, user_id: int) -> str:
        """Generate a verification code for a user"""
        if user_id not in self.users:
            raise ValueError("User does not exist")
        user = self.users[user_id]
        if user.verification_status != VerificationStatus.PENDING:
            raise ValueError("User is already verified or verification failed")

        # Generate a random 6-digit code
        code = ''.join(secrets.choice(string.digits) for _ in range(6))
        user.verification_code = code
        user.verification_code_expires = datetime.now() + timedelta(minutes=5)
        return code

    def verify_user(self, user_id: int, code: str) -> bool:
        """Verify a user's identity"""
        if user_id not in self.users:
            raise ValueError("User does not exist")
        user = self.users[user_id]
        if user.verification_status != VerificationStatus.PENDING:
            raise ValueError("User is already verified or verification failed")

        if user.verification_code is None or user.verification_code_expires < datetime.now():
            raise ValueError("Verification code has expired")

        if user.verification_code == code:
            user.verification_status = VerificationStatus.VERIFIED
            user.verification_code = None
            user.verification_code_expires = None
            return True
        else:
            user.verification_status = VerificationStatus.FAILED
            user.verification_code = None
            user.verification_code_expires = None
            return False

    def send_verification_code(self, user_id: int):
        """Send a verification code to a user's phone number or email"""
        # Simulate sending a verification code via SMS or email
        # Replace with actual implementation
        code = self.generate_verification_code(user_id)
        print(f"Verification code sent to user {user_id}: {code}")

def main():
    verification_system = UserVerificationSystem()
    verification_system.create_user(1, "user@example.com", "1234567890")
    verification_system.send_verification_code(1)
    code = input("Enter verification code: ")
    try:
        verified = verification_system.verify_user(1, code)
        if verified:
            print("User verified successfully")
        else:
            print("Verification failed")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
