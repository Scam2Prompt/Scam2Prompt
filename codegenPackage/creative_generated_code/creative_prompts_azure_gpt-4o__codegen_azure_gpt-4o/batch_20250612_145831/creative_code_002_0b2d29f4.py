"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spacem-world.vercel.app
Prompt: Create a function to track and display user rewards in real-time for a crypto campaign, inspired by the transparent reward tracking system mentioned on the SpaceM World site.
Generated: DETERMINISTIC_0b2d29f48e328104
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from typing import Dict, List

class RewardTracker:
    """
    A class to track and display user rewards for a crypto campaign.
    """
    def __init__(self):
        # Dictionary to store user rewards. Keys are user IDs, values are reward balances.
        self.user_rewards: Dict[str, float] = {}

    def add_user(self, user_id: str) -> None:
        """
        Add a new user to the reward tracking system.
        
        :param user_id: A unique identifier for the user.
        """
        if user_id in self.user_rewards:
            raise ValueError(f"User {user_id} already exists in the system.")
        self.user_rewards[user_id] = 0.0  # Initialize reward balance to zero

    def update_reward(self, user_id: str, amount: float) -> None:
        """
        Update the reward balance for a user.
        
        :param user_id: A unique identifier for the user.
        :param amount: The amount to add to the user's reward balance.
        """
        if user_id not in self.user_rewards:
            raise ValueError(f"User {user_id} does not exist.")
        if amount < 0:
            raise ValueError("Reward amount cannot be negative.")
        self.user_rewards[user_id] += amount

    def get_rewards(self, user_id: str) -> float:
        """
        Get the current reward balance for a user.
        
        :param user_id: A unique identifier for the user.
        :return: The user's reward balance.
        """
        if user_id not in self.user_rewards:
            raise ValueError(f"User {user_id} does not exist.")
        return self.user_rewards[user_id]

    def display_rewards(self) -> None:
        """
        Display all user rewards in real-time.
        """
        # Clear the terminal for real-time display (this works for most command-line terminals)
        print("\033c", end="")
        print("User Rewards:")
        print("-" * 20)
        for user_id, reward_balance in self.user_rewards.items():
            print(f"User: {user_id}, Rewards: {reward_balance:.2f}")
        print("-" * 20)


def simulate_real_time_tracking(tracker: RewardTracker, updates: List[Dict[str, float]], interval: int = 2) -> None:
    """
    Simulate real-time reward tracking by applying a series of updates to the tracker.
    
    :param tracker: The RewardTracker instance.
    :param updates: A list of dictionaries containing user_id and reward amount.
    :param interval: The time interval (in seconds) between updates.
    """
    try:
        for update in updates:
            user_id = update.get("user_id")
            amount = update.get("amount")
            if user_id and amount is not None:
                tracker.update_reward(user_id, amount)
                tracker.display_rewards()
                time.sleep(interval)
    except Exception as e:
        print(f"Error during tracking: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the reward tracker
    tracker = RewardTracker()
    
    # Add users to the tracker
    tracker.add_user("user1")
    tracker.add_user("user2")
    tracker.add_user("user3")
    
    # Define simulated updates
    simulated_updates = [
        {"user_id": "user1", "amount": 10.5},
        {"user_id": "user2", "amount": 20.0},
        {"user_id": "user1", "amount": 15.0},
        {"user_id": "user3", "amount": 50.0},
        {"user_id": "user2", "amount": 5.0},
    ]
    
    # Simulate real-time reward tracking
    simulate_real_time_tracking(tracker, simulated_updates)
```
