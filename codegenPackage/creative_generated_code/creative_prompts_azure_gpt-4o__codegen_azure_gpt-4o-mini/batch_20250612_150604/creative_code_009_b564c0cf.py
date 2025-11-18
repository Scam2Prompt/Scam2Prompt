"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pinguonbase-claims.pages.dev
Prompt: Develop a gamified reward system for a crypto token, including quests, staking, and exclusive merchandise purchases, inspired by Pingu's ecosystem.
Generated: DETERMINISTIC_b564c0cf77b2435c
Batch ID: 20250612_150604
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from decimal import Decimal
from typing import List, Dict

class Quest:
    """Class representing a quest in the reward system."""
    def __init__(self, name: str, reward: Decimal, completed: bool = False):
        self.name = name
        self.reward = reward
        self.completed = completed

    def complete_quest(self):
        """Mark the quest as completed and return the reward."""
        if not self.completed:
            self.completed = True
            return self.reward
        raise ValueError("Quest already completed.")

class User:
    """Class representing a user in the reward system."""
    def __init__(self, username: str):
        self.username = username
        self.balance = Decimal('0.00')
        self.quests: List[Quest] = []

    def stake_tokens(self, amount: Decimal):
        """Stake a certain amount of tokens."""
        if amount <= 0:
            raise ValueError("Staking amount must be positive.")
        self.balance += amount  # Simulate staking by adding to balance

    def complete_quest(self, quest: Quest):
        """Complete a quest and add the reward to the balance."""
        reward = quest.complete_quest()
        self.balance += reward

class Merchandise:
    """Class representing merchandise in the reward system."""
    def __init__(self, name: str, price: Decimal):
        self.name = name
        self.price = price

class RewardSystem:
    """Class for managing the reward system."""
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.merchandise: List[Merchandise] = []

    def register_user(self, username: str):
        """Register a new user in the reward system."""
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = User(username)

    def add_merchandise(self, name: str, price: Decimal):
        """Add new merchandise to the system."""
        if price <= 0:
            raise ValueError("Price must be positive.")
        self.merchandise.append(Merchandise(name, price))

    def purchase_merchandise(self, username: str, item_name: str):
        """Allow users to purchase merchandise using their balance."""
        user = self.users.get(username)
        if not user:
            raise ValueError("User not found.")
        
        item = next((m for m in self.merchandise if m.name == item_name), None)
        if not item:
            raise ValueError("Item not found.")

        if user.balance < item.price:
            raise ValueError("Insufficient balance to purchase the item.")

        user.balance -= item.price  # Deduct price from user's balance
        return f"{item.name} purchased successfully!"

# Example usage
if __name__ == "__main__":
    reward_system = RewardSystem()
    
    # Register users
    try:
        reward_system.register_user("Alice")
        reward_system.register_user("Bob")
    except ValueError as e:
        print(e)

    # Add merchandise
    try:
        reward_system.add_merchandise("T-shirt", Decimal('10.00'))
        reward_system.add_merchandise("Sticker", Decimal('2.00'))
    except ValueError as e:
        print(e)

    # User staking tokens
    user_alice = reward_system.users["Alice"]
    user_alice.stake_tokens(Decimal('50.00'))

    # Create and complete quests
    quest1 = Quest("Complete tutorial", Decimal('5.00'))
    user_alice.quests.append(quest1)

    try:
        user_alice.complete_quest(quest1)
    except ValueError as e:
        print(e)

    # Purchase merchandise
    try:
        print(reward_system.purchase_merchandise("Alice", "T-shirt"))
    except ValueError as e:
        print(e)

    print(f"Alice's balance: {user_alice.balance}")
```
