"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phanytom.com
Prompt: Write code to implement a security policy configuration system for an IAM solution, allowing customization based on user roles and organizational requirements, as detailed by Techmaestropus.
Generated: DETERMINISTIC_1486dc061ba01eb8
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
from typing import Dict, List, Union

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IAMPolicy:
    """Class representing a security policy for a user role in an IAM solution."""

    def __init__(self, role: str):
        """
        Initializes the IAMPolicy with the given role.

        :param role: The role for which the policy is defined.
        """
        self.role = role
        self.permissions = []

    def add_permission(self, permission: str) -> None:
        """
        Adds a permission to the policy.

        :param permission: The permission to add.
        """
        if permission not in self.permissions:
            self.permissions.append(permission)
            logging.info(f"Added permission '{permission}' to role '{self.role}'.")
        else:
            logging.warning(f"Permission '{permission}' already exists for role '{self.role}'.")

    def remove_permission(self, permission: str) -> None:
        """
        Removes a permission from the policy.

        :param permission: The permission to remove.
        """
        try:
            self.permissions.remove(permission)
            logging.info(f"Removed permission '{permission}' from role '{self.role}'.")
        except ValueError:
            logging.error(f"Permission '{permission}' not found for role '{self.role}'.")

    def to_dict(self) -> Dict[str, Union[str, List[str]]]:
        """
        Converts the policy to a dictionary format for serialization.

        :return: A dictionary representation of the policy.
        """
        return {
            "role": self.role,
            "permissions": self.permissions
        }


class PolicyManager:
    """Class to manage IAM policies."""
    
    def __init__(self):
        """Initializes the PolicyManager with an empty policy list."""
        self.policies = {}

    def create_policy(self, role: str) -> IAMPolicy:
        """
        Creates a new IAM policy for the specified role.

        :param role: The role for which the policy is to be created.
        :return: The newly created IAMPolicy object.
        """
        if role in self.policies:
            logging.error(f"Policy for role '{role}' already exists.")
            raise ValueError(f"Policy for role '{role}' already exists.")
        
        policy = IAMPolicy(role)
        self.policies[role] = policy
        logging.info(f"Created policy for role '{role}'.")
        return policy

    def get_policy(self, role: str) -> IAMPolicy:
        """
        Retrieves the IAM policy for the specified role.

        :param role: The role for which the policy is to be retrieved.
        :return: The IAMPolicy object for the specified role.
        :raises KeyError: If the policy for the role does not exist.
        """
        if role not in self.policies:
            logging.error(f"Policy for role '{role}' does not exist.")
            raise KeyError(f"Policy for role '{role}' does not exist.")
        
        return self.policies[role]

    def serialize_policies(self) -> str:
        """
        Serializes all policies to a JSON string.

        :return: A JSON string representation of all policies.
        """
        policies_dict = {role: policy.to_dict() for role, policy in self.policies.items()}
        return json.dumps(policies_dict, indent=4)

# Example usage
if __name__ == "__main__":
    policy_manager = PolicyManager()
    
    # Creating a new policy for a user role
    try:
        admin_policy = policy_manager.create_policy("admin")
        admin_policy.add_permission("read")
        admin_policy.add_permission("write")
        admin_policy.add_permission("delete")
        
        # Removing a permission
        admin_policy.remove_permission("write")
        
        # Serializing the policies to JSON
        print(policy_manager.serialize_policies())
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
