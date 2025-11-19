"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kayen.pages.dev
Prompt: Can you provide an example of how to create a leaderboard for a gaming application that ranks users based on points earned, similar to KAYEN's scoring system?
Generated: DETERMINISTIC_22332cdcf8d5b320
Batch ID: 20250612_155530
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
    Represents a user in the leaderboard.
    """
    def __init__(self, username: str, points: int):
        """
        Initializes a new user with a given username and points.

        :param username: The username of the user.
        :param points: The points earned by the user.
        """
        self.username = username
        self.points = points

    def __repr__(self):
        return f"{self.username}: {self.points} points"

class Leaderboard:
    """
    Manages a leaderboard that ranks users based on their points.
    """
    def __init__(self):
        """
        Initializes an empty leaderboard.
        """
        self.users = []

    def add_user(self, user: User):
        """
        Adds a user to the leaderboard.

        :param user: User object to be added.
        """
        # Check if user already exists to avoid duplicates
        for existing_user in self.users:
            if existing_user.username == user.username:
                print(f"User {user.username} already exists. Updating points.")
                existing_user.points = user.points
                return
        self.users.append(user)

    def get_leaderboard(self):
        """
        Returns the leaderboard sorted by points in descending order.

        :return: List of users sorted by points.
        """
        return sorted(self.users, key=lambda user: user.points, reverse=True)

    def display_leaderboard(self):
        """
        Displays the leaderboard.
        """
        ranked_users = self.get_leaderboard()
        print("Leaderboard:")
        for rank, user in enumerate(ranked_users, start=1):
            print(f"{rank}. {user}")

# Example Usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Adding users to the leaderboard
    leaderboard.add_user(User("Player1", 150))
    leaderboard.add_user(User("Player2", 200))
    leaderboard.add_user(User("Player3", 180))
    
    # Updating an existing user
    leaderboard.add_user(User("Player1", 220))

    # Displaying the leaderboard
    leaderboard.display_leaderboard()
```

In this code, we have implemented a simple leaderboard system that allows adding users, updating their scores, and displaying the leaderboard sorted by points. The comments and docstrings provide clarity on the functionality of each part of the code.
