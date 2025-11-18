"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cosmicrewards.com
Prompt: Generate code for a leaderboard system that tracks user interaction time and rewards accumulation, similar to Cosmic Rewards' "play longer, earn more Stardust" feature.
Generated: DETERMINISTIC_3f5e216401f1c324
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import json
from typing import Dict, List

class User:
    """Class representing a user in the leaderboard."""
    
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.interaction_time = 0  # Total interaction time in seconds
        self.stardust = 0  # Total rewards accumulated

    def add_interaction_time(self, time_spent: int):
        """Add interaction time for the user."""
        if time_spent < 0:
            raise ValueError("Time spent must be non-negative")
        self.interaction_time += time_spent
        self.update_stardust()

    def update_stardust(self):
        """Update stardust based on interaction time."""
        # Assume 1 stardust per minute of interaction time
        self.stardust = self.interaction_time // 60

class Leaderboard:
    """Class representing the leaderboard system."""

    def __init__(self):
        self.users: Dict[str, User] = {}

    def add_user(self, user_id: str):
        """Add a new user to the leaderboard."""
        if user_id in self.users:
            raise ValueError("User ID already exists")
        self.users[user_id] = User(user_id)

    def record_interaction(self, user_id: str, time_spent: int):
        """Record interaction time for a user."""
        if user_id not in self.users:
            raise ValueError("User does not exist")
        self.users[user_id].add_interaction_time(time_spent)

    def get_leaderboard(self) -> List[Dict[str, int]]:
        """Get the current leaderboard sorted by stardust in descending order."""
        leaderboard = sorted(
            self.users.values(),
            key=lambda user: user.stardust,
            reverse=True
        )
        return [
            {"user_id": user.user_id, "stardust": user.stardust}
            for user in leaderboard
        ]

    def save_to_file(self, filename: str):
        """Save the leaderboard data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_leaderboard(), file)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str):
        """Load the leaderboard data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.users = {item['user_id']: User(item['user_id']) for item in data}
                for item in data:
                    self.users[item['user_id']].stardust = item['stardust']
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

# Example usage (this would typically be in a separate module or a main function)
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Add users
    leaderboard.add_user("user_1")
    leaderboard.add_user("user_2")

    # Record interactions
    leaderboard.record_interaction("user_1", 180)  # 3 minutes
    leaderboard.record_interaction("user_2", 120)  # 2 minutes
    
    # Print leaderboard
    print("Current Leaderboard:")
    print(leaderboard.get_leaderboard())

    # Save to file
    leaderboard.save_to_file("leaderboard.json")

    # Load from file
    new_leaderboard = Leaderboard()
    new_leaderboard.load_from_file("leaderboard.json")
    print("Loaded Leaderboard:")
    print(new_leaderboard.get_leaderboard())
```
