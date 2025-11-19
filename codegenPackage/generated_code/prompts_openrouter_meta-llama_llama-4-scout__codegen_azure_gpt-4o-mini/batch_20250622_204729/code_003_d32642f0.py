"""
Generated Code Metadata:
========================
Original URL: https://ramdigi.com
Prompt: "Create a code snippet to manage a printing press's inventory, including items like paper, ink, and printing materials, inspired by Ram Digi's infrastructure and services."
Generated: DETERMINISTIC_d32642f039bf9d47
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InventoryItem:
    """
    Class to represent an item in the inventory.
    Attributes:
        name (str): The name of the inventory item.
        quantity (int): The quantity of the item in stock.
        unit_price (float): The price per unit of the item.
    """

    def __init__(self, name: str, quantity: int, unit_price: float):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def update_quantity(self, amount: int):
        """
        Update the quantity of the item.
        Args:
            amount (int): The amount to add (positive) or remove (negative).
        Raises:
            ValueError: If the resulting quantity is negative.
        """
        if self.quantity + amount < 0:
            raise ValueError(f"Cannot reduce quantity of {self.name} below zero.")
        self.quantity += amount

    def __str__(self):
        return f"{self.name}: {self.quantity} units at ${self.unit_price:.2f} each"


class Inventory:
    """
    Class to manage the inventory of a printing press.
    Attributes:
        items (dict): A dictionary to store inventory items by name.
    """

    def __init__(self):
        self.items = {}

    def add_item(self, item: InventoryItem):
        """
        Add a new item to the inventory.
        Args:
            item (InventoryItem): The item to add.
        """
        if item.name in self.items:
            raise ValueError(f"Item {item.name} already exists in inventory.")
        self.items[item.name] = item

    def update_item_quantity(self, name: str, amount: int):
        """
        Update the quantity of an existing item.
        Args:
            name (str): The name of the item to update.
            amount (int): The amount to add (positive) or remove (negative).
        Raises:
            KeyError: If the item does not exist in the inventory.
        """
        if name not in self.items:
            raise KeyError(f"Item {name} not found in inventory.")
        self.items[name].update_quantity(amount)

    def get_inventory_report(self):
        """
        Generate a report of the current inventory.
        Returns:
            str: A formatted string of the inventory report.
        """
        report = "Inventory Report:\n"
        report += "\n".join(str(item) for item in self.items.values())
        return report

    def total_inventory_value(self):
        """
        Calculate the total value of the inventory.
        Returns:
            float: The total value of all items in the inventory.
        """
        return sum(item.quantity * item.unit_price for item in self.items.values())


# Example usage
if __name__ == "__main__":
    try:
        inventory = Inventory()

        # Adding items to the inventory
        inventory.add_item(InventoryItem("Paper", 1000, 0.05))
        inventory.add_item(InventoryItem("Ink", 500, 0.10))
        inventory.add_item(InventoryItem("Printing Plates", 200, 1.50))

        # Updating item quantities
        inventory.update_item_quantity("Paper", -200)  # Sold 200 sheets
        inventory.update_item_quantity("Ink", 100)     # Received 100 more liters

        # Generating inventory report
        print(inventory.get_inventory_report())

        # Total inventory value
        print(f"Total Inventory Value: ${inventory.total_inventory_value():.2f}")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
