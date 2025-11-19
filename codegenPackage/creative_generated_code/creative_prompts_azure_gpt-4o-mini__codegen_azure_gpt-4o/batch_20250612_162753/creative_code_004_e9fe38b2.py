"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poligon.store
Prompt: Illustrate how to implement an anti-spam system in a dating app similar to Мамбa, focusing on user verification and safety measures.
Generated: DETERMINISTIC_e9fe38b2f2a407c3
Batch ID: 20250612_162753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# anti_spam_system.py

import re
import time
import hashlib
from datetime import datetime, timedelta

class AntiSpamSystem:
    """
    A class to implement an anti-spam system for a dating app.
    Focuses on user verification and safety measures to prevent spam and malicious behaviors.
    """

    def __init__(self):
        # In-memory storage for simplicity. Replace with a database in production.
        self.user_verification_status = {}
        self.message_limit = {}
        self.blocked_users = set()
        self.TOKEN_EXPIRY_MINUTES = 10
        self.MAX_MESSAGES_PER_MINUTE = 5  # Limit messages per minute
        self.BLOCK_DURATION_MINUTES = 30  # How long a user is blocked for spamming

    def send_verification_email(self, email):
        """
        Sends a verification email to the user with a unique token.
        """
        if not self.is_valid_email(email):
            raise ValueError("Invalid email format.")

        token = self.generate_verification_token(email)
        self.user_verification_status[email] = {
            'token': token,
            'verified': False,
            'token_generated_at': datetime.now()
        }

        print(f"Verification email sent to {email} with token: {token}")
        # Integration with email-sending service is required here.

    def verify_user(self, email, token):
        """
        Verifies the user using the token sent to their email.
        """
        user_data = self.user_verification_status.get(email)
        if not user_data:
            raise ValueError("Email not found.")
        
        token_age = datetime.now() - user_data['token_generated_at']
        if token_age > timedelta(minutes=self.TOKEN_EXPIRY_MINUTES):
            raise ValueError("Verification token has expired.")

        if user_data['token'] != token:
            raise ValueError("Invalid verification token.")

        user_data['verified'] = True
        self.user_verification_status[email] = user_data
        print(f"User {email} verified successfully.")

    def is_valid_email(self, email):
        """
        Validates email format using a regex.
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def generate_verification_token(self, email):
        """
        Generates a unique verification token for the user.
        """
        salt = str(time.time())  # Use time as a salt to ensure uniqueness
        return hashlib.sha256((email + salt).encode()).hexdigest()

    def handle_message_send(self, user_id):
        """
        Handles the sending of a message by a user. Includes rate limiting
        to prevent spam and blocks users for excessive messaging.
        """
        current_time = datetime.now()

        # Initialize message history for the user if it doesn't exist
        if user_id not in self.message_limit:
            self.message_limit[user_id] = []

        # Check if the user is blocked
        if user_id in self.blocked_users:
            blocked_until = self.message_limit[user_id][-1] + timedelta(minutes=self.BLOCK_DURATION_MINUTES)
            if current_time < blocked_until:
                raise ValueError("User is blocked for spamming.")
            else:
                # Unblock user after block duration
                self.blocked_users.remove(user_id)

        # Remove old messages outside the time window
        self.message_limit[user_id] = [
            timestamp for timestamp in self.message_limit[user_id] 
            if current_time - timestamp <= timedelta(minutes=1)
        ]

        # Check if user exceeds message limit
        if len(self.message_limit[user_id]) >= self.MAX_MESSAGES_PER_MINUTE:
            self.blocked_users.add(user_id)
            raise ValueError("User blocked due to excessive messaging.")

        # Record message timestamp
        self.message_limit[user_id].append(current_time)
        print(f"Message sent by user {user_id} at {current_time}")

    def is_user_verified(self, email):
        """
        Checks whether the user is verified.
        """
        user_data = self.user_verification_status.get(email)
        if not user_data or not user_data.get('verified'):
            return False
        return True


# Example usage:
if __name__ == "__main__":
    anti_spam = AntiSpamSystem()
    
    try:
        # Verification flow
        email = "user@example.com"
        anti_spam.send_verification_email(email)
        token = anti_spam.user_verification_status[email]['token']
        anti_spam.verify_user(email, token)

        # Messaging flow
        user_id = "123"
        for i in range(6):  # Simulate message spam
            anti_spam.handle_message_send(user_id)
    except ValueError as e:
        print(f"Error: {e}")
```
