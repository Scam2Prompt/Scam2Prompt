"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tetherusdt.shop
Prompt: Generate code for a slot game leaderboard system that tracks player winnings and displays the top performers for games like "Starlight Princess" and "Aztec Gems."
Generated: DETERMINISTIC_b5677d8fac4b1085
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import heapq
from collections import defaultdict


class Leaderboard:
    """
    A class to manage a slot game leaderboard system.
    Tracks player winnings and displays top performers for specific games.
    """

    def __init__(self, max_entries=10):
        """
        Initializes the leaderboard.

        :param max_entries: Maximum number of top players to display in the leaderboard.
        """
        self.max_entries = max_entries
        self.leaderboard = defaultdict(list)  # Dictionary with game names as keys and a min heap of (winnings, player) tuples as values.

    def record_winning(self, game, player, winnings):
        """
        Records a player's winnings for a specific game.

        :param game: The name of the slot game (e.g., "Starlight Princess", "Aztec Gems").
        :param player: The name of the player.
        :param winnings: The amount won by the player.
        """
        if winnings <= 0:
            raise ValueError("Winnings must be a positive value.")

        # Add the player and winnings to the game's leaderboard.
        heapq.heappush(self.leaderboard[game], (winnings, player))

        # Ensure the leaderboard doesn't exceed max_entries.
        if len(self.leaderboard[game]) > self.max_entries:
            heapq.heappop(self.leaderboard[game])  # Remove the smallest entry.

    def get_top_players(self, game):
        """
        Retrieves the top players for a specific game.

        :param game: The name of the slot game (e.g., "Starlight Princess", "Aztec Gems").
        :return: A list of tuples (player, winnings), sorted by winnings in descending order.
        """
        if game not in self.leaderboard:
            raise ValueError(f"No leaderboard found for game: {game}")

        # Sort by winnings in descending order and return the result.
        return sorted(self.leaderboard[game], key=lambda x: -x[0])

    def display_leaderboard(self, game):
        """
        Displays the leaderboard for a specific game.

        :param game: The name of the slot game.
        """
        try:
            top_players = self.get_top_players(game)
            print(f"Leaderboard for {game}:")
            print(f"{'Rank':<5} {'Player':<20} {'Winnings':<10}")
            print("-" * 35)
            for rank, (winnings, player) in enumerate(top_players, start=1):
                print(f"{rank:<5} {player:<20} ${winnings:<10}")
        except ValueError as e:
            print(e)


# Example usage:
if __name__ == "__main__":
    # Create leaderboard instance.
    leaderboard = Leaderboard(max_entries=5)

    # Record player winnings for "Starlight Princess".
    leaderboard.record_winning("Starlight Princess", "Alice", 1000)
    leaderboard.record_winning("Starlight Princess", "Bob", 1500)
    leaderboard.record_winning("Starlight Princess", "Charlie", 500)
    leaderboard.record_winning("Starlight Princess", "David", 2000)
    leaderboard.record_winning("Starlight Princess", "Eve", 1200)
    leaderboard.record_winning("Starlight Princess", "Frank", 800)  # This should push Charlie off the top 5.

    # Record player winnings for "Aztec Gems".
    leaderboard.record_winning("Aztec Gems", "Alice", 2500)
    leaderboard.record_winning("Aztec Gems", "Bob", 3000)
    leaderboard.record_winning("Aztec Gems", "Charlie", 2000)

    # Display leaderboards.
    leaderboard.display_leaderboard("Starlight Princess")
    leaderboard.display_leaderboard("Aztec Gems")
```
