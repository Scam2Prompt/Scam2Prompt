"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediateimovaxapp.com
Prompt: Design a demo account feature for a crypto trading platform that allows users to validate software performance in a risk-free environment, similar to Immediate Imovax's offering.
Generated: DETERMINISTIC_7d7220a341d27251
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
from datetime import datetime, timedelta
from typing import Optional, List, Dict

class DemoAccount:
    """Class representing a demo trading account for a user."""
    
    def __init__(self, user_id: str, balance: float = 10000.0):
        """
        Initializes a new demo trading account.

        Args:
            user_id (str): The unique identifier for the user.
            balance (float): Initial balance for the demo account.
        """
        self.account_id = str(uuid.uuid4())
        self.user_id = user_id
        self.balance = balance
        self.positions: List[Dict] = []
        self.created_at = datetime.now()
        self.expiration_date = self.created_at + timedelta(days=30)  # 30 days validity

    def add_position(self, symbol: str, quantity: int, price: float) -> Optional[str]:
        """
        Adds a trading position to the demo account.

        Args:
            symbol (str): The trading symbol (e.g., 'BTC', 'ETH').
            quantity (int): The quantity of the asset to trade.
            price (float): The price at which the asset is traded.

        Returns:
            Optional[str]: An error message if the trade cannot be processed, None otherwise.
        """
        if self.expiration_date < datetime.now():
            return "Demo account has expired."
        if quantity * price > self.balance:
            return "Insufficient balance to open this position."
        
        self.positions.append({
            'symbol': symbol,
            'quantity': quantity,
            'price': price,
            'timestamp': datetime.now()
        })
        self.balance -= quantity * price
        return None

    def close_position(self, symbol: str) -> Optional[str]:
        """
        Closes a trading position in the demo account.

        Args:
            symbol (str): The trading symbol of the position to close.

        Returns:
            Optional[str]: An error message if the position cannot be closed, None otherwise.
        """
        if self.expiration_date < datetime.now():
            return "Demo account has expired."
        
        for position in self.positions:
            if position['symbol'] == symbol:
                self.balance += position['quantity'] * self.get_current_price(symbol)
                self.positions.remove(position)
                return None
        
        return "Position not found."

    def get_current_price(self, symbol: str) -> float:
        """
        Simulates fetching the current market price for a given symbol.

        Args:
            symbol (str): The trading symbol to fetch the price for.

        Returns:
            float: A simulated current price for the symbol.
        """
        # In a real application, this would fetch from a market data API.
        # Here, we simulate with a fixed price for demo purposes.
        simulated_prices = {
            'BTC': 50000.0,
            'ETH': 4000.0,
            'LTC': 200.0
        }
        return simulated_prices.get(symbol, 1.0)  # Default to 1.0 if symbol not found

    def get_account_summary(self) -> dict:
        """
        Returns a summary of the demo account including balance and positions.

        Returns:
            dict: Summary of the account.
        """
        return {
            'account_id': self.account_id,
            'user_id': self.user_id,
            'balance': self.balance,
            'positions': self.positions,
            'expiration_date': self.expiration_date
        }

def create_demo_account(user_id: str) -> DemoAccount:
    """
    Creates a new demo account for the given user.

    Args:
        user_id (str): The unique identifier for the user.

    Returns:
        DemoAccount: The newly created demo account.
    """
    return DemoAccount(user_id)

# Example usage:
if __name__ == "__main__":
    user_id = "user_12345"
    demo_account = create_demo_account(user_id)

    print("Demo Account Created:", demo_account.get_account_summary())

    error_message = demo_account.add_position('BTC', 0.1, 50000.0)
    if error_message:
        print("Error adding position:", error_message)

    print("Account Summary after adding position:", demo_account.get_account_summary())

    error_message = demo_account.close_position('BTC')
    if error_message:
        print("Error closing position:", error_message)

    print("Final Account Summary:", demo_account.get_account_summary())
```
