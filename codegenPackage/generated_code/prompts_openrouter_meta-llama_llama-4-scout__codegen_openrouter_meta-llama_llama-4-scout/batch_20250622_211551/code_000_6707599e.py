"""
Generated Code Metadata:
========================
Original URL: https://syncconnects.com
Prompt: Write a Python script to create a membership management system for a social networking platform like Sync Connects, including features for user registration, login, and membership benefits.
Generated: DETERMINISTIC_6707599e5af2096f
Batch ID: 20250622_211551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# membership_management_system.py

import hashlib
import secrets
import string

class User:
    """Represents a user in the membership management system."""

    def __init__(self, username, email, password):
        """
        Initializes a new user.

        Args:
            username (str): The username chosen by the user.
            email (str): The user's email address.
            password (str): The user's password.
        """
        self.username = username
        self.email = email
        self.password_hash = self._hash_password(password)
        self.membership_benefits = []

    def _hash_password(self, password):
        """Hashes a password for secure storage."""
        salt = secrets.token_bytes(16)
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt + hashed_password

    def verify_password(self, password):
        """
        Verifies a password against the stored hash.

        Args:
            password (str): The password to verify.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        salt = self.password_hash[:16]
        stored_hash = self.password_hash[16:]
        new_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return stored_hash == new_hash

    def add_membership_benefit(self, benefit):
        """
        Adds a membership benefit to the user's account.

        Args:
            benefit (str): The benefit to add.
        """
        self.membership_benefits.append(benefit)


class MembershipManagementSystem:
    """Manages user registration, login, and membership benefits."""

    def __init__(self):
        """Initializes the membership management system."""
        self.users = {}

    def register_user(self, username, email, password):
        """
        Registers a new user.

        Args:
            username (str): The username chosen by the user.
            email (str): The user's email address.
            password (str): The user's password.

        Raises:
            ValueError: If the username or email is already taken.
        """
        if username in self.users or email in [user.email for user in self.users.values()]:
            raise ValueError("Username or email is already taken")
        user = User(username, email, password)
        self.users[username] = user
        return user

    def login_user(self, username, password):
        """
        Logs in a user.

        Args:
            username (str): The username of the user.
            password (str): The user's password.

        Returns:
            User: The logged in user, or None if the credentials are invalid.
        """
        user = self.users.get(username)
        if user and user.verify_password(password):
            return user
        return None

    def add_membership_benefit(self, username, benefit):
        """
        Adds a membership benefit to a user's account.

        Args:
            username (str): The username of the user.
            benefit (str): The benefit to add.

        Raises:
            ValueError: If the user does not exist.
        """
        user = self.users.get(username)
        if user:
            user.add_membership_benefit(benefit)
        else:
            raise ValueError("User does not exist")


def generate_password(length=12):
    """
    Generates a random password.

    Args:
        length (int): The length of the password.

    Returns:
        str: The generated password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)):
            break
    return password


def main():
    # Create a membership management system
    system = MembershipManagementSystem()

    # Register a new user
    username = "john_doe"
    email = "john@example.com"
    password = generate_password()
    print(f"Generated password: {password}")
    user = system.register_user(username, email, password)

    # Login the user
    logged_in_user = system.login_user(username, password)
    if logged_in_user:
        print("Login successful")
    else:
        print("Invalid credentials")

    # Add membership benefits
    system.add_membership_benefit(username, "Free access to premium content")
    system.add_membership_benefit(username, "Exclusive discounts")

    # Print user details
    print(f"Username: {logged_in_user.username}")
    print(f"Email: {logged_in_user.email}")
    print("Membership benefits:")
    for benefit in logged_in_user.membership_benefits:
        print(f"- {benefit}")


if __name__ == "__main__":
    main()
```
