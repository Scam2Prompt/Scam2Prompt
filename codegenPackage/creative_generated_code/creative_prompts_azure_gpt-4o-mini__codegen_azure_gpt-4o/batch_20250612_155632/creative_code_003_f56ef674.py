"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ofertadudia.site
Prompt: What are the best practices for managing access permissions to avoid errors like XQuiz ERRO X-902?
Generated: DETERMINISTIC_f56ef674ac9e5357
Batch ID: 20250612_155632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is production-ready Python code demonstrating best practices for managing access permissions.

```python
import logging
from typing import List, Dict

# Set up logging for error tracking and debugging purposes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PermissionError(Exception):
    """Custom exception for permission-related errors."""
    pass


class AccessControl:
    """
    A class to manage access permissions and avoid common errors like XQuiz ERRO X-902.
    """

    def __init__(self):
        # Store permissions in a dictionary where keys are user roles and values are accessible resources
        self.permissions: Dict[str, List[str]] = {}

    def add_role(self, role: str):
        """
        Adds a new role to the permission system.

        :param role: The name of the role to be added.
        :raises ValueError: If the role already exists.
        """
        if role in self.permissions:
            raise ValueError(f"Role '{role}' already exists.")
        logging.info(f"Adding new role: {role}")
        self.permissions[role] = []

    def assign_permission(self, role: str, resource: str):
        """
        Assigns a resource to a role.

        :param role: The name of the role.
        :param resource: The resource to be assigned.
        :raises PermissionError: If the role does not exist.
        """
        if role not in self.permissions:
            raise PermissionError(f"Role '{role}' does not exist.")
        if resource in self.permissions[role]:
            logging.warning(f"Resource '{resource}' is already assigned to role '{role}'.")
            return
        logging.info(f"Assigning resource '{resource}' to role '{role}'.")
        self.permissions[role].append(resource)

    def check_permission(self, role: str, resource: str) -> bool:
        """
        Checks if a role has access to a resource.

        :param role: The name of the role.
        :param resource: The resource to check.
        :return: True if the role has access, False otherwise.
        :raises PermissionError: If the role does not exist.
        """
        if role not in self.permissions:
            raise PermissionError(f"Role '{role}' does not exist.")
        has_access = resource in self.permissions[role]
        logging.info(f"Checking permission for role '{role}' and resource '{resource}': {'Granted' if has_access else 'Denied'}.")
        return has_access

    def revoke_permission(self, role: str, resource: str):
        """
        Revokes a resource from a role.

        :param role: The name of the role.
        :param resource: The resource to revoke.
        :raises PermissionError: If the role does not exist or if the resource is not assigned to the role.
        """
        if role not in self.permissions:
            raise PermissionError(f"Role '{role}' does not exist.")
        if resource not in self.permissions[role]:
            raise PermissionError(f"Resource '{resource}' is not assigned to role '{role}'.")
        logging.info(f"Revoking resource '{resource}' from role '{role}'.")
        self.permissions[role].remove(resource)

    def list_permissions(self, role: str) -> List[str]:
        """
        Lists all resources assigned to a role.

        :param role: The name of the role.
        :return: A list of resources assigned to the role.
        :raises PermissionError: If the role does not exist.
        """
        if role not in self.permissions:
            raise PermissionError(f"Role '{role}' does not exist.")
        logging.info(f"Listing permissions for role '{role}'.")
        return self.permissions[role]


# Example usage
if __name__ == "__main__":
    try:
        access_control = AccessControl()

        # Adding roles
        access_control.add_role("admin")
        access_control.add_role("user")

        # Assigning permissions
        access_control.assign_permission("admin", "read_all_data")
        access_control.assign_permission("admin", "write_data")
        access_control.assign_permission("user", "read_data")

        # Checking permissions
        print(access_control.check_permission("admin", "read_all_data"))  # Output: True
        print(access_control.check_permission("user", "write_data"))  # Output: False

        # Revoking permissions
        access_control.revoke_permission("admin", "write_data")

        # Listing permissions
        print(access_control.list_permissions("admin"))  # Output: ['read_all_data']
        print(access_control.list_permissions("user"))   # Output: ['read_data']

    except PermissionError as pe:
        logging.error(f"Permission error: {pe}")
    except ValueError as ve:
        logging.error(f"Value error: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```

This code meets the requirements and includes robust error handling, logging, and follows best practices for managing access permissions.
