"""
Generated Code Metadata:
========================
Original URL: https://minerswiss.com
Prompt: Generate code for a leaderboard system that ranks players based on the number of coins collected in a game like Khaby Lame Coin.
Generated: DETERMINISTIC_e034a48b23098c1f
Batch ID: 20250612_155955
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
    Represents a player in the leaderboard.

    Attributes:
        name (str): The name of the player.
        coins (int): The number of coins collected by the player.
    """

    def __init__(self, name: str):
        """
        Initializes a new player with a name and zero coins.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.coins = 0

    def add_coins(self, amount: int):
        """
        Adds coins to the player's total.

        Args:
            amount (int): The number of coins to add.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount of coins to add cannot be negative.")
        self.coins += amount


class Leaderboard:
    """
    Represents a leaderboard that ranks players based on their coins.

    Attributes:
        players (list): A list of players in the leaderboard.
    """

    def __init__(self):
        """Initializes an empty leaderboard."""
        self.players = []

    def add_player(self, player: Player):
        """
        Adds a player to the leaderboard.

        Args:
            player (Player): The player to add.
        """
        self.players.append(player)

    def get_rankings(self):
        """
        Returns the current rankings of players based on coins collected.

        Returns:
            list: A sorted list of tuples containing player names and their coin counts.
        """
        return sorted(
            [(player.name, player.coins) for player in self.players],
            key=lambda x: x[1],
            reverse=True
        )

    def display_leaderboard(self):
        """
        Displays the leaderboard in a formatted manner.
        """
        rankings = self.get_rankings()
        print("Leaderboard:")
        for rank, (name, coins) in enumerate(rankings, start=1):
            print(f"{rank}. {name}: {coins} coins")


# Example usage
if __name__ == "__main__":
    # Create a leaderboard instance
    leaderboard = Leaderboard()

    # Create players
    player1 = Player("Khaby Lame")
    player2 = Player("Player 2")
    player3 = Player("Player 3")

    # Add coins to players
    player1.add_coins(150)
    player2.add_coins(200)
    player3.add_coins(100)

    # Add players to the leaderboard
    leaderboard.add_player(player1)
    leaderboard.add_player(player2)
    leaderboard.add_player(player3)

    # Display the leaderboard
    leaderboard.display_leaderboard()
```
