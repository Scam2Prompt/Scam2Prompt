"""
Generated Code Metadata:
========================
Original URL: https://hamstercombat.hk
Prompt: Generate a function to handle daily rewards in a game similar to Hamster Kombat, focusing on user engagement and retention.
Generated: DETERMINISTIC_4e2a0c81e716a026
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, Optional, Tuple

class DailyRewardSystem:
    """
    A class to handle daily rewards for a game, promoting user engagement and retention.
    Features include consecutive login streaks, bonus rewards, and reward scaling.
    """

    def __init__(self, rewards_config: Dict, data_file: str = "user_data.json"):
        """
        Initialize the DailyRewardSystem with rewards configuration and user data storage.

        Args:
            rewards_config (Dict): Configuration for daily rewards and streaks.
                Example:
                {
                    "daily_rewards": [100, 200, 300, 400, 500, 600, 700],
                    "streak_bonus": 0.1,  # 10% bonus for maintaining streak
                    "max_streak": 7        # Max streak days before reset
                }
            data_file (str): Path to the JSON file storing user data.
        """
        self.rewards_config = rewards_config
        self.data_file = data_file
        self.user_data = self._load_user_data()

    def _load_user_data(self) -> Dict:
        """Load user data from JSON file or return empty dict if file doesn't exist."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading user data: {e}")
        return {}

    def _save_user_data(self) -> None:
        """Save user data to JSON file."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.user_data, f, indent=4)
        except IOError as e:
            print(f"Error saving user data: {e}")

    def _get_current_date(self) -> str:
        """Return current date in YYYY-MM-DD format."""
        return datetime.date.today().isoformat()

    def _get_user_record(self, user_id: str) -> Dict:
        """Get or create a user record."""
        if user_id not in self.user_data:
            self.user_data[user_id] = {
                "last_login_date": None,
                "current_streak": 0,
                "total_rewards_claimed": 0
            }
        return self.user_data[user_id]

    def _is_consecutive_day(self, last_date: str, current_date: str) -> bool:
        """Check if the current login is consecutive to the last login."""
        try:
            last = datetime.date.fromisoformat(last_date)
            current = datetime.date.fromisoformat(current_date)
            return (current - last).days == 1
        except (ValueError, TypeError):
            return False

    def claim_daily_reward(self, user_id: str) -> Tuple[bool, Optional[int], int]:
        """
        Attempt to claim the daily reward for a user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            Tuple[bool, Optional[int], int]:
                - bool: Whether the reward was successfully claimed
                - Optional[int]: Amount of reward claimed (None if failed)
                - int: Current streak count
        """
        try:
            current_date = self._get_current_date()
            user_record = self._get_user_record(user_id)
            last_date = user_record["last_login_date"]
            current_streak = user_record["current_streak"]

            # Check if already claimed reward today
            if last_date == current_date:
                return False, None, current_streak

            # Reset streak if not consecutive or first time
            if last_date is None or not self._is_consecutive_day(last_date, current_date):
                current_streak = 0

            # Increment streak (capped at max_streak)
            current_streak = min(current_streak + 1, self.rewards_config["max_streak"])

            # Calculate reward
            reward_day = (current_streak - 1) % len(self.rewards_config["daily_rewards"])
            base_reward = self.rewards_config["daily_rewards"][reward_day]
            bonus_reward = int(base_reward * self.rewards_config["streak_bonus"] * (current_streak - 1))
            total_reward = base_reward + bonus_reward

            # Update user record
            user_record.update({
                "last_login_date": current_date,
                "current_streak": current_streak,
                "total_rewards_claimed": user_record["total_rewards_claimed"] + total_reward
            })

            self._save_user_data()
            return True, total_reward, current_streak

        except Exception as e:
            print(f"Error claiming daily reward: {e}")
            return False, None, 0

    def get_user_stats(self, user_id: str) -> Dict:
        """Get the current statistics for a user."""
        user_record = self._get_user_record(user_id)
        return {
            "last_login_date": user_record["last_login_date"],
            "current_streak": user_record["current_streak"],
            "total_rewards_claimed": user_record["total_rewards_claimed"]
        }
```
