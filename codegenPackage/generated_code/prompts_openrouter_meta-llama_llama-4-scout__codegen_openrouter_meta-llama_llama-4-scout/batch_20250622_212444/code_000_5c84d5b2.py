"""
Generated Code Metadata:
========================
Original URL: https://lnynperlqiud.com
Prompt: What are the key features of Hyperliquid, a decentralized perpetual crypto exchange, and how does it address common challenges faced by traditional decentralized exchanges?
Generated: DETERMINISTIC_5c84d5b2ecd76381
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hyperliquid_exchange.py

class HyperliquidExchange:
    """
    A class representing the key features of Hyperliquid, 
    a decentralized perpetual crypto exchange.
    """

    def __init__(self):
        # Initialize the exchange with default parameters
        self.orderbook = {}
        self.trades = []
        self.users = {}

    def add_user(self, user_id, balance):
        """
        Add a new user to the exchange.

        Args:
            user_id (str): Unique identifier for the user.
            balance (float): Initial balance of the user.

        Raises:
            ValueError: If the user_id is already taken or balance is negative.
        """
        if user_id in self.users:
            raise ValueError("User ID already taken")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.users[user_id] = balance

    def place_order(self, user_id, symbol, side, quantity, price):
        """
        Place a new order on the exchange.

        Args:
            user_id (str): Unique identifier for the user.
            symbol (str): Symbol of the cryptocurrency.
            side (str): Side of the order (buy/sell).
            quantity (float): Quantity of the cryptocurrency.
            price (float): Price of the cryptocurrency.

        Raises:
            ValueError: If the user does not exist or quantity/price is negative.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist")
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price cannot be negative")

        # Add order to the orderbook
        if symbol not in self.orderbook:
            self.orderbook[symbol] = []
        self.orderbook[symbol].append({
            'user_id': user_id,
            'side': side,
            'quantity': quantity,
            'price': price
        })

    def match_orders(self, symbol):
        """
        Match buy and sell orders for a given symbol.

        Args:
            symbol (str): Symbol of the cryptocurrency.

        Raises:
            ValueError: If the symbol does not exist in the orderbook.
        """
        if symbol not in self.orderbook:
            raise ValueError("Symbol does not exist in the orderbook")

        # Separate buy and sell orders
        buy_orders = [order for order in self.orderbook[symbol] if order['side'] == 'buy']
        sell_orders = [order for order in self.orderbook[symbol] if order['side'] == 'sell']

        # Sort orders by price
        buy_orders.sort(key=lambda x: x['price'], reverse=True)
        sell_orders.sort(key=lambda x: x['price'])

        # Match orders
        while buy_orders and sell_orders and buy_orders[0]['price'] >= sell_orders[0]['price']:
            buy_order = buy_orders.pop(0)
            sell_order = sell_orders.pop(0)

            # Execute trade
            trade_quantity = min(buy_order['quantity'], sell_order['quantity'])
            self.trades.append({
                'symbol': symbol,
                'buy_user_id': buy_order['user_id'],
                'sell_user_id': sell_order['user_id'],
                'quantity': trade_quantity,
                'price': sell_order['price']
            })

            # Update user balances
            self.users[buy_order['user_id']] += trade_quantity * sell_order['price']
            self.users[sell_order['user_id']] -= trade_quantity * sell_order['price']

            # Update order quantities
            if buy_order['quantity'] > trade_quantity:
                buy_order['quantity'] -= trade_quantity
                buy_orders.append(buy_order)
            if sell_order['quantity'] > trade_quantity:
                sell_order['quantity'] -= trade_quantity
                sell_orders.append(sell_order)

    def get_trades(self):
        """
        Get a list of all trades executed on the exchange.

        Returns:
            list: A list of trades, each containing symbol, buy_user_id, sell_user_id, quantity, and price.
        """
        return self.trades


def main():
    exchange = HyperliquidExchange()

    # Add users
    exchange.add_user('user1', 1000)
    exchange.add_user('user2', 1000)

    # Place orders
    exchange.place_order('user1', 'BTC', 'buy', 1, 50000)
    exchange.place_order('user2', 'BTC', 'sell', 1, 50000)

    # Match orders
    exchange.match_orders('BTC')

    # Get trades
    trades = exchange.get_trades()
    for trade in trades:
        print(trade)


if __name__ == "__main__":
    main()
```
