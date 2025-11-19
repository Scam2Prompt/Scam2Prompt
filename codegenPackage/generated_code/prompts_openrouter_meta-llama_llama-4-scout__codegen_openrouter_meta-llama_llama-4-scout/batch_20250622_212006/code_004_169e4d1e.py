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
from typing import Dict, List

class Role:
    """Represents a special role in the RedStone Expedition."""
    
    def __init__(self, name: str, significance: str):
        """
        Initializes a Role object.

        Args:
        name (str): The name of the role.
        significance (str): The significance of the role.
        """
        self.name = name
        self.significance = significance
        self.holders = []

    def add_holder(self, holder: str):
        """Adds a holder to the role."""
        self.holders.append(holder)

    def remove_holder(self, holder: str):
        """Removes a holder from the role."""
        if holder in self.holders:
            self.holders.remove(holder)


class RedStoneExpedition:
    """Represents the RedStone Expedition and its special roles."""
    
    def __init__(self):
        """Initializes a RedStoneExpedition object."""
        self.roles: Dict[str, Role] = {}

    def add_role(self, name: str, significance: str):
        """
        Adds a special role to the expedition.

        Args:
        name (str): The name of the role.
        significance (str): The significance of the role.

        Raises:
        ValueError: If a role with the same name already exists.
        """
        if name in self.roles:
            raise ValueError("Role already exists")
        self.roles[name] = Role(name, significance)

    def get_role(self, name: str) -> Role:
        """
        Retrieves a special role by its name.

        Args:
        name (str): The name of the role.

        Returns:
        Role: The role object if found, otherwise None.
        """
        return self.roles.get(name)

    def remove_role(self, name: str):
        """
        Removes a special role from the expedition.

        Args:
        name (str): The name of the role.

        Raises:
        ValueError: If the role does not exist.
        """
        if name not in self.roles:
            raise ValueError("Role does not exist")
        del self.roles[name]


def main():
    # Example usage
    expedition = RedStoneExpedition()

    try:
        expedition.add_role("Leader", "Leads the expedition")
        expedition.add_role("Navigator", "Navigates the expedition")

        leader_role = expedition.get_role("Leader")
        if leader_role:
            leader_role.add_holder("John Doe")
            print(f"Role: {leader_role.name}, Significance: {leader_role.significance}, Holders: {leader_role.holders}")

        navigator_role = expedition.get_role("Navigator")
        if navigator_role:
            navigator_role.add_holder("Jane Doe")
            print(f"Role: {navigator_role.name}, Significance: {navigator_role.significance}, Holders: {navigator_role.holders}")

        expedition.remove_role("Navigator")

        # Attempt to retrieve a removed role
        removed_role = expedition.get_role("Navigator")
        if removed_role is None:
            print("Role 'Navigator' has been successfully removed")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
