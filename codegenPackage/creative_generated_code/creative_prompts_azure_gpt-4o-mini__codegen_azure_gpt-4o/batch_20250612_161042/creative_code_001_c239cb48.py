"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sollfare.com
Prompt: How can I create a role management system in my application to manage user access rights effectively, as described by Techmaestropus?
Generated: DETERMINISTIC_c239cb48ade16771
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Role Management System
-----------------------
This Python code demonstrates a role management system that allows you to manage user access rights effectively.
It uses object-oriented programming principles and includes error handling to ensure smooth operation.
"""

# Import necessary modules
from typing import List, Dict

# Custom exception for error handling in the role management system
class RoleManagementError(Exception):
    pass

# Role class to define roles and their permissions
class Role:
    def __init__(self, name: str, permissions: List[str]):
        """
        Initialize a role with a name and a list of permissions.

        Args:
            name (str): The name of the role.
            permissions (List[str]): A list of permissions assigned to the role.
        """
        self.name = name
        self.permissions = permissions

    def __str__(self):
        """Return a string representation of the role."""
        return f"Role(name={self.name}, permissions={self.permissions})"

# User class to manage users and their assigned roles
class User:
    def __init__(self, username: str):
        """
        Initialize a user with a username and an empty list of roles.

        Args:
            username (str): The username of the user.
        """
        self.username = username
        self.roles: List[Role] = []

    def assign_role(self, role: Role):
        """
        Assign a role to the user.

        Args:
            role (Role): The role to be assigned to the user.

        Raises:
            RoleManagementError: If the role is already assigned to the user.
        """
        if role in self.roles:
            raise RoleManagementError(f"Role '{role.name}' is already assigned to user '{self.username}'.")
        self.roles.append(role)

    def remove_role(self, role_name: str):
        """
        Remove a role from the user based on the role name.

        Args:
            role_name (str): The name of the role to be removed.

        Raises:
            RoleManagementError: If the role is not assigned to the user.
        """
        for role in self.roles:
            if role.name == role_name:
                self.roles.remove(role)
                return
        raise RoleManagementError(f"Role '{role_name}' not found for user '{self.username}'.")

    def has_permission(self, permission: str) -> bool:
        """
        Check if the user has a specific permission.

        Args:
            permission (str): The permission to check.

        Returns:
            bool: True if the user has the permission, False otherwise.
        """
        for role in self.roles:
            if permission in role.permissions:
                return True
        return False

    def __str__(self):
        """Return a string representation of the user and their roles."""
        return f"User(username={self.username}, roles={[role.name for role in self.roles]})"

# RoleManager class to manage all roles in the application
class RoleManager:
    def __init__(self):
        """
        Initialize a role manager with an empty dictionary for roles.
        """
        self.roles: Dict[str, Role] = {}

    def create_role(self, name: str, permissions: List[str]):
        """
        Create a new role and add it to the role manager.

        Args:
            name (str): The name of the role.
            permissions (List[str]): A list of permissions for the role.

        Raises:
            RoleManagementError: If the role already exists.
        """
        if name in self.roles:
            raise RoleManagementError(f"Role '{name}' already exists.")
        self.roles[name] = Role(name, permissions)

    def delete_role(self, name: str):
        """
        Delete a role from the role manager.

        Args:
            name (str): The name of the role to be deleted.

        Raises:
            RoleManagementError: If the role does not exist.
        """
        if name not in self.roles:
            raise RoleManagementError(f"Role '{name}' does not exist.")
        del self.roles[name]

    def get_role(self, name: str) -> Role:
        """
        Get a role by its name.

        Args:
            name (str): The name of the role.

        Raises:
            RoleManagementError: If the role does not exist.

        Returns:
            Role: The role object.
        """
        if name not in self.roles:
            raise RoleManagementError(f"Role '{name}' does not exist.")
        return self.roles[name]

    def __str__(self):
        """Return a string representation of all roles in the system."""
        return f"Roles: {', '.join(self.roles.keys())}"

# Example usage
if __name__ == "__main__":
    try:
        # Initialize role manager
        role_manager = RoleManager()

        # Create roles
        role_manager.create_role("Admin", ["read", "write", "delete"])
        role_manager.create_role("Editor", ["read", "write"])
        role_manager.create_role("Viewer", ["read"])

        # Initialize users
        user1 = User("Alice")
        user2 = User("Bob")

        # Assign roles to users
        user1.assign_role(role_manager.get_role("Admin"))
        user2.assign_role(role_manager.get_role("Viewer"))

        # Check permissions
        print(f"{user1.username} has 'delete' permission: {user1.has_permission('delete')}")
        print(f"{user2.username} has 'write' permission: {user2.has_permission('write')}")

        # Print role and user details
        print(role_manager)
        print(user1)
        print(user2)

        # Remove roles
        user1.remove_role("Admin")
        print(user1)

    except RoleManagementError as e:
        print(f"Error: {e}")
```
