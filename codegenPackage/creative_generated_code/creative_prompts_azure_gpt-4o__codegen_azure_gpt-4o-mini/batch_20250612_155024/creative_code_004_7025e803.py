"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantpm.com
Prompt: Write code to configure access rights based on user roles, ensuring compliance with Techmaestropus IAM role management policies.
Generated: DETERMINISTIC_7025e8036f069735
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
    """Class to represent a user role with associated permissions."""
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

    def __str__(self):
        return self.name


class User:
    """Class to represent a user with an assigned role."""
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def __str__(self):
        return self.username


class AccessManager:
    """Class to manage access rights based on user roles."""
    
    def __init__(self):
        self.roles = {}
        self.users = {}
        
    def add_role(self, role_name, permissions):
        """Add a new role with associated permissions."""
        if role_name in self.roles:
            raise ValueError(f"Role '{role_name}' already exists.")
        self.roles[role_name] = Role(role_name, permissions)
    
    def add_user(self, username, role_name):
        """Add a new user with a specified role."""
        if username in self.users:
            raise ValueError(f"User '{username}' already exists.")
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist.")
        self.users[username] = User(username, self.roles[role_name])
    
    def check_permission(self, username, permission):
        """Check if a user has a specific permission based on their role."""
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        
        user_role = self.users[username].role
        if permission in user_role.permissions:
            return True
        return False


# Example Usage:
if __name__ == "__main__":
    try:
        access_manager = AccessManager()

        # Configure roles and permissions
        access_manager.add_role("admin", ["create", "read", "update", "delete"])
        access_manager.add_role("editor", ["read", "update"])
        access_manager.add_role("viewer", ["read"])

        # Create users
        access_manager.add_user("alice", "admin")
        access_manager.add_user("bob", "editor")
        access_manager.add_user("charlie", "viewer")

        # Check permissions
        print("Alice can delete:", access_manager.check_permission("alice", "delete"))  # True
        print("Bob can delete:", access_manager.check_permission("bob", "delete"))      # False
        print("Charlie can read:", access_manager.check_permission("charlie", "read"))  # True

    except ValueError as e:
        print(f"Error: {e}")
```
