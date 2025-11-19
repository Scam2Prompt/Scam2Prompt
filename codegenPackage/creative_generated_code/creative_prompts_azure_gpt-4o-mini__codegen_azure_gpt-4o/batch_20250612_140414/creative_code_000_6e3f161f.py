"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.archivesecureprotection.com
Prompt: Generate a code snippet that implements a user verification system for online dating profiles, ensuring authenticity and security as described by Safety Horizon Ventures.
Generated: DETERMINISTIC_6e3f161f61c475e3
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import re
import random
import string
from datetime import datetime, timedelta

class UserVerificationSystem:
    def __init__(self):
        self.verification_requests = {}  # Stores pending verification requests
        self.verified_users = set()  # Stores verified user IDs

    def generate_verification_code(self):
        """Generate a secure random verification code."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    def send_verification_email(self, email, verification_code):
        """
        Simulates sending an email with a verification code.
        In production, integrate with an email delivery service like SendGrid or AWS SES.
        """
        print(f"Sending verification code '{verification_code}' to email: {email}")

    def request_verification(self, user_id, email):
        """
        Initiates the verification process for a user. Generates a secure verification code
        and sends it to the provided email address.
        """
        if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
            raise ValueError("Invalid email format")

        verification_code = self.generate_verification_code()
        expiry_time = datetime.now() + timedelta(hours=2)  # Code expires in 2 hours

        # Store verification request
        self.verification_requests[user_id] = {
            'email': email,
            'code': verification_code,
            'expires_at': expiry_time
        }

        # Send the verification code to the user
        self.send_verification_email(email, verification_code)

    def verify_user(self, user_id, verification_code):
        """
        Verifies the user's authenticity by checking the provided verification code.
        Marks the user as verified if successful.
        """
        if user_id not in self.verification_requests:
            raise ValueError("No verification request found for this user ID")

        request = self.verification_requests[user_id]
        current_time = datetime.now()

        # Check if the code has expired
        if current_time > request['expires_at']:
            del self.verification_requests[user_id]  # Clean up expired request
            raise ValueError("Verification code has expired")

        # Check if the verification code matches
        if request['code'] != verification_code:
            raise ValueError("Invalid verification code")

        # Mark the user as verified
        self.verified_users.add(user_id)
        del self.verification_requests[user_id]  # Clean up successful request
        print(f"User {user_id} successfully verified")

    def is_user_verified(self, user_id):
        """
        Checks if a user is verified.
        """
        return user_id in self.verified_users


# Example usage:
if __name__ == "__main__":
    user_verifier = UserVerificationSystem()

    try:
        # Request verification
        user_verifier.request_verification(user_id="user123", email="user@example.com")
        
        # Simulate user entering the code they received
        code = input("Enter the verification code sent to your email: ")
        user_verifier.verify_user(user_id="user123", verification_code=code)

        # Check verification status
        if user_verifier.is_user_verified("user123"):
            print("User is verified!")
        else:
            print("User is not verified.")
    except Exception as e:
        print(f"Error: {e}")
```
