"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerswiss.com
Prompt: Implement a leaderboard system in Python that ranks players based on their coin balance, as outlined in the Khaby Lame Coin game. Include functionality for displaying the top players.
Generated: DETERMINISTIC_099ef290bc5387de
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import heapq

class Leaderboard:
    """
    A leaderboard system to rank players based on their coin balance.
    """

    def __init__(self):
        # Dictionary to store player data in the form {player_name: coin_balance}
        self.players = {}
        # Max heap for leaderboard ranking (stored as negative balances for max heap behavior)
        self.leaderboard = []

    def add_player(self, player_name: str, initial_balance: int = 0):
        """
        Adds a new player to the system with an optional initial coin balance.

        :param player_name: Name of the player.
        :param initial_balance: Initial coin balance for the player. Defaults to 0.
        :raises ValueError: If the player already exists.
        """
        if player_name in self.players:
            raise ValueError("Player already exists.")
        
        self.players[player_name] = initial_balance
        # Push the player into the leaderboard heap
        heapq.heappush(self.leaderboard, (-initial_balance, player_name))

    def update_balance(self, player_name: str, new_balance: int):
        """
        Updates the coin balance of an existing player.

        :param player_name: Name of the player.
        :param new_balance: New coin balance for the player.
        :raises ValueError: If the player does not exist.
        """
        if player_name not in self.players:
            raise ValueError("Player does not exist.")
        
        self.players[player_name] = new_balance
        # Rebuild the leaderboard to reflect updated balance
        self._rebuild_leaderboard()

    def display_top_players(self, n: int = 10):
        """
        Displays the top `n` players based on their coin balance.

        :param n: Number of top players to display. Defaults to 10.
        :return: List of tuples [(player_name, coin_balance)] for the top players.
        """
        return [(player_name, -balance) for balance, player_name in heapq.nsmallest(n, self.leaderboard)]

    def _rebuild_leaderboard(self):
        """
        Rebuilds the heap with updated player balances.
        This method is private and is called internally when player balances change.
        """
        self.leaderboard = [(-balance, player_name) for player_name, balance in self.players.items()]
        heapq.heapify(self.leaderboard)


# Example usage:
if __name__ == "__main__":
    # Initialize the leaderboard system
    lb = Leaderboard()
    
    # Add players
    lb.add_player("Alice", 100)
    lb.add_player("Bob", 150)
    lb.add_player("Charlie", 120)

    # Update balance for a player
    lb.update_balance("Alice", 200)

    # Display top players
    print("Top Players:")
    for rank, (player, balance) in enumerate(lb.display_top_players(), start=1):
        print(f"{rank}. {player}: {balance} coins")
```
