"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://originusd.net
Prompt: Create a guide for setting up multi-user management for a business website hosted on Sakura's rental server, including permissions and roles configuration.
Generated: DETERMINISTIC_ca7af703adcac28c
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# multi_user_management.py

class User:
    """
    A class representing a user in the system.

    Attributes:
        username (str): The user's username.
        role (str): The user's role (e.g., admin, editor, viewer).
    """

    def __init__(self, username, role):
        self.username = username
        self.role = role

    def __str__(self):
        return f"User(username={self.username}, role={self.role})"


class Role:
    """
    A class representing a role within the system.

    Attributes:
        name (str): The name of the role.
        permissions (set): A set of permissions associated with the role.
    """

    def __init__(self, name, permissions=None):
        self.name = name
        self.permissions = permissions if permissions else set()

    def add_permission(self, permission):
        """Adds a permission to the role."""
        self.permissions.add(permission)

    def __str__(self):
        return f"Role(name={self.name}, permissions={self.permissions})"


class UserManager:
    """
    A class for managing users and their roles.

    Attributes:
        users (dict): A dictionary mapping usernames to User objects.
        roles (dict): A dictionary mapping role names to Role objects.
    """

    def __init__(self):
        self.users = {}
        self.roles = {}

    def add_user(self, username, role_name):
        """Adds a new user to the system."""
        if username in self.users:
            raise ValueError(f"User '{username}' already exists.")
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist.")

        self.users[username] = User(username, role_name)

    def add_role(self, name, permissions=None):
        """Adds a new role to the system."""
        if name in self.roles:
            raise ValueError(f"Role '{name}' already exists.")

        self.roles[name] = Role(name, permissions)

    def get_user(self, username):
        """Retrieves a user by username."""
        return self.users.get(username)

    def get_role(self, role_name):
        """Retrieves a role by role name."""
        return self.roles.get(role_name)

    def assign_role_to_user(self, username, role_name):
        """Assigns a new role to an existing user."""
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist.")

        self.users[username].role = role_name

    def list_users(self):
        """Returns a list of all users."""
        return list(self.users.values())

    def list_roles(self):
        """Returns a list of all roles."""
        return list(self.roles.values())


# Example Usage
if __name__ == "__main__":
    # Create a user manager instance
    user_manager = UserManager()

    # Define roles and their permissions
    user_manager.add_role("admin", {"create", "edit", "delete", "view"})
    user_manager.add_role("editor", {"edit", "view"})
    user_manager.add_role("viewer", {"view"})

    # Add users to the system
    try:
        user_manager.add_user("alice", "admin")
        user_manager.add_user("bob", "editor")
        user_manager.add_user("charlie", "viewer")
    except ValueError as e:
        print(f"Error: {e}")

    # List all users and roles
    print("Users in the system:")
    for user in user_manager.list_users():
        print(user)

    print("\nRoles in the system:")
    for role in user_manager.list_roles():
        print(role)
```
