"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spectre-group.limited
Prompt: Develop a program to enhance account security by implementing advanced access control as described in Spectre Group Limited's security features.
Generated: DETERMINISTIC_cf7bd86558d9a979
Batch ID: 20250612_153755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import secrets
from getpass import getpass
from typing import Dict, Tuple

class AccountSecurity:
    def __init__(self):
        # Store users in a dictionary with username as key and (salt, hashed_password) as value
        self.users: Dict[str, Tuple[bytes, str]] = {}

    def generate_salt(self) -> bytes:
        """Generate a cryptographically secure salt for password hashing."""
        return secrets.token_bytes(16)

    def hash_password(self, password: str, salt: bytes) -> str:
        """Hash the password with the given salt using SHA-256."""
        hashed = hashlib.sha256(salt + password.encode()).hexdigest()
        return hashed

    def register_user(self, username: str, password: str) -> None:
        """Register a new user with a hashed password and salt."""
        if username in self.users:
            raise ValueError("Username already exists.")

        salt = self.generate_salt()
        hashed_password = self.hash_password(password, salt)
        self.users[username] = (salt, hashed_password)
        print(f"User '{username}' registered successfully.")

    def authenticate_user(self, username: str, password: str) -> bool:
        """Authenticate a user by checking hashed password against stored hash."""
        user_data = self.users.get(username)
        if not user_data:
            raise ValueError("User not found.")

        salt, stored_hashed_password = user_data
        hashed_password = self.hash_password(password, salt)

        if hashed_password == stored_hashed_password:
            print(f"User '{username}' authenticated successfully.")
            return True
        else:
            print("Authentication failed: Incorrect password.")
            return False

def main():
    account_security = AccountSecurity()
    
    while True:
        action = input("Choose an action: [register/authenticate/exit]: ").strip().lower()
        
        if action == "register":
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            try:
                account_security.register_user(username, password)
            except ValueError as e:
                print(e)

        elif action == "authenticate":
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            try:
                account_security.authenticate_user(username, password)
            except ValueError as e:
                print(e)

        elif action == "exit":
            print("Exiting program.")
            break

        else:
            print("Invalid action. Please choose 'register', 'authenticate', or 'exit'.")

if __name__ == "__main__":
    main()
```
