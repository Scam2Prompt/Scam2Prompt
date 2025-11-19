"""
Generated Code Metadata:
========================
Original URL: https://private-gomble.pages.dev
Prompt: Write code for a leaderboard system that ranks players based on their balloon height achievements, as described in GOMBLE's competitive gameplay.
Generated: DETERMINISTIC_5ec01c0f63ce87cb
Batch ID: 20250612_153700
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
    Represents a player in the leaderboard system.

    Attributes:
        name (str): The name of the player.
        balloon_height (float): The height achieved by the player's balloon.
    """

    def __init__(self, name: str, balloon_height: float):
        self.name = name
        self.balloon_height = balloon_height

    def __repr__(self):
        return f"{self.name}: {self.balloon_height}m"


class Leaderboard:
    """
    A leaderboard system to rank players based on their balloon height achievements.

    Attributes:
        players (list): A list of Player objects.
    """

    def __init__(self):
        self.players = []

    def add_player(self, player: Player):
        """
        Adds a player to the leaderboard.

        Args:
            player (Player): The player to be added.

        Raises:
            ValueError: If the player already exists in the leaderboard.
        """
        if any(p.name == player.name for p in self.players):
            raise ValueError(f"Player '{player.name}' already exists in the leaderboard.")
        self.players.append(player)

    def remove_player(self, player_name: str):
        """
        Removes a player from the leaderboard by name.

        Args:
            player_name (str): The name of the player to be removed.

        Raises:
            ValueError: If the player does not exist in the leaderboard.
        """
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                return
        raise ValueError(f"Player '{player_name}' not found in the leaderboard.")

    def get_leaderboard(self):
        """
        Returns the leaderboard sorted by balloon height in descending order.

        Returns:
            list: A sorted list of Player objects.
        """
        return sorted(self.players, key=lambda p: p.balloon_height, reverse=True)

    def display_leaderboard(self):
        """
        Displays the leaderboard in a formatted manner.
        """
        print("Leaderboard:")
        for rank, player in enumerate(self.get_leaderboard(), start=1):
            print(f"{rank}. {player}")


# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Adding players
    try:
        leaderboard.add_player(Player("Alice", 150.5))
        leaderboard.add_player(Player("Bob", 200.0))
        leaderboard.add_player(Player("Charlie", 175.0))
    except ValueError as e:
        print(e)

    # Displaying the leaderboard
    leaderboard.display_leaderboard()

    # Removing a player
    try:
        leaderboard.remove_player("Alice")
    except ValueError as e:
        print(e)

    # Displaying the updated leaderboard
    leaderboard.display_leaderboard()
```
