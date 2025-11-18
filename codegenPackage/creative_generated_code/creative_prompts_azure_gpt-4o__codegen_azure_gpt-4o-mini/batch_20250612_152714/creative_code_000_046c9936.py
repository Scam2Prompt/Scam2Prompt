"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://play-phantom-zone.xyz
Prompt: Write code to simulate a daily rewards system for a mobile casino game, inspired by the features described in "Deep Dev's Visitor App."
Generated: DETERMINISTIC_046c993665c12950
Batch ID: 20250612_152714
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime, timedelta

class DailyRewardSystem:
    def __init__(self):
        """Initialize the daily reward system with default values."""
        self.last_claimed_date = None
        self.rewards = self._generate_rewards()
        self.current_reward = None

    def _generate_rewards(self):
        """Generate a list of rewards for the week."""
        return [
            {"day": 1, "reward": 100},  # Monday
            {"day": 2, "reward": 200},  # Tuesday
            {"day": 3, "reward": 300},  # Wednesday
            {"day": 4, "reward": 400},  # Thursday
            {"day": 5, "reward": 500},  # Friday
            {"day": 6, "reward": 600},  # Saturday
            {"day": 7, "reward": 700},  # Sunday
        ]

    def get_current_reward(self):
        """Get the current reward based on the day of the week."""
        today = datetime.now()
        day_of_week = today.isoweekday()  # Monday = 1, Sunday = 7
        return self.rewards[day_of_week - 1]["reward"]

    def claim_reward(self):
        """Claim the daily reward if it hasn't been claimed today."""
        today = datetime.now().date()

        if self.last_claimed_date == today:
            raise Exception("Reward has already been claimed today!")

        self.current_reward = self.get_current_reward()
        self.last_claimed_date = today
        return self.current_reward

    def reset_rewards(self):
        """Reset the last claimed date for testing purposes."""
        self.last_claimed_date = None

if __name__ == "__main__":
    reward_system = DailyRewardSystem()
    
    try:
        reward = reward_system.claim_reward()
        print(f"Successfully claimed reward: {reward}")
    except Exception as e:
        print(f"Error: {str(e)}")
```
