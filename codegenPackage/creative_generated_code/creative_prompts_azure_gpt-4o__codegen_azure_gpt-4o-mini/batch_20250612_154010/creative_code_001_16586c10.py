"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-flow.web.app
Prompt: Generate code to track user activity in Flow-based apps like Crypto Kitties or NBA Top Shot and assign reward points based on usage.
Generated: DETERMINISTIC_16586c1053c73114
Batch ID: 20250612_154010
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
from collections import defaultdict

# Set up logging for better traceability
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UserActivityTracker:
    def __init__(self):
        # Dictionary to track user activity and reward points
        self.user_activity = defaultdict(list)
        self.reward_points = defaultdict(int)

    def log_activity(self, user_id, activity_type):
        """
        Logs user activity and updates the reward points based on activity type.

        :param user_id: Unique identifier for the user
        :param activity_type: Type of activity performed by the user
        """
        try:
            # Capture current time for the activity log
            activity_time = datetime.now()
            self.user_activity[user_id].append((activity_time, activity_type))
            logging.info(f"Logged activity for user {user_id}: {activity_type} at {activity_time}")

            # Update reward points based on activity type
            self.update_reward_points(user_id, activity_type)
        except Exception as e:
            logging.error(f"Error logging activity for user {user_id}: {e}")

    def update_reward_points(self, user_id, activity_type):
        """
        Updates reward points based on the type of activity.

        :param user_id: Unique identifier for the user
        :param activity_type: Type of activity performed by the user
        """
        try:
            # Define points based on activity types
            activity_points = {
                'view': 1,
                'buy': 5,
                'trade': 3,
                'mint': 10
            }
            # Add points for the activity if the type is recognized
            points = activity_points.get(activity_type, 0)
            self.reward_points[user_id] += points
            
            logging.info(f"User {user_id} earned {points} points for activity: {activity_type}. Total points: {self.reward_points[user_id]}")
        except Exception as e:
            logging.error(f"Error updating reward points for user {user_id}: {e}")

    def get_user_points(self, user_id):
        """
        Retrieves the total reward points for a user.

        :param user_id: Unique identifier for the user
        :return: Total reward points for the user
        """
        return self.reward_points.get(user_id, 0)

    def get_user_activity(self, user_id):
        """
        Retrieves the activity log for a user.

        :param user_id: Unique identifier for the user
        :return: List of activities for the user
        """
        return self.user_activity.get(user_id, [])

    def save_data(self, filename='user_activity.json'):
        """
        Saves user activity and reward points data to a JSON file.

        :param filename: Name of the file to save data
        """
        try:
            data = {
                'user_activity': self.user_activity,
                'reward_points': self.reward_points
            }
            with open(filename, 'w') as f:
                json.dump(data, f, default=str)  # Convert datetime to string for JSON
            logging.info(f"Data saved to {filename}")
        except Exception as e:
            logging.error(f"Error saving data: {e}")

    def load_data(self, filename='user_activity.json'):
        """
        Loads user activity and reward points data from a JSON file.

        :param filename: Name of the file to load data from
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.user_activity = defaultdict(list, {k: v for k, v in data['user_activity'].items()})
                self.reward_points = defaultdict(int, {k: v for k, v in data['reward_points'].items()})
            logging.info(f"Data loaded from {filename}")
        except FileNotFoundError:
            logging.warning(f"No data file found at {filename}. Starting fresh.")
        except json.JSONDecodeError:
            logging.error("Data file is corrupted or improperly formatted.")
        except Exception as e:
            logging.error(f"Error loading data: {e}")

# Example usage
if __name__ == "__main__":
    tracker = UserActivityTracker()
    tracker.log_activity('user_1', 'view')
    tracker.log_activity('user_1', 'buy')
    tracker.save_data()
    tracker.load_data()
    print(f"User 1 Points: {tracker.get_user_points('user_1')}")
    print(f"User 1 Activities: {tracker.get_user_activity('user_1')}")
```
