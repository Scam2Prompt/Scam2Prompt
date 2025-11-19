"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-alpha.nl
Prompt: How can I implement a demo account feature in a cryptocurrency trading platform similar to Immediate Alpha to allow users to practice trading without financial risk?
Generated: DETERMINISTIC_976d75ffc67c293d
Batch ID: 20250612_163029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: demo_account.py

import uuid
import datetime


class DemoAccount:
    """
    Class representing a demo account for cryptocurrency trading.
    Allows users to trade with virtual funds without financial risk.
    """

    def __init__(self, initial_balance=10000):
        """
        Initializes a demo account with a default virtual balance.

        Args:
            initial_balance (float): Initial virtual balance for the demo account. Default is $10,000.
        """
        self.account_id = str(uuid.uuid4())  # Generate unique account ID
        self.balance = initial_balance  # Virtual balance
        self.trade_history = []  # List to store trade history
        self.created_at = datetime.datetime.now()  # Timestamp for account creation

    def place_trade(self, trade_type, cryptocurrency, amount, price):
        """
        Places a virtual trade.

        Args:
            trade_type (str): Type of trade ('buy' or 'sell').
            cryptocurrency (str): Name of cryptocurrency being traded.
            amount (float): Amount of cryptocurrency to trade.
            price (float): Price of cryptocurrency per unit.

        Returns:
            dict: Details of the executed trade.

        Raises:
            ValueError: If trade_type is invalid or funds are insufficient.
        """
        if trade_type not in ('buy', 'sell'):
            raise ValueError("Invalid trade type. Must be 'buy' or 'sell'.")

        trade_cost = amount * price

        if trade_type == 'buy':
            if trade_cost > self.balance:
                raise ValueError("Insufficient virtual funds for this trade.")
            self.balance -= trade_cost
        elif trade_type == 'sell':
            self.balance += trade_cost

        trade = {
            'trade_id': str(uuid.uuid4()),
            'trade_type': trade_type,
            'cryptocurrency': cryptocurrency,
            'amount': amount,
            'price': price,
            'cost': trade_cost,
            'timestamp': datetime.datetime.now()
        }

        self.trade_history.append(trade)

        return trade

    def get_balance(self):
        """
        Retrieves the current virtual balance of the demo account.

        Returns:
            float: Current virtual balance.
        """
        return self.balance

    def get_trade_history(self):
        """
        Retrieves the trade history of the demo account.

        Returns:
            list: List of trade history.
        """
        return self.trade_history

    def reset_account(self):
        """
        Resets the demo account to the initial state with the default balance.

        Returns:
            None
        """
        self.balance = 10000  # Reset to default balance
        self.trade_history = []  # Clear trade history


# Example usage:
if __name__ == "__main__":
    try:
        # Create a demo account with a default balance of $10,000
        demo_account = DemoAccount()

        # Place a buy trade
        buy_trade = demo_account.place_trade("buy", "Bitcoin", 0.1, 40000)
        print("Buy Trade:", buy_trade)

        # Place a sell trade
        sell_trade = demo_account.place_trade("sell", "Ethereum", 0.5, 3000)
        print("Sell Trade:", sell_trade)

        # Check balance
        print("Current Balance:", demo_account.get_balance())

        # Check trade history
        print("Trade History:", demo_account.get_trade_history())

        # Reset account
        demo_account.reset_account()
        print("Account reset. Current Balance:", demo_account.get_balance())

    except Exception as e:
        print(f"Error: {e}")
```
