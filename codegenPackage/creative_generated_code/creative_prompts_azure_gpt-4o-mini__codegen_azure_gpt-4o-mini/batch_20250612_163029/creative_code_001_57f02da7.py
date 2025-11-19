"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-alpha.net
Prompt: How can I implement a demo account feature similar to Immediate Alpha's, allowing users to practice cryptocurrency trading without financial risk?
Generated: DETERMINISTIC_57f02da7e9c16a24
Batch ID: 20250612_163029
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

class DemoAccount:
    """
    A class to represent a demo cryptocurrency trading account.
    The account allows users to practice trading without any financial risk.
    """

    def __init__(self, user_id):
        """
        Initializes a new demo account for the user.

        Args:
            user_id (str): The unique identifier for the user.
        """
        self.user_id = user_id
        self.account_id = str(uuid.uuid4())  # Unique account identifier
        self.balance = 100000.0  # Starting balance for demo trading
        self.positions = {}  # Current open positions
        self.history = []  # Transaction history
        self.start_time = datetime.now()
        self.expiry_time = self.start_time + timedelta(days=30)  # Account valid for 30 days

    def buy(self, asset, quantity, price):
        """
        Simulates buying an asset in the demo account.

        Args:
            asset (str): The asset to buy (e.g., 'BTC').
            quantity (float): The quantity of the asset to buy.
            price (float): The price per unit of the asset.

        Returns:
            dict: Transaction result or error message.
        """
        total_cost = quantity * price
        
        if self.balance < total_cost:
            return {'error': 'Insufficient funds for this transaction.'}
        
        # Update balance and positions
        self.balance -= total_cost
        if asset in self.positions:
            self.positions[asset] += quantity
        else:
            self.positions[asset] = quantity
        
        # Record transaction
        self.history.append({
            'action': 'buy',
            'asset': asset,
            'quantity': quantity,
            'price': price,
            'total_cost': total_cost,
            'timestamp': datetime.now()
        })

        return {'success': True, 'balance': self.balance}

    def sell(self, asset, quantity, price):
        """
        Simulates selling an asset in the demo account.

        Args:
            asset (str): The asset to sell (e.g., 'BTC').
            quantity (float): The quantity of the asset to sell.
            price (float): The price per unit of the asset.

        Returns:
            dict: Transaction result or error message.
        """
        if asset not in self.positions or self.positions[asset] < quantity:
            return {'error': 'Not enough asset to sell.'}

        # Update balance and positions
        total_revenue = quantity * price
        self.balance += total_revenue
        self.positions[asset] -= quantity
        
        # Remove asset from positions if quantity reaches zero
        if self.positions[asset] == 0:
            del self.positions[asset]
        
        # Record transaction
        self.history.append({
            'action': 'sell',
            'asset': asset,
            'quantity': quantity,
            'price': price,
            'total_revenue': total_revenue,
            'timestamp': datetime.now()
        })

        return {'success': True, 'balance': self.balance}

    def get_balance(self):
        """
        Returns the current balance of the demo account.

        Returns:
            float: Current balance.
        """
        return self.balance

    def get_positions(self):
        """
        Returns the current open positions in the demo account.

        Returns:
            dict: Dictionary of open positions.
        """
        return self.positions

    def get_history(self):
        """
        Returns the transaction history of the demo account.

        Returns:
            list: List of transactions.
        """
        return self.history

    def is_active(self):
        """
        Checks whether the demo account is still active.

        Returns:
            bool: True if active, False otherwise.
        """
        return datetime.now() < self.expiry_time

# Example usage
if __name__ == "__main__":
    demo_account = DemoAccount(user_id="user123")

    # Simulating buying and selling assets
    print(demo_account.buy("BTC", 0.5, 20000))  # Example buy
    print(demo_account.sell("BTC", 0.2, 21000))  # Example sell
    print("Current Balance:", demo_account.get_balance())
    print("Open Positions:", demo_account.get_positions())
    print("Transaction History:", demo_account.get_history())
    print("Is Account Active?", demo_account.is_active())
```
