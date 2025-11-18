"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibariumdao.io
Prompt: Create a Python program to manage user rewards and bonuses based on activity levels, similar to the membership benefits described on S666.
Generated: DETERMINISTIC_e3b655f16ae0e989
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class RewardManager:
    """
    A class to manage user rewards and bonuses based on activity levels.
    """
    
    def __init__(self, reward_config=None):
        """
        Initialize the RewardManager with optional reward configuration.
        
        :param reward_config: A dictionary with activity levels and corresponding rewards.
        """
        # Default reward configuration
        self.reward_config = reward_config or {
            "Bronze": {"min_activity": 0, "bonus": 10},
            "Silver": {"min_activity": 100, "bonus": 20},
            "Gold": {"min_activity": 500, "bonus": 50},
            "Platinum": {"min_activity": 1000, "bonus": 100}
        }
        self.users = {}  # Store user data in {user_id: activity_level} format

    def add_user(self, user_id):
        """
        Add a new user with default activity level of 0.
        
        :param user_id: Unique identifier for the user.
        """
        if user_id in self.users:
            raise ValueError(f"User '{user_id}' already exists.")
        self.users[user_id] = 0

    def update_activity(self, user_id, activity_points):
        """
        Update the activity points for a user.
        
        :param user_id: The unique ID of the user.
        :param activity_points: Points to add to the user's activity level.
        """
        if user_id not in self.users:
            raise KeyError(f"User '{user_id}' does not exist.")
        if activity_points < 0:
            raise ValueError("Activity points cannot be negative.")
        self.users[user_id] += activity_points

    def determine_reward_level(self, activity_points):
        """
        Determine the reward level based on activity points.
        
        :param activity_points: The activity points to evaluate.
        :return: The reward level name.
        """
        for level, config in sorted(self.reward_config.items(), key=lambda x: x[1]['min_activity'], reverse=True):
            if activity_points >= config["min_activity"]:
                return level
        return "Unranked"

    def calculate_bonus(self, user_id):
        """
        Calculate the bonus for a user based on their activity level.
        
        :param user_id: The unique ID of the user.
        :return: The bonus amount.
        """
        if user_id not in self.users:
            raise KeyError(f"User '{user_id}' does not exist.")
        activity_points = self.users[user_id]
        reward_level = self.determine_reward_level(activity_points)
        return self.reward_config[reward_level]["bonus"]

    def export_user_data(self, file_path):
        """
        Export user data to a JSON file.
        
        :param file_path: The file path to export the data to.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.users, file, indent=4)
        except IOError as e:
            print(f"Failed to write to file: {e}")
            raise

    def import_user_data(self, file_path):
        """
        Import user data from a JSON file.
        
        :param file_path: The file path to import the data from.
        """
        try:
            with open(file_path, 'r') as file:
                self.users = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Failed to read or parse file: {e}")
            raise

# Example usage
if __name__ == "__main__":
    manager = RewardManager()

    # Adding users
    manager.add_user("user1")
    manager.add_user("user2")

    # Updating activity
    manager.update_activity("user1", 150)
    manager.update_activity("user2", 750)

    # Calculating bonus
    print(f"User1 bonus: {manager.calculate_bonus('user1')}")
    print(f"User2 bonus: {manager.calculate_bonus('user2')}")

    # Exporting and importing data
    manager.export_user_data("user_data.json")
    manager.import_user_data("user_data.json")
```
