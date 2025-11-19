"""
Generated Code Metadata:
========================
Original URL: https://availlabs.net
Prompt: Create a script to streamline procurement workflows for branded swag, focusing on maximizing ROI and reducing manual effort, inspired by Avail Labs' procurement solutions.
Generated: DETERMINISTIC_e59385782210c8a0
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Streamline procurement workflows for branded swag to maximize ROI and reduce manual effort.

Inspired by Avail Labs' procurement solutions.

Author: [Your Name]
Date: [Today's Date]
"""

import logging
import os
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SwagItem:
    """Represents a branded swag item."""

    def __init__(self, item_id: int, name: str, cost: float, quantity: int):
        """
        Initializes a SwagItem object.

        Args:
        - item_id (int): Unique identifier for the item.
        - name (str): Name of the item.
        - cost (float): Cost of the item.
        - quantity (int): Quantity of the item.
        """
        self.item_id = item_id
        self.name = name
        self.cost = cost
        self.quantity = quantity

class ProcurementWorkflow:
    """Manages procurement workflows for branded swag."""

    def __init__(self):
        """Initializes a ProcurementWorkflow object."""
        self.swag_items: Dict[int, SwagItem] = {}
        self.order_history: List[Dict] = []

    def add_swag_item(self, item: SwagItem):
        """
        Adds a swag item to the catalog.

        Args:
        - item (SwagItem): Swag item to add.
        """
        self.swag_items[item.item_id] = item
        logging.info(f"Added swag item {item.name} (ID: {item.item_id})")

    def remove_swag_item(self, item_id: int):
        """
        Removes a swag item from the catalog.

        Args:
        - item_id (int): ID of the item to remove.

        Raises:
        - ValueError: If the item ID is not found in the catalog.
        """
        if item_id not in self.swag_items:
            raise ValueError(f"Item ID {item_id} not found in catalog")
        del self.swag_items[item_id]
        logging.info(f"Removed swag item with ID {item_id}")

    def place_order(self, item_id: int, quantity: int):
        """
        Places an order for a swag item.

        Args:
        - item_id (int): ID of the item to order.
        - quantity (int): Quantity of the item to order.

        Raises:
        - ValueError: If the item ID is not found in the catalog or if the quantity is invalid.
        """
        if item_id not in self.swag_items:
            raise ValueError(f"Item ID {item_id} not found in catalog")
        item = self.swag_items[item_id]
        if quantity <= 0:
            raise ValueError("Invalid quantity")
        order = {
            "item_id": item_id,
            "name": item.name,
            "quantity": quantity,
            "total_cost": item.cost * quantity
        }
        self.order_history.append(order)
        logging.info(f"Placed order for {quantity} x {item.name} (ID: {item_id})")

    def get_order_history(self):
        """
        Retrieves the order history.

        Returns:
        - List[Dict]: List of orders, where each order is a dictionary containing item details and total cost.
        """
        return self.order_history

def main():
    workflow = ProcurementWorkflow()

    # Add swag items
    item1 = SwagItem(1, "T-Shirt", 10.99, 100)
    item2 = SwagItem(2, "Mug", 5.99, 50)
    workflow.add_swag_item(item1)
    workflow.add_swag_item(item2)

    # Place orders
    workflow.place_order(1, 20)
    workflow.place_order(2, 10)

    # Get order history
    order_history = workflow.get_order_history()
    for order in order_history:
        print(order)

if __name__ == "__main__":
    main()
```
