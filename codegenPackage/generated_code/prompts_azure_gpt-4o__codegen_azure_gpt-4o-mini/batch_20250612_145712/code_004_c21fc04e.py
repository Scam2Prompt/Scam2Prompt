"""
Generated Code Metadata:
========================
Original URL: https://minerinde.com
Prompt: Implement a leaderboard system in Python that tracks the top players based on their coin earnings, as described in the "Die besten Spieler" section of the TG WebApp Euro Verdienen webpage.
Generated: DETERMINISTIC_c21fc04e175e82a8
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Player:
    """Class representing a player in the leaderboard."""
    
    def __init__(self, name: str):
        """
        Initialize a new player with a name and zero coins.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.coins = 0

    def add_coins(self, amount: int):
        """
        Add coins to the player's total.

        Args:
            amount (int): The amount of coins to add.
        
        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount of coins to add must be non-negative.")
        self.coins += amount

    def __repr__(self):
        """Return a string representation of the player."""
        return f"{self.name}: {self.coins} coins"


class Leaderboard:
    """Class representing a leaderboard for tracking players' coin earnings."""
    
    def __init__(self):
        """Initialize an empty leaderboard."""
        self.players = {}

    def add_player(self, name: str):
        """
        Add a new player to the leaderboard.

        Args:
            name (str): The name of the player.
        
        Raises:
            ValueError: If the player already exists.
        """
        if name in self.players:
            raise ValueError("Player already exists.")
        self.players[name] = Player(name)

    def update_coins(self, name: str, amount: int):
        """
        Update the coins for a player.

        Args:
            name (str): The name of the player.
            amount (int): The amount of coins to add.
        
        Raises:
            ValueError: If the player does not exist.
        """
        if name not in self.players:
            raise ValueError("Player not found.")
        self.players[name].add_coins(amount)

    def get_top_players(self, top_n: int = 10):
        """
        Get the top players sorted by their coin earnings.

        Args:
            top_n (int): The number of top players to return.
        
        Returns:
            List[Player]: A list of the top players.
        """
        sorted_players = sorted(self.players.values(), key=lambda p: p.coins, reverse=True)
        return sorted_players[:top_n]

    def __repr__(self):
        """Return a string representation of the leaderboard."""
        return "\n".join(str(player) for player in self.get_top_players())


# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Adding players
    leaderboard.add_player("Alice")
    leaderboard.add_player("Bob")
    leaderboard.add_player("Charlie")

    # Updating coins
    leaderboard.update_coins("Alice", 150)
    leaderboard.update_coins("Bob", 200)
    leaderboard.update_coins("Charlie", 100)

    # Displaying the leaderboard
    print("Current Leaderboard:")
    print(leaderboard)
```
