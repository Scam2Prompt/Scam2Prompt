"""
Generated Code Metadata:
========================
Original URL: https://projectdeksa.pages.dev
Prompt: "Design a basic virtual economy system using $MASA token, allowing users to earn, trade, and contribute to the ecosystem."
Generated: DETERMINISTIC_29cd110bf16e8999
Batch ID: 20250622_204830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# virtual_economy.py

class User:
    """
    Represents a user in the virtual economy system.
    Each user has a unique ID and a balance of MASA tokens.
    """
    def __init__(self, user_id):
        self.user_id = user_id
        self.balance = 0.0

    def earn_tokens(self, amount):
        """
        Earn MASA tokens.
        
        :param amount: Amount of tokens to earn
        :raises ValueError: If the amount is negative
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        self.balance += amount

    def spend_tokens(self, amount):
        """
        Spend MASA tokens.
        
        :param amount: Amount of tokens to spend
        :raises ValueError: If the amount is negative or exceeds balance
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def get_balance(self):
        """
        Get the current balance of MASA tokens.
        
        :return: Current balance
        """
        return self.balance


class Economy:
    """
    Represents the virtual economy system.
    It allows users to earn, trade, and contribute to the ecosystem.
    """
    def __init__(self):
        self.users = {}

    def add_user(self, user_id):
        """
        Add a new user to the economy.
        
        :param user_id: Unique identifier for the user
        :raises ValueError: If the user already exists
        """
        if user_id in self.users:
            raise ValueError("User already exists.")
        self.users[user_id] = User(user_id)

    def earn_tokens(self, user_id, amount):
        """
        Allow a user to earn MASA tokens.
        
        :param user_id: Unique identifier for the user
        :param amount: Amount of tokens to earn
        :raises ValueError: If the user does not exist
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        self.users[user_id].earn_tokens(amount)

    def spend_tokens(self, user_id, amount):
        """
        Allow a user to spend MASA tokens.
        
        :param user_id: Unique identifier for the user
        :param amount: Amount of tokens to spend
        :raises ValueError: If the user does not exist
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        self.users[user_id].spend_tokens(amount)

    def get_user_balance(self, user_id):
        """
        Get the balance of a user.
        
        :param user_id: Unique identifier for the user
        :return: User's balance
        :raises ValueError: If the user does not exist
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        return self.users[user_id].get_balance()


# Example usage
if __name__ == "__main__":
    economy = Economy()
    
    # Adding users
    try:
        economy.add_user("user1")
        economy.add_user("user2")
        
        # Earning tokens
        economy.earn_tokens("user1", 100)
        economy.earn_tokens("user2", 50)
        
        # Spending tokens
        economy.spend_tokens("user1", 30)
        
        # Checking balances
        print(f"User1 Balance: {economy.get_user_balance('user1')}")
        print(f"User2 Balance: {economy.get_user_balance('user2')}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
