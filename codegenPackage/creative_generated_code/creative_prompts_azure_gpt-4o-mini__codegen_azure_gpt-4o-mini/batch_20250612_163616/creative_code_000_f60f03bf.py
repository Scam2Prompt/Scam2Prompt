"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixpelinfobrazz.blogspot.com
Prompt: Generate a code snippet for an inventory management system that tracks computer hardware and accessories like SSDs and projectors, similar to the offerings on mixpelinfobrazz.
Generated: DETERMINISTIC_f60f03bf7ef5e141
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InventoryItem:
    """
    A class to represent an item in the inventory.
    Attributes:
        name (str): The name of the item.
        quantity (int): The number of items available in stock.
        price (float): The price of the item.
    """

    def __init__(self, name, quantity, price):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, amount):
        """
        Update the quantity of the item.
        Args:
            amount (int): The amount to adjust the quantity by.
        Raises:
            ValueError: If resulting quantity is negative.
        """
        new_quantity = self.quantity + amount
        if new_quantity < 0:
            raise ValueError("Cannot reduce quantity below zero.")
        self.quantity = new_quantity

    def __str__(self):
        return f"{self.name}: {self.quantity} in stock, ${self.price:.2f}"

class Inventory:
    """
    A class to represent the inventory system for hardware and accessories.
    Attributes:
        items (dict): A dictionary to hold InventoryItem objects indexed by name.
    """

    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity, price):
        """
        Add a new item to the inventory.
        Args:
            name (str): The name of the item.
            quantity (int): The number of items to add.
            price (float): The price of the item.
        """
        if name in self.items:
            raise ValueError(f"Item '{name}' already exists in inventory.")
        
        self.items[name] = InventoryItem(name, quantity, price)

    def update_item_quantity(self, name, amount):
        """
        Update the quantity of an existing item.
        Args:
            name (str): The name of the item to update.
            amount (int): The amount to adjust the quantity by.
        Raises:
            KeyError: If the item does not exist in the inventory.
        """
        if name not in self.items:
            raise KeyError(f"Item '{name}' not found in inventory.")
        
        self.items[name].update_quantity(amount)

    def list_inventory(self):
        """List all items in the inventory."""
        for item in self.items.values():
            print(item)

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding items to inventory
    try:
        inventory.add_item("SSD 1TB", 10, 99.99)
        inventory.add_item("Projector", 5, 299.99)

        # Listing current inventory
        print("Current Inventory:")
        inventory.list_inventory()

        # Updating item quantity
        inventory.update_item_quantity("SSD 1TB", -2)
        print("\nUpdated Inventory after selling 2 SSDs:")
        inventory.list_inventory()

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
