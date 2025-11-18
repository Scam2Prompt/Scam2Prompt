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

class SecurityPolicyConfiguration:
    """
    Security Policy Configuration System for IAM Solution.
    Allows customization based on user roles and organizational requirements.
    """

    def __init__(self):
        """
        Initialize the configuration system with default policies.
        """
        self.policies = {}
        self.roles = set()

    def add_role(self, role_name):
        """
        Add a new role to the IAM system.

        Args:
            role_name (str): The name of the role to be added.
        
        Raises:
            ValueError: If the role already exists.
        """
        if role_name in self.roles:
            raise ValueError(f"Role '{role_name}' already exists.")
        self.roles.add(role_name)
        self.policies[role_name] = {}

    def configure_policy(self, role_name, policy_name, policy_details):
        """
        Configure a policy for a specific role.

        Args:
            role_name (str): The name of the role.
            policy_name (str): The name of the policy.
            policy_details (dict): The details of the policy (e.g., permissions, restrictions).
        
        Raises:
            ValueError: If the role does not exist.
        """
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist.")
        self.policies[role_name][policy_name] = policy_details

    def get_policy(self, role_name, policy_name):
        """
        Retrieve a specific policy for a role.

        Args:
            role_name (str): The name of the role.
            policy_name (str): The name of the policy.
        
        Returns:
            dict: The policy details.
        
        Raises:
            ValueError: If the role or policy does not exist.
        """
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist.")
        if policy_name not in self.policies[role_name]:
            raise ValueError(f"Policy '{policy_name}' does not exist for role '{role_name}'.")
        return self.policies[role_name][policy_name]

    def delete_policy(self, role_name, policy_name):
        """
        Delete a specific policy for a role.

        Args:
            role_name (str): The name of the role.
            policy_name (str): The name of the policy to be deleted.
        
        Raises:
            ValueError: If the role or policy does not exist.
        """
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist.")
        if policy_name not in self.policies[role_name]:
            raise ValueError(f"Policy '{policy_name}' does not exist for role '{role_name}'.")
        del self.policies[role_name][policy_name]

    def export_policies(self, filepath):
        """
        Export all policies to a JSON file.

        Args:
            filepath (str): The path to the file where policies will be exported.
        
        Raises:
            IOError: If the file cannot be written.
        """
        try:
            with open(filepath, 'w') as file:
                json.dump(self.policies, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write policies to file: {e}")

    def import_policies(self, filepath):
        """
        Import policies from a JSON file.

        Args:
            filepath (str): The path to the file containing policies in JSON format.
        
        Raises:
            IOError: If the file cannot be read.
            ValueError: If the file contains invalid data.
        """
        try:
            with open(filepath, 'r') as file:
                imported_policies = json.load(file)
                if not isinstance(imported_policies, dict):
                    raise ValueError("Invalid policy data in file.")
                self.policies = imported_policies
                self.roles = set(imported_policies.keys())
        except IOError as e:
            raise IOError(f"Failed to read policies from file: {e}")
        except ValueError as e:
            raise ValueError(f"Invalid policy data: {e}")

# Example usage:
# Create an instance of the configuration system.
config_system = SecurityPolicyConfiguration()

# Add roles and configure policies.
config_system.add_role("Admin")
config_system.configure_policy("Admin", "FullAccess", {"permissions": ["read", "write", "delete"], "restrictions": []})

config_system.add_role("User")
config_system.configure_policy("User", "ReadOnly", {"permissions": ["read"], "restrictions": ["write", "delete"]})

# Export policies to a file.
config_system.export_policies("policies.json")

# Import policies from a file.
config_system.import_policies("policies.json")
```
