"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cosmicrewards.com
Prompt: Write a Python script that tracks user interactions in a gaming app to calculate rewards like Stardust, as described on Cosmic Rewards.
Generated: DETERMINISTIC_edbf8a93de03e2b1
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UserInteractionTracker:
    """
    A class to track user interactions and calculate rewards based on those interactions.
    """

    def __init__(self, user_id):
        """
        Initializes the tracker for a specific user.

        Args:
            user_id (str): The unique identifier for the user.
        """
        self.user_id = user_id
        self.interactions = []
        self.reward_points = 0

    def log_interaction(self, interaction_type):
        """
        Logs a user interaction.

        Args:
            interaction_type (str): Type of interaction (e.g. 'battle', 'exploration', 'trade').
        """
        if interaction_type not in ['battle', 'exploration', 'trade']:
            logging.error("Invalid interaction type: %s", interaction_type)
            raise ValueError("Invalid interaction type. Must be one of: 'battle', 'exploration', 'trade'.")

        interaction = {
            'type': interaction_type,
            'timestamp': datetime.now()
        }
        self.interactions.append(interaction)
        logging.info("Logged interaction: %s for user: %s", interaction, self.user_id)

    def calculate_rewards(self):
        """
        Calculates the rewards based on logged interactions.

        Returns:
            int: The total reward points calculated based on interactions.
        """
        for interaction in self.interactions:
            if interaction['type'] == 'battle':
                self.reward_points += 10
            elif interaction['type'] == 'exploration':
                self.reward_points += 5
            elif interaction['type'] == 'trade':
                self.reward_points += 15

        logging.info("Total reward points calculated: %d for user: %s", self.reward_points, self.user_id)
        return self.reward_points

    def reset_interactions(self):
        """
        Resets all logged interactions and reward points for the user.
        """
        self.interactions = []
        self.reward_points = 0
        logging.info("Reset interactions and reward points for user: %s", self.user_id)

    def save_to_file(self, filename):
        """
        Saves interactions and rewards to a JSON file.

        Args:
            filename (str): The path to the file where data will be saved.
        """
        data = {
            'user_id': self.user_id,
            'interactions': self.interactions,
            'reward_points': self.reward_points
        }
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, default=str)  # Serialize datetime objects as strings
                logging.info("Data saved to file: %s", filename)
        except IOError as e:
            logging.error("Failed to save data to file: %s", e)
            raise

    def load_from_file(self, filename):
        """
        Loads interactions and rewards from a JSON file.

        Args:
            filename (str): The path to the file from which data will be loaded.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.user_id = data['user_id']
                self.interactions = data['interactions']
                self.reward_points = data['reward_points']
                logging.info("Data loaded from file: %s", filename)
        except IOError as e:
            logging.error("Failed to load data from file: %s", e)
            raise
        except json.JSONDecodeError as e:
            logging.error("Failed to decode JSON from file: %s", e)
            raise

# Example usage
if __name__ == "__main__":
    user_tracker = UserInteractionTracker(user_id='user123')

    try:
        user_tracker.log_interaction('battle')
        user_tracker.log_interaction('exploration')
        user_tracker.log_interaction('trade')

        rewards = user_tracker.calculate_rewards()
        print(f"Total rewards for user {user_tracker.user_id}: {rewards}")

        user_tracker.save_to_file('user_data.json')
        user_tracker.reset_interactions()
        user_tracker.load_from_file('user_data.json')

    except Exception as e:
        logging.error("An error occurred: %s", e)
```
