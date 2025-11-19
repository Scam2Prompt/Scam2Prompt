"""
Generated Code Metadata:
========================
Original URL: https://sui-deepbook-ui.vercel.app
Prompt: Create a function to display trade book orders in a format used by the Deeptrade application.
Generated: DETERMINISTIC_91012e74b0580f3d
Batch ID: 20250612_155643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Any
from dataclasses import dataclass
import json
from decimal import Decimal

@dataclass
class Order:
    """Represents a single order in the trade book."""
    order_id: str
    symbol: str
    price: Decimal
    quantity: Decimal
    side: str  # 'BUY' or 'SELL'
    timestamp: str

class TradeBookDisplay:
    """Handles the display of trade book orders in Deeptrade format."""
    
    def __init__(self):
        self.orders: List[Order] = []
    
    def add_order(self, order: Order) -> None:
        """Adds an order to the trade book.
        
        Args:
            order: Order object to be added
        """
        self.orders.append(order)
    
    def display_orders(self, format_type: str = 'table') -> str:
        """Displays orders in the specified format.
        
        Args:
            format_type: Output format ('table', 'json', or 'csv')
            
        Returns:
            Formatted string representation of orders
            
        Raises:
            ValueError: If invalid format_type is provided
        """
        if format_type == 'table':
            return self._display_table()
        elif format_type == 'json':
            return self._display_json()
        elif format_type == 'csv':
            return self._display_csv()
        else:
            raise ValueError(f"Invalid format type: {format_type}")
    
    def _display_table(self) -> str:
        """Generates a table-formatted string of orders."""
        header = f"{'ID':<10} {'Symbol':<8} {'Price':<10} {'Qty':<10} {'Side':<6} {'Timestamp':<20}"
        separator = '-' * len(header)
        rows = [header, separator]
        
        for order in sorted(self.orders, key=lambda x: x.timestamp):
            row = (f"{order.order_id:<10} {order.symbol:<8} "
                  f"{str(order.price):<10} {str(order.quantity):<10} "
                  f"{order.side:<6} {order.timestamp:<20}")
            rows.append(row)
        
        return '\n'.join(rows)
    
    def _display_json(self) -> str:
        """Generates a JSON-formatted string of orders."""
        orders_data = [
            {
                'order_id': order.order_id,
                'symbol': order.symbol,
                'price': str(order.price),
                'quantity': str(order.quantity),
                'side': order.side,
                'timestamp': order.timestamp
            }
            for order in self.orders
        ]
        return json.dumps(orders_data, indent=2)
    
    def _display_csv(self) -> str:
        """Generates a CSV-formatted string of orders."""
        header = "ID,Symbol,Price,Quantity,Side,Timestamp"
        rows = [header]
        
        for order in self.orders:
            row = (f"{order.order_id},{order.symbol},"
                  f"{order.price},{order.quantity},"
                  f"{order.side},{order.timestamp}")
            rows.append(row)
        
        return '\n'.join(rows)
    
    def clear_orders(self) -> None:
        """Clears all orders from the trade book."""
        self.orders.clear()

# Example usage
if __name__ == "__main__":
    trade_book = TradeBookDisplay()
    
    # Add sample orders
    trade_book.add_order(Order(
        order_id="ORD12345",
        symbol="AAPL",
        price=Decimal("150.25"),
        quantity=Decimal("100"),
        side="BUY",
        timestamp="2023-01-01T10:00:00Z"
    ))
    
    trade_book.add_order(Order(
        order_id="ORD67890",
        symbol="GOOGL",
        price=Decimal("2750.50"),
        quantity=Decimal("50"),
        side="SELL",
        timestamp="2023-01-01T10:01:00Z"
    ))
    
    # Display in different formats
    print("Table Format:")
    print(trade_book.display_orders('table'))
    
    print("\nJSON Format:")
    print(trade_book.display_orders('json'))
    
    print("\nCSV Format:")
    print(trade_book.display_orders('csv'))
```
