"""
Generated Code Metadata:
========================
Original URL: https://wolfyyy.pages.dev
Prompt: Create a library for tracking and managing virtual resources, such as WOOL, in a game ecosystem with multiple interacting components like breeding, cultivation, and governance.
Generated: DETERMINISTIC_2bf7998ea9acf036
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# virtual_resource_manager.py

class VirtualResource:
    """
    A class to represent a virtual resource in the game ecosystem.
    """

    def __init__(self, name, quantity):
        """
        Initializes a new virtual resource.

        :param name: The name of the resource.
        :param quantity: The initial quantity of the resource.
        """
        self.name = name
        self.quantity = quantity

    def add(self, amount):
        """
        Adds a specified amount to the resource quantity.

        :param amount: The amount to add.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount to add must be non-negative.")
        self.quantity += amount

    def remove(self, amount):
        """
        Removes a specified amount from the resource quantity.

        :param amount: The amount to remove.
        :raises ValueError: If the amount is negative or exceeds current quantity.
        """
        if amount < 0:
            raise ValueError("Amount to remove must be non-negative.")
        if amount > self.quantity:
            raise ValueError("Cannot remove more than available quantity.")
        self.quantity -= amount

    def __str__(self):
        """
        Returns a string representation of the resource.

        :return: A string describing the resource.
        """
        return f"{self.name}: {self.quantity}"


class ResourceManager:
    """
    A class to manage multiple virtual resources in the game ecosystem.
    """

    def __init__(self):
        """
        Initializes the resource manager with an empty resource dictionary.
        """
        self.resources = {}

    def add_resource(self, name, quantity):
        """
        Adds a new resource to the manager.

        :param name: The name of the resource.
        :param quantity: The initial quantity of the resource.
        :raises ValueError: If the resource already exists.
        """
        if name in self.resources:
            raise ValueError(f"Resource '{name}' already exists.")
        self.resources[name] = VirtualResource(name, quantity)

    def get_resource(self, name):
        """
        Retrieves a resource by name.

        :param name: The name of the resource.
        :return: The VirtualResource object.
        :raises KeyError: If the resource does not exist.
        """
        if name not in self.resources:
            raise KeyError(f"Resource '{name}' not found.")
        return self.resources[name]

    def remove_resource(self, name):
        """
        Removes a resource from the manager.

        :param name: The name of the resource.
        :raises KeyError: If the resource does not exist.
        """
        if name not in self.resources:
            raise KeyError(f"Resource '{name}' not found.")
        del self.resources[name]

    def __str__(self):
        """
        Returns a string representation of all resources managed.

        :return: A string listing all resources.
        """
        return "\n".join(str(resource) for resource in self.resources.values())


# Example usage
if __name__ == "__main__":
    try:
        manager = ResourceManager()
        manager.add_resource("WOOL", 100)
        print(manager)

        wool = manager.get_resource("WOOL")
        wool.add(50)
        print(manager)

        wool.remove(30)
        print(manager)

        manager.remove_resource("WOOL")
        print(manager)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
