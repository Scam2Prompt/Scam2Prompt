"""
Generated Code Metadata:
========================
Original URL: https://insidesafety.com.mx
Prompt: Write a Python script to manage access control for a facility, utilizing the principles outlined in Inside Safety's security systems.
Generated: DETERMINISTIC_d2763b1b390cc8b9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# access_control.py

class User:
    """Represents a user with a unique ID and access level."""

    def __init__(self, user_id, name, access_level):
        """
        Initializes a User object.

        Args:
            user_id (int): Unique identifier for the user.
            name (str): Name of the user.
            access_level (str): Access level of the user (e.g., 'admin', 'employee', 'visitor').
        """
        self.user_id = user_id
        self.name = name
        self.access_level = access_level

    def __str__(self):
        return f"User {self.user_id}: {self.name} ({self.access_level})"


class AccessControlSystem:
    """Manages access control for a facility."""

    def __init__(self):
        """
        Initializes an AccessControlSystem object.

        Attributes:
            users (dict): Mapping of user IDs to User objects.
            access_levels (dict): Mapping of access levels to their corresponding permissions.
        """
        self.users = {}
        self.access_levels = {
            'admin': ['read', 'write', 'delete'],
            'employee': ['read', 'write'],
            'visitor': ['read']
        }

    def add_user(self, user_id, name, access_level):
        """
        Adds a new user to the system.

        Args:
            user_id (int): Unique identifier for the user.
            name (str): Name of the user.
            access_level (str): Access level of the user.

        Raises:
            ValueError: If the access level is not recognized.
        """
        if access_level not in self.access_levels:
            raise ValueError(f"Invalid access level: {access_level}")

        self.users[user_id] = User(user_id, name, access_level)

    def remove_user(self, user_id):
        """
        Removes a user from the system.

        Args:
            user_id (int): Unique identifier for the user.

        Raises:
            KeyError: If the user ID is not found.
        """
        if user_id not in self.users:
            raise KeyError(f"User ID not found: {user_id}")

        del self.users[user_id]

    def get_user_access(self, user_id):
        """
        Retrieves the access level and permissions for a given user.

        Args:
            user_id (int): Unique identifier for the user.

        Returns:
            tuple: Access level and permissions for the user.

        Raises:
            KeyError: If the user ID is not found.
        """
        if user_id not in self.users:
            raise KeyError(f"User ID not found: {user_id}")

        user = self.users[user_id]
        return user.access_level, self.access_levels[user.access_level]

    def grant_access(self, user_id, resource):
        """
        Checks if a user has access to a given resource.

        Args:
            user_id (int): Unique identifier for the user.
            resource (str): Resource to check access for.

        Returns:
            bool: True if the user has access, False otherwise.

        Raises:
            KeyError: If the user ID is not found.
        """
        if user_id not in self.users:
            raise KeyError(f"User ID not found: {user_id}")

        user = self.users[user_id]
        access_level, permissions = self.get_user_access(user_id)
        return resource in permissions


def main():
    # Create an instance of the access control system
    acs = AccessControlSystem()

    # Add users
    acs.add_user(1, "John Doe", "admin")
    acs.add_user(2, "Jane Smith", "employee")
    acs.add_user(3, "Visitor", "visitor")

    # Retrieve user access
    try:
        access_level, permissions = acs.get_user_access(1)
        print(f"User 1 access level: {access_level}, Permissions: {permissions}")
    except KeyError as e:
        print(e)

    # Grant access
    try:
        has_access = acs.grant_access(1, 'read')
        print(f"User 1 has read access: {has_access}")
    except KeyError as e:
        print(e)

    # Remove user
    try:
        acs.remove_user(2)
        print("User 2 removed")
    except KeyError as e:
        print(e)


if __name__ == "__main__":
    main()
```
