"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerswiss.com
Prompt: Generate code for a leaderboard system that ranks players based on the number of coins collected in a game like Khaby Lame Coin.
Generated: DETERMINISTIC_e034a48b23098c1f
Batch ID: 20250612_155955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Player:
    """Class representing a player in the leaderboard."""
    
    def __init__(self, name: str):
        """Initialize a player with a name and zero coins.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.coins = 0

    def collect_coins(self, amount: int):
        """Increase the player's coin count.

        Args:
            amount (int): The number of coins to add.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount of coins to collect cannot be negative.")
        self.coins += amount

    def __repr__(self):
        """Return a string representation of the player."""
        return f"Player(name='{self.name}', coins={self.coins})"


class Leaderboard:
    """Class managing a leaderboard of players."""
    
    def __init__(self):
        """Initialize an empty leaderboard."""
        self.players = {}

    def add_player(self, name: str):
        """Add a new player to the leaderboard.

        Args:
            name (str): The name of the player to add.

        Raises:
            ValueError: If the player already exists.
        """
        if name in self.players:
            raise ValueError(f"Player '{name}' already exists.")
        self.players[name] = Player(name)

    def collect_coins(self, name: str, amount: int):
        """Increase the player's coin count by the specified amount.

        Args:
            name (str): The name of the player.
            amount (int): The number of coins to add.

        Raises:
            ValueError: If the player does not exist.
        """
        if name not in self.players:
            raise ValueError(f"Player '{name}' does not exist.")
        self.players[name].collect_coins(amount)

    def get_leaderboard(self):
        """Get a sorted list of players ranked by coins.

        Returns:
            List[Tuple[str, int]]: A sorted list of tuples (player name, coins) in descending order of coins.
        """
        return sorted(self.players.values(), key=lambda player: player.coins, reverse=True)

    def display_leaderboard(self):
        """Display the leaderboard in a formatted manner."""
        leaderboard = self.get_leaderboard()
        print("Leaderboard:")
        for idx, player in enumerate(leaderboard, start=1):
            print(f"{idx}. {player.name} - {player.coins} coins")


if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Adding players
    try:
        leaderboard.add_player("Khaby Lame")
        leaderboard.add_player("Player 2")
        
        # Collecting coins
        leaderboard.collect_coins("Khaby Lame", 100)
        leaderboard.collect_coins("Player 2", 50)

        # Display the leaderboard
        leaderboard.display_leaderboard()
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
