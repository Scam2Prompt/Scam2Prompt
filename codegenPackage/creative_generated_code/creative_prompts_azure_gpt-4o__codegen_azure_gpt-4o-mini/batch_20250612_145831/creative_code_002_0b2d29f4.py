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
import random
import json
from typing import Dict, Any

class RewardTracker:
    def __init__(self):
        """
        Initialize the RewardTracker with an empty rewards dictionary.
        """
        self.rewards: Dict[str, float] = {}

    def add_user(self, user_id: str) -> None:
        """
        Add a new user to the rewards tracker.

        Args:
            user_id: Unique identifier for the user.
        """
        if user_id not in self.rewards:
            self.rewards[user_id] = 0.0
        else:
            raise ValueError(f"User '{user_id}' already exists.")

    def update_rewards(self, user_id: str, amount: float) -> None:
        """
        Update the rewards for a user.

        Args:
            user_id: Unique identifier for the user.
            amount: Amount of rewards to add.

        Raises:
            ValueError: If the user does not exist or if amount is negative.
        """
        if user_id not in self.rewards:
            raise ValueError(f"User '{user_id}' not found.")
        if amount < 0:
            raise ValueError("Amount must be non-negative.")

        self.rewards[user_id] += amount

    def get_rewards(self, user_id: str) -> float:
        """
        Get the current rewards amount for a user.

        Args:
            user_id: Unique identifier for the user.

        Returns:
            The current rewards amount for the user.

        Raises:
            ValueError: If the user does not exist.
        """
        if user_id not in self.rewards:
            raise ValueError(f"User '{user_id}' not found.")
        return self.rewards[user_id]

    def display_rewards(self) -> None:
        """
        Display the current rewards for all users in a readable format.
        """
        print("\nCurrent User Rewards:")
        for user_id, reward in self.rewards.items():
            print(f"User: {user_id}, Rewards: {reward:.2f}")

    def simulate_reward_updates(self, duration: int = 30) -> None:
        """
        Simulate real-time reward updates for a specified duration.

        Args:
            duration: Duration in seconds for which to simulate updates.
        """
        start_time = time.time()
        while time.time() - start_time < duration:
            user_id = random.choice(list(self.rewards.keys()))
            amount = random.uniform(1, 10)  # Simulate a reward between 1 and 10
            self.update_rewards(user_id, amount)
            self.display_rewards()
            time.sleep(5)  # Pause for 5 seconds before the next update

if __name__ == "__main__":
    # Example usage
    tracker = RewardTracker()
    
    # Add users
    tracker.add_user("user_1")
    tracker.add_user("user_2")
    
    # Start simulating reward updates
    try:
        tracker.simulate_reward_updates(duration=30)
    except ValueError as e:
        print(f"Error: {e}")
```
