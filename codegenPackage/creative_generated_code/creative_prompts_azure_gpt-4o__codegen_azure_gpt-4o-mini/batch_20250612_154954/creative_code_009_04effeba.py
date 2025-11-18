"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imperial-holding.com.co
Prompt: Write code for a trading simulation tool that mimics the competitive trading conditions and transparent execution described on the Imperial Capital website.
Generated: DETERMINISTIC_04effebae8cab6e3
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Any

class Order:
    """Class representing a trading order."""
    
    def __init__(self, order_id: int, price: float, quantity: int, order_type: str):
        self.order_id: int = order_id
        self.price: float = price
        self.quantity: int = quantity
        self.order_type: str = order_type  # 'buy' or 'sell'

class TradingSimulation:
    """Class to simulate a trading environment."""
    
    def __init__(self):
        self.order_book: List[Order] = []  # List to hold active orders
        self.trades: List[Dict[str, Any]] = []  # List to store executed trades
        self.current_order_id: int = 0  # Order ID counter

    def create_order(self, price: float, quantity: int, order_type: str) -> Order:
        """Creates a new trading order and adds it to the order book."""
        if order_type not in ['buy', 'sell']:
            raise ValueError("Order type must be 'buy' or 'sell'")
        
        self.current_order_id += 1
        new_order = Order(order_id=self.current_order_id, price=price, quantity=quantity, order_type=order_type)
        self.order_book.append(new_order)
        return new_order

    def execute_trades(self):
        """Execute trades based on the current order book."""
        # Sort buy and sell orders
        buy_orders = sorted([order for order in self.order_book if order.order_type == 'buy'],
                            key=lambda x: x.price, reverse=True)
        sell_orders = sorted([order for order in self.order_book if order.order_type == 'sell'],
                             key=lambda x: x.price)

        while buy_orders and sell_orders:
            highest_buy = buy_orders[0]
            lowest_sell = sell_orders[0]

            # Check if the highest buy price meets or exceeds the lowest sell price
            if highest_buy.price >= lowest_sell.price:
                # Determine trade quantity
                trade_quantity = min(highest_buy.quantity, lowest_sell.quantity)
                
                # Record the trade
                trade = {
                    'buy_order_id': highest_buy.order_id,
                    'sell_order_id': lowest_sell.order_id,
                    'price': lowest_sell.price,
                    'quantity': trade_quantity
                }
                self.trades.append(trade)

                # Update quantities
                highest_buy.quantity -= trade_quantity
                lowest_sell.quantity -= trade_quantity

                # Remove orders if fully executed
                if highest_buy.quantity == 0:
                    buy_orders.pop(0)
                if lowest_sell.quantity == 0:
                    sell_orders.pop(0)
            else:
                break  # No more trades possible

    def get_order_book(self) -> List[Order]:
        """Returns the current order book."""
        return self.order_book

    def get_trades(self) -> List[Dict[str, Any]]:
        """Returns the list of executed trades."""
        return self.trades

# Example usage
if __name__ == "__main__":
    trading_sim = TradingSimulation()
    
    try:
        # Create some orders
        trading_sim.create_order(price=100.0, quantity=10, order_type='buy')
        trading_sim.create_order(price=99.0, quantity=5, order_type='sell')
        trading_sim.create_order(price=101.0, quantity=15, order_type='buy')
        trading_sim.create_order(price=98.0, quantity=10, order_type='sell')

        # Execute trades
        trading_sim.execute_trades()

        # Display executed trades
        for trade in trading_sim.get_trades():
            print(f"Trade executed: Buy Order ID {trade['buy_order_id']} "
                  f"Sell Order ID {trade['sell_order_id']} "
                  f"Price: {trade['price']} Quantity: {trade['quantity']}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
