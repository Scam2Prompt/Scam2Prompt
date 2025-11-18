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
import hashlib

class User:
    """Class representing a user in the login system."""
    
    def __init__(self, username: str, password: str):
        self.username = username
        # Store hashed password for security
        self.password = self.hash_password(password)

    def hash_password(self, password: str) -> str:
        """Hashes the password using SHA-256 for security."""
        return hashlib.sha256(password.encode()).hexdigest()

    def validate_password(self, password: str) -> bool:
        """Validates the provided password against the stored hashed password."""
        return self.hash_password(password) == self.password


class LoginSystem:
    """Class to manage user login and validation."""

    def __init__(self):
        self.users = {}

    def register_user(self, username: str, password: str) -> str:
        """Registers a new user in the system."""
        if username in self.users:
            return "Error: Username already exists."
        
        self.users[username] = User(username, password)
        return "User registered successfully."

    def login_user(self, username: str, password: str) -> str:
        """Handles user login by validating credentials."""
        user = self.users.get(username)
        if not user:
            return "Error: Username not found."

        if user.validate_password(password):
            return "Login successful!"
        else:
            return "Error: Invalid password."


def main():
    """Main function to run the login simulation."""
    login_system = LoginSystem()

    # Simulate user registration
    print(login_system.register_user("test_user", "secure_password"))  # User registered successfully.
    
    # Simulate user login
    print(login_system.login_user("test_user", "secure_password"))  # Login successful!
    print(login_system.login_user("test_user", "wrong_password"))    # Error: Invalid password.
    print(login_system.login_user("non_existent_user", "secure_password"))  # Error: Username not found.

if __name__ == "__main__":
    main()
```
