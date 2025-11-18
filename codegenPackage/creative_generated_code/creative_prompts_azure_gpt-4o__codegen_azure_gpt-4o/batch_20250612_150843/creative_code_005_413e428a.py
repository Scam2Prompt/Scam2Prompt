"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-immediateduac.com
Prompt: Create a demo account system for a cryptocurrency trading platform, similar to IMMEDIATE DUAC's free and unlimited demo account offering.
Generated: DETERMINISTIC_413e428a3abc640f
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# demo_account_system.py
import uuid
from datetime import datetime

class DemoAccount:
    """
    A class representing a demo account for a cryptocurrency trading platform.
    """
    def __init__(self, username):
        """
        Initialize a new demo account.
        
        :param username: The username for the demo account.
        """
        self.account_id = str(uuid.uuid4())  # Unique identifier for each demo account
        self.username = username
        self.balance = 100000.00  # Default starting balance for demo accounts in USD
        self.trades = []  # List to track trade history
        self.created_at = datetime.now()  # Timestamp for when the account was created

    def place_trade(self, trade_type, amount, crypto):
        """
        Simulate placing a trade in the demo account.

        :param trade_type: The type of trade ('Buy' or 'Sell').
        :param amount: The amount in USD to trade.
        :param crypto: The cryptocurrency being traded (e.g., 'BTC').
        :raises ValueError: If the trade type is invalid or the amount exceeds the balance.
        """
        if trade_type not in ('Buy', 'Sell'):
            raise ValueError("Invalid trade type. Must be 'Buy' or 'Sell'.")
        if amount <= 0:
            raise ValueError("Trade amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance for the trade.")
        
        # Deduct amount from balance and record the trade
        self.balance -= amount
        trade = {
            "trade_id": str(uuid.uuid4()),
            "trade_type": trade_type,
            "amount": amount,
            "crypto": crypto,
            "timestamp": datetime.now()
        }
        self.trades.append(trade)

    def get_account_summary(self):
        """
        Retrieve a summary of the demo account.
        
        :return: A dictionary containing account details.
        """
        return {
            "account_id": self.account_id,
            "username": self.username,
            "balance": self.balance,
            "trade_count": len(self.trades),
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    def get_trade_history(self):
        """
        Retrieve the trade history for the demo account.

        :return: A list of all trades placed in the account.
        """
        return self.trades


# Error handling and system simulation
def main():
    try:
        # Create a demo account
        print("Creating demo account...")
        demo_account = DemoAccount(username="demo_user")
        
        print("Demo account created successfully!")
        print(demo_account.get_account_summary())

        # Place a few trades
        print("\nPlacing trades...")
        demo_account.place_trade(trade_type="Buy", amount=1000, crypto="BTC")
        demo_account.place_trade(trade_type="Sell", amount=500, crypto="ETH")

        # Show updated account summary
        print("\nUpdated account summary:")
        print(demo_account.get_account_summary())

        # Show trade history
        print("\nTrade history:")
        for trade in demo_account.get_trade_history():
            print(trade)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
