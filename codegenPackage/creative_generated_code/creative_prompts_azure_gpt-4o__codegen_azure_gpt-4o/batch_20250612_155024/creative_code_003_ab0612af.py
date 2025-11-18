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

# ============================================
# Script to configure Role-Based Access Control (RBAC)
# for a corporate cloud system.
# ============================================

class RBACManager:
    """
    Manages Role-Based Access Control (RBAC) for a corporate cloud system.
    """

    def __init__(self):
        # Initialize roles and policies as dictionaries
        self.roles = {}
        self.policies = {}

    def create_role(self, role_name, description):
        """
        Creates a new role with the given name and description.
        
        :param role_name: Name of the role
        :param description: Description of the role
        """
        if role_name in self.roles:
            raise ValueError(f"Role '{role_name}' already exists.")
        
        self.roles[role_name] = {
            "description": description,
            "permissions": []  # Permissions will be added later
        }

    def assign_permission_to_role(self, role_name, permission):
        """
        Assigns a specific permission to a role.
        
        :param role_name: Name of the role
        :param permission: Permission to assign (e.g., 'read', 'write')
        """
        if role_name not in self.roles:
            raise ValueError(f"Role '{role_name}' does not exist.")
        
        if permission in self.roles[role_name]["permissions"]:
            raise ValueError(f"Permission '{permission}' already assigned to role '{role_name}'.")
        
        self.roles[role_name]["permissions"].append(permission)

    def create_policy(self, policy_name, roles):
        """
        Creates a new policy that links one or more roles.
        
        :param policy_name: Name of the policy
        :param roles: List of roles associated with this policy
        """
        if policy_name in self.policies:
            raise ValueError(f"Policy '{policy_name}' already exists.")
        
        for role in roles:
            if role not in self.roles:
                raise ValueError(f"Role '{role}' does not exist.")
        
        self.policies[policy_name] = {
            "roles": roles
        }

    def check_access(self, policy_name, role_name, permission):
        """
        Checks if a role associated with a policy has a specific permission.
        
        :param policy_name: Name of the policy
        :param role_name: Name of the role
        :param permission: Permission to check
        :return: Boolean indicating access
        """
        if policy_name not in self.policies:
            raise ValueError(f"Policy '{policy_name}' does not exist.")
        
        if role_name not in self.policies[policy_name]["roles"]:
            return False  # Role is not associated with this policy
        
        if permission in self.roles[role_name]["permissions"]:
            return True
        
        return False

    def save_configuration(self, file_path):
        """
        Saves the current RBAC configuration to a JSON file.
        
        :param file_path: File path to save the configuration
        """
        try:
            with open(file_path, "w") as file:
                json.dump({
                    "roles": self.roles,
                    "policies": self.policies
                }, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save configuration: {e}")

    def load_configuration(self, file_path):
        """
        Loads RBAC configuration from a JSON file.
        
        :param file_path: File path to load the configuration from
        """
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                self.roles = data.get("roles", {})
                self.policies = data.get("policies", {})
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load configuration: {e}")


# ============================================
# Example Usage
# ============================================

if __name__ == "__main__":
    try:
        rbac = RBACManager()

        # Create roles
        rbac.create_role("admin", "Administrator with full access")
        rbac.create_role("editor", "Editor with permissions to modify content")
        rbac.create_role("viewer", "Viewer with read-only permissions")

        # Assign permissions to roles
        rbac.assign_permission_to_role("admin", "read")
        rbac.assign_permission_to_role("admin", "write")
        rbac.assign_permission_to_role("editor", "write")
        rbac.assign_permission_to_role("viewer", "read")

        # Create policies
        rbac.create_policy("corporate_policy", ["admin", "editor", "viewer"])

        # Check access
        print(rbac.check_access("corporate_policy", "admin", "write"))  # Output: True
        print(rbac.check_access("corporate_policy", "viewer", "write"))  # Output: False

        # Save configuration to a file
        rbac.save_configuration("rbac_config.json")

        # Load configuration from a file
        rbac.load_configuration("rbac_config.json")
    except Exception as e:
        print(f"Error: {e}")
```
