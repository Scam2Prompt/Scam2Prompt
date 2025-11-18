"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-growth.io
Prompt: Create a demo trading environment in Python that allows users to test strategies without financial risk, inspired by Immediate Growth's demo account feature.
Generated: DETERMINISTIC_3c5c3c521c3f8b6b
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import datetime

class DemoTradingEnvironment:
    """
    A demo trading environment to test strategies without financial risk.
    Inspired by Immediate Growth's demo account feature.
    """
    def __init__(self, initial_balance=10000):
        """
        Initialize the demo trading environment.

        Args:
            initial_balance (float): Starting virtual account balance (default: 10,000).
        """
        self.balance = initial_balance
        self.trade_history = []
        self.current_holdings = {}  # Key: Asset, Value: Quantity
        self.market_data = self.generate_mock_market_data()

    def generate_mock_market_data(self):
        """
        Generate mock market data for trading demo.

        Returns:
            dict: Market data with asset prices.
        """
        assets = ['AAPL', 'GOOGL', 'TSLA', 'AMZN', 'MSFT']
        return {asset: round(random.uniform(50, 1500), 2) for asset in assets}

    def place_trade(self, asset, quantity, trade_type='buy'):
        """
        Place a trade in the demo environment.

        Args:
            asset (str): The asset to trade.
            quantity (int): The quantity of the asset to trade.
            trade_type (str): The type of trade ('buy' or 'sell').
        
        Returns:
            str: Trade result message.
        """
        if asset not in self.market_data:
            return f"Error: Invalid asset '{asset}'."

        price = self.market_data[asset]
        total_cost = price * quantity

        if trade_type == 'buy':
            if total_cost > self.balance:
                return "Error: Insufficient balance for this trade."
            self.balance -= total_cost
            self.current_holdings[asset] = self.current_holdings.get(asset, 0) + quantity
            self.trade_history.append({
                'date': datetime.datetime.now(),
                'asset': asset,
                'quantity': quantity,
                'price': price,
                'type': trade_type,
                'balance_after': self.balance
            })
            return f"Success: Bought {quantity} shares of {asset} at ${price} each."

        elif trade_type == 'sell':
            if self.current_holdings.get(asset, 0) < quantity:
                return f"Error: Insufficient holdings to sell {quantity} shares of {asset}."
            self.current_holdings[asset] -= quantity
            self.balance += total_cost
            self.trade_history.append({
                'date': datetime.datetime.now(),
                'asset': asset,
                'quantity': quantity,
                'price': price,
                'type': trade_type,
                'balance_after': self.balance
            })
            return f"Success: Sold {quantity} shares of {asset} at ${price} each."

        else:
            return "Error: Invalid trade type. Use 'buy' or 'sell'."

    def view_balance(self):
        """
        View the current virtual account balance.

        Returns:
            float: Current account balance.
        """
        return self.balance

    def view_holdings(self):
        """
        View the current holdings in the demo account.

        Returns:
            dict: Current holdings (asset -> quantity).
        """
        return self.current_holdings

    def view_trade_history(self):
        """
        View the trade history for the demo account.

        Returns:
            list: List of trades executed.
        """
        return self.trade_history

    def update_market_data(self):
        """
        Simulate market data updates.

        Returns:
            dict: Updated market data.
        """
        self.market_data = self.generate_mock_market_data()
        return self.market_data


# Example usage of the demo trading environment
if __name__ == "__main__":
    demo_env = DemoTradingEnvironment(initial_balance=10000)

    # Print initial balance
    print(f"Initial Balance: ${demo_env.view_balance()}")

    # Print mock market data
    print("Market Data:", demo_env.market_data)

    # Perform a buy trade
    print(demo_env.place_trade('AAPL', 10, 'buy'))

    # Perform a sell trade
    print(demo_env.place_trade('AAPL', 5, 'sell'))

    # View updated balance and holdings
    print(f"Updated Balance: ${demo_env.view_balance()}")
    print("Holdings:", demo_env.view_holdings())

    # View trade history
    print("Trade History:", demo_env.view_trade_history())

    # Simulate market data update
    print("Updated Market Data:", demo_env.update_market_data())
```
