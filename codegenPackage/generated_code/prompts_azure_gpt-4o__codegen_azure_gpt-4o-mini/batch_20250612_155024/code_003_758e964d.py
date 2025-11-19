"""
Generated Code Metadata:
========================
Original URL: https://phanytom.com
Prompt: Create a prototype for role-based access management in an IAM system, ensuring flexible access rights configuration as described by Techmaestropus.
Generated: DETERMINISTIC_758e964d7e5a79a6
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Role:
    """
    Represents a role in the IAM system with associated permissions.
    """
    def __init__(self, name):
        self.name = name
        self.permissions = set()

    def add_permission(self, permission):
        """
        Adds a permission to the role.
        :param permission: The permission to add.
        """
        self.permissions.add(permission)

    def remove_permission(self, permission):
        """
        Removes a permission from the role.
        :param permission: The permission to remove.
        """
        self.permissions.discard(permission)

    def has_permission(self, permission):
        """
        Checks if the role has a specific permission.
        :param permission: The permission to check.
        :return: True if the permission exists, False otherwise.
        """
        return permission in self.permissions


class User:
    """
    Represents a user in the IAM system with associated roles.
    """
    def __init__(self, username):
        self.username = username
        self.roles = set()

    def add_role(self, role):
        """
        Assigns a role to the user.
        :param role: The role to assign.
        """
        self.roles.add(role)

    def remove_role(self, role):
        """
        Removes a role from the user.
        :param role: The role to remove.
        """
        self.roles.discard(role)

    def has_permission(self, permission):
        """
        Checks if the user has a specific permission through their roles.
        :param permission: The permission to check.
        :return: True if the user has the permission, False otherwise.
        """
        return any(role.has_permission(permission) for role in self.roles)


class AccessManager:
    """
    Manages roles and users in the IAM system.
    """
    def __init__(self):
        self.roles = {}
        self.users = {}

    def create_role(self, role_name):
        """
        Creates a new role.
        :param role_name: The name of the role to create.
        :raises ValueError: If the role already exists.
        """
        if role_name in self.roles:
            raise ValueError(f"Role '{role_name}' already exists.")
        self.roles[role_name] = Role(role_name)

    def create_user(self, username):
        """
        Creates a new user.
        :param username: The username of the user to create.
        :raises ValueError: If the user already exists.
        """
        if username in self.users:
            raise ValueError(f"User '{username}' already exists.")
        self.users[username] = User(username)

    def assign_role_to_user(self, username, role_name):
        """
        Assigns a role to a user.
        :param username: The username of the user.
        :param role_name: The name of the role to assign.
        :raises KeyError: If the user or role does not exist.
        """
        if username not in self.users:
            raise KeyError(f"User '{username}' does not exist.")
        if role_name not in self.roles:
            raise KeyError(f"Role '{role_name}' does not exist.")
        self.users[username].add_role(self.roles[role_name])

    def add_permission_to_role(self, role_name, permission):
        """
        Adds a permission to a role.
        :param role_name: The name of the role.
        :param permission: The permission to add.
        :raises KeyError: If the role does not exist.
        """
        if role_name not in self.roles:
            raise KeyError(f"Role '{role_name}' does not exist.")
        self.roles[role_name].add_permission(permission)

    def check_user_permission(self, username, permission):
        """
        Checks if a user has a specific permission.
        :param username: The username of the user.
        :param permission: The permission to check.
        :raises KeyError: If the user does not exist.
        :return: True if the user has the permission, False otherwise.
        """
        if username not in self.users:
            raise KeyError(f"User '{username}' does not exist.")
        return self.users[username].has_permission(permission)


# Example usage
if __name__ == "__main__":
    try:
        access_manager = AccessManager()
        
        # Create roles
        access_manager.create_role("admin")
        access_manager.create_role("editor")
        
        # Create users
        access_manager.create_user("alice")
        access_manager.create_user("bob")
        
        # Assign permissions to roles
        access_manager.add_permission_to_role("admin", "edit")
        access_manager.add_permission_to_role("admin", "delete")
        access_manager.add_permission_to_role("editor", "edit")
        
        # Assign roles to users
        access_manager.assign_role_to_user("alice", "admin")
        access_manager.assign_role_to_user("bob", "editor")
        
        # Check permissions
        print(access_manager.check_user_permission("alice", "delete"))  # True
        print(access_manager.check_user_permission("bob", "delete"))    # False

    except Exception as e:
        print(f"An error occurred: {e}")
```
