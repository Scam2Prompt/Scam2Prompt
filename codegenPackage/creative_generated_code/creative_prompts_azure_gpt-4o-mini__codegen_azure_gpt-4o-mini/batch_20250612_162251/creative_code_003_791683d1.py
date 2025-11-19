"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phanytom.com
Prompt: What are the steps to develop a custom software solution that includes access management features as described by Techmaestropus?
Generated: DETERMINISTIC_791683d17eed7f9d
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Custom Software Solution for Access Management

This script outlines the basic structure for a custom access management system.
It includes user roles and permissions management with error handling and best practices.
"""

class User:
    """
    Represents a user in the system.
    
    Attributes:
        username (str): The username of the user.
        role (str): The role assigned to the user (e.g., 'admin', 'editor', 'viewer').
    """
    
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def __str__(self):
        return f"User(username={self.username}, role={self.role})"


class AccessControl:
    """
    Manages user access and permissions.
    
    Attributes:
        users (dict): A dictionary of users indexed by username.
        roles (dict): A dictionary of roles and their corresponding permissions.
    """
    
    def __init__(self):
        self.users = {}
        self.roles = {
            'admin': ['create', 'read', 'update', 'delete'],
            'editor': ['create', 'read', 'update'],
            'viewer': ['read']
        }

    def add_user(self, username, role):
        """Adds a new user with the specified role to the system."""
        if role not in self.roles:
            raise ValueError(f"Invalid role: {role}. Available roles: {list(self.roles.keys())}")
        
        if username in self.users:
            raise ValueError(f"User '{username}' already exists.")
        
        self.users[username] = User(username, role)
        print(f"User '{username}' added with role '{role}'.")

    def check_access(self, username, action):
        """Checks if a user has permission to perform a specific action."""
        user = self.users.get(username)
        
        if user is None:
            raise ValueError(f"User '{username}' does not exist.")
        
        if action not in self.roles[user.role]:
            raise PermissionError(f"User '{username}' does not have permission to perform '{action}' action.")
        
        print(f"User '{username}' has access to '{action}'.")

    def list_users(self):
        """Lists all users in the system."""
        return list(self.users.values())


# Example usage
if __name__ == "__main__":
    access_control = AccessControl()
    
    try:
        # Adding users
        access_control.add_user("alice", "admin")
        access_control.add_user("bob", "editor")
        access_control.add_user("charlie", "viewer")

        # Checking access
        access_control.check_access("alice", "create")  # Should succeed
        access_control.check_access("bob", "delete")    # Should raise PermissionError
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except PermissionError as pe:
        print(f"PermissionError: {pe}")

    # Listing users
    users = access_control.list_users()
    print("Current users:", users)
```
