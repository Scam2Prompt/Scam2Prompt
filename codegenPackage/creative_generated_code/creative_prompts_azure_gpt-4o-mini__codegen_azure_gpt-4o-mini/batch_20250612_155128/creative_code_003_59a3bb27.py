"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://compensadosscursel.blogspot.com
Prompt: Suggest a library for managing inventory of construction materials, specifically for products like compensados and doors, as highlighted by Fabrica de Compensados Scursel.
Generated: DETERMINISTIC_59a3bb272d4b3a38
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# inventory_manager.py

class InventoryItem:
    """
    Class to represent an inventory item, such as a construction material.
    Attributes:
        name (str): The name of the item.
        quantity (int): The quantity of the item in stock.
        unit_price (float): Price per unit of the item.
    """

    def __init__(self, name: str, quantity: int, unit_price: float):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def __str__(self):
        return f"{self.name}: {self.quantity} units at ${self.unit_price:.2f} each"

    def update_quantity(self, amount: int):
        """
        Updates the quantity of the inventory item.
        Args:
            amount (int): Amount to add or subtract from the current quantity.
        Raises:
            ValueError: If the resulting quantity is negative.
        """
        if self.quantity + amount < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity += amount


class Inventory:
    """
    Class to manage a collection of inventory items.
    Attributes:
        items (dict): A dictionary to store inventory items by name.
    """

    def __init__(self):
        self.items = {}

    def add_item(self, item: InventoryItem):
        """
        Adds a new inventory item to the inventory.
        Args:
            item (InventoryItem): The inventory item to add.
        """
        if item.name in self.items:
            raise ValueError("Item already exists in the inventory.")
        self.items[item.name] = item

    def update_item_quantity(self, item_name: str, amount: int):
        """
        Updates the quantity of a specified inventory item.
        Args:
            item_name (str): The name of the inventory item.
            amount (int): The amount to add or subtract.
        Raises:
            KeyError: If the item is not found in the inventory.
        """
        if item_name not in self.items:
            raise KeyError("Item not found in the inventory.")
        self.items[item_name].update_quantity(amount)

    def get_inventory_report(self):
        """
        Generates a report of all inventory items.
        Returns:
            str: A string representation of the inventory report.
        """
        report = "Inventory Report:\n"
        for item in self.items.values():
            report += str(item) + "\n"
        return report


# Example usage
if __name__ == "__main__":
    try:
        inventory = Inventory()

        # Adding inventory items
        compensados = InventoryItem("Compensados", 50, 25.0)
        doors = InventoryItem("Doors", 30, 150.0)

        inventory.add_item(compensados)
        inventory.add_item(doors)

        # Updating quantities
        inventory.update_item_quantity("Compensados", -10)
        inventory.update_item_quantity("Doors", 5)

        # Print the inventory report
        print(inventory.get_inventory_report())

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
