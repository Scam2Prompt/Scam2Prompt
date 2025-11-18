"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafkreicoon64gkkbjxpmodgbslmgl7ogwalyvfj6heqdicaqv3pqkepbvm.ipfs.dweb.link
Prompt: Write a program to monitor and redistribute forfeited rewards among all holders if a user sells or transfers more than 300 $BANANA during an epoch.
Generated: DETERMINISTIC_13b26aeda76bd493
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict

class User:
    def __init__(self, user_id: str, balance: float):
        self.user_id = user_id    # Unique identifier for the user
        self.balance = balance      # Balance of $BANANA tokens

class RewardManager:
    def __init__(self):
        self.users: Dict[str, User] = {}  # Dictionary to hold users and their balances
        self.total_rewards: float = 0.0    # Total rewards to distribute
        self.forfeited_rewards: float = 0.0 # Rewards forfeited from users

    def add_user(self, user_id: str, initial_balance: float):
        """Add a new user to the reward system with an initial balance."""
        if user_id in self.users:
            raise ValueError(f"User {user_id} already exists.")
        self.users[user_id] = User(user_id, initial_balance)

    def record_transfer(self, user_id: str, amount: float):
        """Record a transfer and check if it exceeds the limit."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} not found.")
        
        if amount > 300:
            self.forfeit_rewards(amount)
        else:
            print(f"Transfer of {amount} by {user_id} is within the limit.")

    def forfeited_rewards(self, amount: float):
        """Handle the forfeiture of rewards during significant transfers."""
        self.forfeited_rewards += amount * 0.1  # Forfeit 10% of the transfer amount
        print(f"Forfeited rewards updated to: {self.forfeited_rewards}")

    def redistribute_rewards(self):
        """Redistribute the forfeited rewards among all users."""
        if not self.users:
            print("No users to redistribute rewards.")
            return

        # Calculate the amount to distribute per user
        reward_per_user = self.forfeited_rewards / len(self.users)
        for user in self.users.values():
            user.balance += reward_per_user
            print(f"Distributed {reward_per_user} to user {user.user_id}. New balance: {user.balance}")

        # Reset forfeited rewards after redistribution
        self.forfeited_rewards = 0.0

def main():
    reward_manager = RewardManager()
    
    # Adding users
    reward_manager.add_user("user1", 1000)
    reward_manager.add_user("user2", 1500)

    # Simulating transfers
    try:
        reward_manager.record_transfer("user1", 350)  # Exceeds limit
        reward_manager.record_transfer("user2", 250)  # Within limit
    except ValueError as e:
        print(f"Error: {e}")

    # Redistribute forfeited rewards if any
    reward_manager.redistribute_rewards()

if __name__ == "__main__":
    main()
```
