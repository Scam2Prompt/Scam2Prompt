"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kayenferno.pages.dev
Prompt: How can I implement a leaderboard system for the KAYEN League that tracks user points and ranks based on mission completions?
Generated: DETERMINISTIC_c7e726c1f1d43b8d
Batch ID: 20250612_155606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """
    Represents a user in the KAYEN League.
    
    Attributes:
        id (int): Unique identifier for the user.
        name (str): Name of the user.
        points (int): Total points accumulated by the user.
    """
    
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.points = 0

    def add_points(self, points):
        """Adds points to the user's total points."""
        if points < 0:
            raise ValueError("Points to add must be non-negative.")
        self.points += points


class Leaderboard:
    """
    Represents a leaderboard for the KAYEN League.
    
    Attributes:
        users (dict): A dictionary of users indexed by user ID.
    """
    
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        """Adds a user to the leaderboard."""
        if user.id in self.users:
            raise ValueError("User already exists in the leaderboard.")
        self.users[user.id] = user

    def record_mission_completion(self, user_id, points):
        """
        Records the completion of a mission for the user and updates their points.
        
        Args:
            user_id (int): The ID of the user.
            points (int): The points earned from the mission completion.
        """
        if user_id not in self.users:
            raise ValueError("User not found in the leaderboard.")
        if points < 0:
            raise ValueError("Points earned must be non-negative.")
        
        self.users[user_id].add_points(points)

    def get_leaderboard(self):
        """Returns a sorted list of users based on their points."""
        # Sort users by points in descending order
        leaderboard = sorted(self.users.values(), key=lambda u: u.points, reverse=True)
        return leaderboard

    def display_leaderboard(self):
        """Displays the leaderboard in a formatted manner."""
        leaderboard = self.get_leaderboard()
        print("KAYEN League Leaderboard:")
        for rank, user in enumerate(leaderboard, start=1):
            print(f"{rank}. {user.name} - {user.points} points")


# Example Usage
if __name__ == "__main__":
    # Initialize the leaderboard
    leaderboard = Leaderboard()

    # Create users
    user1 = User(1, "Alice")
    user2 = User(2, "Bob")
    user3 = User(3, "Charlie")

    # Add users to the leaderboard
    leaderboard.add_user(user1)
    leaderboard.add_user(user2)
    leaderboard.add_user(user3)

    # Record mission completions
    leaderboard.record_mission_completion(1, 10)  # Alice earns 10 points
    leaderboard.record_mission_completion(2, 20)  # Bob earns 20 points
    leaderboard.record_mission_completion(3, 15)  # Charlie earns 15 points

    # Display the current leaderboard
    leaderboard.display_leaderboard()
```
