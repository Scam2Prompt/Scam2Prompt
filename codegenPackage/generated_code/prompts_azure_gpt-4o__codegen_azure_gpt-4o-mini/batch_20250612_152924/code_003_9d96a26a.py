"""
Generated Code Metadata:
========================
Original URL: https://mememoguls-en.pages.dev
Prompt: Implement a leaderboard system in Python that tracks and ranks Meme Moguls players based on their earnings and trading activity, using the wealth leaderboard feature described on the site.
Generated: DETERMINISTIC_9d96a26a40996936
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Player:
    """
    Represents a player in the Meme Moguls game.

    Attributes:
        username (str): The player's username.
        earnings (float): The total earnings of the player.
        trades (int): The number of trades made by the player.
    """

    def __init__(self, username: str):
        """
        Initializes a new player with a username, earnings set to 0, and trades set to 0.

        Args:
            username (str): The player's username.
        """
        self.username = username
        self.earnings = 0.0
        self.trades = 0

    def update_earnings(self, amount: float):
        """
        Updates the player's earnings.

        Args:
            amount (float): The amount to add to the player's earnings. Can be negative.

        Raises:
            ValueError: If the amount is not a number.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")
        self.earnings += amount

    def increment_trades(self):
        """Increments the number of trades made by the player."""
        self.trades += 1


class Leaderboard:
    """
    Represents a leaderboard for tracking players' earnings and trading activity.

    Attributes:
        players (dict): A dictionary mapping usernames to Player objects.
    """

    def __init__(self):
        """Initializes an empty leaderboard."""
        self.players = {}

    def add_player(self, username: str):
        """
        Adds a new player to the leaderboard.

        Args:
            username (str): The player's username.

        Raises:
            ValueError: If the username already exists in the leaderboard.
        """
        if username in self.players:
            raise ValueError("Player already exists.")
        self.players[username] = Player(username)

    def update_player(self, username: str, earnings: float):
        """
        Updates the earnings and increments trades for a player.

        Args:
            username (str): The player's username.
            earnings (float): The amount to update the player's earnings.

        Raises:
            KeyError: If the player does not exist in the leaderboard.
        """
        if username not in self.players:
            raise KeyError("Player not found.")
        player = self.players[username]
        player.update_earnings(earnings)
        player.increment_trades()

    def get_leaderboard(self):
        """
        Returns a sorted list of players based on their earnings.

        Returns:
            list: A list of tuples containing (username, earnings, trades) sorted by earnings.
        """
        return sorted(
            [(player.username, player.earnings, player.trades) for player in self.players.values()],
            key=lambda x: x[1],
            reverse=True
        )

    def display_leaderboard(self):
        """Displays the leaderboard in a formatted manner."""
        leaderboard = self.get_leaderboard()
        print("Leaderboard:")
        print("{:<20} {:<15} {:<10}".format("Username", "Earnings", "Trades"))
        print("-" * 45)
        for username, earnings, trades in leaderboard:
            print("{:<20} ${:<14.2f} {:<10}".format(username, earnings, trades))


# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Adding players
    leaderboard.add_player("MemeMaster")
    leaderboard.add_player("FunnyGuy")
    
    # Updating player earnings and trades
    leaderboard.update_player("MemeMaster", 1500.75)
    leaderboard.update_player("FunnyGuy", 2000.50)
    
    # Displaying the leaderboard
    leaderboard.display_leaderboard()
```
