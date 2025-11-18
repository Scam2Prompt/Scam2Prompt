"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-en.pages.dev
Prompt: Implement a leaderboard system in Python that tracks and ranks Meme Moguls players based on their earnings and trading activity, using the wealth leaderboard feature described on the site.
Generated: DETERMINISTIC_9d96a26a40996936
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Player:
    """Class representing a player in the Meme Moguls game."""
    
    def __init__(self, username):
        """
        Initializes a new player with a username and initial earnings.

        Parameters:
            username (str): The username of the player.
        """
        self.username = username
        self.earnings = 0.0
        self.activity_count = 0

    def update_earnings(self, amount):
        """
        Updates the player's earnings.

        Parameters:
            amount (float): The amount to be added to the player's earnings.
        """
        if amount < 0:
            raise ValueError("Earnings amount cannot be negative.")
        self.earnings += amount

    def increment_activity(self):
        """Increments the player's trading activity count."""
        self.activity_count += 1


class Leaderboard:
    """Class representing the leaderboard for Meme Moguls players."""
    
    def __init__(self):
        """Initializes an empty leaderboard."""
        self.players = {}

    def add_player(self, username):
        """
        Adds a new player to the leaderboard.

        Parameters:
            username (str): The username of the player to be added.
        
        Raises:
            ValueError: If the player already exists.
        """
        if username in self.players:
            raise ValueError(f"Player '{username}' already exists.")
        self.players[username] = Player(username)

    def record_activity(self, username, earnings):
        """
        Records a player's trading activity and updates their earnings.

        Parameters:
            username (str): The username of the player.
            earnings (float): The earnings from the trading activity.

        Raises:
            ValueError: If the player does not exist.
        """
        if username not in self.players:
            raise ValueError(f"Player '{username}' not found.")
        
        player = self.players[username]
        player.increment_activity()
        player.update_earnings(earnings)

    def get_leaderboard(self):
        """
        Returns the leaderboard sorted by earnings.

        Returns:
            List[Tuple[str, float]]: A list of tuples containing usernames and their earnings, sorted by earnings.
        """
        return sorted(
            self.players.items(),
            key=lambda item: item[1].earnings,
            reverse=True
        )

    def display_leaderboard(self):
        """Displays the leaderboard to the console."""
        leaderboard = self.get_leaderboard()
        print("Meme Moguls Leaderboard:")
        for i, (username, player) in enumerate(leaderboard, start=1):
            print(f"{i}. {username}: ${player.earnings:.2f} (Activities: {player.activity_count})")


# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Adding players
    leaderboard.add_player("MemeMaster")
    leaderboard.add_player("FunnyGuy")

    # Recording activities
    leaderboard.record_activity("MemeMaster", 150.0)
    leaderboard.record_activity("FunnyGuy", 200.0)
    leaderboard.record_activity("MemeMaster", 50.0)

    # Displaying the leaderboard
    leaderboard.display_leaderboard()
```
