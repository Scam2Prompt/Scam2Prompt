"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phanytom.com
Prompt: How can I create a role management system for user access rights in a corporate environment with Techmaestropus IAM?
Generated: DETERMINISTIC_d7ec9906d4411475
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# role_management.py
"""
Role Management System for User Access Rights in a Corporate Environment
Using Techmaestropus IAM

This system allows for the creation, assignment, and management of user roles
and access rights within an organization.
"""

class Role:
    """
    Represents a user role within the system.
    
    Attributes:
        name (str): The name of the role.
        permissions (set): A set of permissions associated with the role.
    """

    def __init__(self, name):
        self.name = name
        self.permissions = set()

    def add_permission(self, permission):
        """Adds a permission to the role."""
        self.permissions.add(permission)

    def remove_permission(self, permission):
        """Removes a permission from the role."""
        self.permissions.discard(permission)

    def __repr__(self):
        return f"Role(name={self.name}, permissions={self.permissions})"


class User:
    """
    Represents a user in the system.
    
    Attributes:
        username (str): The username of the user.
        roles (set): A set of roles assigned to the user.
    """

    def __init__(self, username):
        self.username = username
        self.roles = set()

    def assign_role(self, role):
        """Assigns a role to the user."""
        self.roles.add(role)

    def remove_role(self, role):
        """Removes a role from the user."""
        self.roles.discard(role)

    def has_permission(self, permission):
        """
        Checks if the user has a specific permission.
        
        Args:
            permission (str): The permission to check.
        
        Returns:
            bool: True if the user has the permission, False otherwise.
        """
        return any(permission in role.permissions for role in self.roles)

    def __repr__(self):
        return f"User(username={self.username}, roles={self.roles})"


class RoleManager:
    """
    Manages roles and users within the system.
    
    Attributes:
        roles (dict): A dictionary to store roles by name.
        users (dict): A dictionary to store users by username.
    """

    def __init__(self):
        self.roles = {}
        self.users = {}

    def create_role(self, role_name):
        """Creates a new role."""
        if role_name in self.roles:
            raise ValueError(f"Role '{role_name}' already exists.")
        self.roles[role_name] = Role(role_name)

    def get_role(self, role_name):
        """Retrieves a role by name."""
        return self.roles.get(role_name)

    def create_user(self, username):
        """Creates a new user."""
        if username in self.users:
            raise ValueError(f"User '{username}' already exists.")
        self.users[username] = User(username)

    def get_user(self, username):
        """Retrieves a user by username."""
        return self.users.get(username)

    def assign_role_to_user(self, username, role_name):
        """Assigns a role to a user."""
        user = self.get_user(username)
        role = self.get_role(role_name)
        if user is None:
            raise ValueError(f"User '{username}' not found.")
        if role is None:
            raise ValueError(f"Role '{role_name}' not found.")
        user.assign_role(role)

    def remove_role_from_user(self, username, role_name):
        """Removes a role from a user."""
        user = self.get_user(username)
        role = self.get_role(role_name)
        if user is None:
            raise ValueError(f"User '{username}' not found.")
        if role is None:
            raise ValueError(f"Role '{role_name}' not found.")
        user.remove_role(role)


# Example usage
if __name__ == "__main__":
    try:
        role_manager = RoleManager()

        # Create roles
        role_manager.create_role('Admin')
        role_manager.create_role('Editor')

        # Create users
        role_manager.create_user('alice')
        role_manager.create_user('bob')

        # Assign roles to users
        role_manager.assign_role_to_user('alice', 'Admin')
        role_manager.assign_role_to_user('bob', 'Editor')

        # Check permissions
        print(role_manager.get_user('alice'))
        print(role_manager.get_user('bob'))

    except ValueError as e:
        print(f"Error: {e}")
```
