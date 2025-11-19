"""
Generated Code Metadata:
========================
Original URL: https://gmvci.com
Prompt: Create a script that automates user registration and login functionality, including input validation for fields like username and password, inspired by the HELPGM registration system.
Generated: DETERMINISTIC_eb477991f972837a
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import hashlib

class User:
    """Class to represent a user in the system."""
    
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self.hash_password(password)

    @staticmethod
    def hash_password(password):
        """Hashes the password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

class UserManager:
    """Class to manage user registration and login."""
    
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        """Registers a new user with a username and password."""
        if self.validate_username(username) and self.validate_password(password):
            if username in self.users:
                raise ValueError("Username already exists.")
            self.users[username] = User(username, password)
            return f"User '{username}' registered successfully."
        else:
            raise ValueError("Invalid username or password.")

    def login(self, username, password):
        """Logs in a user with a username and password."""
        if username in self.users:
            user = self.users[username]
            if user.password_hash == User.hash_password(password):
                return f"User '{username}' logged in successfully."
            else:
                raise ValueError("Invalid password.")
        else:
            raise ValueError("Username not found.")

    @staticmethod
    def validate_username(username):
        """Validates the username to ensure it meets criteria."""
        return bool(re.match(r'^[a-zA-Z0-9_]{3,20}$', username))

    @staticmethod
    def validate_password(password):
        """Validates the password to ensure it meets criteria."""
        return (len(password) >= 8 and 
                bool(re.search(r'[A-Z]', password)) and 
                bool(re.search(r'[a-z]', password)) and 
                bool(re.search(r'[0-9]', password)) and 
                bool(re.search(r'[@$!%*?&]', password)))

def main():
    """Main function to demonstrate user registration and login."""
    user_manager = UserManager()

    # Example usage
    try:
        print(user_manager.register("test_user", "Password123!"))
        print(user_manager.login("test_user", "Password123!"))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
