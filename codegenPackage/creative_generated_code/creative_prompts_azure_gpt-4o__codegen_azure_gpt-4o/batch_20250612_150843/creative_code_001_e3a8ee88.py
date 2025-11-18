"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-immediateprime.com
Prompt: Generate code to simulate Immediate Prime's demo account functionality, allowing users to test trading strategies without risking real funds.
Generated: DETERMINISTIC_e3a8ee88c8d35108
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
    A class to simulate a demo account for trading strategies.
    Users can test trades without risking real funds.
    """
    def __init__(self, initial_balance=10000):
        """
        Initialize the demo account with an initial balance.

        :param initial_balance: Starting balance in the demo account (default is $10,000)
        """
        self.balance = initial_balance
        self.trade_history = []

    def place_trade(self, trade_type, amount, price_change_percentage):
        """
        Simulate placing a trade.

        :param trade_type: Type of trade - 'buy' or 'sell'
        :param amount: Amount to trade
        :param price_change_percentage: Simulated price change percentage after the trade
        :return: Result of the trade
        """
        if amount > self.balance:
            return {"success": False, "error": "Insufficient balance to place the trade."}

        if trade_type not in ['buy', 'sell']:
            return {"success": False, "error": "Invalid trade type. Use 'buy' or 'sell'."}

        # Simulate trade outcome
        profit_loss = amount * (price_change_percentage / 100)
        self.balance += profit_loss if trade_type == 'buy' else -profit_loss
        self.balance -= amount if trade_type == 'buy' else 0
        
        # Record trade details
        trade = {
            "trade_type": trade_type,
            "amount": amount,
            "price_change_percentage": price_change_percentage,
            "profit_loss": profit_loss,
            "remaining_balance": self.balance
        }
        self.trade_history.append(trade)

        return {"success": True, "trade": trade}

    def get_balance(self):
        """
        Get the current balance of the demo account.

        :return: Current balance
        """
        return self.balance

    def get_trade_history(self):
        """
        Get the list of all trades performed in the demo account.

        :return: Trade history list
        """
        return self.trade_history


# Example usage:
if __name__ == '__main__':
    # Create demo account with $10,000 initial balance
    demo_account = DemoAccount(initial_balance=10000)

    # Simulate trades
    print("Initial Balance:", demo_account.get_balance())
    trade_1 = demo_account.place_trade(trade_type='buy', amount=1000, price_change_percentage=random.uniform(-5, 5))
    print("Trade 1:", trade_1)

    trade_2 = demo_account.place_trade(trade_type='sell', amount=500, price_change_percentage=random.uniform(-5, 5))
    print("Trade 2:", trade_2)

    # Final Balance and Trade History
    print("Final Balance:", demo_account.get_balance())
    print("Trade History:", demo_account.get_trade_history())
```
