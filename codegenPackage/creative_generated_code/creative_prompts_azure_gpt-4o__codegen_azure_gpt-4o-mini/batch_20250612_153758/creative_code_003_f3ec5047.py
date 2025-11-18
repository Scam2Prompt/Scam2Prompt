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
from typing import List, Dict, Any

class Order:
    """
    A class to represent a trading order.

    Attributes:
        order_id (str): Unique identifier for the order.
        symbol (str): The stock symbol for the order.
        quantity (int): Number of shares for the order.
        price (float): Price per share at which the order is placed.
        order_type (str): Type of order (e.g., 'buy', 'sell').
        status (str): Current status of the order (e.g., 'open', 'closed').
    """

    def __init__(self, order_id: str, symbol: str, quantity: int, price: float, order_type: str, status: str) -> None:
        self.order_id = order_id
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.order_type = order_type
        self.status = status

    def to_dict(self) -> Dict[str, Any]:
        """Converts the order to a dictionary format."""
        return {
            "order_id": self.order_id,
            "symbol": self.symbol,
            "quantity": self.quantity,
            "price": self.price,
            "order_type": self.order_type,
            "status": self.status
        }

class TradingBook:
    """
    A class to represent a trading book containing multiple orders.

    Attributes:
        orders (List[Order]): A list of orders in the trading book.
    """

    def __init__(self) -> None:
        self.orders: List[Order] = []

    def add_order(self, order: Order) -> None:
        """Adds an order to the trading book."""
        self.orders.append(order)

    def display_orders(self) -> None:
        """Displays the details of all orders in the trading book."""
        if not self.orders:
            print("No orders available.")
            return
        
        print(f"{'Order ID':<15}{'Symbol':<10}{'Quantity':<10}{'Price':<10}{'Order Type':<10}{'Status':<10}")
        print("=" * 65)
        for order in self.orders:
            print(f"{order.order_id:<15}{order.symbol:<10}{order.quantity:<10}{order.price:<10}{order.order_type:<10}{order.status:<10}")

    def save_to_file(self, file_path: str) -> None:
        """Saves the orders to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump([order.to_dict() for order in self.orders], file, indent=4)
            print(f"Orders saved to {file_path}")
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, file_path: str) -> None:
        """Loads orders from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                orders_data = json.load(file)
                for order_data in orders_data:
                    order = Order(
                        order_id=order_data['order_id'],
                        symbol=order_data['symbol'],
                        quantity=order_data['quantity'],
                        price=order_data['price'],
                        order_type=order_data['order_type'],
                        status=order_data['status']
                    )
                    self.add_order(order)
            print(f"Orders loaded from {file_path}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

# Example usage of TradingBook
if __name__ == "__main__":
    trading_book = TradingBook()
    trading_book.add_order(Order("1", "AAPL", 10, 150.0, "buy", "open"))
    trading_book.add_order(Order("2", "GOOGL", 5, 2800.0, "sell", "open"))
    
    trading_book.display_orders()
    
    # Save orders to a file
    trading_book.save_to_file("trading_orders.json")
    
    # Load orders from a file
    trading_book.load_from_file("trading_orders.json")
    
    # Display loaded orders
    trading_book.display_orders()
```
