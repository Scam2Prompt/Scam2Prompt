"""
Generated Code Metadata:
========================
Original URL: https://w-4kn.pages.dev
Prompt: Generate code for a leaderboard system that ranks users based on the number of taps they contribute in an app inspired by TapSwap.
Generated: DETERMINISTIC_b1e0cdd29f56d2d8
Batch ID: 20250612_151117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class User:
    """Class representing a user in the leaderboard."""
    
    def __init__(self, username):
        """
        Initialize a new user with a username and a tap count.
        
        Args:
            username (str): The username of the user.
        """
        self.username = username
        self.taps = 0

    def add_taps(self, count):
        """
        Increment the user's tap count by a specified amount.
        
        Args:
            count (int): The number of taps to add.
        
        Raises:
            ValueError: If count is not a positive integer.
        """
        if not isinstance(count, int) or count < 0:
            raise ValueError("Count must be a non-negative integer.")
        self.taps += count


class Leaderboard:
    """Class representing a leaderboard for ranking users based on taps."""
    
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

    def record_taps(self, username, count):
        """
        Record taps for a user.
        
        Args:
            username (str): The username of the user.
            count (int): The number of taps to record.
        
        Raises:
            ValueError: If the user does not exist or count is invalid.
        """
        if username not in self.users:
            raise ValueError("User does not exist.")
        self.users[username].add_taps(count)

    def get_leaderboard(self):
        """
        Get the leaderboard sorted by the number of taps in descending order.
        
        Returns:
            list: A list of tuples containing usernames and their tap counts.
        """
        sorted_users = sorted(self.users.values(), key=lambda user: user.taps, reverse=True)
        return [(user.username, user.taps) for user in sorted_users]

    def display_leaderboard(self):
        """Display the leaderboard in a readable format."""
        leaderboard = self.get_leaderboard()
        print("Leaderboard:")
        for rank, (username, taps) in enumerate(leaderboard, start=1):
            print(f"{rank}. {username}: {taps} taps")


# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Adding users
    try:
        leaderboard.add_user("Alice")
        leaderboard.add_user("Bob")
        
        # Recording taps
        leaderboard.record_taps("Alice", 5)
        leaderboard.record_taps("Bob", 3)
        leaderboard.record_taps("Alice", 2)
        
        # Displaying the leaderboard
        leaderboard.display_leaderboard()
    except ValueError as e:
        print(f"Error: {e}")
```
