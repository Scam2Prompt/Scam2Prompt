"""
Generated Code Metadata:
========================
Original URL: https://redstones-finance.com
Prompt: Explain the role of special roles in the RedStone Expedition and provide a JSON example of a roles table.
Generated: DETERMINISTIC_6e94493987eca3be
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# roles.py

import json

class Role:
    """Represents a role in the RedStone Expedition."""

    def __init__(self, name, description, permissions):
        """
        Initializes a Role object.

        Args:
            name (str): The name of the role.
            description (str): A brief description of the role.
            permissions (list): A list of permissions associated with the role.
        """
        self.name = name
        self.description = description
        self.permissions = permissions

    def to_dict(self):
        """Converts the Role object to a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "permissions": self.permissions
        }

    def __str__(self):
        return f"Role('{self.name}', '{self.description}', {self.permissions})"


class RolesTable:
    """Represents a table of roles in the RedStone Expedition."""

    def __init__(self):
        """Initializes an empty RolesTable object."""
        self.roles = []

    def add_role(self, role):
        """
        Adds a role to the roles table.

        Args:
            role (Role): The role to add.

        Raises:
            ValueError: If the role already exists in the table.
        """
        if any(r.name == role.name for r in self.roles):
            raise ValueError(f"Role '{role.name}' already exists.")
        self.roles.append(role)

    def remove_role(self, role_name):
        """
        Removes a role from the roles table.

        Args:
            role_name (str): The name of the role to remove.

        Raises:
            ValueError: If the role does not exist in the table.
        """
        for role in self.roles:
            if role.name == role_name:
                self.roles.remove(role)
                return
        raise ValueError(f"Role '{role_name}' does not exist.")

    def to_json(self):
        """Converts the RolesTable object to a JSON string."""
        roles_dict = [role.to_dict() for role in self.roles]
        return json.dumps(roles_dict, indent=4)


# Example usage:
if __name__ == "__main__":
    # Create roles
    admin_role = Role(
        "Admin",
        "System administrator role.",
        ["create", "read", "update", "delete"]
    )
    moderator_role = Role(
        "Moderator",
        "Moderator role.",
        ["read", "update"]
    )
    user_role = Role(
        "User",
        "Basic user role.",
        ["read"]
    )

    # Create roles table
    roles_table = RolesTable()
    roles_table.add_role(admin_role)
    roles_table.add_role(moderator_role)
    roles_table.add_role(user_role)

    # Print roles table as JSON
    print(roles_table.to_json())

    # Try to add duplicate role
    try:
        roles_table.add_role(admin_role)
    except ValueError as e:
        print(e)

    # Remove role
    roles_table.remove_role("Moderator")

    # Print updated roles table as JSON
    print(roles_table.to_json())
```
