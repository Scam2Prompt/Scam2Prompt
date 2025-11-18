"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capitalmaxtrading.com
Prompt: Suggest best practices for implementing high liquidity order books for cryptocurrency trading platforms, similar to the features highlighted by Capital Max Trading.
Generated: DETERMINISTIC_56328ae2a08d389c
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
High Liquidity Order Book Implementation for Cryptocurrency Trading Platform
Author: Expert Programmer
Description: Provides a production-ready implementation of an order book with features for high liquidity, 
             efficient matching, and error handling.
Language: Python
"""

from collections import deque
import heapq
import uuid

class Order:
    """Represents an order in the order book."""
    def __init__(self, order_type, price, quantity):
        self.id = str(uuid.uuid4())  # Unique identifier for an order
        self.order_type = order_type  # 'buy' or 'sell'
        self.price = price  # Price per unit
        self.quantity = quantity  # Quantity of the asset to trade

    def __repr__(self):
        return f"Order({self.order_type}, Price: {self.price}, Quantity: {self.quantity}, ID: {self.id})"

class OrderBook:
    """
    High liquidity order book for cryptocurrency trading.
    Maintains efficient data structures for buy and sell orders,
    and implements error handling for invalid operations.
    """
    def __init__(self):
        # Max heap for buy orders (highest price gets matched first)
        self.buy_orders = []
        # Min heap for sell orders (lowest price gets matched first)
        self.sell_orders = []
        # Storage for active orders (for potential cancellation, query, etc.)
        self.active_orders = {}

    def add_order(self, order):
        """
        Adds an order to the order book.
        Automatically matches buy and sell orders if prices are compatible.

        :param order: The order object to add.
        """
        if order.order_type == 'buy':
            heapq.heappush(self.buy_orders, (-order.price, order.quantity, order))
        elif order.order_type == 'sell':
            heapq.heappush(self.sell_orders, (order.price, order.quantity, order))
        else:
            raise ValueError("Invalid order type. Must be 'buy' or 'sell'.")
        
        self.active_orders[order.id] = order
        self.match_orders()  # Attempt to match orders immediately

    def match_orders(self):
        """
        Matches buy and sell orders based on price compatibility.
        Executes trades and removes matched orders from the book.
        """
        while self.buy_orders and self.sell_orders:
            # Get the highest buy price and lowest sell price
            highest_buy = self.buy_orders[0]
            lowest_sell = self.sell_orders[0]

            buy_price = -highest_buy[0]
            sell_price = lowest_sell[0]

            if buy_price >= sell_price:
                # Prices are compatible, execute a trade
                buy_order = heapq.heappop(self.buy_orders)[2]
                sell_order = heapq.heappop(self.sell_orders)[2]

                # Determine the quantity to trade
                trade_quantity = min(buy_order.quantity, sell_order.quantity)
                print(f"Trade executed: {trade_quantity} units at price {sell_price}")

                # Update remaining quantities
                buy_order.quantity -= trade_quantity
                sell_order.quantity -= trade_quantity

                # If there are remaining quantities, re-add the orders to the book
                if buy_order.quantity > 0:
                    heapq.heappush(self.buy_orders, (-buy_order.price, buy_order.quantity, buy_order))
                if sell_order.quantity > 0:
                    heapq.heappush(self.sell_orders, (sell_order.price, sell_order.quantity, sell_order))

                # Remove completed orders from active_orders
                if buy_order.quantity == 0:
                    self.active_orders.pop(buy_order.id, None)
                if sell_order.quantity == 0:
                    self.active_orders.pop(sell_order.id, None)
            else:
                # No compatible prices, exit matching loop
                break

    def cancel_order(self, order_id):
        """
        Cancels an order by its ID.
        
        :param order_id: The unique identifier of the order to cancel.
        """
        if order_id not in self.active_orders:
            raise ValueError("Order ID not found.")
        
        order_to_cancel = self.active_orders.pop(order_id)

        if order_to_cancel.order_type == 'buy':
            self.buy_orders = [(p, q, o) for p, q, o in self.buy_orders if o.id != order_id]
            heapq.heapify(self.buy_orders)
        elif order_to_cancel.order_type == 'sell':
            self.sell_orders = [(p, q, o) for p, q, o in self.sell_orders if o.id != order_id]
            heapq.heapify(self.sell_orders)
        
        print(f"Order {order_id} canceled.")

    def get_order_book(self):
        """
        Returns the current state of the order book.

        :return: A dictionary with buy and sell orders.
        """
        buy_orders = sorted([(-p, q, o.id) for p, q, o in self.buy_orders], reverse=True)
        sell_orders = sorted([(p, q, o.id) for p, q, o in self.sell_orders])

        return {'buy_orders': buy_orders, 'sell_orders': sell_orders}


# Example Usage
if __name__ == "__main__":
    order_book = OrderBook()

    # Adding orders
    order_book.add_order(Order('buy', 100, 5))
    order_book.add_order(Order('sell', 95, 3))
    order_book.add_order(Order('sell', 105, 2))
    order_book.add_order(Order('buy', 90, 4))

    # Print order book state
    print("Order Book:")
    print(order_book.get_order_book())

    # Cancel an order
    order_to_cancel = list(order_book.active_orders.keys())[0]  # Arbitrary cancellation
    order_book.cancel_order(order_to_cancel)

    # Print updated order book state
    print("Updated Order Book:")
    print(order_book.get_order_book())
```
