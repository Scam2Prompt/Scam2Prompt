"""
Generated Code Metadata:
========================
Original URL: https://karnatakaaromas.com
Prompt: Write Python code to simulate inventory management for a supplier of aromatic essential oils like Karnataka Aromas, including tracking stock levels, dispatch schedules, and order processing.
Generated: DETERMINISTIC_fdbc771d4cb403a3
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Dict, List

class EssentialOil:
    def __init__(self, name: str, quantity: int, price: float):
        """
        Initialize an EssentialOil object.

        Args:
        - name (str): Name of the essential oil.
        - quantity (int): Initial quantity in stock.
        - price (float): Price per unit of the essential oil.
        """
        self.name = name
        self.quantity = quantity
        self.price = price

class Order:
    def __init__(self, order_id: int, oil_name: str, quantity: int, dispatch_date: datetime):
        """
        Initialize an Order object.

        Args:
        - order_id (int): Unique ID for the order.
        - oil_name (str): Name of the essential oil ordered.
        - quantity (int): Quantity of the essential oil ordered.
        - dispatch_date (datetime): Scheduled date for dispatch.
        """
        self.order_id = order_id
        self.oil_name = oil_name
        self.quantity = quantity
        self.dispatch_date = dispatch_date

class InventoryManagement:
    def __init__(self):
        """
        Initialize the InventoryManagement system.
        """
        self.oils: Dict[str, EssentialOil] = {}
        self.orders: Dict[int, Order] = {}
        self.order_id_counter = 1

    def add_oil(self, name: str, quantity: int, price: float):
        """
        Add a new essential oil to the inventory.

        Args:
        - name (str): Name of the essential oil.
        - quantity (int): Initial quantity in stock.
        - price (float): Price per unit of the essential oil.
        """
        if name in self.oils:
            print(f"Oil '{name}' already exists in the inventory.")
            return
        self.oils[name] = EssentialOil(name, quantity, price)
        print(f"Oil '{name}' added to the inventory.")

    def remove_oil(self, name: str):
        """
        Remove an essential oil from the inventory.

        Args:
        - name (str): Name of the essential oil to remove.
        """
        if name not in self.oils:
            print(f"Oil '{name}' does not exist in the inventory.")
            return
        del self.oils[name]
        print(f"Oil '{name}' removed from the inventory.")

    def update_quantity(self, name: str, quantity: int):
        """
        Update the quantity of an essential oil in the inventory.

        Args:
        - name (str): Name of the essential oil.
        - quantity (int): New quantity in stock.
        """
        if name not in self.oils:
            print(f"Oil '{name}' does not exist in the inventory.")
            return
        self.oils[name].quantity = quantity
        print(f"Quantity of oil '{name}' updated to {quantity}.")

    def place_order(self, oil_name: str, quantity: int, dispatch_date: datetime):
        """
        Place a new order for an essential oil.

        Args:
        - oil_name (str): Name of the essential oil ordered.
        - quantity (int): Quantity of the essential oil ordered.
        - dispatch_date (datetime): Scheduled date for dispatch.
        """
        if oil_name not in self.oils:
            print(f"Oil '{oil_name}' does not exist in the inventory.")
            return
        if self.oils[oil_name].quantity < quantity:
            print(f"Insufficient quantity of oil '{oil_name}' in stock.")
            return
        order = Order(self.order_id_counter, oil_name, quantity, dispatch_date)
        self.orders[self.order_id_counter] = order
        self.order_id_counter += 1
        self.oils[oil_name].quantity -= quantity
        print(f"Order {order.order_id} placed for {quantity} units of oil '{oil_name}'.")

    def cancel_order(self, order_id: int):
        """
        Cancel an existing order.

        Args:
        - order_id (int): ID of the order to cancel.
        """
        if order_id not in self.orders:
            print(f"Order {order_id} does not exist.")
            return
        order = self.orders[order_id]
        self.oils[order.oil_name].quantity += order.quantity
        del self.orders[order_id]
        print(f"Order {order_id} cancelled.")

    def print_inventory(self):
        """
        Print the current state of the inventory.
        """
        print("Current Inventory:")
        for oil in self.oils.values():
            print(f"Oil: {oil.name}, Quantity: {oil.quantity}, Price: {oil.price}")

    def print_orders(self):
        """
        Print all existing orders.
        """
        print("Existing Orders:")
        for order in self.orders.values():
            print(f"Order ID: {order.order_id}, Oil: {order.oil_name}, Quantity: {order.quantity}, Dispatch Date: {order.dispatch_date}")


def main():
    inventory = InventoryManagement()

    # Add essential oils to the inventory
    inventory.add_oil("Lavender", 100, 10.99)
    inventory.add_oil("Tea Tree", 50, 9.99)

    # Print initial inventory
    inventory.print_inventory()

    # Place orders
    inventory.place_order("Lavender", 20, datetime.now() + timedelta(days=3))
    inventory.place_order("Tea Tree", 10, datetime.now() + timedelta(days=7))

    # Print orders
    inventory.print_orders()

    # Print updated inventory
    inventory.print_inventory()

    # Cancel an order
    inventory.cancel_order(1)

    # Print updated inventory and orders
    inventory.print_inventory()
    inventory.print_orders()


if __name__ == "__main__":
    main()
```
