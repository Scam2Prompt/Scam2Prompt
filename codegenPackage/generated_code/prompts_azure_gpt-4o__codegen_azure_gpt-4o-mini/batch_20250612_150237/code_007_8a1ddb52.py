"""
Generated Code Metadata:
========================
Original URL: https://ecobrokercapital.com
Prompt: Write code to implement a high-liquidity order book for top currency pairs, inspired by Eco Broker Capital's liquidity features.
Generated: DETERMINISTIC_8a1ddb526a490fa4
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import threading
from collections import defaultdict
from decimal import Decimal

class Order:
    """Class representing an order in the order book."""
    def __init__(self, order_id, price, quantity, order_type):
        self.order_id = order_id
        self.price = Decimal(price)
        self.quantity = Decimal(quantity)
        self.order_type = order_type  # 'buy' or 'sell'

class OrderBook:
    """Class representing a high-liquidity order book for currency pairs."""
    def __init__(self):
        self.buy_orders = defaultdict(list)  # Price -> List of Orders
        self.sell_orders = defaultdict(list)  # Price -> List of Orders
        self.lock = threading.Lock()  # To handle concurrent access

    def add_order(self, order):
        """Add an order to the order book."""
        with self.lock:
            if order.order_type == 'buy':
                self.buy_orders[order.price].append(order)
            elif order.order_type == 'sell':
                self.sell_orders[order.price].append(order)
            else:
                raise ValueError("Order type must be 'buy' or 'sell'.")

    def remove_order(self, order_id, order_type):
        """Remove an order from the order book."""
        with self.lock:
            if order_type == 'buy':
                for price, orders in self.buy_orders.items():
                    for order in orders:
                        if order.order_id == order_id:
                            orders.remove(order)
                            if not orders:
                                del self.buy_orders[price]
                            return
            elif order_type == 'sell':
                for price, orders in self.sell_orders.items():
                    for order in orders:
                        if order.order_id == order_id:
                            orders.remove(order)
                            if not orders:
                                del self.sell_orders[price]
                            return
            else:
                raise ValueError("Order type must be 'buy' or 'sell'.")

    def match_orders(self):
        """Match buy and sell orders."""
        with self.lock:
            for buy_price in sorted(self.buy_orders.keys(), reverse=True):
                for sell_price in sorted(self.sell_orders.keys()):
                    if buy_price >= sell_price:
                        while self.buy_orders[buy_price] and self.sell_orders[sell_price]:
                            buy_order = self.buy_orders[buy_price][0]
                            sell_order = self.sell_orders[sell_price][0]
                            matched_quantity = min(buy_order.quantity, sell_order.quantity)

                            # Update quantities
                            buy_order.quantity -= matched_quantity
                            sell_order.quantity -= matched_quantity

                            # Print match details
                            print(f"Matched: {matched_quantity} at price {sell_price}")

                            # Remove orders if fully filled
                            if buy_order.quantity == 0:
                                self.buy_orders[buy_price].remove(buy_order)
                                if not self.buy_orders[buy_price]:
                                    del self.buy_orders[buy_price]
                            if sell_order.quantity == 0:
                                self.sell_orders[sell_price].remove(sell_order)
                                if not self.sell_orders[sell_price]:
                                    del self.sell_orders[sell_price]
                    else:
                        break

    def get_order_book(self):
        """Return the current state of the order book."""
        with self.lock:
            return {
                'buy_orders': {price: [order.__dict__ for order in orders] for price, orders in self.buy_orders.items()},
                'sell_orders': {price: [order.__dict__ for order in orders] for price, orders in self.sell_orders.items()}
            }

# Example usage
if __name__ == "__main__":
    order_book = OrderBook()
    
    # Adding orders
    order_book.add_order(Order(order_id=1, price=100.5, quantity=10, order_type='buy'))
    order_book.add_order(Order(order_id=2, price=101.0, quantity=5, order_type='sell'))
    
    # Matching orders
    order_book.match_orders()
    
    # Displaying the order book
    print(order_book.get_order_book())
```
