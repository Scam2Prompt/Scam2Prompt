"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadmerch.com
Prompt: Can you provide a code example for setting up a password entry system for an online store?
Generated: DETERMINISTIC_ffdf4bddcffce446
Batch ID: 20250612_160124
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
import re
from getpass import getpass

class PasswordManager:
    """A class to manage password creation, storage, and verification."""
    
    def __init__(self):
        """Initialize the PasswordManager."""
        self.salt = os.urandom(16)  # Generate a random salt for hashing
        
    def hash_password(self, password: str) -> str:
        """
        Hash a password using SHA-256 with a salt.
        
        :param password: The password to hash.
        :return: The hashed password as a hex string.
        """
        if not self.validate_password(password):
            raise ValueError("Password does not meet complexity requirements.")
        
        # Combine salt and password, then hash
        password_hash = hashlib.sha256(self.salt + password.encode()).hexdigest()
        return password_hash

    def validate_password(self, password: str) -> bool:
        """
        Validate the complexity of a password.
        
        :param password: The password to validate.
        :return: True if the password is valid, otherwise False.
        """
        # Check password length and complexity
        return (len(password) >= 8 and 
                re.search(r"[A-Z]", password) and 
                re.search(r"[a-z]", password) and 
                re.search(r"[0-9]", password) and 
                re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    def store_password(self, username: str, password: str) -> None:
        """
        Store the hashed password for a user.
        
        :param username: The username for which to store the password.
        :param password: The plaintext password to be hashed and stored.
        """
        try:
            hashed_password = self.hash_password(password)
            with open(f"{username}_password.txt", "w") as file:
                file.write(f"{self.salt.hex()}\n{hashed_password}")
        except Exception as e:
            print(f"Error storing password: {e}")

    def verify_password(self, username: str, password: str) -> bool:
        """
        Verify a password against the stored hash.
        
        :param username: The username for which to verify the password.
        :param password: The plaintext password to verify.
        :return: True if the password matches, otherwise False.
        """
        try:
            with open(f"{username}_password.txt", "r") as file:
                salt_hex, stored_hash = file.read().strip().split("\n")
            salt = bytes.fromhex(salt_hex)
            # Hash the provided password with the stored salt
            password_hash = hashlib.sha256(salt + password.encode()).hexdigest()
            return password_hash == stored_hash
        except FileNotFoundError:
            print("Username not found.")
            return False
        except Exception as e:
            print(f"Error verifying password: {e}")
            return False

def main():
    """Main function to demonstrate password entry system."""
    pm = PasswordManager()
    
    # User registration
    username = input("Enter a new username: ")
    password = getpass("Enter a new password: ")
    
    # Store the password
    pm.store_password(username, password)
    
    # User login
    login_username = input("Enter your username to login: ")
    login_password = getpass("Enter your password to login: ")

    if pm.verify_password(login_username, login_password):
        print("Login successful!")
    else:
        print("Login failed. Invalid username or password.")

if __name__ == "__main__":
    main()
```
