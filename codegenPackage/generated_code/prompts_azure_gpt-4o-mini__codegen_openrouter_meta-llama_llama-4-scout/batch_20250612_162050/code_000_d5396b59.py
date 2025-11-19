"""
Generated Code Metadata:
========================
Original URL: https://kingoficecream.com
Prompt: Generate a Python script to simulate an ice cream truck inventory management system for a snow cone truck.
Generated: DETERMINISTIC_d5396b59319004f0
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ice_cream_truck_inventory.py

class SnowConeFlavor:
    """Represents a snow cone flavor in the inventory."""

    def __init__(self, name, quantity, price):
        """
        Initializes a SnowConeFlavor object.

        Args:
            name (str): The name of the snow cone flavor.
            quantity (int): The quantity of the snow cone flavor in stock.
            price (float): The price of the snow cone flavor.
        """
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.quantity} units @ ${self.price:.2f} each"


class SnowConeTruckInventory:
    """Manages the inventory of a snow cone truck."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.flavors = {}

    def add_flavor(self, name, quantity, price):
        """
        Adds a new snow cone flavor to the inventory.

        Args:
            name (str): The name of the snow cone flavor.
            quantity (int): The quantity of the snow cone flavor in stock.
            price (float): The price of the snow cone flavor.

        Raises:
            ValueError: If the quantity or price is invalid.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if price < 0:
            raise ValueError("Price cannot be negative")

        self.flavors[name] = SnowConeFlavor(name, quantity, price)

    def remove_flavor(self, name):
        """
        Removes a snow cone flavor from the inventory.

        Args:
            name (str): The name of the snow cone flavor to remove.

        Raises:
            KeyError: If the flavor is not in the inventory.
        """
        if name not in self.flavors:
            raise KeyError(f"Flavor '{name}' not found in inventory")
        del self.flavors[name]

    def restock_flavor(self, name, quantity):
        """
        Restocks a snow cone flavor in the inventory.

        Args:
            name (str): The name of the snow cone flavor to restock.
            quantity (int): The quantity to add to the flavor's stock.

        Raises:
            KeyError: If the flavor is not in the inventory.
            ValueError: If the quantity is invalid.
        """
        if name not in self.flavors:
            raise KeyError(f"Flavor '{name}' not found in inventory")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.flavors[name].quantity += quantity

    def sell_flavor(self, name, quantity):
        """
        Sells a certain quantity of a snow cone flavor.

        Args:
            name (str): The name of the snow cone flavor to sell.
            quantity (int): The quantity to sell.

        Raises:
            KeyError: If the flavor is not in the inventory.
            ValueError: If the quantity is invalid.
        """
        if name not in self.flavors:
            raise KeyError(f"Flavor '{name}' not found in inventory")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if quantity > self.flavors[name].quantity:
            raise ValueError("Insufficient stock")

        self.flavors[name].quantity -= quantity

    def get_flavor(self, name):
        """
        Retrieves a snow cone flavor from the inventory.

        Args:
            name (str): The name of the snow cone flavor to retrieve.

        Returns:
            SnowConeFlavor: The snow cone flavor object.

        Raises:
            KeyError: If the flavor is not in the inventory.
        """
        if name not in self.flavors:
            raise KeyError(f"Flavor '{name}' not found in inventory")
        return self.flavors[name]

    def __str__(self):
        inventory_str = "Snow Cone Truck Inventory:\n"
        for flavor in self.flavors.values():
            inventory_str += f"- {flavor}\n"
        return inventory_str


def main():
    try:
        inventory = SnowConeTruckInventory()

        # Add some initial flavors
        inventory.add_flavor("Blue Raspberry", 100, 1.50)
        inventory.add_flavor("Lemon Lime", 50, 1.25)
        inventory.add_flavor("Strawberry", 75, 1.75)

        print(inventory)

        # Restock a flavor
        inventory.restock_flavor("Blue Raspberry", 25)
        print(f"Restocked Blue Raspberry. New quantity: {inventory.get_flavor('Blue Raspberry').quantity}")

        # Sell some flavors
        inventory.sell_flavor("Lemon Lime", 10)
        print(f"Sold 10 Lemon Lime snow cones. New quantity: {inventory.get_flavor('Lemon Lime').quantity}")

        # Remove a flavor
        inventory.remove_flavor("Strawberry")
        print("Removed Strawberry flavor from inventory.")

        print(inventory)

    except (KeyError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
