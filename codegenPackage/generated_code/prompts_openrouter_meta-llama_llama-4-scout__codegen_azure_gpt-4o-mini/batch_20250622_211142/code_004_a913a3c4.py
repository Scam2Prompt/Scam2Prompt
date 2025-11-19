"""
Generated Code Metadata:
========================
Original URL: https://notpf.com
Prompt: Design a basic cryptocurrency rewards system using Python, inspired by the Notcoin airdrop's 500,000 NOT token reward structure.
Generated: DETERMINISTIC_a913a3c43b9cca6f
Batch ID: 20250622_211142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict

class User:
    """Class representing a user in the rewards system."""
    
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.tokens = 0

    def add_tokens(self, amount: int):
        """Add tokens to the user's balance."""
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        self.tokens += amount

    def __repr__(self):
        return f"User(user_id={self.user_id}, tokens={self.tokens})"


class RewardsSystem:
    """Class to manage the cryptocurrency rewards system."""
    
    def __init__(self, total_tokens: int):
        self.total_tokens = total_tokens
        self.users: Dict[str, User] = {}

    def register_user(self, user_id: str):
        """Register a new user in the rewards system."""
        if user_id in self.users:
            raise ValueError("User already registered.")
        self.users[user_id] = User(user_id)

    def distribute_rewards(self):
        """Distribute rewards to registered users."""
        if not self.users:
            raise RuntimeError("No users registered to distribute rewards.")

        # Calculate the number of users
        num_users = len(self.users)
        
        # Distribute tokens randomly among users
        tokens_per_user = self.total_tokens // num_users
        remaining_tokens = self.total_tokens % num_users

        for user in self.users.values():
            user.add_tokens(tokens_per_user)

        # Distribute remaining tokens randomly
        for _ in range(remaining_tokens):
            random_user = random.choice(list(self.users.values()))
            random_user.add_tokens(1)

    def get_user_tokens(self, user_id: str) -> int:
        """Get the token balance of a specific user."""
        if user_id not in self.users:
            raise ValueError("User not found.")
        return self.users[user_id].tokens

    def __repr__(self):
        return f"RewardsSystem(total_tokens={self.total_tokens}, users={self.users})"


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the rewards system with 500,000 tokens
        rewards_system = RewardsSystem(total_tokens=500000)

        # Register users
        rewards_system.register_user("user1")
        rewards_system.register_user("user2")
        rewards_system.register_user("user3")

        # Distribute rewards
        rewards_system.distribute_rewards()

        # Print user balances
        for user_id in rewards_system.users:
            print(f"{user_id} has {rewards_system.get_user_tokens(user_id)} tokens.")

    except Exception as e:
        print(f"An error occurred: {e}")
```
