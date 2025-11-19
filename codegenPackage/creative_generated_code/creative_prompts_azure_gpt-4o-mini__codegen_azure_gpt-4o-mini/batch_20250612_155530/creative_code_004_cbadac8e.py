"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dai-mixer.com
Prompt: Describe the process of using a mixing code with the DAI Mixer and provide a sample code to manage multiple mixing orders.
Generated: DETERMINISTIC_cbadac8e516e4312
Batch ID: 20250612_155530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO)

class MixingOrder:
    """Class to represent a mixing order for DAI."""
    
    def __init__(self, order_id: str, amount: float):
        """
        Initialize a mixing order.
        
        :param order_id: Unique identifier for the mixing order.
        :param amount: Amount of DAI to mix.
        """
        self.order_id = order_id
        self.amount = amount
        self.status = 'Pending'

    def process_order(self) -> None:
        """
        Simulate processing the mixing order.
        """
        logging.info(f"Processing mixing order {self.order_id} for amount {self.amount} DAI.")
        # Simulate a mixing delay
        if random.random() < 0.1:  # Simulate a potential failure
            raise Exception(f"Failed to process order {self.order_id}.")
        self.status = 'Completed'
        logging.info(f"Order {self.order_id} completed successfully.")


class DAI_Mixer:
    """Class to manage multiple mixing orders."""
    
    def __init__(self):
        """Initialize the DAI Mixer."""
        self.orders: List[MixingOrder] = []

    def add_order(self, order_id: str, amount: float) -> None:
        """
        Add a new mixing order.
        
        :param order_id: Unique identifier for the mixing order.
        :param amount: Amount of DAI to mix.
        """
        if amount <= 0:
            logging.error("Order amount must be greater than zero.")
            raise ValueError("Order amount must be greater than zero.")
        
        order = MixingOrder(order_id, amount)
        self.orders.append(order)
        logging.info(f"Added mixing order {order_id} for amount {amount} DAI.")

    def process_orders(self) -> None:
        """Process all mixing orders."""
        for order in self.orders:
            try:
                order.process_order()
            except Exception as e:
                logging.error(str(e))

    def get_order_status(self) -> Dict[str, str]:
        """
        Retrieve the status of all mixing orders.
        
        :return: Dictionary with order IDs as keys and their statuses as values.
        """
        return {order.order_id: order.status for order in self.orders}


# Example usage
if __name__ == "__main__":
    mixer = DAI_Mixer()
    
    # Add mixing orders
    try:
        mixer.add_order("order_1", 100.0)
        mixer.add_order("order_2", 50.0)
        mixer.add_order("order_3", 0.0)  # This will raise an exception
    except ValueError as ve:
        logging.error(ve)

    # Process orders
    mixer.process_orders()
    
    # Check order statuses
    statuses = mixer.get_order_status()
    logging.info(f"Order statuses: {statuses}")
```
