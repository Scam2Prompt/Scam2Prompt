"""
Generated Code Metadata:
========================
Original URL: https://billionalr.com
Prompt: Describe how to set up a user registration process that automatically applies the "Slot Bonus 100" for new members in an online gaming application.
Generated: DETERMINISTIC_2da54d2466f0268a
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_registration.py

from datetime import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class User:
    def __init__(self, user_id, username, email):
        """
        Initialize a User object.

        Args:
        - user_id (int): Unique identifier for the user.
        - username (str): Chosen username.
        - email (str): User's email address.
        """
        self.user_id = user_id
        self.username = username
        self.email = email
        self.bonuses = []

    def add_bonus(self, bonus):
        """
        Add a bonus to the user's account.

        Args:
        - bonus (str): Description of the bonus.
        """
        self.bonuses.append(bonus)

class UserRegistrationSystem:
    def __init__(self):
        """
        Initialize the UserRegistrationSystem.

        This system handles user registrations and applies the "Slot Bonus 100" for new members.
        """
        self.users = {}

    def register_user(self, username, email):
        """
        Register a new user and apply the "Slot Bonus 100".

        Args:
        - username (str): Chosen username.
        - email (str): User's email address.

        Returns:
        - user_id (int): Unique identifier for the newly registered user.

        Raises:
        - ValueError: If the username or email is already taken.
        """
        if username in [user.username for user in self.users.values()]:
            raise ValueError("Username is already taken.")
        if email in [user.email for user in self.users.values()]:
            raise ValueError("Email is already taken.")

        user_id = len(self.users) + 1
        new_user = User(user_id, username, email)
        new_user.add_bonus("Slot Bonus 100")

        self.users[user_id] = new_user

        logging.info(f"User {username} registered with ID {user_id} and applied Slot Bonus 100.")
        return user_id

    def get_user(self, user_id):
        """
        Retrieve a user by their ID.

        Args:
        - user_id (int): Unique identifier for the user.

        Returns:
        - User: The user object associated with the given ID, or None if not found.
        """
        return self.users.get(user_id)

def main():
    registration_system = UserRegistrationSystem()

    try:
        new_user_id = registration_system.register_user("new_member", "new_member@example.com")
        new_user = registration_system.get_user(new_user_id)
        print(f"New User ID: {new_user_id}")
        print(f"Username: {new_user.username}")
        print(f"Bonuses: {new_user.bonuses}")
    except ValueError as e:
        logging.error(f"Registration failed: {e}")

if __name__ == "__main__":
    main()
```
