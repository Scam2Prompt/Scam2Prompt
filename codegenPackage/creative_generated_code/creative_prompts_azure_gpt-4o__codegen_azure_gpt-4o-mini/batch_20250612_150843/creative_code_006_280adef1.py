"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theimmediate-daypro.com
Prompt: Develop a demo account feature for automated trading software, ensuring seamless user experience as described in Immediate Daypro's platform.
Generated: DETERMINISTIC_280adef1ae0312f8
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import json
from datetime import datetime, timedelta

class DemoAccount:
    """
    A class to represent a demo trading account.

    Attributes:
        user_id (str): Unique identifier for the user.
        balance (float): Initial balance for the demo account.
        trading_history (list): Record of trades made during the demo period.
        expiry_date (datetime): Expiration date of the demo account.
    """

    def __init__(self, user_id: str, initial_balance: float = 10000.0):
        """
        Initializes a new DemoAccount instance.

        Args:
            user_id (str): Unique identifier for the user.
            initial_balance (float): Initial balance for the demo account.
        """
        self.user_id = user_id
        self.balance = initial_balance
        self.trading_history = []
        self.expiry_date = datetime.now() + timedelta(days=30)  # Default 30 days demo period

    def add_trade(self, trade: dict):
        """
        Records a trade in the trading history and updates the balance.

        Args:
            trade (dict): A dictionary containing trade information such as 'amount' and 'type'.

        Raises:
            ValueError: If the trade type is invalid or if insufficient balance.
        """
        self.validate_trade(trade)
        # Update balance according to trade type
        if trade['type'] == 'buy':
            self.balance -= trade['amount']
        elif trade['type'] == 'sell':
            self.balance += trade['amount']
        else:
            raise ValueError("Invalid trade type. Must be 'buy' or 'sell'.")

        # Record the trade
        trade['timestamp'] = datetime.now()
        self.trading_history.append(trade)

    def validate_trade(self, trade: dict):
        """
        Validates the trade before adding it.

        Args:
            trade (dict): A dictionary containing trade information.

        Raises:
            ValueError: If the trade amount is negative or exceeds the current balance.
        """
        if trade['amount'] <= 0:
            raise ValueError("Trade amount must be positive.")
        if trade['type'] not in ['buy', 'sell']:
            raise ValueError("Trade type must be 'buy' or 'sell'.")
        if trade['type'] == 'buy' and trade['amount'] > self.balance:
            raise ValueError("Insufficient balance for the buy trade.")

    def get_balance(self):
        """
        Returns the current balance of the demo account.

        Returns:
            float: The current balance.
        """
        return self.balance

    def get_trading_history(self):
        """
        Returns the trading history of the demo account.

        Returns:
            list: A list of trades made during the demo period.
        """
        return self.trading_history

    def is_expired(self):
        """
        Checks if the demo account has expired.

        Returns:
            bool: True if the demo account has expired, False otherwise.
        """
        return datetime.now() > self.expiry_date

    def to_json(self):
        """
        Returns a JSON representation of the demo account.

        Returns:
            str: JSON string of the demo account.
        """
        return json.dumps({
            'user_id': self.user_id,
            'balance': self.balance,
            'trading_history': self.trading_history,
            'expiry_date': self.expiry_date.isoformat()
        })

# Example usage
if __name__ == "__main__":
    try:
        # Create a demo account for a user
        demo_account = DemoAccount(user_id=str(uuid.uuid4()))

        # Add a trade
        demo_account.add_trade({'amount': 100, 'type': 'buy'})
        demo_account.add_trade({'amount': 150, 'type': 'sell'})

        # Output balance and trading history
        print(f"Current Balance: {demo_account.get_balance()}")
        print(f"Trading History: {demo_account.get_trading_history()}")

        # Check if the demo account is expired
        print(f"Is expired: {demo_account.is_expired()}")

        # Get JSON representation of the demo account
        print(demo_account.to_json())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
