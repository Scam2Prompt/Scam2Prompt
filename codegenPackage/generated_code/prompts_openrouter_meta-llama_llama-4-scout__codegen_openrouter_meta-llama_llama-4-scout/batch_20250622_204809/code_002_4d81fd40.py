"""
Generated Code Metadata:
========================
Original URL: https://ev-io.now.sh
Prompt: Generate code for a basic leaderboard system that tracks player XP and performance metrics, as seen in ev.io.
Generated: DETERMINISTIC_4d81fd4082eaed15
Batch ID: 20250622_204809
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
    """Represents a player in the leaderboard."""

    def __init__(self, player_id, name):
        """
        Initializes a new player.

        Args:
            player_id (int): Unique ID of the player.
            name (str): Name of the player.
        """
        self.player_id = player_id
        self.name = name
        self.xp = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def add_xp(self, amount):
        """
        Adds experience points to the player.

        Args:
            amount (int): Amount of XP to add.
        """
        if amount < 0:
            raise ValueError("XP amount cannot be negative")
        self.xp += amount

    def update_performance(self, result):
        """
        Updates the player's performance metrics.

        Args:
            result (str): Result of the game (win, loss, or draw).
        """
        if result not in ["win", "loss", "draw"]:
            raise ValueError("Invalid game result")
        if result == "win":
            self.wins += 1
        elif result == "loss":
            self.losses += 1
        else:
            self.draws += 1

    def get_performance_metrics(self):
        """
        Returns the player's performance metrics.

        Returns:
            dict: Dictionary containing wins, losses, and draws.
        """
        return {
            "wins": self.wins,
            "losses": self.losses,
            "draws": self.draws,
        }

    def __repr__(self):
        return f"Player(player_id={self.player_id}, name='{self.name}')"


class Leaderboard:
    """Represents a leaderboard that tracks player XP and performance metrics."""

    def __init__(self):
        """
        Initializes a new leaderboard.
        """
        self.players = {}

    def add_player(self, player):
        """
        Adds a player to the leaderboard.

        Args:
            player (Player): Player to add.
        """
        if player.player_id in self.players:
            raise ValueError("Player already exists in the leaderboard")
        self.players[player.player_id] = player

    def get_player(self, player_id):
        """
        Retrieves a player from the leaderboard.

        Args:
            player_id (int): ID of the player to retrieve.

        Returns:
            Player: Player object if found, otherwise None.
        """
        return self.players.get(player_id)

    def update_player_xp(self, player_id, amount):
        """
        Updates a player's XP.

        Args:
            player_id (int): ID of the player to update.
            amount (int): Amount of XP to add.
        """
        player = self.get_player(player_id)
        if player:
            player.add_xp(amount)
        else:
            raise ValueError("Player not found in the leaderboard")

    def update_player_performance(self, player_id, result):
        """
        Updates a player's performance metrics.

        Args:
            player_id (int): ID of the player to update.
            result (str): Result of the game (win, loss, or draw).
        """
        player = self.get_player(player_id)
        if player:
            player.update_performance(result)
        else:
            raise ValueError("Player not found in the leaderboard")

    def get_leaderboard(self):
        """
        Returns the leaderboard sorted by XP in descending order.

        Returns:
            list: List of players sorted by XP.
        """
        return sorted(self.players.values(), key=lambda x: x.xp, reverse=True)


def main():
    leaderboard = Leaderboard()

    player1 = Player(1, "JohnDoe")
    player2 = Player(2, "JaneDoe")

    leaderboard.add_player(player1)
    leaderboard.add_player(player2)

    leaderboard.update_player_xp(1, 100)
    leaderboard.update_player_xp(2, 50)

    leaderboard.update_player_performance(1, "win")
    leaderboard.update_player_performance(2, "loss")

    print("Leaderboard:")
    for i, player in enumerate(leaderboard.get_leaderboard()):
        print(f"{i+1}. {player.name} - XP: {player.xp}")
        print(f"  Performance: {player.get_performance_metrics()}")


if __name__ == "__main__":
    main()
```
