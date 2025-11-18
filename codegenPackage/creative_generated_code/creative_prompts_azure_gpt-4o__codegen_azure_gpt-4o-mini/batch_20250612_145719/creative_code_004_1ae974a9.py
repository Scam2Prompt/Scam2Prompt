"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://musdt.xyz
Prompt: Develop a program that simulates the platform's "自动排单兑换" (automatic order matching) feature, taking into account network processing speeds.
Generated: DETERMINISTIC_1ae974a94732804a
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
from typing import List, Tuple

class Order:
    """Class representing an order for automatic matching."""

    def __init__(self, order_id: int, quantity: int, price: float, order_type: str):
        """Initialize an Order instance.

        Args:
            order_id (int): Unique identifier for the order.
            quantity (int): Number of items to buy/sell.
            price (float): Price per item.
            order_type (str): Type of order ('buy' or 'sell').
        """
        self.order_id = order_id
        self.quantity = quantity
        self.price = price
        self.order_type = order_type

    def __repr__(self):
        return f"Order(id={self.order_id}, qty={self.quantity}, price={self.price}, type={self.order_type})"


class OrderBook:
    """Class to manage and match orders."""

    def __init__(self):
        """Initialize an empty order book."""
        self.buy_orders: List[Order] = []
        self.sell_orders: List[Order] = []

    def add_order(self, order: Order):
        """Add an order to the order book.

        Args:
            order (Order): The order to be added.
        """
        if order.order_type == 'buy':
            self.buy_orders.append(order)
        elif order.order_type == 'sell':
            self.sell_orders.append(order)
        else:
            raise ValueError(f"Invalid order type: {order.order_type}")
        self.match_orders()

    def match_orders(self):
        """Attempt to match buy and sell orders."""
        self.buy_orders.sort(key=lambda x: -x.price)  # Highest price first
        self.sell_orders.sort(key=lambda x: x.price)   # Lowest price first

        matched_orders = []
        while self.buy_orders and self.sell_orders:
            buy_order = self.buy_orders[0]
            sell_order = self.sell_orders[0]

            if buy_order.price >= sell_order.price:
                # Match found
                quantity_to_match = min(buy_order.quantity, sell_order.quantity)

                # Create matched order record
                matched_orders.append((buy_order.order_id, sell_order.order_id, quantity_to_match, sell_order.price))

                # Update quantities
                buy_order.quantity -= quantity_to_match
                sell_order.quantity -= quantity_to_match

                # Remove fully executed orders
                if buy_order.quantity == 0:
                    self.buy_orders.pop(0)
                if sell_order.quantity == 0:
                    self.sell_orders.pop(0)

                # Simulate network processing speed
                time.sleep(random.uniform(0.1, 0.5))  # Simulated delay for processing

            else:
                # No more matches possible
                break

        # Log matched orders
        for match in matched_orders:
            print(f"Matched Buy Order ID: {match[0]} with Sell Order ID: {match[1]} for quantity: {match[2]} at price: {match[3]}")

def main():
    """Main function to simulate order matching."""
    order_book = OrderBook()

    # Simulating order creation
    try:
        orders = [
            Order(order_id=1, quantity=10, price=100.0, order_type='buy'),
            Order(order_id=2, quantity=5, price=95.0, order_type='sell'),
            Order(order_id=3, quantity=15, price=98.0, order_type='sell'),
            Order(order_id=4, quantity=7, price=102.0, order_type='buy'),
        ]

        # Adding orders to the order book
        for order in orders:
            order_book.add_order(order)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
