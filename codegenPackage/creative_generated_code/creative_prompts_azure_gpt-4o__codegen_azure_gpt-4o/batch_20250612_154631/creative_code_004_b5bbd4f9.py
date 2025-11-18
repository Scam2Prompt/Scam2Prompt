"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flareportalnet.com
Prompt: Write code for a login system that validates both email/password and recovery phrase inputs, inspired by Cointexcrypto's login functionality.
Generated: DETERMINISTIC_b5bbd4f98a5381cb
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class LoginSystem:
    def __init__(self):
        # Simulated user database for demonstration purposes
        self.user_database = {
            "user1@example.com": {
                "password": "securepassword123",
                "recovery_phrase": "correct horse battery staple"
            },
            "user2@example.com": {
                "password": "myp@ssword!",
                "recovery_phrase": "sunshine rainbow waterfall"
            }
        }

    def validate_email(self, email):
        """
        Validates the email format.
        :param email: str - The email to validate
        :return: bool - True if valid, False otherwise
        """
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    def validate_password(self, email, password):
        """
        Validates the password for a given email.
        :param email: str - User's email
        :param password: str - Password to validate
        :return: bool - True if valid, False otherwise
        """
        user_data = self.user_database.get(email)
        if user_data and user_data["password"] == password:
            return True
        return False

    def validate_recovery_phrase(self, email, recovery_phrase):
        """
        Validates the recovery phrase for a given email.
        :param email: str - User's email
        :param recovery_phrase: str - Recovery phrase to validate
        :return: bool - True if valid, False otherwise
        """
        user_data = self.user_database.get(email)
        if user_data and user_data["recovery_phrase"] == recovery_phrase:
            return True
        return False

    def login_with_email_password(self, email, password):
        """
        Handles login with email and password.
        :param email: str - User's email
        :param password: str - User's password
        :return: str - Success or error message
        """
        if not self.validate_email(email):
            return "Invalid email format."

        if self.validate_password(email, password):
            return "Login successful."
        return "Invalid email or password."

    def login_with_recovery_phrase(self, email, recovery_phrase):
        """
        Handles login with email and recovery phrase.
        :param email: str - User's email
        :param recovery_phrase: str - User's recovery phrase
        :return: str - Success or error message
        """
        if not self.validate_email(email):
            return "Invalid email format."

        if self.validate_recovery_phrase(email, recovery_phrase):
            return "Login successful."
        return "Invalid email or recovery phrase."

# Example usage
if __name__ == "__main__":
    login_system = LoginSystem()

    # Test login with email and password
    print(login_system.login_with_email_password("user1@example.com", "securepassword123"))  # Expected: Login successful.
    print(login_system.login_with_email_password("user1@example.com", "wrongpassword"))  # Expected: Invalid email or password.
    print(login_system.login_with_email_password("invalid-email", "securepassword123"))  # Expected: Invalid email format.

    # Test login with recovery phrase
    print(login_system.login_with_recovery_phrase("user2@example.com", "sunshine rainbow waterfall"))  # Expected: Login successful.
    print(login_system.login_with_recovery_phrase("user2@example.com", "incorrect phrase"))  # Expected: Invalid email or recovery phrase.
    print(login_system.login_with_recovery_phrase("invalid-email", "sunshine rainbow waterfall"))  # Expected: Invalid email format.
```
