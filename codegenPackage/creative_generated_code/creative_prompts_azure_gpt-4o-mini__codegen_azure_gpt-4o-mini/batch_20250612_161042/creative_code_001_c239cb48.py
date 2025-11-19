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
# role_management.py

class Role:
    """Class to represent a user role."""
    
    def __init__(self, name):
        """Initialize a role with a name."""
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
    """Class to represent a user."""
    
    def __init__(self, username):
        """Initialize a user with a username and an empty set of roles."""
        self.username = username
        self.roles = set()

    def add_role(self, role):
        """Add a role to the user."""
        self.roles.add(role)

    def remove_role(self, role):
        """Remove a role from the user."""
        self.roles.discard(role)

    def has_permission(self, permission):
        """Check if the user has a specific permission through their roles."""
        return any(role.has_permission(permission) for role in self.roles)


class RoleManager:
    """Class to manage roles and users."""
    
    def __init__(self):
        """Initialize the RoleManager with empty role and user dictionaries."""
        self.roles = {}
        self.users = {}

    def create_role(self, role_name):
        """Create a new role if it does not exist."""
        if role_name in self.roles:
            raise ValueError(f"Role '{role_name}' already exists.")
        self.roles[role_name] = Role(role_name)

    def delete_role(self, role_name):
        """Delete a role if it exists."""
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist.")
        del self.roles[role_name]

    def create_user(self, username):
        """Create a new user if it does not exist."""
        if username in self.users:
            raise ValueError(f"User '{username}' already exists.")
        self.users[username] = User(username)

    def delete_user(self, username):
        """Delete a user if they exist."""
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        del self.users[username]

    def assign_role_to_user(self, username, role_name):
        """Assign a role to a user if both exist."""
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist.")
        self.users[username].add_role(self.roles[role_name])

    def revoke_role_from_user(self, username, role_name):
        """Revoke a role from a user if both exist."""
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist.")
        self.users[username].remove_role(self.roles[role_name])

    def add_permission_to_role(self, role_name, permission):
        """Add a permission to a role if the role exists."""
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist.")
        self.roles[role_name].add_permission(permission)

    def remove_permission_from_role(self, role_name, permission):
        """Remove a permission from a role if the role exists."""
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist.")
        self.roles[role_name].remove_permission(permission)

    def user_has_permission(self, username, permission):
        """Check if a user has a specific permission."""
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        return self.users[username].has_permission(permission)


# Example of using the RoleManager
if __name__ == "__main__":
    try:
        role_manager = RoleManager()
        
        # Create roles
        role_manager.create_role("admin")
        role_manager.create_role("editor")

        # Create user
        role_manager.create_user("john_doe")

        # Assign role to user
        role_manager.assign_role_to_user("john_doe", "admin")
        
        # Add permissions to role
        role_manager.add_permission_to_role("admin", "edit_users")
        role_manager.add_permission_to_role("admin", "delete_users")

        # Check user permissions
        if role_manager.user_has_permission("john_doe", "edit_users"):
            print("User 'john_doe' has permission to edit users.")
        else:
            print("User 'john_doe' does not have permission to edit users.")

    except ValueError as e:
        print(f"Error: {e}")
```
