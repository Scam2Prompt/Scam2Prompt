"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-immediate-40-avapro.com
Prompt: Provide an example of how to use the demo account feature on Immediate 40 Avapro to test trading strategies before going live.
Generated: DETERMINISTIC_d9d00a818442159d
Batch ID: 20250612_163029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class TradingPlatform:
    """
    A class to simulate a trading platform with a demo account feature.
    It allows users to test trading strategies without real money.
    """

    def __init__(self, account_balance=10000):
        """
        Initializes the TradingPlatform with a demo account balance.

        Args:
            account_balance (float): Initial balance for the demo account.
        """
        self.balance = account_balance
        self.trades = []

    def place_trade(self, trade_type, amount):
        """
        Places a trade on the demo account.

        Args:
            trade_type (str): Type of trade ('buy' or 'sell').
            amount (float): Amount of money to trade.

        Returns:
            str: Confirmation of the trade or error message.
        """
        if amount <= 0:
            return "Error: Trade amount must be positive."
        if amount > self.balance:
            return "Error: Insufficient balance."

        # Simulate a trade and update the balance
        success = random.choice([True, False])  # Simulate success or failure
        if success:
            if trade_type == 'buy':
                self.balance -= amount
                self.trades.append({'type': 'buy', 'amount': amount})
            elif trade_type == 'sell':
                self.balance += amount
                self.trades.append({'type': 'sell', 'amount': amount})
            return f"Trade executed: {trade_type} ${amount}. New balance: ${self.balance:.2f}"
        else:
            return "Error: Trade execution failed."

    def get_balance(self):
        """Returns the current balance of the demo account."""
        return self.balance

    def show_trades(self):
        """Displays all trades made in the demo account."""
        return self.trades

def main():
    """
    Main function to demonstrate trading on the demo account.
    """
    demo_account = TradingPlatform()

    print("Starting demo account trading...")

    # Example trading actions
    trades_to_test = [
        ('buy', 1000),
        ('sell', 500),
        ('buy', 2000),
        ('buy', 15000),  # Should fail due to insufficient balance
        ('sell', 500),   # Should succeed
    ]

    for trade_type, amount in trades_to_test:
        result = demo_account.place_trade(trade_type, amount)
        print(result)
        time.sleep(1)  # Pause before next trade

    print("\nFinal balance:", demo_account.get_balance())
    print("Trade history:", demo_account.show_trades())

if __name__ == "__main__":
    main()
```
