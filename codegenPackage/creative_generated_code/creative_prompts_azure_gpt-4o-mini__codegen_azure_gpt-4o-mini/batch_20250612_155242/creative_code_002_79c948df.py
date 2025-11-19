"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initia.co
Prompt: Can you provide an example of how to unlock value in an app using Initia's aligned economics?
Generated: DETERMINISTIC_79c948df999d6baf
Batch ID: 20250612_155242
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """
    Represents a user in the application.
    Attributes:
        user_id (str): Unique identifier for the user.
        balance (float): The current balance of the user.
    """

    def __init__(self, user_id: str):
        self.user_id = user_id
        self.balance = 0.0  # Initialize balance to zero

    def add_balance(self, amount: float):
        """
        Adds a specified amount to the user's balance.
        
        Args:
            amount (float): The amount to add to the balance.
        """
        if amount < 0:
            raise ValueError("Amount to add must be non-negative.")
        self.balance += amount

    def unlock_value(self, percentage: float):
        """
        Unlocks a portion of the user's balance based on the specified percentage.
        
        Args:
            percentage (float): The percentage of the balance to unlock.
        
        Returns:
            float: The amount of balance that was unlocked.
        
        Raises:
            ValueError: If the percentage is outside the range [0, 100].
        """
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100.")
        
        unlock_amount = (percentage / 100) * self.balance
        self.balance -= unlock_amount
        return unlock_amount


class ValueUnlocker:
    """
    Manages the unlocking of value for users based on Initia's aligned economics.
    """

    def __init__(self):
        self.users = {}

    def register_user(self, user_id: str):
        """
        Registers a new user in the system.
        
        Args:
            user_id (str): Unique identifier for the user.
        
        Raises:
            ValueError: If the user ID is already registered.
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = User(user_id)

    def add_user_balance(self, user_id: str, amount: float):
        """
        Adds balance to a user's account.
        
        Args:
            user_id (str): Unique identifier for the user.
            amount (float): The amount to add to the user's balance.
        
        Raises:
            ValueError: If the user does not exist or the amount is negative.
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        
        self.users[user_id].add_balance(amount)

    def unlock_user_value(self, user_id: str, percentage: float):
        """
        Unlocks value for a user based on the specified percentage.
        
        Args:
            user_id (str): Unique identifier for the user.
            percentage (float): The percentage of the balance to unlock.
        
        Returns:
            float: The amount of balance that was unlocked.
        
        Raises:
            ValueError: If the user does not exist or if the percentage is invalid.
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        
        return self.users[user_id].unlock_value(percentage)


# Example usage
if __name__ == "__main__":
    unlocker = ValueUnlocker()
    
    try:
        # Register a new user
        unlocker.register_user("user123")
        
        # Add balance to the user
        unlocker.add_user_balance("user123", 100.0)
        
        # Unlock 50% of the user's balance
        unlocked_value = unlocker.unlock_user_value("user123", 50.0)
        print(f"Unlocked value: {unlocked_value}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
