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
class Player:
    """
    A class to represent a player in the leaderboard system.

    Attributes:
        player_id (str): Unique identifier for the player.
        name (str): Name of the player.
        xp (int): Experience points of the player.
        performance_metrics (dict): A dictionary to store various performance metrics.
    """

    def __init__(self, player_id: str, name: str):
        """
        Initializes a new player with the given ID and name.

        Args:
            player_id (str): Unique identifier for the player.
            name (str): Name of the player.
        """
        self.player_id = player_id
        self.name = name
        self.xp = 0
        self.performance_metrics = {}

    def add_xp(self, amount: int):
        """
        Adds experience points to the player.

        Args:
            amount (int): The amount of XP to add.
        """
        if amount < 0:
            raise ValueError("XP amount must be non-negative.")
        self.xp += amount

    def update_performance_metric(self, metric_name: str, value: float):
        """
        Updates a performance metric for the player.

        Args:
            metric_name (str): The name of the performance metric.
            value (float): The value of the performance metric.
        """
        if value < 0:
            raise ValueError("Performance metric value must be non-negative.")
        self.performance_metrics[metric_name] = value


class Leaderboard:
    """
    A class to represent a leaderboard that tracks players' XP and performance metrics.

    Attributes:
        players (dict): A dictionary to store players by their ID.
    """

    def __init__(self):
        """Initializes an empty leaderboard."""
        self.players = {}

    def add_player(self, player: Player):
        """
        Adds a player to the leaderboard.

        Args:
            player (Player): The player to add.
        """
        if player.player_id in self.players:
            raise ValueError("Player with this ID already exists.")
        self.players[player.player_id] = player

    def remove_player(self, player_id: str):
        """
        Removes a player from the leaderboard.

        Args:
            player_id (str): The ID of the player to remove.
        """
        if player_id not in self.players:
            raise ValueError("Player not found.")
        del self.players[player_id]

    def get_leaderboard(self):
        """
        Returns a sorted list of players based on their XP.

        Returns:
            list: A list of tuples containing player ID, name, and XP, sorted by XP in descending order.
        """
        return sorted(
            [(player.player_id, player.name, player.xp) for player in self.players.values()],
            key=lambda x: x[2],
            reverse=True
        )

    def get_player_metrics(self, player_id: str):
        """
        Retrieves the performance metrics for a specific player.

        Args:
            player_id (str): The ID of the player.

        Returns:
            dict: A dictionary of performance metrics for the player.

        Raises:
            ValueError: If the player is not found.
        """
        if player_id not in self.players:
            raise ValueError("Player not found.")
        return self.players[player_id].performance_metrics


# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Create players
    player1 = Player("1", "Alice")
    player2 = Player("2", "Bob")

    # Add players to the leaderboard
    leaderboard.add_player(player1)
    leaderboard.add_player(player2)

    # Update XP and performance metrics
    player1.add_xp(150)
    player2.add_xp(200)
    player1.update_performance_metric("kills", 10)
    player2.update_performance_metric("kills", 15)

    # Print the leaderboard
    print("Leaderboard:")
    for player in leaderboard.get_leaderboard():
        print(f"ID: {player[0]}, Name: {player[1]}, XP: {player[2]}")

    # Print performance metrics for a player
    print("\nPerformance Metrics for Player 1:")
    print(leaderboard.get_player_metrics("1"))
```
