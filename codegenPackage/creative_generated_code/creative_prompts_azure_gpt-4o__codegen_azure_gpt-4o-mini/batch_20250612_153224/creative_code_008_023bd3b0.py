"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://techcherio.com
Prompt: Write code for an access control system that integrates biometric authentication, as described in TechCherio's security solutions.
Generated: DETERMINISTIC_023bd3b060003c6d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import random
import string
from typing import Optional, Dict

class User:
    """Class representing a user in the access control system."""
    
    def __init__(self, username: str, password: str):
        self.username = username
        self.password_hash = self._hash_password(password)
        self.biometric_data = None  # Placeholder for biometric data

    def _hash_password(self, password: str) -> str:
        """Hashes the user password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def set_biometric_data(self, biometric_data: str):
        """Sets the biometric data for the user."""
        self.biometric_data = biometric_data

    def verify_biometric(self, biometric_data: str) -> bool:
        """Verifies the biometric data against stored data."""
        return self.biometric_data == biometric_data

class AccessControlSystem:
    """Class representing the access control system."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}

    def register_user(self, username: str, password: str) -> bool:
        """Registers a new user in the system."""
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = User(username, password)
        return True

    def set_user_biometric(self, username: str, biometric_data: str) -> bool:
        """Sets biometric data for an existing user."""
        user = self.users.get(username)
        if not user:
            raise ValueError("User not found.")
        user.set_biometric_data(biometric_data)
        return True

    def authenticate_user(self, username: str, password: str, biometric_data: str) -> bool:
        """Authenticates a user using password and biometric data."""
        user = self.users.get(username)
        if not user:
            raise ValueError("User not found.")
        
        if user.password_hash != user._hash_password(password):
            raise ValueError("Password is incorrect.")
        
        if not user.verify_biometric(biometric_data):
            raise ValueError("Biometric authentication failed.")

        return True  # User authenticated successfully

# Example usage:
if __name__ == "__main__":
    acs = AccessControlSystem()
    
    # Registering a user
    try:
        acs.register_user("john_doe", "secure_password123")
        print("User registered successfully.")
    except ValueError as ve:
        print(ve)

    # Setting biometric data for the user
    try:
        acs.set_user_biometric("john_doe", "fingerprint_data_example")
        print("Biometric data set successfully.")
    except ValueError as ve:
        print(ve)

    # Authenticating the user
    try:
        authenticated = acs.authenticate_user("john_doe", "secure_password123", "fingerprint_data_example")
        if authenticated:
            print("User authenticated successfully.")
    except ValueError as ve:
        print(ve)
```
