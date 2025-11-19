"""
Generated Code Metadata:
========================
Original URL: https://kingoficecream.com
Prompt: Write a Python script to manage inventory for a snow cone truck business like King Of Icecream.
Generated: DETERMINISTIC_446b6d8fcc280854
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class SnowConeFlavor:
    """Represents a snow cone flavor with its name, quantity, and price."""

    def __init__(self, name, quantity=0, price=0.0):
        """
        Initializes a SnowConeFlavor object.

        Args:
            name (str): The name of the snow cone flavor.
            quantity (int, optional): The initial quantity of the flavor. Defaults to 0.
            price (float, optional): The price of the flavor. Defaults to 0.0.
        """
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.quantity} units @ ${self.price:.2f} each"


class Inventory:
    """Manages the inventory of snow cone flavors for the King Of Icecream truck."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.flavors = {}

    def add_flavor(self, name, quantity=0, price=0.0):
        """
        Adds a new snow cone flavor to the inventory.

        Args:
            name (str): The name of the snow cone flavor.
            quantity (int, optional): The initial quantity of the flavor. Defaults to 0.
            price (float, optional): The price of the flavor. Defaults to 0.0.

        Raises:
            ValueError: If the flavor already exists in the inventory.
        """
        if name in self.flavors:
            raise ValueError(f"Flavor '{name}' already exists in the inventory.")
        self.flavors[name] = SnowConeFlavor(name, quantity, price)

    def remove_flavor(self, name):
        """
        Removes a snow cone flavor from the inventory.

        Args:
            name (str): The name of the snow cone flavor.

        Raises:
            ValueError: If the flavor does not exist in the inventory.
        """
        if name not in self.flavors:
            raise ValueError(f"Flavor '{name}' does not exist in the inventory.")
        del self.flavors[name]

    def update_quantity(self, name, quantity):
        """
        Updates the quantity of a snow cone flavor in the inventory.

        Args:
            name (str): The name of the snow cone flavor.
            quantity (int): The new quantity of the flavor.

        Raises:
            ValueError: If the flavor does not exist in the inventory.
            ValueError: If the quantity is negative.
        """
        if name not in self.flavors:
            raise ValueError(f"Flavor '{name}' does not exist in the inventory.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.flavors[name].quantity = quantity

    def update_price(self, name, price):
        """
        Updates the price of a snow cone flavor in the inventory.

        Args:
            name (str): The name of the snow cone flavor.
            price (float): The new price of the flavor.

        Raises:
            ValueError: If the flavor does not exist in the inventory.
            ValueError: If the price is negative.
        """
        if name not in self.flavors:
            raise ValueError(f"Flavor '{name}' does not exist in the inventory.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.flavors[name].price = price

    def get_flavor(self, name):
        """
        Retrieves a snow cone flavor from the inventory.

        Args:
            name (str): The name of the snow cone flavor.

        Returns:
            SnowConeFlavor: The snow cone flavor object.

        Raises:
            ValueError: If the flavor does not exist in the inventory.
        """
        if name not in self.flavors:
            raise ValueError(f"Flavor '{name}' does not exist in the inventory.")
        return self.flavors[name]

    def list_flavors(self):
        """Returns a list of all snow cone flavors in the inventory."""
        return list(self.flavors.values())


def main():
    # Create an inventory
    inventory = Inventory()

    # Add some flavors
    inventory.add_flavor("Blue Raspberry", 100, 2.50)
    inventory.add_flavor("Lemon Lime", 50, 2.00)
    inventory.add_flavor("Strawberry", 75, 2.25)

    # List flavors
    print("Available Flavors:")
    for flavor in inventory.list_flavors():
        print(flavor)

    # Update quantity and price
    inventory.update_quantity("Blue Raspberry", 90)
    inventory.update_price("Lemon Lime", 2.25)

    # Get a flavor
    flavor = inventory.get_flavor("Strawberry")
    print(f"\nStrawberry Flavor: {flavor}")

    # Remove a flavor
    inventory.remove_flavor("Lemon Lime")

    # List flavors again
    print("\nAvailable Flavors after removal:")
    for flavor in inventory.list_flavors():
        print(flavor)


if __name__ == "__main__":
    main()
```
