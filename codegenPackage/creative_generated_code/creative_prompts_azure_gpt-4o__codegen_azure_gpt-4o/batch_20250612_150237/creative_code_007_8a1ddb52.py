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
"""
OrderBook Implementation for High Liquidity Currency Pairs
Inspired by Eco Broker Capital's liquidity features.

This code provides a high-level implementation of an order book that supports 
buy and sell orders for top currency pairs. It manages bids, asks, and liquidity efficiently.
"""

from collections import defaultdict
import heapq
import threading


class OrderBook:
    """
    A class to manage the order book for high liquidity trading of currency pairs.
    """

    def __init__(self):
        """
        Initialize the order book with separate heaps for bids and asks.
        """
        self.bids = []  # Max heap for bids (price descending)
        self.asks = []  # Min heap for asks (price ascending)
        self.lock = threading.Lock()  # Thread-safe operations
        self.order_id_map = {}  # Track orders by ID for modification/cancellation

    def add_order(self, order_id, side, price, quantity):
        """
        Add a new order to the order book.

        :param order_id: Unique identifier for the order.
        :param side: 'buy' or 'sell'.
        :param price: Price of the order.
        :param quantity: Quantity of the order.
        """
        with self.lock:
            if side == "buy":
                heapq.heappush(self.bids, (-price, order_id, quantity))
            elif side == "sell":
                heapq.heappush(self.asks, (price, order_id, quantity))
            else:
                raise ValueError("Invalid side. Must be 'buy' or 'sell'.")

            self.order_id_map[order_id] = (side, price, quantity)

    def cancel_order(self, order_id):
        """
        Cancel an existing order from the order book.

        :param order_id: Unique identifier for the order to cancel.
        """
        with self.lock:
            if order_id in self.order_id_map:
                del self.order_id_map[order_id]
            else:
                raise ValueError("Order ID not found in the order book.")

    def match_orders(self):
        """
        Match buy and sell orders based on price and liquidity.
        """
        with self.lock:
            while self.bids and self.asks:
                highest_bid = self.bids[0]
                lowest_ask = self.asks[0]

                bid_price = -highest_bid[0]
                ask_price = lowest_ask[0]

                if bid_price >= ask_price:
                    bid_quantity = highest_bid[2]
                    ask_quantity = lowest_ask[2]

                    match_quantity = min(bid_quantity, ask_quantity)

                    # Execute trade
                    print(
                        f"Trade executed: {match_quantity} units at price {ask_price}."
                    )

                    # Update heap quantities
                    if bid_quantity > match_quantity:
                        self.bids[0] = (-bid_price, highest_bid[1], bid_quantity - match_quantity)
                    else:
                        heapq.heappop(self.bids)

                    if ask_quantity > match_quantity:
                        self.asks[0] = (ask_price, lowest_ask[1], ask_quantity - match_quantity)
                    else:
                        heapq.heappop(self.asks)

                    # Remove matched orders from ID map
                    if highest_bid[1] in self.order_id_map:
                        del self.order_id_map[highest_bid[1]]
                    if lowest_ask[1] in self.order_id_map:
                        del self.order_id_map[lowest_ask[1]]
                else:
                    # No match possible at the moment
                    break

    def get_order_book_snapshot(self):
        """
        Get a snapshot of the current order book.

        :return: A dictionary with bids and asks.
        """
        with self.lock:
            bids_snapshot = [
                {"price": -bid[0], "quantity": bid[2]} for bid in self.bids
            ]
            asks_snapshot = [
                {"price": ask[0], "quantity": ask[2]} for ask in self.asks
            ]
            return {"bids": bids_snapshot, "asks": asks_snapshot}


# Example usage
if __name__ == "__main__":
    order_book = OrderBook()

    # Add orders
    order_book.add_order("order1", "buy", 100.5, 10)
    order_book.add_order("order2", "sell", 100.0, 5)
    order_book.add_order("order3", "sell", 101.0, 20)

    # Match orders
    order_book.match_orders()

    # Snapshot of the order book
    snapshot = order_book.get_order_book_snapshot()
    print("Order Book Snapshot:", snapshot)

    # Cancel an order
    order_book.cancel_order("order3")
    print("Order Book Snapshot after cancellation:", order_book.get_order_book_snapshot())
```
