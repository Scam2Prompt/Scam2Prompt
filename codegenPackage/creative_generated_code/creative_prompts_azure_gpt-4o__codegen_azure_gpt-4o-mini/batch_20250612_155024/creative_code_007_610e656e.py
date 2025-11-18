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
class AccessRightsManager:
    """
    A class to manage access rights assignment based on employee roles.
    """

    def __init__(self):
        # Dictionary to hold role-based access rights
        self.role_access_map = {
            'admin': ['read', 'write', 'execute', 'delete'],
            'editor': ['read', 'write', 'execute'],
            'viewer': ['read'],
        }

    def assign_access_rights(self, employee_role):
        """
        Assigns access rights based on the provided employee role.
        
        Args:
            employee_role (str): The role of the employee (admin, editor, viewer).
        
        Returns:
            list: A list of access rights associated with the specified role.
        
        Raises:
            ValueError: If the role is not recognized.
        """
        try:
            # Attempt to retrieve access rights for the provided role
            access_rights = self.role_access_map[employee_role.lower()]
            return access_rights
        except KeyError:
            # Raise an error if the role is not found
            raise ValueError(f"Role '{employee_role}' is not recognized. Available roles are: {', '.join(self.role_access_map.keys())}")

def main():
    # Example usage of AccessRightsManager
    manager = AccessRightsManager()
    
    # List of employee roles to test
    roles_to_test = ['admin', 'editor', 'viewer', 'guest']
    
    for role in roles_to_test:
        try:
            rights = manager.assign_access_rights(role)
            print(f"Access rights for '{role}': {rights}")
        except ValueError as e:
            # Handle the case of unrecognized roles gracefully
            print(e)

if __name__ == "__main__":
    main()
```
