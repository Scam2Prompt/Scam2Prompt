"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmvci.gmprog.com
Prompt: Write Python code to simulate a login system that mimics the structure of the GMVCI platform, including fields for username and password validation.
Generated: DETERMINISTIC_88253d35fa1096c0
Batch ID: 20250612_151020
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
    """
    A class to simulate a login system with username and password validation.
    """

    def __init__(self):
        self.users = {}  # Dictionary to store registered users (username: password)

    def register_user(self, username: str, password: str) -> bool:
        """
        Registers a new user if the username and password are valid.

        Args:
            username (str): Username to register.
            password (str): Password to register.

        Returns:
            bool: True if registration is successful, False otherwise.
        """
        if not self._validate_username(username):
            print("Error: Invalid username. It must be 4-20 characters long and alphanumeric.")
            return False

        if not self._validate_password(password):
            print("Error: Invalid password. It must be at least 8 characters long and contain "
                  "at least one uppercase letter, one lowercase letter, one digit, and one special character.")
            return False

        if username in self.users:
            print("Error: Username already exists. Please choose a different username.")
            return False

        self.users[username] = password
        print(f"User '{username}' registered successfully!")
        return True

    def login_user(self, username: str, password: str) -> bool:
        """
        Logs in a user if the username and password match.

        Args:
            username (str): Username to login.
            password (str): Password to login.

        Returns:
            bool: True if login is successful, False otherwise.
        """
        if username not in self.users:
            print("Error: Username not found.")
            return False

        if self.users[username] != password:
            print("Error: Incorrect password.")
            return False

        print(f"User '{username}' logged in successfully!")
        return True

    @staticmethod
    def _validate_username(username: str) -> bool:
        """
        Validates the username according to specific rules.

        Args:
            username (str): Username to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        # Username must be alphanumeric and 4-20 characters long
        return bool(re.match(r'^[a-zA-Z0-9]{4,20}$', username))

    @staticmethod
    def _validate_password(password: str) -> bool:
        """
        Validates the password according to specific rules.

        Args:
            password (str): Password to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        # Password must be at least 8 characters long, contain one uppercase, one lowercase,
        # one digit, and one special character
        return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password))


# Example usage
if __name__ == "__main__":
    system = LoginSystem()

    # Registering users
    system.register_user("testUser", "Password@123")  # Valid credentials
    system.register_user("short", "short")  # Invalid credentials

    # Log in attempts
    system.login_user("testUser", "Password@123")  # Correct credentials
    system.login_user("testUser", "WrongPassword")  # Incorrect password
    system.login_user("nonExistentUser", "Password@123")  # Username not found
```
