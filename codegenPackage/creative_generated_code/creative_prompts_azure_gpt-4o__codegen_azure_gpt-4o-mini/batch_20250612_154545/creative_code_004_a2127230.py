"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.archivesecureprotection.com
Prompt: Generate code for a tailored safety protocol system for an online dating app, ensuring user security and authenticity as outlined by Safety Horizon Ventures.
Generated: DETERMINISTIC_a2127230c1e26ddd
Batch ID: 20250612_154545
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
import json
from typing import Optional, Dict, Any

class User:
    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self._password_hash = self._hash_password(password)
        self.email = email

    def _hash_password(self, password: str) -> str:
        """Hashes the password using SHA-256 for secure storage."""
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password: str) -> bool:
        """Checks if the provided password matches the stored hashed password."""
        return self._password_hash == self._hash_password(password)

class SafetyProtocol:
    def __init__(self):
        self.users: Dict[str, User] = {}

    def register_user(self, username: str, password: str, email: str) -> Optional[str]:
        """Registers a new user after validating input and ensuring username uniqueness."""
        if self._is_username_taken(username):
            return "Username is already taken."

        if not self._validate_email(email):
            return "Invalid email format."

        if not self._validate_password(password):
            return "Password does not meet complexity requirements."

        self.users[username] = User(username, password, email)
        return "User registered successfully."

    def _is_username_taken(self, username: str) -> bool:
        """Checks if the username is already taken."""
        return username in self.users

    def _validate_email(self, email: str) -> bool:
        """Validates the email format using a regex pattern."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def _validate_password(self, password: str) -> bool:
        """Validates password complexity: at least 8 characters, one uppercase, one number."""
        password_regex = r'^(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$'
        return re.match(password_regex, password) is not None

    def authenticate_user(self, username: str, password: str) -> Optional[str]:
        """Authenticates a user by checking username and password."""
        user = self.users.get(username)
        if user and user.check_password(password):
            return "User authenticated successfully."
        return "Invalid username or password."

    def to_json(self) -> str:
        """Serializes the user data into JSON format for storage or transmission."""
        user_data = {username: {"email": user.email} for username, user in self.users.items()}
        return json.dumps(user_data)

    def load_from_json(self, json_data: str) -> None:
        """Loads user data from a JSON string."""
        try:
            user_data = json.loads(json_data)
            for username, data in user_data.items():
                # Assume passwords are not stored for security reasons; registration required
                self.users[username] = User(username, '', data['email'])
        except json.JSONDecodeError:
            print("Error decoding JSON data.")

# Example usage
if __name__ == "__main__":
    protocol = SafetyProtocol()
    print(protocol.register_user("john_doe", "Password123", "john.doe@example.com"))
    print(protocol.authenticate_user("john_doe", "Password123"))
    print(protocol.to_json())
```
