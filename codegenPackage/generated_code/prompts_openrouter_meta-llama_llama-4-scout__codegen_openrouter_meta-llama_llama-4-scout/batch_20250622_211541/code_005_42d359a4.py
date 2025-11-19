"""
Generated Code Metadata:
========================
Original URL: https://coinrush.bet
Prompt: Create a system to track and manage user bonuses and rewards on a platform similar to Coin Rush, focusing on cashback, rake back, and VIP benefits.
Generated: DETERMINISTIC_42d359a4e9147cb1
Batch ID: 20250622_211541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_bonus_system.py

from enum import Enum
from typing import Dict, List

class BonusType(Enum):
    """Enum for bonus types."""
    CASHBACK = 1
    RAKEBACK = 2
    VIP = 3

class User:
    """Class representing a user."""
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.bonuses: Dict[BonusType, float] = {
            BonusType.CASHBACK: 0.0,
            BonusType.RAKEBACK: 0.0,
            BonusType.VIP: 0.0
        }
        self.transactions: List[Dict] = []

    def add_bonus(self, bonus_type: BonusType, amount: float):
        """Add a bonus to the user's account."""
        if amount < 0:
            raise ValueError("Bonus amount cannot be negative.")
        self.bonuses[bonus_type] += amount
        self.transactions.append({
            'user_id': self.user_id,
            'bonus_type': bonus_type.name,
            'amount': amount
        })

    def get_bonus_balance(self, bonus_type: BonusType) -> float:
        """Get the user's current bonus balance for a specific type."""
        return self.bonuses[bonus_type]

    def get_transaction_history(self) -> List[Dict]:
        """Get the user's transaction history."""
        return self.transactions

class BonusSystem:
    """Class representing the bonus system."""
    def __init__(self):
        self.users: Dict[int, User] = {}

    def create_user(self, user_id: int):
        """Create a new user in the system."""
        if user_id in self.users:
            raise ValueError("User already exists.")
        self.users[user_id] = User(user_id)

    def get_user(self, user_id: int) -> User:
        """Get a user from the system."""
        try:
            return self.users[user_id]
        except KeyError:
            raise ValueError("User does not exist.")

    def add_bonus(self, user_id: int, bonus_type: BonusType, amount: float):
        """Add a bonus to a user's account."""
        user = self.get_user(user_id)
        user.add_bonus(bonus_type, amount)

    def get_user_bonus_balance(self, user_id: int, bonus_type: BonusType) -> float:
        """Get a user's current bonus balance for a specific type."""
        user = self.get_user(user_id)
        return user.get_bonus_balance(bonus_type)

def main():
    bonus_system = BonusSystem()

    # Create users
    bonus_system.create_user(1)
    bonus_system.create_user(2)

    # Add bonuses
    bonus_system.add_bonus(1, BonusType.CASHBACK, 10.0)
    bonus_system.add_bonus(1, BonusType.RAKEBACK, 5.0)
    bonus_system.add_bonus(2, BonusType.VIP, 20.0)

    # Get bonus balances
    print(bonus_system.get_user_bonus_balance(1, BonusType.CASHBACK))  # Output: 10.0
    print(bonus_system.get_user_bonus_balance(1, BonusType.RAKEBACK))  # Output: 5.0
    print(bonus_system.get_user_bonus_balance(2, BonusType.VIP))  # Output: 20.0

    # Get transaction history
    user = bonus_system.get_user(1)
    for transaction in user.get_transaction_history():
        print(transaction)

if __name__ == "__main__":
    main()
```
