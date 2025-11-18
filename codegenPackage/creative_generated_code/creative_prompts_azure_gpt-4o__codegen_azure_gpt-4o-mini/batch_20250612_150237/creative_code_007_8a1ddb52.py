"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecobrokercapital.com
Prompt: Write code to implement a high-liquidity order book for top currency pairs, inspired by Eco Broker Capital's liquidity features.
Generated: DETERMINISTIC_8a1ddb526a490fa4
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import threading
import time
from collections import defaultdict
from typing import List, Dict, Any

class Order:
    """Class representing an order in the order book."""
    
    def __init__(self, order_id: str, price: float, quantity: float, order_type: str):
        """
        Initialize an order.

        Parameters:
        - order_id: Unique identifier for the order.
        - price: Price at which the order is placed.
        - quantity: Quantity of currency for the order.
        - order_type: Type of the order ('buy' or 'sell').
        """
        self.order_id = order_id
        self.price = price
        self.quantity = quantity
        self.order_type = order_type

class OrderBook:
    """Class representing an order book for currency pairs."""
    
    def __init__(self):
        """Initialize the order book."""
        self.buy_orders: Dict[float, List[Order]] = defaultdict(list)
        self.sell_orders: Dict[float, List[Order]] = defaultdict(list)
        self.lock = threading.Lock()

    def add_order(self, order: Order) -> None:
        """
        Add an order to the order book.

        Parameters:
        - order: The order to be added.
        """
        with self.lock:
            if order.order_type == 'buy':
                self.buy_orders[order.price].append(order)
            elif order.order_type == 'sell':
                self.sell_orders[order.price].append(order)
            else:
                raise ValueError("Invalid order type. Must be 'buy' or 'sell'.")

    def remove_order(self, order: Order) -> bool:
        """
        Remove an order from the order book.

        Parameters:
        - order: The order to be removed.

        Returns:
        - bool: True if the order was removed successfully, False otherwise.
        """
        with self.lock:
            order_list = self.buy_orders if order.order_type == 'buy' else self.sell_orders
            if order.price in order_list:
                for existing_order in order_list[order.price]:
                    if existing_order.order_id == order.order_id:
                        order_list[order.price].remove(existing_order)
                        if not order_list[order.price]:
                            del order_list[order.price]
                        return True
            return False

    def match_orders(self) -> None:
        """Match buy and sell orders based on price and quantity."""
        while True:
            with self.lock:
                # Match highest buy order with lowest sell order
                if not self.buy_orders or not self.sell_orders:
                    continue

                highest_buy_price = max(self.buy_orders.keys())
                lowest_sell_price = min(self.sell_orders.keys())

                if highest_buy_price >= lowest_sell_price:
                    # Execute trade
                    buy_order = self.buy_orders[highest_buy_price][0]
                    sell_order = self.sell_orders[lowest_sell_price][0]

                    trade_quantity = min(buy_order.quantity, sell_order.quantity)
                    print(f"Trade executed: {trade_quantity} at price {lowest_sell_price}")

                    # Update quantities
                    buy_order.quantity -= trade_quantity
                    sell_order.quantity -= trade_quantity

                    # Remove completed orders
                    if buy_order.quantity == 0:
                        self.remove_order(buy_order)
                    if sell_order.quantity == 0:
                        self.remove_order(sell_order)
                time.sleep(1)  # Sleep to prevent busy-waiting

def main():
    """Main function to demonstrate the order book functionality."""
    order_book = OrderBook()

    # Create orders (example)
    order1 = Order(order_id="1", price=100.0, quantity=5, order_type="buy")
    order2 = Order(order_id="2", price=99.5, quantity=10, order_type="sell")

    # Add orders to the order book
    order_book.add_order(order1)
    order_book.add_order(order2)

    # Start matching orders in a separate thread
    matcher_thread = threading.Thread(target=order_book.match_orders, daemon=True)
    matcher_thread.start()

    # Simulate adding more orders
    order_book.add_order(Order(order_id="3", price=100.5, quantity=3, order_type="buy"))
    order_book.add_order(Order(order_id="4", price=99.0, quantity=2, order_type="sell"))

    # Keep the main thread alive for a while to observe output
    time.sleep(10)

if __name__ == "__main__":
    main()
```
