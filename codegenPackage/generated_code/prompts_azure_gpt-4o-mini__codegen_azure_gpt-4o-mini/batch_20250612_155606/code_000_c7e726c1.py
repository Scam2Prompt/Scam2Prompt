"""
Generated Code Metadata:
========================
Original URL: https://kayenferno.pages.dev
Prompt: How can I implement a leaderboard system for the KAYEN League that tracks user points and ranks based on mission completions?
Generated: DETERMINISTIC_c7e726c1f1d43b8d
Batch ID: 20250612_155606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leaderboard.py

class User:
    """Class representing a user in the KAYEN League."""
    
    def __init__(self, username):
        """
        Initialize a new user with a username and zero points.
        
        Args:
            username (str): The username of the user.
        """
        self.username = username
        self.points = 0

    def add_points(self, points):
        """
        Add points to the user's total points.
        
        Args:
            points (int): The number of points to add.
        
        Raises:
            ValueError: If points are negative.
        """
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.points += points


class Leaderboard:
    """Class to manage the leaderboard for the KAYEN League."""
    
    def __init__(self):
        """Initialize an empty leaderboard."""
        self.users = {}

    def add_user(self, username):
        """
        Add a new user to the leaderboard.
        
        Args:
            username (str): The username of the user.
        
        Raises:
            ValueError: If the username already exists.
        """
        if username in self.users:
            raise ValueError("User already exists.")
        self.users[username] = User(username)

    def update_user_points(self, username, points):
        """
        Update the points for a specific user.
        
        Args:
            username (str): The username of the user.
            points (int): The number of points to add.
        
        Raises:
            ValueError: If the user does not exist.
        """
        if username not in self.users:
            raise ValueError("User does not exist.")
        self.users[username].add_points(points)

    def get_leaderboard(self):
        """
        Get the current leaderboard sorted by points in descending order.
        
        Returns:
            list: A list of tuples containing usernames and their points.
        """
        sorted_users = sorted(self.users.values(), key=lambda user: user.points, reverse=True)
        return [(user.username, user.points) for user in sorted_users]

    def display_leaderboard(self):
        """Display the leaderboard in a formatted manner."""
        leaderboard = self.get_leaderboard()
        print("KAYEN League Leaderboard:")
        for rank, (username, points) in enumerate(leaderboard, start=1):
            print(f"{rank}. {username}: {points} points")


# Example usage
if __name__ == "__main__":
    try:
        leaderboard = Leaderboard()
        leaderboard.add_user("Alice")
        leaderboard.add_user("Bob")
        
        leaderboard.update_user_points("Alice", 10)
        leaderboard.update_user_points("Bob", 15)
        
        leaderboard.display_leaderboard()
        
    except ValueError as e:
        print(f"Error: {e}")
```
