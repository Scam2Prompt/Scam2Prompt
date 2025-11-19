"""
Generated Code Metadata:
========================
Original URL: https://the-cryptogeniusapp.com
Prompt: Design a demo account system for a cryptocurrency trading platform, like Crypto Genius, that allows users to trade with a risk-free environment and unlimited funds.
Generated: DETERMINISTIC_00e4e6b617b8b565
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from decimal import Decimal

class User:
    """Represents a user in the demo account system."""
    
    def __init__(self, username):
        self.username = username
        self.balance = Decimal('1000000.00')  # Starting balance for demo account
        self.id = uuid.uuid4()  # Unique identifier for the user

    def trade(self, amount, price, action):
        """
        Executes a trade for the user.

        :param amount: The amount of cryptocurrency to trade.
        :param price: The price per unit of cryptocurrency.
        :param action: 'buy' or 'sell' to indicate the type of trade.
        :return: A message indicating the result of the trade.
        """
        if action not in ['buy', 'sell']:
            raise ValueError("Action must be 'buy' or 'sell'.")

        total_cost = Decimal(amount) * Decimal(price)

        if action == 'buy':
            self.balance -= total_cost
            return f"{self.username} bought {amount} units at {price} each."
        elif action == 'sell':
            self.balance += total_cost
            return f"{self.username} sold {amount} units at {price} each."

class DemoAccountSystem:
    """Manages the demo accounts for users."""
    
    def __init__(self):
        self.users = {}

    def create_user(self, username):
        """
        Creates a new user in the demo account system.

        :param username: The username for the new user.
        :return: The created User object.
        """
        if username in self.users:
            raise ValueError("Username already exists.")
        
        user = User(username)
        self.users[username] = user
        return user

    def get_user_balance(self, username):
        """
        Retrieves the balance of a user.

        :param username: The username of the user.
        :return: The user's balance.
        """
        user = self.users.get(username)
        if user is None:
            raise ValueError("User not found.")
        return user.balance

# Example usage
if __name__ == "__main__":
    try:
        demo_system = DemoAccountSystem()
        
        # Create a new user
        user1 = demo_system.create_user("trader1")
        print(f"User created: {user1.username} with balance: {user1.balance}")

        # Perform a trade
        trade_result = user1.trade(amount=10, price=50000, action='buy')
        print(trade_result)
        print(f"New balance: {demo_system.get_user_balance(user1.username)}")

        # Perform another trade
        trade_result = user1.trade(amount=5, price=60000, action='sell')
        print(trade_result)
        print(f"New balance: {demo_system.get_user_balance(user1.username)}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
