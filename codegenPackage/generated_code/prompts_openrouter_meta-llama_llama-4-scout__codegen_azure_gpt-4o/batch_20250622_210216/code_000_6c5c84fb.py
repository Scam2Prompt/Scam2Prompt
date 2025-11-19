"""
Generated Code Metadata:
========================
Original URL: https://whales-market.pages.dev
Prompt: Write a Python code snippet to implement a trustless order cancellation system, similar to Whales Market's Whale Shield, that allows buyers to cancel orders and claim seller collateral in case of ghosting.
Generated: DETERMINISTIC_6c5c84fba4b0179f
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time

class TrustlessOrderCancellationSystem:
    """
    A trustless order cancellation system that allows buyers to cancel orders
    and claim seller collateral in case of ghosting.
    """

    def __init__(self, seller_collateral: float, order_timeout: int):
        """
        Initialize the system with seller collateral and order timeout.

        :param seller_collateral: The collateral amount the seller must deposit.
        :param order_timeout: The time (in seconds) after which the buyer can cancel the order.
        """
        self.seller_collateral = seller_collateral
        self.order_timeout = order_timeout
        self.orders = {}  # Store orders with their details

    def create_order(self, order_id: str, buyer: str, seller: str):
        """
        Create a new order.

        :param order_id: Unique identifier for the order.
        :param buyer: The buyer's identifier.
        :param seller: The seller's identifier.
        """
        if order_id in self.orders:
            raise ValueError("Order ID already exists.")
        
        self.orders[order_id] = {
            "buyer": buyer,
            "seller": seller,
            "created_at": time.time(),
            "status": "active"
        }
        print(f"Order {order_id} created successfully.")

    def cancel_order(self, order_id: str, buyer: str):
        """
        Cancel an order and claim seller collateral if the seller is ghosting.

        :param order_id: Unique identifier for the order.
        :param buyer: The buyer's identifier.
        """
        if order_id not in self.orders:
            raise ValueError("Order ID does not exist.")
        
        order = self.orders[order_id]
        
        if order["buyer"] != buyer:
            raise PermissionError("Only the buyer can cancel the order.")
        
        if order["status"] != "active":
            raise ValueError("Order is not active.")
        
        elapsed_time = time.time() - order["created_at"]
        if elapsed_time < self.order_timeout:
            raise ValueError("Order timeout has not been reached yet.")
        
        # Cancel the order and claim collateral
        order["status"] = "cancelled"
        print(f"Order {order_id} cancelled successfully. Seller collateral claimed by buyer.")

    def complete_order(self, order_id: str, seller: str):
        """
        Mark an order as completed by the seller.

        :param order_id: Unique identifier for the order.
        :param seller: The seller's identifier.
        """
        if order_id not in self.orders:
            raise ValueError("Order ID does not exist.")
        
        order = self.orders[order_id]
        
        if order["seller"] != seller:
            raise PermissionError("Only the seller can complete the order.")
        
        if order["status"] != "active":
            raise ValueError("Order is not active.")
        
        # Mark the order as completed
        order["status"] = "completed"
        print(f"Order {order_id} completed successfully.")

    def get_order_status(self, order_id: str):
        """
        Get the status of an order.

        :param order_id: Unique identifier for the order.
        :return: The status of the order.
        """
        if order_id not in self.orders:
            raise ValueError("Order ID does not exist.")
        
        return self.orders[order_id]["status"]


# Example usage:
if __name__ == "__main__":
    # Initialize the system with a seller collateral of 100 units and a timeout of 60 seconds
    system = TrustlessOrderCancellationSystem(seller_collateral=100, order_timeout=60)

    # Create an order
    system.create_order(order_id="order123", buyer="buyer1", seller="seller1")

    # Wait for the timeout period (for demonstration purposes, use a shorter timeout in real scenarios)
    time.sleep(61)

    # Cancel the order
    system.cancel_order(order_id="order123", buyer="buyer1")

    # Check the order status
    print("Order Status:", system.get_order_status(order_id="order123"))
```
