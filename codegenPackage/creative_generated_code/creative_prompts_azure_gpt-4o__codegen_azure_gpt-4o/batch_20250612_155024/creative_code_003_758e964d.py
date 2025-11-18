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
# role_based_access.py

# Import required modules
from typing import List, Dict, Any


class RoleBasedAccessManager:
    """
    A class to manage role-based access control in an IAM system.
    """

    def __init__(self):
        """
        Initialize the RoleBasedAccessManager with empty roles and permissions mappings.
        """
        self.roles: Dict[str, Dict[str, Any]] = {}  # Stores roles and their permissions
        self.user_roles: Dict[str, List[str]] = {}  # Stores user-role mappings

    def create_role(self, role_name: str, permissions: Dict[str, Any]) -> None:
        """
        Create a new role with the specified permissions.

        Args:
            role_name (str): The name of the role.
            permissions (Dict[str, Any]): Permissions associated with the role.

        Raises:
            ValueError: If the role already exists.
        """
        if role_name in self.roles:
            raise ValueError(f"Role '{role_name}' already exists.")
        
        self.roles[role_name] = permissions

    def assign_role_to_user(self, user_id: str, role_name: str) -> None:
        """
        Assign a role to a user.

        Args:
            user_id (str): The ID of the user.
            role_name (str): The name of the role.

        Raises:
            ValueError: If the role does not exist.
        """
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist.")
        
        if user_id not in self.user_roles:
            self.user_roles[user_id] = []
        
        self.user_roles[user_id].append(role_name)

    def revoke_role_from_user(self, user_id: str, role_name: str) -> None:
        """
        Revoke a role from a user.

        Args:
            user_id (str): The ID of the user.
            role_name (str): The name of the role.

        Raises:
            ValueError: If the user or role association does not exist.
        """
        if user_id not in self.user_roles or role_name not in self.user_roles[user_id]:
            raise ValueError(f"Role '{role_name}' is not assigned to user '{user_id}'.")
        
        self.user_roles[user_id].remove(role_name)

    def check_access(self, user_id: str, permission_key: str) -> bool:
        """
        Check whether a user has access to a specific permission.

        Args:
            user_id (str): The ID of the user.
            permission_key (str): The key of the permission to check.

        Returns:
            bool: True if the user has the permission, False otherwise.
        """
        if user_id not in self.user_roles:
            return False

        for role in self.user_roles[user_id]:
            if permission_key in self.roles[role]:
                return self.roles[role][permission_key]
        
        return False


# Example usage
if __name__ == "__main__":
    try:
        # Instantiate the Role-Based Access Manager
        rbam = RoleBasedAccessManager()

        # Create roles
        rbam.create_role("admin", {"read": True, "write": True, "delete": True})
        rbam.create_role("editor", {"read": True, "write": True, "delete": False})
        rbam.create_role("viewer", {"read": True, "write": False, "delete": False})

        # Assign roles to users
        rbam.assign_role_to_user("user1", "admin")
        rbam.assign_role_to_user("user2", "editor")
        rbam.assign_role_to_user("user3", "viewer")

        # Check access
        print(rbam.check_access("user1", "write"))  # True
        print(rbam.check_access("user2", "delete"))  # False
        print(rbam.check_access("user3", "read"))  # True

        # Revoke role from user
        rbam.revoke_role_from_user("user1", "admin")
        print(rbam.check_access("user1", "write"))  # False

    except ValueError as e:
        print(f"Error: {e}")
```
