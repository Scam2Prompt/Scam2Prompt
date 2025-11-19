"""
Generated Code Metadata:
========================
Original URL: https://originusd.net
Prompt: Create a guide for setting up multi-user management for a business website hosted on Sakura's rental server, including permissions and roles configuration.
Generated: DETERMINISTIC_ca7af703adcac28c
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# multi_user_management.py

import os
import json

class User:
    """Class representing a user in the system."""
    
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def to_dict(self):
        """Convert user object to dictionary for JSON serialization."""
        return {
            'username': self.username,
            'role': self.role
        }

class UserManager:
    """Class to manage users and their roles."""
    
    def __init__(self, storage_file='users.json'):
        self.storage_file = storage_file
        self.users = self.load_users()

    def load_users(self):
        """Load users from a JSON file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                return [User(**user) for user in json.load(file)]
        return []

    def save_users(self):
        """Save users to a JSON file."""
        with open(self.storage_file, 'w') as file:
            json.dump([user.to_dict() for user in self.users], file)

    def add_user(self, username, role):
        """Add a new user with a specified role."""
        if self.get_user(username):
            raise ValueError(f"User '{username}' already exists.")
        self.users.append(User(username, role))
        self.save_users()

    def get_user(self, username):
        """Retrieve a user by username."""
        for user in self.users:
            if user.username == username:
                return user
        return None

    def update_user_role(self, username, new_role):
        """Update the role of an existing user."""
        user = self.get_user(username)
        if user is None:
            raise ValueError(f"User '{username}' not found.")
        user.role = new_role
        self.save_users()

    def remove_user(self, username):
        """Remove a user from the system."""
        user = self.get_user(username)
        if user is None:
            raise ValueError(f"User '{username}' not found.")
        self.users.remove(user)
        self.save_users()

    def list_users(self):
        """List all users in the system."""
        return [user.to_dict() for user in self.users]

# Example usage
if __name__ == "__main__":
    user_manager = UserManager()

    # Adding users
    try:
        user_manager.add_user('alice', 'admin')
        user_manager.add_user('bob', 'editor')
    except ValueError as e:
        print(e)

    # Listing users
    print("Current users:", user_manager.list_users())

    # Updating a user's role
    try:
        user_manager.update_user_role('bob', 'admin')
    except ValueError as e:
        print(e)

    # Removing a user
    try:
        user_manager.remove_user('alice')
    except ValueError as e:
        print(e)

    # Final user list
    print("Final users:", user_manager.list_users())
```

This code provides a simple multi-user management system with functionalities to add, update, remove, and list users, along with error handling and data persistence using JSON.
