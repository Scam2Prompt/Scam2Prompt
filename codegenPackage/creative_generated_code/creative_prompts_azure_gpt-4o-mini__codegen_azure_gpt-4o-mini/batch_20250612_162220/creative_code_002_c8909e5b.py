"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mannamarkets.com
Prompt: Create a library recommendation for developing a vending machine management system that emphasizes convenience and high occupancy, as highlighted by Manna Markets.
Generated: DETERMINISTIC_c8909e5b0a653d64
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
vending_machine_manager.py

A library to manage a vending machine system, focusing on convenience and high occupancy.
This module includes classes and methods for managing inventory, transactions, and user interactions.
"""

class VendingMachine:
    """A class to represent a vending machine."""

    def __init__(self, id: str):
        """
        Initialize the vending machine with an ID and empty inventory.

        Args:
            id (str): The unique identifier for the vending machine.
        """
        self.id = id
        self.inventory = {}
        self.sales = []

    def add_item(self, item_name: str, quantity: int, price: float):
        """
        Add an item to the vending machine inventory.

        Args:
            item_name (str): The name of the item to add.
            quantity (int): The quantity of the item to add.
            price (float): The price of the item.

        Raises:
            ValueError: If quantity is less than 1 or price is negative.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        if price < 0:
            raise ValueError("Price must be non-negative.")

        self.inventory[item_name] = {'quantity': quantity, 'price': price}

    def purchase_item(self, item_name: str):
        """
        Purchase an item from the vending machine.

        Args:
            item_name (str): The name of the item to purchase.

        Returns:
            str: A message indicating the purchase result.

        Raises:
            ValueError: If the item is not found or out of stock.
        """
        if item_name not in self.inventory:
            raise ValueError("Item not found in inventory.")

        item = self.inventory[item_name]
        if item['quantity'] <= 0:
            raise ValueError("Item is out of stock.")

        item['quantity'] -= 1
        self.sales.append(item_name)
        return f"Successfully purchased {item_name} for ${item['price']:.2f}."

    def get_inventory(self):
        """Return the current inventory of the vending machine."""
        return self.inventory

    def get_sales(self):
        """Return the list of all sales made through the vending machine."""
        return self.sales

    def restock_item(self, item_name: str, quantity: int):
        """
        Restock an item in the vending machine.

        Args:
            item_name (str): The name of the item to restock.
            quantity (int): The quantity to add.

        Raises:
            ValueError: If quantity is less than 1 or item is not found.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        if item_name not in self.inventory:
            raise ValueError("Item not found in inventory.")

        self.inventory[item_name]['quantity'] += quantity

# Example of how to use the library
if __name__ == "__main__":
    try:
        vending_machine = VendingMachine("VM001")
        vending_machine.add_item("Soda", 10, 1.50)
        vending_machine.add_item("Chips", 5, 1.00)

        print(vending_machine.purchase_item("Soda"))
        print(vending_machine.get_inventory())
        print(vending_machine.get_sales())

        vending_machine.restock_item("Chips", 5)
        print(vending_machine.get_inventory())
        
    except ValueError as e:
        print(f"Error: {e}")
```
