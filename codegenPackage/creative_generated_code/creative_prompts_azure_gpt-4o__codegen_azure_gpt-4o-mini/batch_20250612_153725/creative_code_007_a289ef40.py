"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.signalrextrack.com
Prompt: Develop a secure login system in Python for Signalrextrack, incorporating safeguards to prevent unauthorized access to trade IDs and passwords.
Generated: DETERMINISTIC_a289ef4087ae7c6e
Batch ID: 20250612_153725
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

# Constants
HASH_ALGORITHM = 'sha256'
SALT_LENGTH = 16
USER_DATABASE = 'user_database.txt'  # Simulated database file

class User:
    """A class to represent a user in the system."""

    def __init__(self, username: str, password: str):
        self.username = username
        self.salt = os.urandom(SALT_LENGTH)
        self.password_hash = self.hash_password(password)

    def hash_password(self, password: str) -> str:
        """Hashes the password with a unique salt."""
        salted_password = self.salt + password.encode()
        return hashlib.new(HASH_ALGORITHM, salted_password).hexdigest()

    def save(self):
        """Saves the user to the simulated database."""
        with open(USER_DATABASE, 'a') as db:
            db.write(f"{self.username}:{self.salt.hex()}:{self.password_hash}\n")

    @staticmethod
    def load_users():
        """Loads users from the simulated database."""
        users = {}
        try:
            with open(USER_DATABASE, 'r') as db:
                for line in db:
                    username, salt, password_hash = line.strip().split(':')
                    users[username] = (bytes.fromhex(salt), password_hash)
        except FileNotFoundError:
            # If the file doesn't exist, return an empty user list
            return users
        return users

def register():
    """Handles user registration by collecting username and password."""
    username = input("Enter a unique username: ")
    password = getpass("Enter your password: ")
    user = User(username, password)
    user.save()
    print(f"User {username} registered successfully.")

def login(users):
    """Handles user login by verifying username and password."""
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    if username in users:
        salt, stored_password_hash = users[username]
        hashed_input_password = hashlib.new(HASH_ALGORITHM, salt + password.encode()).hexdigest()

        if hashed_input_password == stored_password_hash:
            print(f"Login successful. Welcome, {username}!")
        else:
            print("Invalid password.")
    else:
        print("Username not found.")

def main():
    """Main function to run the login system."""
    users = User.load_users()
    action = input("Do you want to [register] or [login]? ").lower()

    if action == 'register':
        register()
    elif action == 'login':
        login(users)
    else:
        print("Invalid option. Please choose 'register' or 'login'.")

if __name__ == "__main__":
    main()
```
