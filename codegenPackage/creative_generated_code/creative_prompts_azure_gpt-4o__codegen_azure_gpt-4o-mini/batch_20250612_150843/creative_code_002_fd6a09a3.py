"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitplex-360.com
Prompt: Generate code to simulate trades using Bitplex 360's demo account feature, allowing users to test trading strategies without risking real funds.
Generated: DETERMINISTIC_fd6a09a3251645e5
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
import time
from typing import List, Dict

class Trade:
    """Class to represent a trade."""
    def __init__(self, trade_type: str, amount: float, price: float):
        self.trade_type = trade_type  # 'buy' or 'sell'
        self.amount = amount           # Amount of currency being traded
        self.price = price             # Price at which the trade is executed
        self.timestamp = time.time()   # Time of trade execution

    def __repr__(self):
        return f"Trade(type={self.trade_type}, amount={self.amount}, price={self.price}, timestamp={self.timestamp})"


class DemoAccount:
    """Class to simulate a demo trading account with Bitplex 360."""
    def __init__(self, initial_balance: float):
        self.balance = initial_balance  # Starting balance for the demo account
        self.trade_history: List[Trade] = []  # List to store trades

    def execute_trade(self, trade_type: str, amount: float) -> Dict[str, str]:
        """Executes a trade and updates the balance and trade history.

        Args:
            trade_type (str): The type of trade ('buy' or 'sell').
            amount (float): The amount of currency to trade.

        Returns:
            Dict[str, str]: Result of the trade execution.
        """
        if trade_type not in ['buy', 'sell']:
            return {"error": "Invalid trade type. Must be 'buy' or 'sell'."}

        # Simulate a price for the trade (random price for demo purposes)
        price = random.uniform(1.0, 100.0)  # Simulate market price
        total_cost = amount * price

        # Check if the trade can be executed based on the account balance
        if trade_type == 'buy':
            if total_cost > self.balance:
                return {"error": "Insufficient funds to execute trade."}
            self.balance -= total_cost  # Deduct from balance for buy
        elif trade_type == 'sell':
            self.balance += total_cost  # Add to balance for sell

        # Record the trade
        trade = Trade(trade_type, amount, price)
        self.trade_history.append(trade)

        return {
            "success": True,
            "trade": trade,
            "new_balance": self.balance
        }

    def get_balance(self) -> float:
        """Returns the current balance of the demo account."""
        return self.balance

    def get_trade_history(self) -> List[Trade]:
        """Returns the trade history of the demo account."""
        return self.trade_history

def main():
    """Main function to simulate trading."""
    demo_account = DemoAccount(initial_balance=10000.0)  # Initialize demo account with $10,000

    # Simulate a series of trades
    trades_to_execute = [
        ('buy', 10),  # Buy 10 units
        ('sell', 5),  # Sell 5 units
        ('buy', 20),  # Buy 20 units
        ('sell', 15),  # Sell 15 units
        ('buy', 30)   # Buy 30 units
    ]

    for trade_type, amount in trades_to_execute:
        result = demo_account.execute_trade(trade_type, amount)
        if 'error' in result:
            print(f"Trade failed: {result['error']}")
        else:
            print(f"Executed: {result['trade']}, New Balance: ${result['new_balance']:.2f}")

    # Print final trade history and balance
    print("\nFinal Trade History:")
    for trade in demo_account.get_trade_history():
        print(trade)

    print(f"\nFinal Balance: ${demo_account.get_balance():.2f}")

if __name__ == "__main__":
    main()
```
