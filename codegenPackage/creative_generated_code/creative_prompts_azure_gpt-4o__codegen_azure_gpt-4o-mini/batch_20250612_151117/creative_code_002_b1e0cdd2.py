"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-4kn.pages.dev
Prompt: Generate code for a leaderboard system that ranks users based on the number of taps they contribute in an app inspired by TapSwap.
Generated: DETERMINISTIC_b1e0cdd29f56d2d8
Batch ID: 20250612_151117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """Class representing a user in the TapSwap leaderboard system."""
    
    def __init__(self, username):
        """Initialize a User with a username and a default tap count of 0."""
        self.username = username
        self.tap_count = 0

    def add_taps(self, count):
        """Add taps to the user's total tap count.

        Args:
            count (int): The number of taps to add. Must be a non-negative integer.

        Raises:
            ValueError: If count is negative.
        """
        if count < 0:
            raise ValueError("Tap count must be a non-negative integer.")
        self.tap_count += count

    def __repr__(self):
        """Return a string representation of the user."""
        return f"{self.username}: {self.tap_count} taps"


class Leaderboard:
    """Class representing a leaderboard for the TapSwap app."""

    def __init__(self):
        """Initialize an empty leaderboard."""
        self.users = {}

    def add_user(self, username):
        """Add a new user to the leaderboard.

        Args:
            username (str): The username of the new user.

        Raises:
            ValueError: If the username already exists in the leaderboard.
        """
        if username in self.users:
            raise ValueError("Username already exists in the leaderboard.")
        self.users[username] = User(username)

    def update_taps(self, username, count):
        """Update the tap count for a user.

        Args:
            username (str): The username of the user.
            count (int): The number of taps to add.

        Raises:
            ValueError: If the user does not exist or if count is negative.
        """
        if username not in self.users:
            raise ValueError("User not found in the leaderboard.")
        self.users[username].add_taps(count)

    def get_leaderboard(self):
        """Get the current leaderboard sorted by tap count in descending order.

        Returns:
            list: A list of tuples (username, tap count) sorted by tap count.
        """
        sorted_users = sorted(self.users.values(), key=lambda user: user.tap_count, reverse=True)
        return [(user.username, user.tap_count) for user in sorted_users]

    def display_leaderboard(self):
        """Display the leaderboard in a formatted way."""
        leaderboard = self.get_leaderboard()
        print("Leaderboard:")
        for rank, (username, taps) in enumerate(leaderboard, start=1):
            print(f"{rank}. {username} - {taps} taps")


if __name__ == "__main__":
    # Example usage
    leaderboard = Leaderboard()
    leaderboard.add_user("Alice")
    leaderboard.add_user("Bob")

    leaderboard.update_taps("Alice", 5)
    leaderboard.update_taps("Bob", 3)
    leaderboard.update_taps("Alice", 2)

    leaderboard.display_leaderboard()
```
