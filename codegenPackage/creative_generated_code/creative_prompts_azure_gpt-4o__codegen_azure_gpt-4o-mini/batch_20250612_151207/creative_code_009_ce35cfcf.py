"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ggew.pages.dev
Prompt: Generate code for a leaderboard system that tracks user activity and rewards them with points, as described in Blum's rewarding crypto experience.
Generated: DETERMINISTIC_ce35cfcf5905047d
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, List, Optional

class User:
    """Class to represent a user in the leaderboard."""
    
    def __init__(self, username: str):
        self.username = username
        self.points = 0
        
    def add_points(self, points: int):
        """Add points to the user's total points."""
        if points < 0:
            raise ValueError("Points to add cannot be negative.")
        self.points += points

    def __repr__(self):
        return f"User(username={self.username}, points={self.points})"


class Leaderboard:
    """Class to manage the leaderboard and user activity."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        
    def add_user(self, username: str):
        """Add a new user to the leaderboard."""
        if username in self.users:
            raise ValueError("User already exists.")
        self.users[username] = User(username)

    def reward_user(self, username: str, points: int):
        """Reward points to a user."""
        user = self.get_user(username)
        if user is None:
            raise ValueError("User not found.")
        user.add_points(points)

    def get_user(self, username: str) -> Optional[User]:
        """Retrieve a user from the leaderboard."""
        return self.users.get(username)

    def get_leaderboard(self) -> List[User]:
        """Get the leaderboard sorted by points in descending order."""
        return sorted(self.users.values(), key=lambda u: u.points, reverse=True)

    def save_to_file(self, filename: str):
        """Save the leaderboard to a JSON file."""
        with open(filename, 'w') as file:
            json.dump({username: user.points for username, user in self.users.items()}, file)

    def load_from_file(self, filename: str):
        """Load the leaderboard from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for username, points in data.items():
                    self.add_user(username)
                    self.reward_user(username, points)
        except FileNotFoundError:
            print("File not found. Starting with an empty leaderboard.")
        except json.JSONDecodeError:
            print("Error decoding JSON file. Starting with an empty leaderboard.")


# Example usage:
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    try:
        leaderboard.add_user("Alice")
        leaderboard.add_user("Bob")
        leaderboard.reward_user("Alice", 10)
        leaderboard.reward_user("Bob", 15)

        print("Current leaderboard:")
        for user in leaderboard.get_leaderboard():
            print(user)

        leaderboard.save_to_file("leaderboard.json")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
