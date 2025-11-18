"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-growth.io
Prompt: Write Python code to simulate a cryptocurrency trading strategy using a demo account feature like the one described on the Immediate Growth platform. Include functionality for testing trades with "fake" currency.
Generated: DETERMINISTIC_b6e8dafc2954dffc
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

class DemoAccount:
    """
    A class to simulate a cryptocurrency demo trading account.

    Attributes:
        balance (float): The initial balance of the demo account.
        trades (list): A list to keep track of executed trades.
    """

    def __init__(self, initial_balance=10000.0):
        """
        Initializes the DemoAccount with a given initial balance.

        Args:
            initial_balance (float): The starting balance of the account. Default is 10000.0.
        """
        self.balance = initial_balance
        self.trades = []

    def make_trade(self, currency_pair, trade_type, amount):
        """
        Executes a trade on the demo account.

        Args:
            currency_pair (str): The currency pair to trade (e.g., 'BTC/USD').
            trade_type (str): The type of trade ('buy' or 'sell').
            amount (float): The amount of currency to trade.

        Returns:
            str: A message indicating the result of the trade.
        """
        # Validate inputs
        if trade_type not in ['buy', 'sell']:
            return "Error: Trade type must be 'buy' or 'sell'."
        if amount <= 0:
            return "Error: Trade amount must be greater than 0."
        if amount > self.balance:
            return "Error: Insufficient balance for this trade."

        # Simulate price fluctuation
        price = self.simulate_price(currency_pair)
        trade_value = price * amount

        # Execute trade
        if trade_type == 'buy':
            self.balance -= trade_value
            self.trades.append({'pair': currency_pair, 'type': 'buy', 'amount': amount, 'price': price})
        else:  # trade_type == 'sell'
            self.balance += trade_value
            self.trades.append({'pair': currency_pair, 'type': 'sell', 'amount': amount, 'price': price})

        return f"Executed {trade_type} trade: {amount} of {currency_pair} at {price} each."

    def simulate_price(self, currency_pair):
        """
        Simulates the current price of a cryptocurrency.

        Args:
            currency_pair (str): The currency pair to simulate price for.

        Returns:
            float: A simulated price for the given currency pair.
        """
        # For simulation purposes, we return a random price
        return round(random.uniform(100, 500), 2)  # Simulating a price between $100 and $500

    def get_balance(self):
        """
        Retrieves the current balance of the demo account.

        Returns:
            float: The current balance.
        """
        return self.balance

    def get_trade_history(self):
        """
        Retrieves the trade history of the demo account.

        Returns:
            list: The trade history as a list of executed trades.
        """
        return self.trades

# Example usage
if __name__ == "__main__":
    demo_account = DemoAccount()

    print("Initial Balance:", demo_account.get_balance())
    
    # Simulating some trades
    print(demo_account.make_trade('BTC/USD', 'buy', 0.1))
    print(demo_account.make_trade('ETH/USD', 'sell', 0.5))
    print("Current Balance:", demo_account.get_balance())
    
    # Display trade history
    print("Trade History:", demo_account.get_trade_history())
```
