"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phanytom.com
Prompt: Create a prototype for role-based access management in an IAM system, ensuring flexible access rights configuration as described by Techmaestropus.
Generated: DETERMINISTIC_758e964d7e5a79a6
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Role:
    """Represents a user role in the access management system."""

    def __init__(self, name):
        """Initialize a role with a name and an empty set of permissions."""
        self.name = name
        self.permissions = set()

    def add_permission(self, permission):
        """Add a permission to the role."""
        self.permissions.add(permission)

    def remove_permission(self, permission):
        """Remove a permission from the role."""
        self.permissions.discard(permission)

    def has_permission(self, permission):
        """Check if the role has a specific permission."""
        return permission in self.permissions


class User:
    """Represents a user in the access management system."""

    def __init__(self, username):
        """Initialize a user with a username and an empty set of roles."""
        self.username = username
        self.roles = set()

    def add_role(self, role):
        """Assign a role to the user."""
        self.roles.add(role)

    def remove_role(self, role):
        """Remove a role from the user."""
        self.roles.discard(role)

    def has_permission(self, permission):
        """Check if the user has a specific permission through their roles."""
        return any(role.has_permission(permission) for role in self.roles)


class AccessControl:
    """Manages roles and users and their associated permissions."""

    def __init__(self):
        """Initialize an access control manager with empty lists for roles and users."""
        self.roles = {}
        self.users = {}

    def create_role(self, role_name):
        """Create a new role with the given name."""
        if role_name in self.roles:
            raise ValueError(f"Role '{role_name}' already exists.")
        self.roles[role_name] = Role(role_name)

    def create_user(self, username):
        """Create a new user with the given username."""
        if username in self.users:
            raise ValueError(f"User '{username}' already exists.")
        self.users[username] = User(username)

    def assign_role_to_user(self, username, role_name):
        """Assign a specified role to a user."""
        user = self.users.get(username)
        role = self.roles.get(role_name)
        
        if user is None:
            raise ValueError(f"User '{username}' does not exist.")
        if role is None:
            raise ValueError(f"Role '{role_name}' does not exist.")
        
        user.add_role(role)

    def check_user_permission(self, username, permission):
        """Check if a user has a specific permission."""
        user = self.users.get(username)
        
        if user is None:
            raise ValueError(f"User '{username}' does not exist.")

        return user.has_permission(permission)


# Example usage:
if __name__ == "__main__":
    try:
        access_control = AccessControl()

        # Creating roles
        access_control.create_role("admin")
        access_control.create_role("editor")

        # Creating users
        access_control.create_user("alice")
        access_control.create_user("bob")

        # Assigning permissions
        access_control.roles["admin"].add_permission("edit")
        access_control.roles["admin"].add_permission("delete")
        access_control.roles["editor"].add_permission("edit")

        # Assigning roles to users
        access_control.assign_role_to_user("alice", "admin")
        access_control.assign_role_to_user("bob", "editor")

        # Checking permissions
        print(access_control.check_user_permission("alice", "edit"))  # True
        print(access_control.check_user_permission("bob", "delete"))  # False

    except Exception as e:
        print(f"Error: {e}")
```
