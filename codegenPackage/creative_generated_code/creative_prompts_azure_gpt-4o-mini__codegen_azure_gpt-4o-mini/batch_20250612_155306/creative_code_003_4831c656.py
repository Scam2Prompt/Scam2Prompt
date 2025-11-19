"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token2049.vercel.app
Prompt: Provide a code example for implementing player rewards and analytics features in a game developed on the TOKEN 2049 platform.
Generated: DETERMINISTIC_4831c65604d8ee6f
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rewards_and_analytics.py

import json
import logging
from datetime import datetime

# Set up logging for tracking errors and important events
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GamePlayer:
    def __init__(self, player_id):
        self.player_id = player_id
        self.rewards = 0
        self.achievements = []
        self.analytics_data = []

    def add_reward(self, amount):
        """Add rewards to the player."""
        if amount < 0:
            logging.error("Attempted to add a negative reward amount.")
            raise ValueError("Reward amount must be non-negative.")
        self.rewards += amount
        logging.info(f"Added {amount} rewards to player {self.player_id}. Total now: {self.rewards}")

    def unlock_achievement(self, achievement_name):
        """Unlock a new achievement for the player."""
        if achievement_name in self.achievements:
            logging.warning(f"Achievement '{achievement_name}' already unlocked for player {self.player_id}.")
            return
        self.achievements.append(achievement_name)
        logging.info(f"Unlocked achievement '{achievement_name}' for player {self.player_id}.")

    def log_analytics(self, action_type, details):
        """Log an action performed by the player for analytics."""
        timestamp = datetime.now().isoformat()
        analytics_entry = {
            'timestamp': timestamp,
            'action_type': action_type,
            'details': details
        }
        self.analytics_data.append(analytics_entry)
        logging.info(f"Logged action '{action_type}' for player {self.player_id}: {details}")

    def get_rewards(self):
        """Get the current rewards of the player."""
        return self.rewards

    def get_achievements(self):
        """Get a list of achievements unlocked by the player."""
        return self.achievements

    def get_analytics(self):
        """Get the analytics data logged for the player."""
        return self.analytics_data

    def export_data(self, file_path):
        """Export player's rewards, achievements, and analytics data to a JSON file."""
        data = {
            'player_id': self.player_id,
            'rewards': self.rewards,
            'achievements': self.achievements,
            'analytics_data': self.analytics_data
        }
        try:
            with open(file_path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            logging.info(f"Exported data for player {self.player_id} to {file_path}.")
        except IOError as e:
            logging.error(f"Failed to export data for player {self.player_id}: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        player = GamePlayer(player_id="player123")
        player.add_reward(100)
        player.unlock_achievement("First Kill")
        player.log_analytics("Level Up", {"level": 2})
        player.export_data("player123_data.json")
    except Exception as e:
        logging.critical(f"An error occurred: {e}")
```
