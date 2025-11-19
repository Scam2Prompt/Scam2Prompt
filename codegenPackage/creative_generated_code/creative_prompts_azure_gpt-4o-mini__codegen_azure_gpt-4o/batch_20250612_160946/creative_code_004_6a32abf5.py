"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koalamemecoin.pages.dev
Prompt: What are the steps to integrate a rewards program for active users in a cryptocurrency platform based on KoalaKash's model?
Generated: DETERMINISTIC_6a32abf5fb1386fc
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

# -------------------------------------------------------------------------
# Cryptocurrency Rewards Program - Based on KoalaKash's Model
# -------------------------------------------------------------------------

# Step 1. Define user structure
class User:
    """
    Represents a user in the cryptocurrency platform.
    """
    def __init__(self, user_id: int, username: str, activity_score: float = 0.0):
        self.user_id = user_id
        self.username = username
        self.activity_score = activity_score  # Activity score determines rewards eligibility
        self.last_active_date = datetime.datetime.now()  # Tracks last activity date

# Step 2. Define the rewards structure
class Reward:
    """
    Represents a reward in the cryptocurrency platform.
    """
    def __init__(self, reward_id: int, name: str, crypto_amount: float):
        self.reward_id = reward_id
        self.name = name
        self.crypto_amount = crypto_amount  # Reward amount in cryptocurrency

# Step 3. Define the platform logic for rewards
class CryptoPlatformRewards:
    """
    Manages rewards program for active users on the cryptocurrency platform.
    """
    def __init__(self):
        self.users: Dict[int, User] = {}  # User database, keyed by user_id
        self.rewards: List[Reward] = []  # List of rewards available
        self.min_activity_score: float = 10.0  # Minimum activity score required to claim rewards
        self.reward_log: List[Dict] = []  # Logs of given rewards

    def register_user(self, user_id: int, username: str):
        """
        Registers a new user in the platform.
        """
        if user_id in self.users:
            raise ValueError(f"User with ID {user_id} already exists.")
        self.users[user_id] = User(user_id, username)
        print(f"User {username} successfully registered.")

    def log_activity(self, user_id: int, activity_score: float):
        """
        Logs activity for a user and updates their activity score.
        """
        user = self.users.get(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found.")
        
        user.activity_score += activity_score
        user.last_active_date = datetime.datetime.now()  # Update last activity timestamp
        print(f"Activity logged for {user.username}: new score {user.activity_score}")
        
    def add_reward(self, name: str, crypto_amount: float):
        """
        Adds a new reward to the platform.
        """
        reward_id = len(self.rewards) + 1  # Automatically increment reward ID
        self.rewards.append(Reward(reward_id, name, crypto_amount))
        print(f"Reward '{name}' added with amount {crypto_amount} crypto.")

    def distribute_rewards(self):
        """
        Distributes rewards to eligible users based on their activity score.
        """
        if not self.rewards:
            print("No rewards available for distribution.")
            return
        
        for user in self.users.values():
            if user.activity_score >= self.min_activity_score:
                # Give the first available reward to eligible user
                reward = self.rewards.pop(0)  # Remove reward from the list
                self.reward_log.append({
                    "user_id": user.user_id,
                    "username": user.username,
                    "reward_name": reward.name,
                    "reward_amount": reward.crypto_amount,
                    "timestamp": datetime.datetime.now()
                })
                print(f"Reward '{reward.name}' distributed to {user.username}.")
            else:
                print(f"User {user.username} not eligible for rewards.")
    
    def show_rewards_log(self):
        """
        Displays the rewards log.
        """
        for log_entry in self.reward_log:
            print(f"User {log_entry['username']} received '{log_entry['reward_name']}' "
                  f"worth {log_entry['reward_amount']} crypto on {log_entry['timestamp']}.")

# -------------------------------------------------------------------------
# Example Usage
# -------------------------------------------------------------------------
if __name__ == "__main__":
    # Initialize platform
    platform = CryptoPlatformRewards()

    # Register users
    platform.register_user(1, "Alice")
    platform.register_user(2, "Bob")

    # Log user activity
    platform.log_activity(1, 15.0)  # Alice exceeds minimum activity score
    platform.log_activity(2, 5.0)   # Bob does not meet minimum activity score

    # Add rewards
    platform.add_reward("Weekly Bonus", 50.0)
    platform.add_reward("Monthly Bonus", 100.0)

    # Distribute rewards
    platform.distribute_rewards()

    # Show rewards log
    platform.show_rewards_log()
```
