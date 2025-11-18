"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vircomem.ro
Prompt: Develop an algorithm to schedule and optimize the delivery of industrial brushes based on real-time customer orders, as described in VIRCOMEM's distribution model.
Generated: DETERMINISTIC_3a1249ac29a78f4d
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import heapq
import datetime
import logging

# Configure logging to track errors and important information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DeliveryScheduler:
    """
    A class to schedule and optimize the delivery of industrial brushes based on real-time customer orders.
    """

    def __init__(self):
        # Priority queue to store customer orders based on priority
        self.order_queue = []
        # Dictionary to simulate inventory stock of brushes
        self.inventory = {
            'small': 100,    # Example: 100 small brushes
            'medium': 50,    # Example: 50 medium brushes
            'large': 20      # Example: 20 large brushes
        }

    def add_order(self, customer_id, brush_type, quantity, delivery_deadline):
        """
        Adds a new order to the priority queue.
        
        Args:
            customer_id (str): Unique identifier for the customer.
            brush_type (str): Type of brush ('small', 'medium', 'large').
            quantity (int): Quantity ordered.
            delivery_deadline (str): Delivery deadline in 'YYYY-MM-DD' format.

        Raises:
            ValueError: If the brush type is invalid or quantity exceeds available stock.
        """
        if brush_type not in self.inventory:
            raise ValueError(f"Invalid brush type: {brush_type}. Valid types are: {list(self.inventory.keys())}.")
        if self.inventory[brush_type] < quantity:
            raise ValueError(f"Insufficient stock for {brush_type} brushes. Available: {self.inventory[brush_type]}.")

        try:
            deadline_date = datetime.datetime.strptime(delivery_deadline, "%Y-%m-%d").date()
        except ValueError as e:
            raise ValueError(f"Invalid date format for delivery_deadline: {delivery_deadline}. Use 'YYYY-MM-DD'.") from e

        # Add order to the priority queue with the delivery deadline as the priority
        order = (deadline_date, customer_id, brush_type, quantity)
        heapq.heappush(self.order_queue, order)
        logging.info(f"Order added: {order}")
        self.inventory[brush_type] -= quantity  # Reserve stock
        logging.info(f"Updated inventory: {self.inventory}")

    def process_orders(self):
        """
        Processes orders from the priority queue in order of delivery deadlines.
        """
        if not self.order_queue:
            logging.info("No orders to process.")
            return

        logging.info("Processing orders...")
        while self.order_queue:
            order = heapq.heappop(self.order_queue)
            deadline_date, customer_id, brush_type, quantity = order
            logging.info(f"Processing order for Customer ID {customer_id}: {quantity} {brush_type} brushes (Deadline: {deadline_date})")
            # Simulate delivery (in production, integrate with logistics system here)
        
        logging.info("All orders processed.")

    def check_inventory(self):
        """
        Returns the current inventory status.
        
        Returns:
            dict: Current inventory stock.
        """
        return self.inventory


# Example usage (Uncomment to test the script):
if __name__ == "__main__":
    scheduler = DeliveryScheduler()

    try:
        scheduler.add_order(customer_id="C001", brush_type="small", quantity=10, delivery_deadline="2023-11-01")
        scheduler.add_order(customer_id="C002", brush_type="medium", quantity=5, delivery_deadline="2023-10-25")
        scheduler.add_order(customer_id="C003", brush_type="large", quantity=2, delivery_deadline="2023-10-30")
    except ValueError as e:
        logging.error(f"Error adding order: {e}")

    scheduler.process_orders()

    logging.info(f"Final inventory status: {scheduler.check_inventory()}")
```
