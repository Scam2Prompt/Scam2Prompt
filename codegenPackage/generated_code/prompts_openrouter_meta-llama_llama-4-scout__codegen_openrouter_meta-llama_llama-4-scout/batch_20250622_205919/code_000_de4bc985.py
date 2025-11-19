"""
Generated Code Metadata:
========================
Original URL: https://memefi-club.pages.dev
Prompt: "Write a Python script to implement a leaderboard system for a meme-themed game like MemeFi, where players can earn MemeFi coins and climb the ranks."
Generated: DETERMINISTIC_de4bc985bfcbf787
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leaderboard.py

class Player:
    """Represents a player in the MemeFi game."""

    def __init__(self, player_id, name):
        """
        Initializes a Player object.

        Args:
            player_id (int): Unique identifier for the player.
            name (str): Name of the player.
        """
        self.player_id = player_id
        self.name = name
        self.meme_fi_coins = 0
        self.rank = None

    def earn_coins(self, coins):
        """
        Adds MemeFi coins to the player's balance.

        Args:
            coins (int): Number of coins to add.

        Raises:
            ValueError: If coins is negative.
        """
        if coins < 0:
            raise ValueError("Coins cannot be negative")
        self.meme_fi_coins += coins


class Leaderboard:
    """Manages a leaderboard for the MemeFi game."""

    def __init__(self):
        """
        Initializes a Leaderboard object.
        """
        self.players = {}
        self.ranks = {}

    def add_player(self, player):
        """
        Adds a player to the leaderboard.

        Args:
            player (Player): Player object to add.

        Raises:
            ValueError: If player is already in the leaderboard.
        """
        if player.player_id in self.players:
            raise ValueError("Player already exists in the leaderboard")
        self.players[player.player_id] = player
        self.update_ranks()

    def update_ranks(self):
        """
        Updates the ranks of all players based on their MemeFi coins.
        """
        sorted_players = sorted(self.players.values(), key=lambda p: p.meme_fi_coins, reverse=True)
        for i, player in enumerate(sorted_players):
            player.rank = i + 1
            self.ranks[player.player_id] = player.rank

    def earn_coins(self, player_id, coins):
        """
        Adds MemeFi coins to a player's balance and updates the ranks.

        Args:
            player_id (int): ID of the player.
            coins (int): Number of coins to add.

        Raises:
            ValueError: If player does not exist in the leaderboard.
        """
        if player_id not in self.players:
            raise ValueError("Player does not exist in the leaderboard")
        self.players[player_id].earn_coins(coins)
        self.update_ranks()

    def get_player_rank(self, player_id):
        """
        Gets a player's rank.

        Args:
            player_id (int): ID of the player.

        Returns:
            int: Rank of the player.

        Raises:
            ValueError: If player does not exist in the leaderboard.
        """
        if player_id not in self.ranks:
            raise ValueError("Player does not exist in the leaderboard")
        return self.ranks[player_id]

    def get_leaderboard(self):
        """
        Gets the current leaderboard.

        Returns:
            list: List of tuples containing player information and rank.
        """
        leaderboard = []
        for player in self.players.values():
            leaderboard.append((player.name, player.meme_fi_coins, player.rank))
        return sorted(leaderboard, key=lambda x: x[2])


def main():
    leaderboard = Leaderboard()

    # Create players
    player1 = Player(1, "JohnDoe")
    player2 = Player(2, "JaneDoe")

    # Add players to leaderboard
    leaderboard.add_player(player1)
    leaderboard.add_player(player2)

    # Earn coins
    leaderboard.earn_coins(1, 1000)
    leaderboard.earn_coins(2, 500)

    # Get player ranks
    print(f"Player 1 rank: {leaderboard.get_player_rank(1)}")
    print(f"Player 2 rank: {leaderboard.get_player_rank(2)}")

    # Get leaderboard
    print("Leaderboard:")
    for player in leaderboard.get_leaderboard():
        print(f"Name: {player[0]}, Coins: {player[1]}, Rank: {player[2]}")


if __name__ == "__main__":
    main()
```
