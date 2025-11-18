"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-deepbook-ui.vercel.app
Prompt: Implement a trading book interface that displays order details, based on the "Trade Book Orders" section of the Deeptrade UI.
Generated: DETERMINISTIC_f3ec50479ad19e72
Batch ID: 20250612_153758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class TradeBookOrder:
    """
    Represents an individual order in the trade book.
    """
    def __init__(self, order_id, symbol, quantity, price, side, timestamp):
        """
        Initialize an order object.

        Args:
            order_id (str): Unique identifier for the order.
            symbol (str): The trading pair (e.g., BTC/USD).
            quantity (float): Quantity of the asset being traded.
            price (float): Price of the asset.
            side (str): 'buy' or 'sell'.
            timestamp (str): Timestamp of the order creation.
        """
        self.order_id = order_id
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.side = side
        self.timestamp = timestamp

    def to_dict(self):
        """
        Convert the order object to a dictionary.
        """
        return {
            "order_id": self.order_id,
            "symbol": self.symbol,
            "quantity": self.quantity,
            "price": self.price,
            "side": self.side,
            "timestamp": self.timestamp,
        }


class TradeBook:
    """
    Represents a collection of trading orders (the trade book).
    Provides functionality to display and manage orders.
    """
    def __init__(self):
        """
        Initialize the trade book with an empty list of orders.
        """
        self.orders = []

    def add_order(self, order):
        """
        Add a new order to the trade book.

        Args:
            order (TradeBookOrder): The order to be added.
        """
        if not isinstance(order, TradeBookOrder):
            raise ValueError("Invalid order type. Expected TradeBookOrder object.")
        self.orders.append(order)

    def list_orders(self):
        """
        Retrieve all orders in the trade book.

        Returns:
            list: List of order dictionaries.
        """
        return [order.to_dict() for order in self.orders]

    def display_orders(self):
        """
        Display all orders in the trade book in a user-friendly format.
        """
        print("CURRENT TRADE BOOK ORDERS")
        print("=" * 50)
        for order in self.orders:
            print(f"Order ID: {order.order_id}")
            print(f"Symbol: {order.symbol}")
            print(f"Quantity: {order.quantity}")
            print(f"Price: {order.price}")
            print(f"Side: {order.side}")
            print(f"Timestamp: {order.timestamp}")
            print("-" * 50)

    def save_to_file(self, file_path):
        """
        Save the trade book orders to a JSON file.

        Args:
            file_path (str): Path to the file where orders will be saved.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.list_orders(), file, indent=4)
            print(f"Trade book orders saved to {file_path}")
        except Exception as e:
            print(f"Error saving trade book to file: {e}")

    def load_from_file(self, file_path):
        """
        Load trade book orders from a JSON file.

        Args:
            file_path (str): Path to the JSON file containing orders.
        """
        try:
            with open(file_path, "r") as file:
                orders_data = json.load(file)
                self.orders = [
                    TradeBookOrder(
                        order_id=order["order_id"],
                        symbol=order["symbol"],
                        quantity=order["quantity"],
                        price=order["price"],
                        side=order["side"],
                        timestamp=order["timestamp"],
                    )
                    for order in orders_data
                ]
            print(f"Trade book orders loaded from {file_path}")
        except Exception as e:
            print(f"Error loading trade book from file: {e}")


# Usage Example:

def main():
    # Initialize TradeBook
    trade_book = TradeBook()

    # Add some example orders
    trade_book.add_order(TradeBookOrder("1", "BTC/USD", 0.5, 50000, "buy", "2023-10-12T10:00:00Z"))
    trade_book.add_order(TradeBookOrder("2", "ETH/USD", 10, 1500, "sell", "2023-10-12T11:00:00Z"))

    # Display orders
    trade_book.display_orders()

    # Save orders to a file
    trade_book.save_to_file("trade_book.json")

    # Load orders from the file
    trade_book.load_from_file("trade_book.json")

    # Display orders again after loading
    trade_book.display_orders()


if __name__ == "__main__":
    main()
```
