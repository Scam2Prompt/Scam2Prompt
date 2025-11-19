"""
Generated Code Metadata:
========================
Original URL: https://smartnetrewardls.pages.dev
Prompt: Design a system to track and manage token rewards for community members, including user eligibility and reward claiming functionality.
Generated: DETERMINISTIC_73208e7c4400ece4
Batch ID: 20250622_204712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime, timedelta

class User:
    """Class representing a community member."""
    
    def __init__(self, username):
        self.username = username
        self.user_id = str(uuid.uuid4())
        self.tokens = 0
        self.last_claimed = None

    def add_tokens(self, amount):
        """Add tokens to the user's account."""
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        self.tokens += amount

    def claim_reward(self):
        """Claim reward tokens if eligible."""
        if self.is_eligible_to_claim():
            self.tokens += 10  # Reward amount
            self.last_claimed = datetime.now()
            return True
        return False

    def is_eligible_to_claim(self):
        """Check if the user is eligible to claim rewards."""
        if self.last_claimed is None:
            return True
        return datetime.now() - self.last_claimed >= timedelta(days=1)

class RewardSystem:
    """Class to manage the reward system for community members."""
    
    def __init__(self):
        self.users = {}

    def register_user(self, username):
        """Register a new user in the reward system."""
        if username in self.users:
            raise ValueError("Username already exists.")
        user = User(username)
        self.users[username] = user
        return user

    def add_tokens_to_user(self, username, amount):
        """Add tokens to a specific user's account."""
        if username not in self.users:
            raise ValueError("User not found.")
        self.users[username].add_tokens(amount)

    def claim_reward_for_user(self, username):
        """Allow a user to claim their reward."""
        if username not in self.users:
            raise ValueError("User not found.")
        return self.users[username].claim_reward()

    def get_user_info(self, username):
        """Retrieve user information including tokens and last claimed date."""
        if username not in self.users:
            raise ValueError("User not found.")
        user = self.users[username]
        return {
            "username": user.username,
            "user_id": user.user_id,
            "tokens": user.tokens,
            "last_claimed": user.last_claimed
        }

# Example usage
if __name__ == "__main__":
    reward_system = RewardSystem()
    
    # Register users
    try:
        user1 = reward_system.register_user("alice")
        user2 = reward_system.register_user("bob")
        
        # Add tokens
        reward_system.add_tokens_to_user("alice", 50)
        
        # Claim rewards
        if reward_system.claim_reward_for_user("alice"):
            print("Alice claimed her reward!")
        else:
            print("Alice is not eligible to claim yet.")
        
        # Get user info
        print(reward_system.get_user_info("alice"))
    except ValueError as e:
        print(f"Error: {e}")
```
