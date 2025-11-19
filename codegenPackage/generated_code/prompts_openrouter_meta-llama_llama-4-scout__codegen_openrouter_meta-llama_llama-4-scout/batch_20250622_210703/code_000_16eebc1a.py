"""
Generated Code Metadata:
========================
Original URL: https://kadma-wine.co.il
Prompt: "Write a Python script to manage wine inventory for a winery like Kadma Wine, including tracking wine types, quantities, and prices."
Generated: DETERMINISTIC_16eebc1a4fe587b9
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# wine_inventory.py

class Wine:
    """Represents a wine type with its characteristics."""

    def __init__(self, name, quantity, price):
        """
        Initializes a Wine object.

        Args:
            name (str): The name of the wine.
            quantity (int): The quantity of the wine in stock.
            price (float): The price of the wine per unit.
        """
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.quantity} units @ ${self.price:.2f}/unit"


class WineInventory:
    """Manages a collection of wines."""

    def __init__(self):
        """Initializes an empty wine inventory."""
        self.wines = {}

    def add_wine(self, wine):
        """
        Adds a wine to the inventory.

        Args:
            wine (Wine): The wine to add.

        Raises:
            ValueError: If a wine with the same name already exists.
        """
        if wine.name in self.wines:
            raise ValueError(f"Wine '{wine.name}' already exists in the inventory.")
        self.wines[wine.name] = wine

    def remove_wine(self, name):
        """
        Removes a wine from the inventory.

        Args:
            name (str): The name of the wine to remove.

        Raises:
            KeyError: If the wine does not exist in the inventory.
        """
        if name not in self.wines:
            raise KeyError(f"Wine '{name}' does not exist in the inventory.")
        del self.wines[name]

    def update_quantity(self, name, quantity):
        """
        Updates the quantity of a wine in the inventory.

        Args:
            name (str): The name of the wine to update.
            quantity (int): The new quantity of the wine.

        Raises:
            KeyError: If the wine does not exist in the inventory.
            ValueError: If the quantity is negative.
        """
        if name not in self.wines:
            raise KeyError(f"Wine '{name}' does not exist in the inventory.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.wines[name].quantity = quantity

    def update_price(self, name, price):
        """
        Updates the price of a wine in the inventory.

        Args:
            name (str): The name of the wine to update.
            price (float): The new price of the wine.

        Raises:
            KeyError: If the wine does not exist in the inventory.
            ValueError: If the price is negative.
        """
        if name not in self.wines:
            raise KeyError(f"Wine '{name}' does not exist in the inventory.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.wines[name].price = price

    def get_wine(self, name):
        """
        Retrieves a wine from the inventory.

        Args:
            name (str): The name of the wine to retrieve.

        Returns:
            Wine: The wine object if found, otherwise None.
        """
        return self.wines.get(name)

    def list_wines(self):
        """Returns a list of all wines in the inventory."""
        return list(self.wines.values())


def main():
    # Create a wine inventory
    inventory = WineInventory()

    # Add some wines
    inventory.add_wine(Wine("Kadma Red", 100, 15.99))
    inventory.add_wine(Wine("Kadma White", 50, 12.99))
    inventory.add_wine(Wine("Kadma Sparkling", 200, 19.99))

    # List wines
    print("Wine Inventory:")
    for wine in inventory.list_wines():
        print(wine)

    # Update quantity and price
    inventory.update_quantity("Kadma Red", 80)
    inventory.update_price("Kadma White", 13.99)

    # List wines again
    print("\nUpdated Wine Inventory:")
    for wine in inventory.list_wines():
        print(wine)

    # Try to add a duplicate wine
    try:
        inventory.add_wine(Wine("Kadma Red", 100, 15.99))
    except ValueError as e:
        print(f"\nError: {e}")

    # Try to remove a non-existent wine
    try:
        inventory.remove_wine("Kadma Rosé")
    except KeyError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```
