"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftcap.pages.dev
Prompt: Suggest tools or frameworks for tracking rewards points earned through NFT collateralized loans, similar to the "Rewards" system on NFTfi.com.
Generated: DETERMINISTIC_002b7062a1e60f26
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rewards_tracker.py

import json
import logging
from typing import List, Dict

# Configure logging for better debugging and error tracking.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RewardsTracker:
    def __init__(self, db_file: str):
        """
        Initializes the RewardsTracker with a path to a database file.

        :param db_file: Path to the JSON file used to store rewards data.
        """
        self.db_file = db_file
        self.rewards_data = self.load_rewards_data()

    def load_rewards_data(self) -> Dict:
        """
        Loads rewards data from the specified JSON file.

        :returns: Dictionary containing rewards data or an empty dictionary if the file does not exist.
        """
        try:
            with open(self.db_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.warning("Database file not found, initializing with empty data.")
            return {}
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON from the database file: {e}")
            return {}

    def save_rewards_data(self):
        """
        Saves the current rewards data to the specified JSON file.
        """
        try:
            with open(self.db_file, 'w') as file:
                json.dump(self.rewards_data, file, indent=4)
        except IOError as e:
            logging.error(f"Failed to write to the database file: {e}")

    def add_reward(self, user_id: str, points: int):
        """
        Adds reward points for a specific user.

        :param user_id: Unique identifier for the user.
        :param points: Number of reward points to add.
        """
        if user_id not in self.rewards_data:
            self.rewards_data[user_id] = 0
        self.rewards_data[user_id] += points
        logging.info(f"Added {points} points for user {user_id}. Total points: {self.rewards_data[user_id]}")
        self.save_rewards_data()

    def get_rewards(self, user_id: str) -> int:
        """
        Retrieves the total reward points for a specific user.

        :param user_id: Unique identifier for the user.
        :returns: Total reward points for the user, or zero if the user does not exist.
        """
        return self.rewards_data.get(user_id, 0)

    def get_all_rewards(self) -> List[Dict[str, int]]:
        """
        Retrieves all users and their reward points.

        :returns: List of dictionaries with user IDs and their respective reward points.
        """
        return [{"user_id": user_id, "points": points} for user_id, points in self.rewards_data.items()]

# Example usage:
if __name__ == "__main__":
    tracker = RewardsTracker('rewards_data.json')

    # Adding rewards for demonstration.
    tracker.add_reward("user123", 50)
    tracker.add_reward("user456", 75)

    # Fetching rewards.
    print(tracker.get_rewards("user123"))
    print(tracker.get_all_rewards())
```
