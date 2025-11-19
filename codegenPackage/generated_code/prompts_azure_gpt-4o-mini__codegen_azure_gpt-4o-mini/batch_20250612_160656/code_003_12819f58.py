"""
Generated Code Metadata:
========================
Original URL: https://forestx.se
Prompt: Develop a function that automates order and freight management using the features discussed in the Setra case study from ForestX.
Generated: DETERMINISTIC_12819f58a7cd6028
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Order:
    def __init__(self, order_id: str, items: List[Dict[str, Any]], customer_id: str):
        """
        Initialize an Order instance.

        :param order_id: Unique identifier for the order
        :param items: List of items in the order, each represented as a dictionary
        :param customer_id: Unique identifier for the customer placing the order
        """
        self.order_id = order_id
        self.items = items
        self.customer_id = customer_id

class Freight:
    def __init__(self, freight_id: str, order_id: str, cost: float):
        """
        Initialize a Freight instance.

        :param freight_id: Unique identifier for the freight
        :param order_id: Unique identifier for the associated order
        :param cost: Cost of the freight
        """
        self.freight_id = freight_id
        self.order_id = order_id
        self.cost = cost

class OrderManager:
    def __init__(self):
        self.orders = {}
        self.freights = {}

    def create_order(self, order_id: str, items: List[Dict[str, Any]], customer_id: str) -> Order:
        """
        Create a new order and store it.

        :param order_id: Unique identifier for the order
        :param items: List of items in the order
        :param customer_id: Unique identifier for the customer
        :return: The created Order instance
        """
        if order_id in self.orders:
            logging.error(f"Order ID {order_id} already exists.")
            raise ValueError(f"Order ID {order_id} already exists.")
        
        order = Order(order_id, items, customer_id)
        self.orders[order_id] = order
        logging.info(f"Order created: {order_id}")
        return order

    def create_freight(self, freight_id: str, order_id: str, cost: float) -> Freight:
        """
        Create a new freight for a given order.

        :param freight_id: Unique identifier for the freight
        :param order_id: Unique identifier for the associated order
        :param cost: Cost of the freight
        :return: The created Freight instance
        """
        if freight_id in self.freights:
            logging.error(f"Freight ID {freight_id} already exists.")
            raise ValueError(f"Freight ID {freight_id} already exists.")
        
        if order_id not in self.orders:
            logging.error(f"Order ID {order_id} does not exist.")
            raise ValueError(f"Order ID {order_id} does not exist.")
        
        freight = Freight(freight_id, order_id, cost)
        self.freights[freight_id] = freight
        logging.info(f"Freight created: {freight_id} for Order ID: {order_id}")
        return freight

    def get_order(self, order_id: str) -> Order:
        """
        Retrieve an order by its ID.

        :param order_id: Unique identifier for the order
        :return: The Order instance
        """
        order = self.orders.get(order_id)
        if not order:
            logging.error(f"Order ID {order_id} not found.")
            raise ValueError(f"Order ID {order_id} not found.")
        return order

    def get_freight(self, freight_id: str) -> Freight:
        """
        Retrieve a freight by its ID.

        :param freight_id: Unique identifier for the freight
        :return: The Freight instance
        """
        freight = self.freights.get(freight_id)
        if not freight:
            logging.error(f"Freight ID {freight_id} not found.")
            raise ValueError(f"Freight ID {freight_id} not found.")
        return freight

# Example usage
if __name__ == "__main__":
    order_manager = OrderManager()
    
    try:
        order = order_manager.create_order("ORD123", [{"item_id": "ITEM1", "quantity": 2}], "CUST456")
        freight = order_manager.create_freight("FRT789", order.order_id, 150.0)
        
        logging.info(f"Order Details: {order.__dict__}")
        logging.info(f"Freight Details: {freight.__dict__}")
        
    except ValueError as e:
        logging.error(f"An error occurred: {e}")
```
