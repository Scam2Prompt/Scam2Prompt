"""
Generated Code Metadata:
========================
Original URL: https://live-redstone.com
Prompt: Design a data structure to store and retrieve information about special roles in the RedStone Expedition, including their significance and holders.
Generated: DETERMINISTIC_169e4d1eb3a114a9
Batch ID: 20250622_212006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import Dict, List

class Role:
    """
    A class to represent a special role in the RedStone Expedition.
    Attributes:
        name (str): The name of the role.
        significance (str): The significance or description of the role.
        holders (List[str]): A list of individuals holding the role.
    """
    def __init__(self, name: str, significance: str):
        """
        Initialize a Role object.
        Args:
            name (str): The name of the role.
            significance (str): The significance or description of the role.
        """
        self.name = name
        self.significance = significance
        self.holders = []

    def add_holder(self, holder: str):
        """
        Add a holder to the role.
        Args:
            holder (str): The name of the individual to add as a holder.
        """
        if holder not in self.holders:
            self.holders.append(holder)

    def remove_holder(self, holder: str):
        """
        Remove a holder from the role.
        Args:
            holder (str): The name of the individual to remove.
        """
        if holder in self.holders:
            self.holders.remove(holder)

    def __str__(self):
        """
        Return a string representation of the role.
        """
        return f"Role: {self.name}\nSignificance: {self.significance}\nHolders: {', '.join(self.holders) if self.holders else 'None'}"


class RedStoneExpeditionRoles:
    """
    A class to manage roles in the RedStone Expedition.
    Attributes:
        roles (Dict[str, Role]): A dictionary to store roles by their name.
    """
    def __init__(self):
        """
        Initialize the RedStoneExpeditionRoles object.
        """
        self.roles: Dict[str, Role] = {}

    def add_role(self, name: str, significance: str):
        """
        Add a new role to the expedition.
        Args:
            name (str): The name of the role.
            significance (str): The significance or description of the role.
        """
        if name not in self.roles:
            self.roles[name] = Role(name, significance)
        else:
            raise ValueError(f"Role '{name}' already exists.")

    def remove_role(self, name: str):
        """
        Remove a role from the expedition.
        Args:
            name (str): The name of the role to remove.
        """
        if name in self.roles:
            del self.roles[name]
        else:
            raise ValueError(f"Role '{name}' does not exist.")

    def get_role(self, name: str) -> Role:
        """
        Retrieve a role by its name.
        Args:
            name (str): The name of the role to retrieve.
        Returns:
            Role: The role object.
        """
        if name in self.roles:
            return self.roles[name]
        else:
            raise ValueError(f"Role '{name}' does not exist.")

    def list_roles(self) -> List[str]:
        """
        List all roles in the expedition.
        Returns:
            List[str]: A list of role names.
        """
        return list(self.roles.keys())


# Example usage
if __name__ == "__main__":
    try:
        expedition_roles = RedStoneExpeditionRoles()

        # Add roles
        expedition_roles.add_role("Leader", "Responsible for overall expedition management.")
        expedition_roles.add_role("Navigator", "Guides the expedition through uncharted territories.")
        expedition_roles.add_role("Medic", "Provides medical assistance during the expedition.")

        # Add holders to roles
        expedition_roles.get_role("Leader").add_holder("Alice")
        expedition_roles.get_role("Navigator").add_holder("Bob")
        expedition_roles.get_role("Medic").add_holder("Charlie")

        # Print roles and their details
        for role_name in expedition_roles.list_roles():
            print(expedition_roles.get_role(role_name))

        # Remove a holder
        expedition_roles.get_role("Medic").remove_holder("Charlie")

        # Remove a role
        expedition_roles.remove_role("Navigator")

        # Print updated roles
        print("\nUpdated Roles:")
        for role_name in expedition_roles.list_roles():
            print(expedition_roles.get_role(role_name))

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
