"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidmmx6ovrkgb7pb5l6vt5iccg5zig3n4kdoo3t6qc7oswvkxckfy4.ipfs.dweb.link
Prompt: Recommend libraries or APIs for implementing a high-speed orderbook system similar to the Blitz platform powered by Vertex Edge.
Generated: DETERMINISTIC_a1051bb528d8006d
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# high_speed_orderbook.py

import numpy as np
import pandas as pd
from typing import Dict, List, Optional
import logging

# Configure logging for debugging and error reporting
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Order:
    """Represents a single order in the order book."""
    def __init__(self, order_id: str, price: float, quantity: int, side: str):
        self.order_id = order_id  # Unique order identifier
        self.price = price  # Price of the order
        self.quantity = quantity  # Quantity of the order
        self.side = side  # Side of the order ('buy' or 'sell')

class OrderBook:
    """A high-speed order book for managing buy and sell orders."""
    def __init__(self):
        self.buys: Dict[str, Order] = {}  # Dictionary to hold buy orders
        self.sells: Dict[str, Order] = {}  # Dictionary to hold sell orders

    def add_order(self, order: Order) -> None:
        """Add an order to the order book."""
        if order.side == 'buy':
            self.buys[order.order_id] = order
            logging.info(f"Added buy order: {order}")
        elif order.side == 'sell':
            self.sells[order.order_id] = order
            logging.info(f"Added sell order: {order}")
        else:
            logging.error("Invalid order side. Must be 'buy' or 'sell'.")
            raise ValueError("Invalid order side. Must be 'buy' or 'sell'.")

    def remove_order(self, order_id: str, side: str) -> Optional[Order]:
        """Remove an order from the order book."""
        if side == 'buy':
            order = self.buys.pop(order_id, None)
            if order:
                logging.info(f"Removed buy order: {order}")
            else:
                logging.warning(f"Buy order {order_id} not found.")
            return order
        elif side == 'sell':
            order = self.sells.pop(order_id, None)
            if order:
                logging.info(f"Removed sell order: {order}")
            else:
                logging.warning(f"Sell order {order_id} not found.")
            return order
        else:
            logging.error("Invalid order side. Must be 'buy' or 'sell'.")
            raise ValueError("Invalid order side. Must be 'buy' or 'sell'.")

    def get_best_bid(self) -> Optional[Order]:
        """Get the best bid (highest buy order) from the order book."""
        if not self.buys:
            logging.info("No buy orders available.")
            return None
        best_bid = max(self.buys.values(), key=lambda o: o.price)
        logging.info(f"Best bid: {best_bid}")
        return best_bid

    def get_best_ask(self) -> Optional[Order]:
        """Get the best ask (lowest sell order) from the order book."""
        if not self.sells:
            logging.info("No sell orders available.")
            return None
        best_ask = min(self.sells.values(), key=lambda o: o.price)
        logging.info(f"Best ask: {best_ask}")
        return best_ask

def main() -> None:
    """Main function to demonstrate the order book functionality."""
    order_book = OrderBook()
    
    # Example orders
    try:
        order1 = Order(order_id="1", price=100.5, quantity=10, side='buy')
        order2 = Order(order_id="2", price=101.0, quantity=5, side='sell')
        
        order_book.add_order(order1)
        order_book.add_order(order2)
        
        best_bid = order_book.get_best_bid()
        best_ask = order_book.get_best_ask()
    
        print(f"Best Bid: {best_bid.price if best_bid else 'None'}")
        print(f"Best Ask: {best_ask.price if best_ask else 'None'}")

        # Removing an order
        order_book.remove_order(order_id="1", side='buy')

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
