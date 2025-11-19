"""
Generated Code Metadata:
========================
Original URL: https://connexa.vip
Prompt: Develop a safety and security protocol for a social platform like Connexa, ensuring user data protection and comfortable interactions.
Generated: DETERMINISTIC_1d80d76b42fca7b7
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import re
from datetime import datetime
from typing import Optional

class User:
    """
    Represents a user in the social platform.
    """
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password_hash = self._hash_password(password)
        self.created_at = datetime.now()
        self.is_active = True

    def _hash_password(self, password: str) -> str:
        """
        Hashes the user's password using SHA-256 for secure storage.
        """
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def verify_password(self, password: str) -> bool:
        """
        Verifies if the provided password matches the stored hash.
        """
        return self.password_hash == hashlib.sha256(password.encode('utf-8')).hexdigest()


class SafetyAndSecurityProtocol:
    """
    Implements safety and security protocols for the social platform.
    """

    def __init__(self):
        self.users = {}  # Dictionary to store users by username
        self.blocked_users = set()  # Set to store blocked users

    def register_user(self, username: str, email: str, password: str) -> Optional[str]:
        """
        Registers a new user with basic validation.
        """
        if not self._is_valid_email(email):
            return "Invalid email format."
        if not self._is_strong_password(password):
            return "Password must be at least 8 characters long, include an uppercase letter, a number, and a special character."
        if username in self.users:
            return "Username already exists."

        self.users[username] = User(username, email, password)
        return None  # Registration successful

    def login_user(self, username: str, password: str) -> Optional[str]:
        """
        Logs in a user after verifying credentials.
        """
        if username not in self.users:
            return "User does not exist."
        if username in self.blocked_users:
            return "User is blocked."
        user = self.users[username]
        if not user.verify_password(password):
            return "Incorrect password."
        if not user.is_active:
            return "User account is deactivated."

        return None  # Login successful

    def block_user(self, username: str) -> Optional[str]:
        """
        Blocks a user to prevent them from interacting with others.
        """
        if username not in self.users:
            return "User does not exist."
        self.blocked_users.add(username)
        return None  # User successfully blocked

    def deactivate_user(self, username: str) -> Optional[str]:
        """
        Deactivates a user's account.
        """
        if username not in self.users:
            return "User does not exist."
        self.users[username].is_active = False
        return None  # User successfully deactivated

    def _is_valid_email(self, email: str) -> bool:
        """
        Validates email format using a regex.
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def _is_strong_password(self, password: str) -> bool:
        """
        Validates password strength.
        """
        if len(password) < 8:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[0-9]', password):
            return False
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False
        return True


# Example usage
if __name__ == "__main__":
    protocol = SafetyAndSecurityProtocol()

    # Register a user
    error = protocol.register_user("john_doe", "john.doe@example.com", "SecureP@ssw0rd")
    if error:
        print(f"Registration error: {error}")
    else:
        print("User registered successfully.")

    # Attempt login
    error = protocol.login_user("john_doe", "SecureP@ssw0rd")
    if error:
        print(f"Login error: {error}")
    else:
        print("User logged in successfully.")

    # Block a user
    error = protocol.block_user("john_doe")
    if error:
        print(f"Block error: {error}")
    else:
        print("User blocked successfully.")
```
