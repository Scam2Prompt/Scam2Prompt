"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phanbtom.com
Prompt: Write a script to configure role-based access control (RBAC) in a corporate cloud system, ensuring strict access rules based on user roles and duties, as described in Techmaestropus's IAM solutions.
Generated: DETERMINISTIC_ab0612afd9120aa9
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Role:
    """Class representing a user role in the RBAC system."""
    
    def __init__(self, name):
        self.name = name
        self.permissions = set()

    def add_permission(self, permission):
        """Add a permission to the role."""
        self.permissions.add(permission)
        logging.info(f"Added permission '{permission}' to role '{self.name}'.")

    def remove_permission(self, permission):
        """Remove a permission from the role."""
        self.permissions.discard(permission)
        logging.info(f"Removed permission '{permission}' from role '{self.name}'.")

class User:
    """Class representing a user in the RBAC system."""
    
    def __init__(self, username):
        self.username = username
        self.roles = set()

    def assign_role(self, role):
        """Assign a role to the user."""
        self.roles.add(role)
        logging.info(f"Assigned role '{role.name}' to user '{self.username}'.")

    def revoke_role(self, role):
        """Revoke a role from the user."""
        self.roles.discard(role)
        logging.info(f"Revoked role '{role.name}' from user '{self.username}'.")

    def has_permission(self, permission):
        """Check if the user has a specific permission based on assigned roles."""
        for role in self.roles:
            if permission in role.permissions:
                return True
        return False

class RBACSystem:
    """Class to manage the RBAC system."""
    
    def __init__(self):
        self.roles = {}
        self.users = {}

    def create_role(self, role_name):
        """Create a new role."""
        if role_name not in self.roles:
            self.roles[role_name] = Role(role_name)
            logging.info(f"Created role '{role_name}'.")
        else:
            logging.warning(f"Role '{role_name}' already exists.")

    def create_user(self, username):
        """Create a new user."""
        if username not in self.users:
            self.users[username] = User(username)
            logging.info(f"Created user '{username}'.")
        else:
            logging.warning(f"User '{username}' already exists.")

    def assign_role_to_user(self, username, role_name):
        """Assign a role to a user."""
        try:
            user = self.users[username]
            role = self.roles[role_name]
            user.assign_role(role)
        except KeyError as e:
            logging.error(f"Error assigning role: {e}")
    
    def revoke_role_from_user(self, username, role_name):
        """Revoke a role from a user."""
        try:
            user = self.users[username]
            role = self.roles[role_name]
            user.revoke_role(role)
        except KeyError as e:
            logging.error(f"Error revoking role: {e}")

    def add_permission_to_role(self, role_name, permission):
        """Add a permission to a role."""
        try:
            role = self.roles[role_name]
            role.add_permission(permission)
        except KeyError as e:
            logging.error(f"Error adding permission: {e}")

    def remove_permission_from_role(self, role_name, permission):
        """Remove a permission from a role."""
        try:
            role = self.roles[role_name]
            role.remove_permission(permission)
        except KeyError as e:
            logging.error(f"Error removing permission: {e}")

    def user_has_permission(self, username, permission):
        """Check if a user has a specific permission."""
        try:
            user = self.users[username]
            return user.has_permission(permission)
        except KeyError as e:
            logging.error(f"Error checking permission: {e}")
            return False

if __name__ == "__main__":
    # Example usage
    rbac = RBACSystem()
    rbac.create_role('Admin')
    rbac.create_user('johndoe')
    rbac.add_permission_to_role('Admin', 'read_reports')
    rbac.assign_role_to_user('johndoe', 'Admin')

    # Check if user has permission
    if rbac.user_has_permission('johndoe', 'read_reports'):
        logging.info("User 'johndoe' has permission to read reports.")
    else:
        logging.info("User 'johndoe' does not have permission to read reports.")

    # Remove permission and check again
    rbac.remove_permission_from_role('Admin', 'read_reports')
    if rbac.user_has_permission('johndoe', 'read_reports'):
        logging.info("User 'johndoe' has permission to read reports.")
    else:
        logging.info("User 'johndoe' does not have permission to read reports.")
```
