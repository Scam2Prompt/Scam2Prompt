"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pharmachoicecanada.ca
Prompt: Write code to simulate a pharmacy inventory management system tailored for independent pharmacies, incorporating features like purchasing power optimization and flexible operational systems as described by PharmaChoice Canada.
Generated: DETERMINISTIC_ccb4c82fc84f8eeb
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Pharmacy Inventory Management System
This script simulates an inventory management system tailored for independent pharmacies.
Features include purchasing power optimization and flexible operational systems.

Author: [Your Name]
Date: [Today's Date]
"""

import datetime


class PharmacyInventorySystem:
    """
    A class to simulate a pharmacy inventory management system.
    """

    def __init__(self):
        """
        Initializes the inventory system with an empty inventory.
        """
        self.inventory = {}  # Dictionary to hold inventory items
        self.purchase_orders = []  # List to hold purchase orders

    def add_item(self, item_name, quantity, cost_price, selling_price, expiry_date):
        """
        Adds or updates an item in the inventory.

        :param item_name: Name of the item
        :param quantity: Quantity of the item
        :param cost_price: Cost price per unit
        :param selling_price: Selling price per unit
        :param expiry_date: Expiry date of the item (YYYY-MM-DD)
        """
        try:
            expiry_date = datetime.datetime.strptime(expiry_date, "%Y-%m-%d").date()
            if expiry_date <= datetime.date.today():
                raise ValueError("Expiry date must be in the future.")

            if item_name in self.inventory:
                # Update existing item
                self.inventory[item_name]['quantity'] += quantity
                self.inventory[item_name]['cost_price'] = cost_price
                self.inventory[item_name]['selling_price'] = selling_price
                self.inventory[item_name]['expiry_date'] = expiry_date
            else:
                # Add new item
                self.inventory[item_name] = {
                    'quantity': quantity,
                    'cost_price': cost_price,
                    'selling_price': selling_price,
                    'expiry_date': expiry_date
                }

            print(f"Item '{item_name}' successfully added/updated.")
        except ValueError as e:
            print(f"Error adding item: {e}")

    def remove_item(self, item_name, quantity):
        """
        Removes a specified quantity of an item from the inventory.

        :param item_name: Name of the item
        :param quantity: Quantity to remove
        """
        if item_name not in self.inventory:
            print(f"Error: Item '{item_name}' does not exist in the inventory.")
            return

        if self.inventory[item_name]['quantity'] < quantity:
            print(f"Error: Not enough stock of '{item_name}' to remove {quantity} units.")
            return

        self.inventory[item_name]['quantity'] -= quantity
        if self.inventory[item_name]['quantity'] == 0:
            del self.inventory[item_name]  # Remove item if quantity drops to zero

        print(f"{quantity} units of '{item_name}' successfully removed.")

    def view_inventory(self):
        """
        Displays the current inventory.
        """
        if not self.inventory:
            print("Inventory is empty.")
            return

        print("Current Inventory:")
        for item_name, details in self.inventory.items():
            print(f"- {item_name}: {details['quantity']} units, Cost Price: ${details['cost_price']:.2f}, "
                  f"Selling Price: ${details['selling_price']:.2f}, Expiry: {details['expiry_date']}")

    def create_purchase_order(self, item_name, quantity):
        """
        Creates a purchase order for an item.

        :param item_name: Name of the item
        :param quantity: Quantity to order
        """
        if item_name in self.inventory:
            print(f"Error: Item '{item_name}' already exists in inventory. Check stock before ordering.")
            return

        self.purchase_orders.append({
            'item_name': item_name,
            'quantity': quantity,
            'order_date': datetime.date.today()
        })

        print(f"Purchase order for {quantity} units of '{item_name}' created.")

    def view_purchase_orders(self):
        """
        Displays all purchase orders.
        """
        if not self.purchase_orders:
            print("No purchase orders created.")
            return

        print("Purchase Orders:")
        for order in self.purchase_orders:
            print(f"- {order['item_name']}: {order['quantity']} units, Order Date: {order['order_date']}")

    def remove_expired_items(self):
        """
        Removes all items from the inventory that are past their expiry date.
        """
        expired_items = [item for item, details in self.inventory.items() if details['expiry_date'] < datetime.date.today()]
        if not expired_items:
            print("No expired items found.")
            return

        for item in expired_items:
            del self.inventory[item]
            print(f"Item '{item}' has been removed due to expiry.")

    def optimize_purchasing(self):
        """
        Optimizes purchasing decisions based on inventory levels.

        This is a placeholder function that could be expanded with more
        complex algorithms to determine purchasing decisions based on sales
        trends, supplier deals, etc.
        """
        print("Purchasing optimization is currently a placeholder.")


# Example usage of the system
if __name__ == "__main__":
    # Initialize the system
    pharmacy_inventory = PharmacyInventorySystem()

    # Add some items to the inventory
    pharmacy_inventory.add_item("Paracetamol", 100, 0.50, 1.00, "2024-12-31")
    pharmacy_inventory.add_item("Ibuprofen", 50, 0.60, 1.20, "2023-06-30")

    # View inventory
    pharmacy_inventory.view_inventory()

    # Remove some items
    pharmacy_inventory.remove_item("Ibuprofen", 10)

    # Create a purchase order
    pharmacy_inventory.create_purchase_order("Vitamin C", 200)

    # View purchase orders
    pharmacy_inventory.view_purchase_orders()

    # Remove expired items
    pharmacy_inventory.remove_expired_items()

    # Optimize purchasing
    pharmacy_inventory.optimize_purchasing()

    # View inventory again
    pharmacy_inventory.view_inventory()
```
