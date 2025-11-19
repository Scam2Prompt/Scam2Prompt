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
# leaderboard.py

class Player:
    """Represents a player in the leaderboard."""

    def __init__(self, player_id, name):
        """
        Initializes a new player.

        Args:
            player_id (int): Unique identifier for the player.
            name (str): Name of the player.
        """
        self.player_id = player_id
        self.name = name
        self.balloon_heights = []

    def add_balloon_height(self, height):
        """
        Adds a new balloon height achievement.

        Args:
            height (int): The height achieved.
        """
        self.balloon_heights.append(height)

    def get_highest_balloon_height(self):
        """
        Returns the highest balloon height achieved.

        Returns:
            int: The highest balloon height.
        """
        if not self.balloon_heights:
            return 0
        return max(self.balloon_heights)


class Leaderboard:
    """Represents a leaderboard that ranks players based on their balloon height achievements."""

    def __init__(self):
        """Initializes a new leaderboard."""
        self.players = {}

    def add_player(self, player_id, name):
        """
        Adds a new player to the leaderboard.

        Args:
            player_id (int): Unique identifier for the player.
            name (str): Name of the player.
        """
        if player_id in self.players:
            raise ValueError("Player already exists")
        self.players[player_id] = Player(player_id, name)

    def add_balloon_height(self, player_id, height):
        """
        Adds a new balloon height achievement for a player.

        Args:
            player_id (int): Unique identifier for the player.
            height (int): The height achieved.

        Raises:
            ValueError: If the player does not exist.
        """
        if player_id not in self.players:
            raise ValueError("Player does not exist")
        self.players[player_id].add_balloon_height(height)

    def get_leaderboard(self):
        """
        Returns the leaderboard ranked by highest balloon height.

        Returns:
            list: A list of tuples containing player information and their highest balloon height.
        """
        leaderboard = []
        for player in self.players.values():
            highest_height = player.get_highest_balloon_height()
            leaderboard.append((player.name, highest_height))
        leaderboard.sort(key=lambda x: x[1], reverse=True)
        return leaderboard


def main():
    leaderboard = Leaderboard()

    # Add players
    leaderboard.add_player(1, "Player 1")
    leaderboard.add_player(2, "Player 2")
    leaderboard.add_player(3, "Player 3")

    # Add balloon heights
    leaderboard.add_balloon_height(1, 100)
    leaderboard.add_balloon_height(1, 150)
    leaderboard.add_balloon_height(2, 120)
    leaderboard.add_balloon_height(3, 180)

    # Get leaderboard
    leaderboard_result = leaderboard.get_leaderboard()

    # Print leaderboard
    print("Leaderboard:")
    for i, (player_name, height) in enumerate(leaderboard_result):
        print(f"{i+1}. {player_name} - {height}")


if __name__ == "__main__":
    main()
```
