"""
Generated Code Metadata:
========================
Original URL: https://immediate-enigma.nl
Prompt: What are the benefits of using Immediate Migna's demo account for practicing Ethereum trading, and how can it help traders prepare for live trading?
Generated: DETERMINISTIC_e0298a93439e441c
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DemoAccount:
    """
    A class to represent a demo trading account for practicing Ethereum trading.
    """

    def __init__(self, initial_balance=10000):
        """
        Initializes the demo account with a specified initial balance.

        :param initial_balance: The starting balance for the demo account (default is 10,000).
        """
        self.balance = initial_balance
        self.trades = []

    def execute_trade(self, trade_type, amount, price):
        """
        Executes a trade on the demo account.

        :param trade_type: The type of trade ('buy' or 'sell').
        :param amount: The amount of Ethereum to trade.
        :param price: The price per Ethereum at which to trade.
        :raises ValueError: If the trade type is invalid or if there are insufficient funds.
        """
        if trade_type not in ['buy', 'sell']:
            raise ValueError("Invalid trade type. Use 'buy' or 'sell'.")

        total_cost = amount * price

        if trade_type == 'buy':
            if total_cost > self.balance:
                raise ValueError("Insufficient funds for this trade.")
            self.balance -= total_cost
            self.trades.append({'type': 'buy', 'amount': amount, 'price': price})
        elif trade_type == 'sell':
            self.balance += total_cost
            self.trades.append({'type': 'sell', 'amount': amount, 'price': price})

    def get_balance(self):
        """
        Returns the current balance of the demo account.

        :return: The current balance.
        """
        return self.balance

    def get_trade_history(self):
        """
        Returns the history of trades executed in the demo account.

        :return: A list of executed trades.
        """
        return self.trades

    def reset_account(self):
        """
        Resets the demo account to its initial state.
        """
        self.balance = 10000
        self.trades = []


# Example usage
if __name__ == "__main__":
    try:
        demo_account = DemoAccount()
        print(f"Initial Balance: ${demo_account.get_balance()}")

        # Simulate some trades
        demo_account.execute_trade('buy', 1, 2000)  # Buying 1 ETH at $2000
        print(f"Balance after buying: ${demo_account.get_balance()}")

        demo_account.execute_trade('sell', 0.5, 2500)  # Selling 0.5 ETH at $2500
        print(f"Balance after selling: ${demo_account.get_balance()}")

        # Display trade history
        print("Trade History:", demo_account.get_trade_history())

    except ValueError as e:
        print(f"Error: {e}")
```
