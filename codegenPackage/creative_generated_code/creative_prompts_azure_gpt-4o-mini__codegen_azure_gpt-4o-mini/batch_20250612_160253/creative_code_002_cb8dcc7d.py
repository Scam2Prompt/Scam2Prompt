"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://play-sonic-lab.xyz
Prompt: Write a function to create a daily rewards system for a mobile game, inspired by the Holders App's engaging gameplay.
Generated: DETERMINISTIC_cb8dcc7daff36b49
Batch ID: 20250612_160253
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
import os

class DailyRewardsSystem:
    def __init__(self, user_id):
        """
        Initialize the DailyRewardsSystem for a specific user.

        Args:
            user_id (str): The unique identifier for the user.
        """
        self.user_id = user_id
        self.reward_file = f"{self.user_id}_rewards.json"
        self.rewards = self.load_rewards()

    def load_rewards(self):
        """
        Load the rewards data from a JSON file. If the file does not exist,
        initialize an empty reward structure.

        Returns:
            dict: The rewards data for the user.
        """
        if os.path.exists(self.reward_file):
            with open(self.reward_file, 'r') as file:
                return json.load(file)
        return {"last_claim_date": None, "streak": 0, "total_rewards": 0}

    def save_rewards(self):
        """
        Save the rewards data back to the JSON file.
        """
        with open(self.reward_file, 'w') as file:
            json.dump(self.rewards, file)

    def calculate_reward(self):
        """
        Calculate the reward amount based on the current streak.

        Returns:
            int: The reward amount.
        """
        base_reward = 100  # Base reward for first claim
        return base_reward * (self.rewards["streak"] + 1)

    def claim_daily_reward(self):
        """
        Claim the daily reward for the user. This function handles the
        reward claiming logic, including streak calculations and resets.

        Returns:
            str: A message indicating the result of the reward claim.
        """
        today = datetime.date.today()
        last_claim_date = self.rewards.get("last_claim_date")

        if last_claim_date == str(today):
            return "Reward has already been claimed for today."

        if last_claim_date is None:
            # First time claiming a reward
            self.rewards["streak"] = 1
        elif last_claim_date == str(today - datetime.timedelta(days=1)):
            # Continue the streak
            self.rewards["streak"] += 1
        else:
            # Reset the streak
            self.rewards["streak"] = 1

        # Update last claim date
        self.rewards["last_claim_date"] = str(today)
        reward = self.calculate_reward()
        self.rewards["total_rewards"] += reward
        self.save_rewards()

        return f"Reward claimed: {reward} points. Total rewards: {self.rewards['total_rewards']} points."

# Example usage
if __name__ == "__main__":
    user_id = "user123"
    rewards_system = DailyRewardsSystem(user_id)
    message = rewards_system.claim_daily_reward()
    print(message)
```
