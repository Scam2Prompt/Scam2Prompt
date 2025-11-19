"""
Generated Code Metadata:
========================
Original URL: https://sui-deepbook-ui.vercel.app
Prompt: Implement a trading book interface that displays order details, based on the "Trade Book Orders" section of the Deeptrade UI.
Generated: DETERMINISTIC_f3ec50479ad19e72
Batch ID: 20250612_153758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum
from typing import List

class OrderSide(Enum):
    """Enum for order side"""
    BUY = "Buy"
    SELL = "Sell"

@dataclass
class Order:
    """Dataclass for order details"""
    id: int
    symbol: str
    side: OrderSide
    quantity: float
    price: float

class TradingBookInterface:
    """Interface for trading book"""
    def __init__(self):
        self.orders = []

    def add_order(self, order: Order):
        """Add order to trading book"""
        self.orders.append(order)
        self.orders.sort(key=lambda x: x.price if x.side == OrderSide.SELL else -x.price)

    def remove_order(self, order_id: int):
        """Remove order from trading book"""
        self.orders = [order for order in self.orders if order.id != order_id]

    def get_orders(self) -> List[Order]:
        """Get all orders in trading book"""
        return self.orders

    def get_orders_by_side(self, side: OrderSide) -> List[Order]:
        """Get orders by side"""
        return [order for order in self.orders if order.side == side]

    def update_order(self, order_id: int, quantity: float = None, price: float = None):
        """Update order in trading book"""
        for order in self.orders:
            if order.id == order_id:
                if quantity:
                    order.quantity = quantity
                if price:
                    order.price = price
                break

def print_orders(orders: List[Order]):
    """Print order details"""
    print(f"{'ID':^10} | {'Symbol':^10} | {'Side':^10} | {'Quantity':^15} | {'Price':^15}")
    print("-"*60)
    for order in orders:
        print(f"{order.id:^10} | {order.symbol:^10} | {order.side.value:^10} | {order.quantity:^15.2f} | {order.price:^15.2f}")

def main():
    trading_book = TradingBookInterface()

    # Add orders
    trading_book.add_order(Order(1, "AAPL", OrderSide.BUY, 100, 100.0))
    trading_book.add_order(Order(2, "AAPL", OrderSide.SELL, 50, 120.0))
    trading_book.add_order(Order(3, "GOOG", OrderSide.BUY, 50, 2000.0))

    # Print all orders
    print("All Orders:")
    print_orders(trading_book.get_orders())

    # Print orders by side
    print("\nBuy Orders:")
    print_orders(trading_book.get_orders_by_side(OrderSide.BUY))
    print("\nSell Orders:")
    print_orders(trading_book.get_orders_by_side(OrderSide.SELL))

    # Update order
    trading_book.update_order(1, quantity=50)
    print("\nUpdated Orders:")
    print_orders(trading_book.get_orders())

    # Remove order
    trading_book.remove_order(2)
    print("\nOrders after removal:")
    print_orders(trading_book.get_orders())

if __name__ == "__main__":
    main()
```
