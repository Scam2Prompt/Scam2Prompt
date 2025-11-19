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

class DailyRewardsSystem:
    def __init__(self, max_streak=7):
        """
        Initialize the DailyRewardsSystem.

        :param max_streak: Maximum reward streak days (default is 7).
        """
        self.max_streak = max_streak
        self.current_streak = 0
        self.last_claim_date = None
        self.rewards = self._generate_rewards()

    def _generate_rewards(self):
        """
        Generate rewards based on the streak days.

        :return: A dictionary mapping streak days to rewards.
        """
        return {
            1: "50 coins",
            2: "100 coins",
            3: "150 coins",
            4: "1 rare item",
            5: "200 coins",
            6: "1 epic item",
            7: "500 coins + 1 legendary item"
        }

    def _get_todays_date(self):
        """
        Get today's date.

        :return: A datetime.date object representing today's date.
        """
        return datetime.date.today()

    def claim_reward(self):
        """
        Claim the daily reward.

        :return: A string indicating the reward or an error message.
        """
        today = self._get_todays_date()

        # Error handling: Check if the user is claiming twice on the same day
        if self.last_claim_date == today:
            return "Error: You have already claimed your reward for today."

        # Check if the user broke their streak (by skipping a day)
        if self.last_claim_date and (today - self.last_claim_date).days > 1:
            self.current_streak = 0  # Reset streak due to inactivity

        # Update streak and last claim date
        self.current_streak = min(self.current_streak + 1, self.max_streak)
        self.last_claim_date = today

        # Fetch the reward for the current streak
        reward = self.rewards[self.current_streak]
        return f"Congratulations! You have claimed your reward: {reward}"

    def get_streak_status(self):
        """
        Get the current streak status.

        :return: A string indicating the current streak and last claim date.
        """
        streak_info = f"Current Streak: {self.current_streak}/{self.max_streak}"
        last_claim_info = f"Last Claim Date: {self.last_claim_date}" if self.last_claim_date else "No rewards claimed yet."
        return f"{streak_info}\n{last_claim_info}"


# Example usage
if __name__ == "__main__":
    rewards_system = DailyRewardsSystem()

    # Simulating reward claims
    print(rewards_system.claim_reward())  # First claim
    print(rewards_system.get_streak_status())

    # Simulating another claim on the same day (should throw an error)
    print(rewards_system.claim_reward())

    # Simulating a claim on a new day (advance the date manually for testing)
    rewards_system.last_claim_date -= datetime.timedelta(days=1)  # Simulate a new day
    print(rewards_system.claim_reward())
```
