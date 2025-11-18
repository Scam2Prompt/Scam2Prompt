"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theimmediate-byte-pro.com
Prompt: Generate code to simulate Immediate Byte Pro's demo account functionality, allowing users to test trading strategies without using real funds.
Generated: DETERMINISTIC_b6972cdce9f915c8
Batch ID: 20250612_150843
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
    A class to represent a demo trading account for simulating trading strategies.
    """

    def __init__(self, initial_balance=10000.0):
        """
        Initializes the demo account with a specified balance.

        :param initial_balance: The starting balance for the demo account, default is 10000.0
        """
        self.balance = initial_balance
        self.trades = []

    def get_balance(self):
        """
        Returns the current balance of the demo account.

        :return: Current balance
        """
        return self.balance

    def execute_trade(self, trade_type, amount):
        """
        Executes a trade of a specified type and amount.

        :param trade_type: The type of trade, either 'buy' or 'sell'
        :param amount: The amount to trade
        :raises ValueError: If trade_type is invalid or insufficient balance for buy
        """
        if trade_type not in ['buy', 'sell']:
            raise ValueError("Trade type must be 'buy' or 'sell'.")

        if trade_type == 'buy':
            if amount > self.balance:
                raise ValueError("Insufficient balance to execute the buy trade.")
            # Simulate trade outcome (for demo purposes, we assume 50% win rate)
            outcome = random.choice([True, False])
            if outcome:  # Successful trade
                profit = amount * 0.1  # 10% profit
                self.balance += profit
                self.trades.append({'type': 'buy', 'amount': amount, 'outcome': 'win', 'profit': profit})
            else:  # Unsuccessful trade
                self.balance -= amount  # Loss equal to the amount traded
                self.trades.append({'type': 'buy', 'amount': amount, 'outcome': 'loss', 'profit': -amount})

        elif trade_type == 'sell':
            # Simulate trade outcome
            outcome = random.choice([True, False])
            if outcome:  # Successful trade
                profit = amount * 0.1  # 10% profit
                self.balance += profit
                self.trades.append({'type': 'sell', 'amount': amount, 'outcome': 'win', 'profit': profit})
            else:  # Unsuccessful trade
                self.balance -= amount  # Loss equal to the amount traded
                self.trades.append({'type': 'sell', 'amount': amount, 'outcome': 'loss', 'profit': -amount})

    def get_trade_history(self):
        """
        Returns the trade history for the demo account.

        :return: List of executed trades
        """
        return self.trades

    def reset_account(self):
        """
        Resets the demo account to its initial state.
        """
        self.balance = 10000.0
        self.trades = []

# Example usage of the DemoAccount class
if __name__ == "__main__":
    demo_account = DemoAccount()

    try:
        print(f"Initial Balance: ${demo_account.get_balance()}")

        # Simulate some trades
        demo_account.execute_trade('buy', 1000)
        demo_account.execute_trade('sell', 500)
        demo_account.execute_trade('buy', 2000)

        print(f"Balance after trades: ${demo_account.get_balance()}")
        print("Trade History:")
        for trade in demo_account.get_trade_history():
            print(trade)

        # Resetting the account
        demo_account.reset_account()
        print(f"Balance after reset: ${demo_account.get_balance()}")

    except ValueError as e:
        print(f"Error: {e}")

```
