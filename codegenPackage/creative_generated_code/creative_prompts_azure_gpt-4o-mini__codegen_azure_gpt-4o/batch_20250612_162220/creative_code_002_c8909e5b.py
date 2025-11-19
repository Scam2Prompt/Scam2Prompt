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
# vending_machine.py

"""
Library for Vending Machine Management System emphasizing convenience and high occupancy.

This library provides functionalities to manage vending machine inventory, sales tracking, 
payment processing, and reporting for efficient operations.

Author: Expert Programmer
Version: 1.0
"""

import json
from datetime import datetime


class VendingMachine:
    """
    A class to represent a vending machine.
    """

    def __init__(self, machine_id, location):
        """
        Initialize the vending machine.

        Args:
            machine_id (str): Unique ID for the vending machine.
            location (str): Location of the vending machine.
        """
        self.machine_id = machine_id
        self.location = location
        self.inventory = {}  # {'item_id': {'name': str, 'price': float, 'quantity': int}}
        self.sales = []  # [{'item_id': str, 'quantity': int, 'timestamp': datetime}]
        self.balance = 0.0  # Total earnings from sales

    def add_item(self, item_id, name, price, quantity):
        """
        Add or update items in the inventory.

        Args:
            item_id (str): Unique ID of the item.
            name (str): Name of the item.
            price (float): Price of the item.
            quantity (int): Quantity of the item.

        Raises:
            ValueError: If price or quantity is invalid.
        """
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative.")
        self.inventory[item_id] = {"name": name, "price": price, "quantity": quantity}

    def purchase_item(self, item_id, quantity):
        """
        Process the purchase of an item.

        Args:
            item_id (str): Unique ID of the item to be purchased.
            quantity (int): Quantity of the item to be purchased.

        Returns:
            dict: Details of the purchase.

        Raises:
            ValueError: If the item_id is invalid, out of stock, or quantity is invalid.
        """
        if item_id not in self.inventory:
            raise ValueError(f"Item ID '{item_id}' does not exist.")
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if self.inventory[item_id]["quantity"] < quantity:
            raise ValueError("Insufficient stock for the requested item.")

        # Process the purchase
        self.inventory[item_id]["quantity"] -= quantity
        total_cost = self.inventory[item_id]["price"] * quantity
        self.balance += total_cost
        transaction = {
            "item_id": item_id,
            "quantity": quantity,
            "timestamp": datetime.now(),
            "total_cost": total_cost,
        }
        self.sales.append(transaction)
        return transaction

    def get_inventory(self):
        """
        Get the current inventory.

        Returns:
            dict: Current inventory details.
        """
        return self.inventory

    def get_sales_report(self):
        """
        Get a sales report.

        Returns:
            dict: Sales report containing total sales and individual transaction details.
        """
        return {
            "total_balance": self.balance,
            "transactions": self.sales,
        }

    def save_state(self, file_path):
        """
        Save the current state of the vending machine to a file.

        Args:
            file_path (str): Path to the file where the state will be saved.

        Raises:
            IOError: If there is an issue saving the state.
        """
        try:
            state = {
                "machine_id": self.machine_id,
                "location": self.location,
                "inventory": self.inventory,
                "sales": self.sales,
                "balance": self.balance,
            }
            with open(file_path, "w") as file:
                json.dump(state, file, indent=4, default=str)
        except IOError as e:
            raise IOError(f"Error saving state to file: {e}")

    def load_state(self, file_path):
        """
        Load the state of the vending machine from a file.

        Args:
            file_path (str): Path to the file where the state is saved.

        Raises:
            IOError: If there is an issue loading the state.
        """
        try:
            with open(file_path, "r") as file:
                state = json.load(file)
                self.machine_id = state["machine_id"]
                self.location = state["location"]
                self.inventory = state["inventory"]
                self.sales = state["sales"]
                self.balance = state["balance"]
        except IOError as e:
            raise IOError(f"Error loading state from file: {e}")


# Example usage (when testing this library):
if __name__ == "__main__":
    # Create a vending machine instance
    vending_machine = VendingMachine("VM001", "Central Park")

    # Add items to the inventory
    vending_machine.add_item("A1", "Soda", 1.50, 20)
    vending_machine.add_item("B2", "Chips", 1.00, 30)

    # Process a purchase
    try:
        transaction = vending_machine.purchase_item("A1", 2)
        print(f"Purchase successful: {transaction}")
    except ValueError as e:
        print(f"Error during purchase: {e}")

    # Get inventory and sales report
    print("Current Inventory:", vending_machine.get_inventory())
    print("Sales Report:", vending_machine.get_sales_report())

    # Save and load state
    vending_machine.save_state("vending_machine_state.json")
    vending_machine.load_state("vending_machine_state.json")
```
