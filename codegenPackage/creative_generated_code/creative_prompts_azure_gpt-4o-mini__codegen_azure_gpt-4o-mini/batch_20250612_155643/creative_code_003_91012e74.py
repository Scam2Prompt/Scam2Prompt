"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-deepbook-ui.vercel.app
Prompt: Create a function to display trade book orders in a format used by the Deeptrade application.
Generated: DETERMINISTIC_91012e74b0580f3d
Batch ID: 20250612_155643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class TradeOrder:
    """Class to represent a single trade order."""
    def __init__(self, order_id: str, symbol: str, quantity: int, price: float, side: str):
        """
        Initialize a TradeOrder instance.
        
        :param order_id: Unique identifier for the order.
        :param symbol: The stock or asset symbol.
        :param quantity: The number of shares or units for the order.
        :param price: The price at which the order was placed.
        :param side: The side of the order ('buy' or 'sell').
        """
        self.order_id = order_id
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.side = side
    
    def format_order(self) -> str:
        """Format the order for display."""
        return f"Order ID: {self.order_id}, Symbol: {self.symbol}, Quantity: {self.quantity}, Price: {self.price:.2f}, Side: {self.side}"


def display_trade_orders(orders: List[Dict[str, str]]) -> None:
    """
    Display trade orders in the format used by the Deeptrade application.

    :param orders: A list of dictionaries containing trade order details.
    :raises ValueError: If any required order field is missing or invalid.
    """
    if not orders:
        print("No trade orders to display.")
        return
    
    for order in orders:
        try:
            # Ensure the order has all necessary fields
            required_fields = ['order_id', 'symbol', 'quantity', 'price', 'side']
            if not all(field in order for field in required_fields):
                raise ValueError("Order is missing required fields.")

            # Parse the values from the order dictionary
            order_id = order['order_id']
            symbol = order['symbol']
            quantity = int(order['quantity'])
            price = float(order['price'])
            side = order['side'].lower()

            if side not in ['buy', 'sell']:
                raise ValueError("Order side must be 'buy' or 'sell'.")

            # Create a TradeOrder instance and display it
            trade_order = TradeOrder(order_id, symbol, quantity, price, side)
            print(trade_order.format_order())

        except ValueError as e:
            print(f"Error processing order: {e}")
        except (TypeError, ValueError) as e:
            print(f"Invalid data type in order: {e}")

# Example usage
if __name__ == "__main__":
    sample_orders = [
        {'order_id': '1', 'symbol': 'AAPL', 'quantity': '10', 'price': '145.30', 'side': 'buy'},
        {'order_id': '2', 'symbol': 'TSLA', 'quantity': '5', 'price': '720.00', 'side': 'sell'},
        {'order_id': '3', 'symbol': 'GOOGL', 'quantity': '3', 'price': '2800.00', 'side': 'buy'},
    ]
    
    display_trade_orders(sample_orders)
```
