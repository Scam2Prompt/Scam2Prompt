"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-st.pages.dev
Prompt: Explain how to implement a leaderboard system for the Kangamoon community, focusing on tracking user participation in challenges and rewards.
Generated: DETERMINISTIC_bdb4e847b97394c1
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Tuple
import json

class User:
    """Represents a user in the Kangamoon community."""
    
    def __init__(self, user_id: str, username: str):
        self.user_id = user_id
        self.username = username
        self.participation_count = 0
        self.rewards = 0

    def participate(self) -> None:
        """Increments the participation count for the user."""
        self.participation_count += 1

    def add_reward(self, points: int) -> None:
        """Adds rewards to the user."""
        if points < 0:
            raise ValueError("Reward points must be non-negative.")
        self.rewards += points


class Leaderboard:
    """Tracks user participation and rewards in challenges."""

    def __init__(self):
        self.users: Dict[str, User] = {}

    def add_user(self, user_id: str, username: str) -> None:
        """Adds a new user to the leaderboard."""
        if user_id in self.users:
            raise ValueError("User already exists.")
        self.users[user_id] = User(user_id, username)

    def record_participation(self, user_id: str) -> None:
        """Records a user's participation in a challenge."""
        user = self.users.get(user_id)
        if not user:
            raise ValueError("User not found.")
        user.participate()

    def reward_user(self, user_id: str, points: int) -> None:
        """Awards points to a user for participation."""
        user = self.users.get(user_id)
        if not user:
            raise ValueError("User not found.")
        user.add_reward(points)

    def get_leaderboard(self) -> List[Tuple[str, str, int, int]]:
        """Returns a sorted leaderboard based on participation count and rewards."""
        sorted_leaderboard = sorted(
            self.users.values(),
            key=lambda user: (-user.participation_count, -user.rewards)
        )
        return [
            (user.user_id, user.username, user.participation_count, user.rewards)
            for user in sorted_leaderboard
        ]

    def save_to_file(self, filename: str) -> None:
        """Saves the leaderboard data to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.get_leaderboard(), f, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save leaderboard to {filename}: {str(e)}")

    def load_from_file(self, filename: str) -> None:
        """Loads the leaderboard data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                leaderboard_data = json.load(f)
                for user_data in leaderboard_data:
                    user_id, username, participation_count, rewards = user_data
                    user = self.add_user(user_id, username)
                    user.participation_count = participation_count
                    user.rewards = rewards
        except IOError as e:
            raise RuntimeError(f"Failed to load leaderboard from {filename}: {str(e)}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in {filename}: {str(e)}")

# Example usage:
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Adding users
    leaderboard.add_user("1", "Alice")
    leaderboard.add_user("2", "Bob")
    
    # Recording participation
    leaderboard.record_participation("1")
    leaderboard.record_participation("2")
    leaderboard.record_participation("1")
    
    # Rewarding users
    leaderboard.reward_user("1", 10)
    leaderboard.reward_user("2", 5)

    # Displaying leaderboard
    print(leaderboard.get_leaderboard())
    
    # Saving to a file
    leaderboard.save_to_file("leaderboard.json")

    # Loading from a file
    new_leaderboard = Leaderboard()
    new_leaderboard.load_from_file("leaderboard.json")
    print(new_leaderboard.get_leaderboard())
```
