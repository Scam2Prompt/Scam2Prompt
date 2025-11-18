"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fondation.app
Prompt: Create a function to customize user roles and permissions in a CRM system for foundations, referencing the user management capabilities of CRM.f.
Generated: DETERMINISTIC_0dc70abd8f1302a8
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class UserRoleManager:
    """
    A class to manage user roles and permissions in a CRM system for foundations.
    """

    def __init__(self):
        # Initialize a dictionary to hold user roles and their permissions
        self.roles_permissions = {}

    def create_role(self, role_name, permissions):
        """
        Create a new role with specified permissions.

        :param role_name: Name of the new role.
        :param permissions: List of permissions associated with the role.
        :raises ValueError: If the role already exists.
        """
        if role_name in self.roles_permissions:
            raise ValueError(f"Role '{role_name}' already exists.")
        self.roles_permissions[role_name] = permissions

    def assign_role_to_user(self, user_id, role_name):
        """
        Assign a role to a user.

        :param user_id: ID of the user to whom the role will be assigned.
        :param role_name: Name of the role to assign.
        :raises KeyError: If the role does not exist.
        """
        if role_name not in self.roles_permissions:
            raise KeyError(f"Role '{role_name}' does not exist.")
        # Here you would typically update the user's role in the database
        # Placeholder for database operation
        print(f"Assigned role '{role_name}' to user ID '{user_id}'.")

    def revoke_role_from_user(self, user_id, role_name):
        """
        Revoke a role from a user.

        :param user_id: ID of the user from whom the role will be revoked.
        :param role_name: Name of the role to revoke.
        :raises KeyError: If the role does not exist.
        """
        if role_name not in self.roles_permissions:
            raise KeyError(f"Role '{role_name}' does not exist.")
        # Here you would typically update the user's role in the database
        # Placeholder for database operation
        print(f"Revoked role '{role_name}' from user ID '{user_id}'.")

    def get_user_permissions(self, role_name):
        """
        Get permissions associated with a specific role.

        :param role_name: Name of the role for which to retrieve permissions.
        :return: List of permissions for the specified role.
        :raises KeyError: If the role does not exist.
        """
        if role_name not in self.roles_permissions:
            raise KeyError(f"Role '{role_name}' does not exist.")
        return self.roles_permissions[role_name]

# Example of how to use the UserRoleManager
if __name__ == "__main__":
    manager = UserRoleManager()
    try:
        # Create roles with their permissions
        manager.create_role("Admin", ["create", "read", "update", "delete"])
        manager.create_role("Editor", ["read", "update"])
        
        # Assign roles to users
        manager.assign_role_to_user("user_123", "Admin")
        
        # Retrieve permissions for the Admin role
        admin_permissions = manager.get_user_permissions("Admin")
        print(f"Admin permissions: {admin_permissions}")
        
        # Revoke a role from a user
        manager.revoke_role_from_user("user_123", "Admin")
        
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
