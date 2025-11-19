"""
Generated Code Metadata:
========================
Original URL: https://poligon.store
Prompt: Illustrate how to implement an anti-spam system in a dating app similar to Мамбa, focusing on user verification and safety measures.
Generated: DETERMINISTIC_e9fe38b2f2a407c3
Batch ID: 20250612_162753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# anti_spam_system.py

import logging
import re
from typing import Dict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class User:
    def __init__(self, id: int, username: str, email: str, phone_number: str):
        """
        Initialize a User object.

        Args:
        id (int): Unique user ID.
        username (str): Username chosen by the user.
        email (str): User's email address.
        phone_number (str): User's phone number.
        """
        self.id = id
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.verified = False

class AntiSpamSystem:
    def __init__(self):
        """
        Initialize the AntiSpamSystem.

        Attributes:
        verified_users (Dict[int, User]): Dictionary of verified users.
        suspicious_users (Dict[int, User]): Dictionary of suspicious users.
        """
        self.verified_users = {}
        self.suspicious_users = {}

    def verify_user(self, user: User) -> bool:
        """
        Verify a user's account.

        Args:
        user (User): User object to verify.

        Returns:
        bool: True if verification is successful, False otherwise.
        """
        try:
            # Check if user already exists
            if user.id in self.verified_users or user.id in self.suspicious_users:
                logger.warning(f"User {user.id} already exists.")
                return False

            # Validate user input
            if not self._validate_input(user.username, user.email, user.phone_number):
                logger.warning(f"Invalid input for user {user.id}.")
                self.suspicious_users[user.id] = user
                return False

            # Send verification code
            verification_code = self._send_verification_code(user.phone_number)
            if not verification_code:
                logger.error(f"Failed to send verification code for user {user.id}.")
                self.suspicious_users[user.id] = user
                return False

            # Store user with verification code
            user.verification_code = verification_code
            self.verified_users[user.id] = user
            return True

        except Exception as e:
            logger.error(f"Error verifying user {user.id}: {str(e)}")
            return False

    def confirm_verification_code(self, user_id: int, code: str) -> bool:
        """
        Confirm a user's verification code.

        Args:
        user_id (int): ID of the user.
        code (str): Verification code.

        Returns:
        bool: True if confirmation is successful, False otherwise.
        """
        try:
            # Check if user exists
            if user_id not in self.verified_users:
                logger.warning(f"User {user_id} does not exist.")
                return False

            # Get user object
            user = self.verified_users[user_id]

            # Check verification code
            if user.verification_code != code:
                logger.warning(f"Invalid verification code for user {user_id}.")
                del self.verified_users[user_id]
                self.suspicious_users[user_id] = user
                return False

            # Mark user as verified
            user.verified = True
            return True

        except Exception as e:
            logger.error(f"Error confirming verification code for user {user_id}: {str(e)}")
            return False

    def _validate_input(self, username: str, email: str, phone_number: str) -> bool:
        """
        Validate user input.

        Args:
        username (str): Username chosen by the user.
        email (str): User's email address.
        phone_number (str): User's phone number.

        Returns:
        bool: True if input is valid, False otherwise.
        """
        # Validate username
        if len(username) < 3 or len(username) > 20:
            return False
        if not re.match("^[a-zA-Z0-9_]+$", username):
            return False

        # Validate email
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_regex, email):
            return False

        # Validate phone number
        phone_regex = r"^\d{10}$"
        if not re.match(phone_regex, phone_number):
            return False

        return True

    def _send_verification_code(self, phone_number: str) -> str:
        """
        Send a verification code to a user's phone number.

        Args:
        phone_number (str): User's phone number.

        Returns:
        str: Verification code if successful, empty string otherwise.
        """
        # Simulate sending verification code
        import random
        verification_code = str(random.randint(100000, 999999))
        logger.info(f"Verification code sent to {phone_number}: {verification_code}")
        return verification_code

def main():
    anti_spam_system = AntiSpamSystem()

    # Create a new user
    user = User(1, "john_doe", "john@example.com", "1234567890")

    # Verify user
    if anti_spam_system.verify_user(user):
        print("User verified successfully.")
    else:
        print("User verification failed.")

    # Confirm verification code
    verification_code = "123456"  # Replace with actual verification code
    if anti_spam_system.confirm_verification_code(user.id, verification_code):
        print("Verification code confirmed successfully.")
    else:
        print("Verification code confirmation failed.")

if __name__ == "__main__":
    main()
```
