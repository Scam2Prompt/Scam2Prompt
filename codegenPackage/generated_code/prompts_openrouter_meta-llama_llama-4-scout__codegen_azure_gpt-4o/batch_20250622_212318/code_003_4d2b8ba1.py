"""
Generated Code Metadata:
========================
Original URL: https://monadguide.site
Prompt: "Explain the concept of Onchain CLOB and its application in DeFi trading, referencing the KuruExchange example."
Generated: DETERMINISTIC_4d2b8ba18cacc158
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script explains the concept of Onchain Central Limit Order Book (CLOB) and its application in DeFi trading.
It uses a simplified example inspired by KuruExchange, a decentralized exchange (DEX) that implements an onchain CLOB.
"""

from typing import List, Dict, Union
import datetime

# Define custom exception classes for error handling
class OrderError(Exception):
    """Custom exception for order-related errors."""
    pass

class InsufficientLiquidityError(Exception):
    """Custom exception for liquidity-related errors."""
    pass

# Define the Order class
class Order:
    """
    Represents a single order in the order book.
    Attributes:
        order_id (int): Unique identifier for the order.
        trader (str): Address of the trader placing the order.
        side (str): 'buy' or 'sell'.
        price (float): Price per unit of the asset.
        quantity (float): Quantity of the asset to trade.
        timestamp (datetime): Time when the order was placed.
    """
    def __init__(self, order_id: int, trader: str, side: str, price: float, quantity: float):
        if side not in ['buy', 'sell']:
            raise OrderError("Invalid order side. Must be 'buy' or 'sell'.")
        if price <= 0 or quantity <= 0:
            raise OrderError("Price and quantity must be positive values.")
        
        self.order_id = order_id
        self.trader = trader
        self.side = side
        self.price = price
        self.quantity = quantity
        self.timestamp = datetime.datetime.now()

    def __repr__(self):
        return f"Order({self.order_id}, {self.trader}, {self.side}, {self.price}, {self.quantity}, {self.timestamp})"

# Define the OrderBook class
class OrderBook:
    """
    Represents the onchain Central Limit Order Book (CLOB).
    Attributes:
        buy_orders (List[Order]): List of buy orders sorted by price (highest first).
        sell_orders (List[Order]): List of sell orders sorted by price (lowest first).
    """
    def __init__(self):
        self.buy_orders: List[Order] = []
        self.sell_orders: List[Order] = []

    def add_order(self, order: Order):
        """
        Adds an order to the order book.
        Automatically sorts buy orders by descending price and sell orders by ascending price.
        """
        if order.side == 'buy':
            self.buy_orders.append(order)
            self.buy_orders.sort(key=lambda o: (-o.price, o.timestamp))  # Sort by price (desc), then timestamp
        elif order.side == 'sell':
            self.sell_orders.append(order)
            self.sell_orders.sort(key=lambda o: (o.price, o.timestamp))  # Sort by price (asc), then timestamp

    def match_orders(self) -> List[Dict[str, Union[int, str, float]]]:
        """
        Matches buy and sell orders in the order book.
        Returns a list of executed trades.
        """
        trades = []
        while self.buy_orders and self.sell_orders:
            best_buy = self.buy_orders[0]
            best_sell = self.sell_orders[0]

            if best_buy.price >= best_sell.price:  # Match condition
                trade_quantity = min(best_buy.quantity, best_sell.quantity)
                trade_price = best_sell.price  # Trade at the sell price

                # Record the trade
                trades.append({
                    "buyer": best_buy.trader,
                    "seller": best_sell.trader,
                    "price": trade_price,
                    "quantity": trade_quantity,
                    "timestamp": datetime.datetime.now()
                })

                # Update order quantities
                best_buy.quantity -= trade_quantity
                best_sell.quantity -= trade_quantity

                # Remove fully executed orders
                if best_buy.quantity == 0:
                    self.buy_orders.pop(0)
                if best_sell.quantity == 0:
                    self.sell_orders.pop(0)
            else:
                break  # No match possible

        return trades

    def __repr__(self):
        return f"OrderBook(Buy Orders: {self.buy_orders}, Sell Orders: {self.sell_orders})"

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the order book
        order_book = OrderBook()

        # Add some orders
        order_book.add_order(Order(order_id=1, trader="TraderA", side="buy", price=100.0, quantity=5.0))
        order_book.add_order(Order(order_id=2, trader="TraderB", side="sell", price=95.0, quantity=3.0))
        order_book.add_order(Order(order_id=3, trader="TraderC", side="sell", price=105.0, quantity=2.0))

        print("Order Book Before Matching:")
        print(order_book)

        # Match orders
        trades = order_book.match_orders()

        print("\nExecuted Trades:")
        for trade in trades:
            print(trade)

        print("\nOrder Book After Matching:")
        print(order_book)

    except OrderError as e:
        print(f"Order Error: {e}")
    except InsufficientLiquidityError as e:
        print(f"Liquidity Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
```

This code provides a simplified implementation of an onchain Central Limit Order Book (CLOB) for DeFi trading, inspired by the KuruExchange example. It includes error handling, clean structure, and comments for clarity.
