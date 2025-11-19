"""
Generated Code Metadata:
========================
Original URL: https://minerswiss.com
Prompt: Implement a leaderboard system in Python that ranks players based on their coin balance, as outlined in the Khaby Lame Coin game. Include functionality for displaying the top players.
Generated: DETERMINISTIC_099ef290bc5387de
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
    
    def __init__(self, name: str, coins: int = 0):
        """
        Initialize a new player with a name and an optional coin balance.
        
        :param name: The name of the player.
        :param coins: The initial coin balance of the player (default is 0).
        """
        self.name = name
        self.coins = coins

    def __repr__(self):
        """Return a string representation of the player."""
        return f"{self.name}: {self.coins} coins"


class Leaderboard:
    """Class to manage the leaderboard of players."""
    
    def __init__(self):
        """Initialize an empty leaderboard."""
        self.players = []

    def add_player(self, player: Player):
        """
        Add a player to the leaderboard.
        
        :param player: An instance of Player to be added.
        """
        if not isinstance(player, Player):
            raise ValueError("Only Player instances can be added to the leaderboard.")
        self.players.append(player)

    def update_coins(self, player_name: str, coins: int):
        """
        Update the coin balance of a player.
        
        :param player_name: The name of the player whose coins will be updated.
        :param coins: The new coin balance for the player.
        """
        for player in self.players:
            if player.name == player_name:
                player.coins = coins
                return
        raise ValueError(f"Player '{player_name}' not found in the leaderboard.")

    def get_top_players(self, top_n: int = 10):
        """
        Retrieve the top players sorted by their coin balance.
        
        :param top_n: The number of top players to retrieve (default is 10).
        :return: A list of the top players.
        """
        if top_n < 1:
            raise ValueError("top_n must be at least 1.")
        return sorted(self.players, key=lambda p: p.coins, reverse=True)[:top_n]

    def display_leaderboard(self, top_n: int = 10):
        """
        Display the leaderboard of top players.
        
        :param top_n: The number of top players to display (default is 10).
        """
        top_players = self.get_top_players(top_n)
        print("Leaderboard:")
        for rank, player in enumerate(top_players, start=1):
            print(f"{rank}. {player}")


# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Adding players
    leaderboard.add_player(Player("Alice", 150))
    leaderboard.add_player(Player("Bob", 200))
    leaderboard.add_player(Player("Charlie", 100))
    
    # Updating player coins
    leaderboard.update_coins("Alice", 250)
    
    # Displaying the leaderboard
    leaderboard.display_leaderboard()
```
