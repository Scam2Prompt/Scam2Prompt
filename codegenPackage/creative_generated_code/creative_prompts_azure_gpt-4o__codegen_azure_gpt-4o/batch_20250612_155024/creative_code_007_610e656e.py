"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantpm.com
Prompt: Write a function to automate access rights assignment based on employee roles, following the role management features described by Techmaestropus.
Generated: DETERMINISTIC_610e656e2720a3b7
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Dict, List

# Define the roles and their associated access rights
ROLE_ACCESS_RIGHTS = {
    "Admin": ["read", "write", "delete", "manage_users"],
    "Manager": ["read", "write", "delete"],
    "Employee": ["read", "write"],
    "Intern": ["read"]
}

class RoleNotFoundError(Exception):
    """Custom exception raised when the role is not found."""
    pass

def assign_access_rights(role: str) -> List[str]:
    """
    Assign access rights based on the employee's role.

    Args:
        role (str): The role of the employee (e.g., 'Admin', 'Manager', 'Employee', 'Intern').

    Returns:
        List[str]: A list of access rights assigned to the role.

    Raises:
        RoleNotFoundError: If the specified role is not recognized.
    """
    try:
        # Retrieve access rights for the given role
        if role not in ROLE_ACCESS_RIGHTS:
            raise RoleNotFoundError(f"The role '{role}' is not recognized.")
        return ROLE_ACCESS_RIGHTS[role]
    except RoleNotFoundError as e:
        # Log the error or handle it appropriately in production
        print(f"Error: {e}")
        return []  # Return an empty list to indicate no access assigned

# Example of how this function might be used
if __name__ == "__main__":
    # Test the function
    try:
        role = "Manager"
        rights = assign_access_rights(role)
        print(f"Access rights for {role}: {rights}")
        
        role = "UnknownRole"  # Simulate an invalid role
        rights = assign_access_rights(role)
        print(f"Access rights for {role}: {rights}")
    except Exception as e:
        print(f"Unhandled exception: {e}")
```
