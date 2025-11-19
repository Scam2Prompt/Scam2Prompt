"""
Generated Code Metadata:
========================
Original URL: https://www.executivo2000.com
Prompt: Write a program to manage cocktail and snack inventory for an airport lounge, referencing the food and drink services provided by Executivo 2000.
Generated: DETERMINISTIC_d7ae5b749b6f9865
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InventoryItem:
    """Class to represent an item in the inventory."""
    
    def __init__(self, name: str, quantity: int, price: float):
        """
        Initialize an inventory item.

        :param name: Name of the item
        :param quantity: Quantity of the item in stock
        :param price: Price of the item
        """
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, amount: int):
        """
        Update the quantity of the item.

        :param amount: Amount to add (positive) or remove (negative)
        """
        if self.quantity + amount < 0:
            raise ValueError("Cannot reduce quantity below zero.")
        self.quantity += amount

    def __str__(self):
        """Return a string representation of the inventory item."""
        return f"{self.name}: {self.quantity} available at ${self.price:.2f}"


class Inventory:
    """Class to manage the inventory of cocktails and snacks."""
    
    def __init__(self):
        """Initialize the inventory with an empty dictionary."""
        self.items = {}

    def add_item(self, name: str, quantity: int, price: float):
        """
        Add a new item to the inventory.

        :param name: Name of the item
        :param quantity: Quantity of the item
        :param price: Price of the item
        """
        if name in self.items:
            raise ValueError("Item already exists in inventory.")
        self.items[name] = InventoryItem(name, quantity, price)

    def update_item_quantity(self, name: str, amount: int):
        """
        Update the quantity of an existing item.

        :param name: Name of the item
        :param amount: Amount to add (positive) or remove (negative)
        """
        if name not in self.items:
            raise KeyError("Item not found in inventory.")
        self.items[name].update_quantity(amount)

    def get_inventory(self):
        """Return a list of all items in the inventory."""
        return [str(item) for item in self.items.values()]

    def __str__(self):
        """Return a string representation of the entire inventory."""
        return "\n".join(self.get_inventory())


def main():
    """Main function to manage the inventory."""
    inventory = Inventory()

    # Sample items for the inventory
    try:
        inventory.add_item("Mojito", 50, 8.50)
        inventory.add_item("Caipirinha", 30, 7.00)
        inventory.add_item("Chips", 100, 2.50)
        inventory.add_item("Nuts", 75, 3.00)

        print("Initial Inventory:")
        print(inventory)

        # Update quantities
        inventory.update_item_quantity("Mojito", -5)  # Sold 5 Mojitos
        inventory.update_item_quantity("Chips", 20)   # Received 20 more Chips

        print("\nUpdated Inventory:")
        print(inventory)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
