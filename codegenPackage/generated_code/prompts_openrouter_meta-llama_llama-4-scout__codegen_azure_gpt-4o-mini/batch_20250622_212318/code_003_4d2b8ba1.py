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
Onchain Central Limit Order Book (CLOB) Implementation Example

This code provides a simplified representation of an Onchain CLOB for a decentralized finance (DeFi) trading platform.
The example includes basic functionalities such as placing orders, matching orders, and handling errors.

KuruExchange is a hypothetical DeFi exchange that utilizes this CLOB model for trading assets.
"""

class Order:
    """
    Represents a trading order in the CLOB.
    """
    def __init__(self, order_id, trader, price, quantity, order_type):
        self.order_id = order_id  # Unique identifier for the order
        self.trader = trader        # Trader's address
        self.price = price          # Price at which the order is placed
        self.quantity = quantity    # Quantity of the asset to trade
        self.order_type = order_type  # 'buy' or 'sell'

class CLOB:
    """
    Central Limit Order Book for managing buy and sell orders.
    """
    def __init__(self):
        self.buy_orders = []  # List to hold buy orders
        self.sell_orders = [] # List to hold sell orders

    def place_order(self, order):
        """
        Places an order in the CLOB.
        
        :param order: An instance of Order to be placed
        :raises ValueError: If the order type is invalid
        """
        if order.order_type not in ['buy', 'sell']:
            raise ValueError("Invalid order type. Must be 'buy' or 'sell'.")

        if order.order_type == 'buy':
            self.buy_orders.append(order)
            self.buy_orders.sort(key=lambda x: x.price, reverse=True)  # Highest price first
        else:
            self.sell_orders.append(order)
            self.sell_orders.sort(key=lambda x: x.price)  # Lowest price first

        self.match_orders()  # Attempt to match orders after placing a new one

    def match_orders(self):
        """
        Matches buy and sell orders based on price and quantity.
        """
        while self.buy_orders and self.sell_orders:
            highest_buy = self.buy_orders[0]
            lowest_sell = self.sell_orders[0]

            if highest_buy.price >= lowest_sell.price:
                # Execute trade
                trade_quantity = min(highest_buy.quantity, lowest_sell.quantity)
                print(f"Trade executed: {trade_quantity} at price {lowest_sell.price}")

                # Update quantities
                highest_buy.quantity -= trade_quantity
                lowest_sell.quantity -= trade_quantity

                # Remove orders if fully filled
                if highest_buy.quantity == 0:
                    self.buy_orders.pop(0)
                if lowest_sell.quantity == 0:
                    self.sell_orders.pop(0)
            else:
                break  # No more matches possible

# Example usage
if __name__ == "__main__":
    try:
        clob = CLOB()
        
        # Placing buy orders
        clob.place_order(Order(order_id=1, trader="0xTrader1", price=100, quantity=5, order_type='buy'))
        clob.place_order(Order(order_id=2, trader="0xTrader2", price=101, quantity=3, order_type='buy'))
        
        # Placing sell orders
        clob.place_order(Order(order_id=3, trader="0xTrader3", price=99, quantity=2, order_type='sell'))
        clob.place_order(Order(order_id=4, trader="0xTrader4", price=100, quantity=4, order_type='sell'))

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
