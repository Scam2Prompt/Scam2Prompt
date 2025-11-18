"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bananagunn.io
Prompt: Create a system that tracks reward forfeiture when a user sells or transfers more than 300 $BANANA tokens during an epoch, redistributing forfeited rewards among other holders.
Generated: DETERMINISTIC_ef2184d103ef70a7
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from decimal import Decimal
from collections import defaultdict

class RewardTracker:
    def __init__(self):
        # Initialize a dictionary to track user balances and their forfeited tokens
        self.user_balances = defaultdict(Decimal)
        self.total_supply = Decimal(0)
        self.forfeited_rewards = Decimal(0)
        self.epoch_rewards = Decimal(0)
        self.epoch_users = set()
    
    def update_balance(self, user_id: str, amount: Decimal):
        """Updates the balance of a user and the total supply."""
        # Ensure the amount is a valid decimal
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        
        # Update user's balance and total supply
        self.user_balances[user_id] += amount
        self.total_supply += amount
    
    def sell_or_transfer(self, user_id: str, amount: Decimal):
        """Handles the selling or transferring of tokens by a user."""
        if amount > 300:
            forfeited = self.calculate_forfeiture(user_id, amount)
            self.forfeited_rewards += forfeited
            print(f"User {user_id} forfeited {forfeited} rewards due to transferring {amount} $BANANA tokens.")
        
        # Deduct the sold/transferred amount from user's balance
        self.user_balances[user_id] -= amount
        self.epoch_users.add(user_id)

    def calculate_forfeiture(self, user_id: str, amount: Decimal) -> Decimal:
        """Calculates the forfeited rewards based on the transfer amount."""
        # Forfeiture is capped at the user's total balance
        forfeited = min(self.user_balances[user_id], amount - 300)
        return forfeited

    def redistribute_rewards(self):
        """Redistributes the forfeited rewards among users in the epoch."""
        if not self.epoch_users:
            print("No users to redistribute rewards to.")
            return
        
        # Calculate the reward per user
        reward_per_user = self.forfeited_rewards / len(self.epoch_users)
        
        for user_id in self.epoch_users:
            self.user_balances[user_id] += reward_per_user
            print(f"User {user_id} received {reward_per_user} redistributed rewards.")
        
        # Reset the epoch state
        self.forfeited_rewards = Decimal(0)
        self.epoch_users.clear()

    def get_user_balance(self, user_id: str) -> Decimal:
        """Returns the balance of a user."""
        return self.user_balances[user_id]

# Example usage:
if __name__ == "__main__":
    tracker = RewardTracker()
    
    # Adding users
    tracker.update_balance("user1", Decimal(500))
    tracker.update_balance("user2", Decimal(400))
    
    # User1 sells more than 300 tokens
    tracker.sell_or_transfer("user1", Decimal(350))
    
    # User2 sells more than 300 tokens
    tracker.sell_or_transfer("user2", Decimal(400))
    
    # Redistribute forfeited rewards
    tracker.redistribute_rewards()
    
    # Print final balances
    print("Final balances:")
    print(f"User1: {tracker.get_user_balance('user1')}")
    print(f"User2: {tracker.get_user_balance('user2')}")
```
