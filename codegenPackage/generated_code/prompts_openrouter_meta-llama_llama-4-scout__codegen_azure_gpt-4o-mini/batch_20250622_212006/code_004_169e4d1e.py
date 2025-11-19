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
class Role:
    """
    A class to represent a special role in the RedStone Expedition.

    Attributes:
        name (str): The name of the role.
        significance (str): The significance of the role.
        holder (str): The current holder of the role.
    """

    def __init__(self, name: str, significance: str, holder: str):
        """
        Initializes a new Role instance.

        Args:
            name (str): The name of the role.
            significance (str): The significance of the role.
            holder (str): The current holder of the role.
        """
        self.name = name
        self.significance = significance
        self.holder = holder

    def __repr__(self):
        """Returns a string representation of the Role instance."""
        return f"Role(name={self.name}, significance={self.significance}, holder={self.holder})"


class RoleManager:
    """
    A class to manage special roles in the RedStone Expedition.

    Attributes:
        roles (dict): A dictionary to store roles by their name.
    """

    def __init__(self):
        """Initializes the RoleManager with an empty roles dictionary."""
        self.roles = {}

    def add_role(self, name: str, significance: str, holder: str) -> None:
        """
        Adds a new role to the manager.

        Args:
            name (str): The name of the role.
            significance (str): The significance of the role.
            holder (str): The current holder of the role.

        Raises:
            ValueError: If the role already exists.
        """
        if name in self.roles:
            raise ValueError(f"Role '{name}' already exists.")
        self.roles[name] = Role(name, significance, holder)

    def get_role(self, name: str) -> Role:
        """
        Retrieves a role by its name.

        Args:
            name (str): The name of the role to retrieve.

        Returns:
            Role: The Role instance associated with the given name.

        Raises:
            KeyError: If the role does not exist.
        """
        if name not in self.roles:
            raise KeyError(f"Role '{name}' not found.")
        return self.roles[name]

    def update_holder(self, name: str, new_holder: str) -> None:
        """
        Updates the holder of a specified role.

        Args:
            name (str): The name of the role to update.
            new_holder (str): The new holder of the role.

        Raises:
            KeyError: If the role does not exist.
        """
        if name not in self.roles:
            raise KeyError(f"Role '{name}' not found.")
        self.roles[name].holder = new_holder

    def remove_role(self, name: str) -> None:
        """
        Removes a role from the manager.

        Args:
            name (str): The name of the role to remove.

        Raises:
            KeyError: If the role does not exist.
        """
        if name not in self.roles:
            raise KeyError(f"Role '{name}' not found.")
        del self.roles[name]

    def list_roles(self) -> list:
        """
        Lists all roles in the manager.

        Returns:
            list: A list of Role instances.
        """
        return list(self.roles.values())


# Example usage:
if __name__ == "__main__":
    role_manager = RoleManager()
    
    # Adding roles
    role_manager.add_role("Explorer", "Leads expeditions into unknown territories", "Alice")
    role_manager.add_role("Guardian", "Protects the expedition from threats", "Bob")

    # Retrieving a role
    try:
        explorer_role = role_manager.get_role("Explorer")
        print(explorer_role)
    except KeyError as e:
        print(e)

    # Updating a holder
    try:
        role_manager.update_holder("Guardian", "Charlie")
        print(role_manager.get_role("Guardian"))
    except KeyError as e:
        print(e)

    # Listing all roles
    print(role_manager.list_roles())

    # Removing a role
    try:
        role_manager.remove_role("Explorer")
        print(role_manager.list_roles())
    except KeyError as e:
        print(e)
```
