"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bboop.fun
Prompt: Write code to simulate a decentralized cult-like rewards system, inspired by the staking and rewards structure on bboop.fun.
Generated: DETERMINISTIC_e35d67ccd1ef50b5
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class User:
    """Represents a user in the rewards system."""

    def __init__(self, username: str):
        """Initialize a user with a username and a balance of rewards."""
        self.username = username
        self.balance = 0  # User's balance of rewards
        self.staked_amount = 0  # Amount currently staked

    def stake(self, amount: int):
        """Stake a certain amount of rewards."""
        if amount < 0:
            raise ValueError("Amount to stake must be non-negative.")
        if amount > self.balance:
            raise ValueError("Insufficient balance to stake.")
        
        self.balance -= amount
        self.staked_amount += amount
        print(f"{self.username} staked {amount} rewards.")

    def unstake(self):
        """Unstake the user's currently staked rewards."""
        if self.staked_amount == 0:
            raise ValueError("No rewards currently staked to unstake.")
        
        self.balance += self.staked_amount
        print(f"{self.username} unstaked {self.staked_amount} rewards.")
        self.staked_amount = 0

    def earn_rewards(self, amount: int):
        """Earn rewards through the system."""
        if amount < 0:
            raise ValueError("Amount earned must be non-negative.")
        
        self.balance += amount
        print(f"{self.username} earned {amount} rewards.")

class RewardSystem:
    """Simulates a decentralized cult-like rewards system."""

    def __init__(self):
        """Initialize the rewards system with an empty user list and a rewards pool."""
        self.users = {}
        self.rewards_pool = 10000  # Total rewards available in the system

    def add_user(self, username: str):
        """Add a new user to the rewards system."""
        if username in self.users:
            raise ValueError("User already exists.")
        
        self.users[username] = User(username)
        print(f"User '{username}' added to the rewards system.")

    def distribute_rewards(self):
        """Randomly distribute rewards to users based on their stake."""
        total_staked = sum(user.staked_amount for user in self.users.values())
        if total_staked == 0:
            print("No rewards can be distributed, no stakes found.")
            return

        # Distributing rewards proportionally to staked amounts
        for user in self.users.values():
            if user.staked_amount > 0:
                reward_multiplier = user.staked_amount / total_staked
                reward = int(self.rewards_pool * reward_multiplier)
                user.earn_rewards(reward)

    def simulate_day(self):
        """Simulate a day in the rewards system."""
        print("\nSimulating a day in the rewards system...")
        # Randomly add rewards to the pool
        new_rewards = random.randint(1000, 5000)
        self.rewards_pool += new_rewards
        print(f"{new_rewards} new rewards added to the pool.")

        # Distribute rewards to users
        self.distribute_rewards()

# Example of how to use the RewardSystem
if __name__ == "__main__":
    reward_system = RewardSystem()

    # Adding users
    reward_system.add_user("Alice")
    reward_system.add_user("Bob")

    # Users stake rewards
    reward_system.users["Alice"].earn_rewards(500)
    reward_system.users["Bob"].earn_rewards(300)
    
    reward_system.users["Alice"].stake(200)
    reward_system.users["Bob"].stake(150)

    # Simulate multiple days
    for _ in range(5):
        reward_system.simulate_day()
        time.sleep(1)  # Wait a second between simulations for clarity

    # Unstaking rewards
    reward_system.users["Alice"].unstake()
    reward_system.users["Bob"].unstake()
```
