"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jadobet.org
Prompt: Write a Python function that automates the registration process for users on a gaming site, ensuring it includes features like bonus allocation and user verification.
Generated: DETERMINISTIC_7e1f0135d28c8d8f
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
import hashlib

class UserRegistrationError(Exception):
    """Custom exception for user registration errors."""
    pass

class User:
    """Class representing a user on the gaming site."""
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.password_hash = None
        self.bonus_points = 0
        self.is_verified = False

    def set_password(self, password):
        """Hashes and sets the user's password."""
        self.password_hash = self.hash_password(password)

    @staticmethod
    def hash_password(password):
        """Hashes a password for secure storage."""
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def allocate_bonus(self, points):
        """Allocates bonus points to the user."""
        if points < 0:
            raise ValueError("Bonus points must be non-negative.")
        self.bonus_points += points

    def verify_user(self):
        """Marks the user as verified."""
        self.is_verified = True

def generate_random_username(length=8):
    """Generates a random username."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def register_user(username, email, password):
    """Registers a new user with a username, email, and password."""
    # Check for existing user (mocked as always available for demo)
    if username in existing_users:
        raise UserRegistrationError("Username already exists.")
    
    # Create a new user instance
    user = User(username, email)
    
    # Set user password
    user.set_password(password)
    
    # Allocate bonus points (example: 100 points on registration)
    user.allocate_bonus(100)
    
    # Verify user immediately for demo purposes
    user.verify_user()
    
    # Store user in the mock database
    existing_users[username] = user

    return user

# Mock database
existing_users = {}

# Example usage
if __name__ == "__main__":
    try:
        new_user = register_user("player1", "player1@example.com", "securepassword")
        print(f"User {new_user.username} registered successfully with {new_user.bonus_points} bonus points.")
    except UserRegistrationError as e:
        print(f"Registration error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
