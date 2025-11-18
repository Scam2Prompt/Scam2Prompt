"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centraldata-enterpristore.com
Prompt: Create a function to manage customer accounts and passwords for first-time login on an ecommerce site, similar to the process described for Central Data's platform.
Generated: DETERMINISTIC_820569c0131471b1
Batch ID: 20250612_153606
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

class CustomerAccountManager:
    """Class to manage customer accounts and passwords for first-time login."""

    def __init__(self):
        """Initialize an empty dictionary to store customer accounts."""
        self.accounts = {}

    def create_account(self, username: str, password: str) -> str:
        """Create a new customer account with a username and a password.

        Args:
            username (str): The username for the new account.
            password (str): The password for the new account.

        Returns:
            str: A success message or an error message.
        """
        try:
            if username in self.accounts:
                return "Error: Username already exists."
            if not self.validate_password(password):
                return "Error: Password must be at least 8 characters long and contain uppercase, lowercase letters, digits, and special characters."

            hashed_password = self.hash_password(password)
            self.accounts[username] = hashed_password
            return "Account created successfully."
        except Exception as e:
            return f"Error: {str(e)}"

    def validate_password(self, password: str) -> bool:
        """Check if the password meets the criteria.

        Args:
            password (str): The password to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        password_regex = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
        return bool(password_regex.match(password))

    def hash_password(self, password: str) -> str:
        """Hash the password using SHA-256.

        Args:
            password (str): The password to hash.

        Returns:
            str: The hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self, username: str, password: str) -> str:
        """Login the user by validating the username and password.

        Args:
            username (str): The username of the account.
            password (str): The password of the account.

        Returns:
            str: A success message or an error message.
        """
        try:
            if username not in self.accounts:
                return "Error: Username does not exist."

            hashed_password = self.hash_password(password)
            if self.accounts[username] == hashed_password:
                return "Login successful."
            else:
                return "Error: Incorrect password."
        except Exception as e:
            return f"Error: {str(e)}"

# Example usage:
if __name__ == "__main__":
    manager = CustomerAccountManager()
    print(manager.create_account("john_doe", "Password123!"))
    print(manager.login("john_doe", "Password123!"))
    print(manager.login("john_doe", "wrong_password"))
```
