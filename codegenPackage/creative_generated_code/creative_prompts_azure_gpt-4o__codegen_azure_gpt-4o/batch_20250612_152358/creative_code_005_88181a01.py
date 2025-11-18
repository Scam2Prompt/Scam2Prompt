"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sus.weebly.com
Prompt: Write code to implement a role-based access control system for healthcare professionals in a SUS-inspired system, ensuring that general practitioners, nurses, and community health agents have access to relevant patient data.
Generated: DETERMINISTIC_88181a014dd5f0a6
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict


class RoleBasedAccessControl:
    """
    A class to implement Role-Based Access Control (RBAC) for healthcare professionals.
    """
    
    def __init__(self):
        """
        Initialize the RBAC system with roles and permissions.
        """
        # Define roles and their permissions
        self.roles_permissions = {
            "General Practitioner": {"view_medical_records", "write_notes", "update_treatment_plans"},
            "Nurse": {"view_medical_records", "update_medication_schedule"},
            "Community Health Agent": {"view_basic_patient_info"}
        }

        # Define a mapping of users to roles
        self.user_roles: Dict[str, str] = {}

    def assign_role(self, user: str, role: str) -> None:
        """
        Assign a role to a user.
        
        Args:
            user (str): The name or identifier of the user.
            role (str): The name of the role to assign to the user.
            
        Raises:
            ValueError: If the role is invalid.
        """
        if role not in self.roles_permissions:
            raise ValueError(f"Invalid role: {role}")
        self.user_roles[user] = role

    def get_permissions(self, user: str) -> List[str]:
        """
        Get the permissions for a specific user based on their role.
        
        Args:
            user (str): The name or identifier of the user.
            
        Returns:
            List[str]: A list of permissions for the user.
            
        Raises:
            ValueError: If the user does not have a role assigned.
        """
        if user not in self.user_roles:
            raise ValueError(f"User {user} does not have a role assigned.")
        
        role = self.user_roles[user]
        return list(self.roles_permissions[role])

    def check_permission(self, user: str, permission: str) -> bool:
        """
        Check if a user has a specific permission.
        
        Args:
            user (str): The name or identifier of the user.
            permission (str): The permission to check.
            
        Returns:
            bool: True if the user has the permission, False otherwise.
            
        Raises:
            ValueError: If the user does not have a role assigned.
        """
        if user not in self.user_roles:
            raise ValueError(f"User {user} does not have a role assigned.")
        
        role = self.user_roles[user]
        return permission in self.roles_permissions[role]


# Example usage of the RBAC system
if __name__ == "__main__":
    try:
        rbac = RoleBasedAccessControl()

        # Assign roles to users
        rbac.assign_role("Alice", "General Practitioner")
        rbac.assign_role("Bob", "Nurse")
        rbac.assign_role("Charlie", "Community Health Agent")
        
        # Get permissions for users
        print(rbac.get_permissions("Alice"))  # Output: ['view_medical_records', 'write_notes', 'update_treatment_plans']
        print(rbac.get_permissions("Bob"))    # Output: ['view_medical_records', 'update_medication_schedule']
        print(rbac.get_permissions("Charlie"))  # Output: ['view_basic_patient_info']

        # Check specific permissions
        print(rbac.check_permission("Alice", "write_notes"))  # Output: True
        print(rbac.check_permission("Bob", "write_notes"))    # Output: False

    except ValueError as e:
        # Handle errors gracefully
        print(f"Error: {e}")
```
