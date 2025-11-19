"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://forestx.se
Prompt: Develop a function that automates order and freight management using the features discussed in the Setra case study from ForestX.
Generated: DETERMINISTIC_12819f58a7cd6028
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict

# Set up logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Order:
    def __init__(self, order_id: str, customer_id: str, items: List[str], total_amount: float):
        """
        Initialize an Order instance.

        :param order_id: Unique identifier for the order
        :param customer_id: Unique identifier for the customer
        :param items: List of items in the order
        :param total_amount: Total amount for the order
        """
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items
        self.total_amount = total_amount

class Freight:
    def __init__(self, freight_id: str, order_id: str, carrier: str, cost: float):
        """
        Initialize a Freight instance.

        :param freight_id: Unique identifier for the freight
        :param order_id: Associated order identifier
        :param carrier: Name of the freight carrier
        :param cost: Cost of the freight
        """
        self.freight_id = freight_id
        self.order_id = order_id
        self.carrier = carrier
        self.cost = cost

class OrderManagement:
    def __init__(self):
        self.orders: Dict[str, Order] = {}
        self.freights: Dict[str, Freight] = {}

    def create_order(self, order_id: str, customer_id: str, items: List[str], total_amount: float) -> Order:
        """
        Create a new order.

        :param order_id: Unique identifier for the order
        :param customer_id: Unique identifier for the customer
        :param items: List of items in the order
        :param total_amount: Total amount for the order
        :return: The created Order instance
        """
        if order_id in self.orders:
            logging.error(f"Order ID {order_id} already exists.")
            raise ValueError("Order ID already exists.")
        
        order = Order(order_id, customer_id, items, total_amount)
        self.orders[order_id] = order
        logging.info(f"Order created: {order_id}")
        return order

    def create_freight(self, freight_id: str, order_id: str, carrier: str, cost: float) -> Freight:
        """
        Create a new freight record associated with an order.

        :param freight_id: Unique identifier for the freight
        :param order_id: The order associated with the freight
        :param carrier: Name of the freight carrier
        :param cost: Cost of the freight
        :return: The created Freight instance
        """
        if freight_id in self.freights:
            logging.error(f"Freight ID {freight_id} already exists.")
            raise ValueError("Freight ID already exists.")
        
        if order_id not in self.orders:
            logging.error(f"Order ID {order_id} does not exist.")
            raise ValueError("Associated order does not exist.")
        
        freight = Freight(freight_id, order_id, carrier, cost)
        self.freights[freight_id] = freight
        logging.info(f"Freight created: {freight_id} for order: {order_id}")
        return freight

    def get_order_details(self, order_id: str) -> Dict:
        """
        Retrieve details of an order by its ID.

        :param order_id: Unique identifier for the order
        :return: Dictionary containing order details
        """
        try:
            order = self.orders[order_id]
            logging.info(f"Retrieved details for order: {order_id}")
            return {
                "order_id": order.order_id,
                "customer_id": order.customer_id,
                "items": order.items,
                "total_amount": order.total_amount
            }
        except KeyError:
            logging.error(f"Order ID {order_id} not found.")
            raise ValueError("Order ID not found.")

    def get_freight_details(self, freight_id: str) -> Dict:
        """
        Retrieve details of a freight record by its ID.

        :param freight_id: Unique identifier for the freight
        :return: Dictionary containing freight details
        """
        try:
            freight = self.freights[freight_id]
            logging.info(f"Retrieved details for freight: {freight_id}")
            return {
                "freight_id": freight.freight_id,
                "order_id": freight.order_id,
                "carrier": freight.carrier,
                "cost": freight.cost
            }
        except KeyError:
            logging.error(f"Freight ID {freight_id} not found.")
            raise ValueError("Freight ID not found.")

# Example of how the OrderManagement class can be used:
if __name__ == "__main__":
    order_management = OrderManagement()

    # Create a new order
    try:
        order = order_management.create_order("O123", "C456", ["item1", "item2"], 150.00)
        # Create a freight for the order
        freight = order_management.create_freight("F789", order.order_id, "CarrierX", 20.00)
    except ValueError as e:
        logging.error(f"Error occurred: {e}")

    # Fetch order and freight details
    try:
        order_details = order_management.get_order_details("O123")
        freight_details = order_management.get_freight_details("F789")
        logging.info(f"Order details: {order_details}")
        logging.info(f"Freight details: {freight_details}")
    except ValueError as e:
        logging.error(f"Error occurred: {e}")
```
