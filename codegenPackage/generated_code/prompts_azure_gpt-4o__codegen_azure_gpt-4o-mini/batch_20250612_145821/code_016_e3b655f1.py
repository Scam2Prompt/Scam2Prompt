"""
Generated Code Metadata:
========================
Original URL: https://shibariumdao.io
Prompt: Create a Python program to manage user rewards and bonuses based on activity levels, similar to the membership benefits described on S666.
Generated: DETERMINISTIC_e3b655f16ae0e989
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List

class User:
    """Class to represent a user with rewards and bonuses based on activity levels."""
    
    def __init__(self, user_id: str, name: str):
        """Initialize a new user with an ID and name."""
        self.user_id = user_id
        self.name = name
        self.activity_level = 0  # Activity level starts at 0
        self.rewards = 0  # Initial rewards

    def update_activity(self, activity_points: int):
        """Update the user's activity level and calculate rewards based on activity points."""
        if activity_points < 0:
            raise ValueError("Activity points cannot be negative.")
        
        self.activity_level += activity_points
        self.calculate_rewards()

    def calculate_rewards(self):
        """Calculate rewards based on the current activity level."""
        # Example reward calculation: 1 reward point for every 10 activity points
        self.rewards = self.activity_level // 10

    def to_dict(self) -> Dict:
        """Convert user data to a dictionary for easy serialization."""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "activity_level": self.activity_level,
            "rewards": self.rewards
        }

class RewardManager:
    """Class to manage multiple users and their rewards."""
    
    def __init__(self):
        """Initialize the reward manager with an empty user list."""
        self.users: Dict[str, User] = {}

    def add_user(self, user_id: str, name: str):
        """Add a new user to the reward manager."""
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        
        self.users[user_id] = User(user_id, name)

    def update_user_activity(self, user_id: str, activity_points: int):
        """Update the activity level for a specific user."""
        if user_id not in self.users:
            raise ValueError("User ID not found.")
        
        self.users[user_id].update_activity(activity_points)

    def get_user_rewards(self, user_id: str) -> Dict:
        """Retrieve the rewards information for a specific user."""
        if user_id not in self.users:
            raise ValueError("User ID not found.")
        
        return self.users[user_id].to_dict()

    def save_to_file(self, filename: str):
        """Save all user data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({user_id: user.to_dict() for user_id, user in self.users.items()}, file)
        except IOError as e:
            raise RuntimeError(f"Failed to save data to file: {e}")

    def load_from_file(self, filename: str):
        """Load user data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for user_id, user_data in data.items():
                    user = User(user_data['user_id'], user_data['name'])
                    user.activity_level = user_data['activity_level']
                    user.rewards = user_data['rewards']
                    self.users[user_id] = user
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load data from file: {e}")

# Example usage
if __name__ == "__main__":
    manager = RewardManager()
    
    # Adding users
    manager.add_user("001", "Alice")
    manager.add_user("002", "Bob")
    
    # Updating activity
    manager.update_user_activity("001", 25)  # Alice earns rewards
    manager.update_user_activity("002", 5)   # Bob does not earn rewards yet
    
    # Retrieving rewards
    print(manager.get_user_rewards("001"))  # Should show Alice's rewards
    print(manager.get_user_rewards("002"))  # Should show Bob's rewards
    
    # Saving to file
    manager.save_to_file("user_rewards.json")
    
    # Loading from file
    new_manager = RewardManager()
    new_manager.load_from_file("user_rewards.json")
    print(new_manager.get_user_rewards("001"))  # Should show Alice's rewards from loaded data
```
