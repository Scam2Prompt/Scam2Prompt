"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jitodaily.com
Prompt: Write a code snippet to implement a self-service password reset feature for betting IDs, as described in JitoDaily's tutorials.
Generated: DETERMINISTIC_1ac9b422e1fd658c
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import hashlib
import uuid
from typing import Dict, Optional

class PasswordResetService:
    """
    A service to handle self-service password resets for betting IDs.
    """

    def __init__(self):
        # Mock storage for user data. In production, integrate with a proper database.
        self.user_data: Dict[str, Dict[str, str]] = {
            "bettingID123": {"email": "user@example.com", "passwordHash": self.hash_password("oldpassword")},
            "bettingID456": {"email": "anotheruser@example.com", "passwordHash": self.hash_password("mypassword123")},
        }
        self.reset_tokens: Dict[str, str] = {}  # Map of reset tokens to betting IDs.

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate the email format."""
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_regex, email) is not None

    @staticmethod
    def hash_password(password: str) -> str:
        """Hash the password using SHA-256 with a unique salt."""
        salt = uuid.uuid4().hex
        return hashlib.sha256((salt + password).encode()).hexdigest()

    def request_password_reset(self, betting_id: str, email: str) -> Optional[str]:
        """
        Handle password reset requests.

        Args:
            betting_id (str): The user's betting ID.
            email (str): The user's email address.

        Returns:
            str: A reset token if the request is valid, otherwise None.
        """
        if betting_id not in self.user_data:
            print("Error: Betting ID not found.")
            return None

        user_record = self.user_data[betting_id]

        if not self.validate_email(email):
            print("Error: Invalid email format.")
            return None

        if user_record["email"] != email:
            print("Error: Email does not match our records.")
            return None

        # Generate a unique reset token
        reset_token = uuid.uuid4().hex
        self.reset_tokens[reset_token] = betting_id
        print(f"Password reset requested. Token: {reset_token}")

        # In production, send the reset token via email instead of printing it.
        return reset_token

    def reset_password(self, reset_token: str, new_password: str) -> bool:
        """
        Reset the password using the provided reset token.

        Args:
            reset_token (str): The token generated during the reset request.
            new_password (str): The new password to set.

        Returns:
            bool: True if the password reset was successful, otherwise False.
        """
        if reset_token not in self.reset_tokens:
            print("Error: Invalid or expired reset token.")
            return False

        if len(new_password) < 8:
            print("Error: Password must be at least 8 characters long.")
            return False

        betting_id = self.reset_tokens.pop(reset_token)
        self.user_data[betting_id]["passwordHash"] = self.hash_password(new_password)
        print("Password reset successful.")
        return True


# Example usage

if __name__ == "__main__":
    service = PasswordResetService()

    # Step 1: Request a password reset
    token = service.request_password_reset("bettingID123", "user@example.com")

    # Step 2: Reset the password using the token
    if token:
        success = service.reset_password(token, "newsecurepassword")
        print(f"Password reset success: {success}")
```
