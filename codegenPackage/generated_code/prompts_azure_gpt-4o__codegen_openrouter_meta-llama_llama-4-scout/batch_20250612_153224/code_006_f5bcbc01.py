"""
Generated Code Metadata:
========================
Original URL: https://createxpro.com
Prompt: Develop a program to manage customer orders for personalized promotional items, incorporating customization options like DTF printing and vinyl textile designs.
Generated: DETERMINISTIC_f5bcbc010a77c73c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# order_management_system.py

from enum import Enum
from typing import List, Dict

class CustomizationOption(Enum):
    """Enum for customization options."""
    DTF_PRINTING = "DTF Printing"
    VINYL_TEXTILE_DESIGN = "Vinyl Textile Design"

class OrderStatus(Enum):
    """Enum for order status."""
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELED = "Canceled"

class CustomerOrder:
    """Class to represent a customer order."""

    def __init__(self, order_id: int, customer_name: str, item_description: str, 
                 customization_option: CustomizationOption, status: OrderStatus = OrderStatus.PENDING):
        """
        Initialize a customer order.

        Args:
        - order_id (int): Unique order ID.
        - customer_name (str): Customer name.
        - item_description (str): Description of the item.
        - customization_option (CustomizationOption): Customization option chosen.
        - status (OrderStatus): Order status (default: PENDING).
        """
        self.order_id = order_id
        self.customer_name = customer_name
        self.item_description = item_description
        self.customization_option = customization_option
        self.status = status

    def update_status(self, status: OrderStatus):
        """Update the order status."""
        self.status = status

    def __str__(self):
        return f"Order ID: {self.order_id}, Customer Name: {self.customer_name}, Item Description: {self.item_description}, Customization Option: {self.customization_option.value}, Status: {self.status.value}"

class OrderManagementSystem:
    """Class to manage customer orders."""

    def __init__(self):
        self.orders: Dict[int, CustomerOrder] = {}

    def create_order(self, order_id: int, customer_name: str, item_description: str, 
                     customization_option: CustomizationOption):
        """
        Create a new customer order.

        Args:
        - order_id (int): Unique order ID.
        - customer_name (str): Customer name.
        - item_description (str): Description of the item.
        - customization_option (CustomizationOption): Customization option chosen.

        Raises:
        - ValueError: If order ID already exists.
        """
        if order_id in self.orders:
            raise ValueError("Order ID already exists.")
        self.orders[order_id] = CustomerOrder(order_id, customer_name, item_description, customization_option)

    def get_order(self, order_id: int) -> CustomerOrder:
        """
        Get a customer order by order ID.

        Args:
        - order_id (int): Unique order ID.

        Returns:
        - CustomerOrder: Customer order object.

        Raises:
        - ValueError: If order ID does not exist.
        """
        try:
            return self.orders[order_id]
        except KeyError:
            raise ValueError("Order ID does not exist.")

    def update_order_status(self, order_id: int, status: OrderStatus):
        """
        Update the status of a customer order.

        Args:
        - order_id (int): Unique order ID.
        - status (OrderStatus): New order status.

        Raises:
        - ValueError: If order ID does not exist.
        """
        try:
            self.orders[order_id].update_status(status)
        except KeyError:
            raise ValueError("Order ID does not exist.")

    def list_orders(self) -> List[CustomerOrder]:
        """Get a list of all customer orders."""
        return list(self.orders.values())

def main():
    # Example usage
    order_system = OrderManagementSystem()

    try:
        order_system.create_order(1, "John Doe", "T-Shirt", CustomizationOption.DTF_PRINTING)
        order_system.create_order(2, "Jane Doe", "Mug", CustomizationOption.VINYL_TEXTILE_DESIGN)

        print("Orders:")
        for order in order_system.list_orders():
            print(order)

        order_system.update_order_status(1, OrderStatus.IN_PROGRESS)
        print("\nUpdated Order:")
        print(order_system.get_order(1))

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
