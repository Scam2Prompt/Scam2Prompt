"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://play-phantom-zone.xyz
Prompt: Create a leaderboard system for tracking tournament scores in a mobile arcade game, referencing the competitive gameplay described in "Visitor App."
Generated: DETERMINISTIC_4342f156382f89b8
Batch ID: 20250612_152714
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Player:
    """
    Represents a player in the tournament.

    Attributes:
        name (str): The name of the player.
        score (int): The player's score in the tournament.
    """

    def __init__(self, name: str):
        self.name = name
        self.score = 0

    def update_score(self, points: int):
        """
        Update the player's score with the given points.

        Args:
            points (int): The points to add to the player's score.
        """
        if points < 0:
            raise ValueError("Points must be non-negative.")
        self.score += points

    def __repr__(self):
        return f"{self.name}: {self.score}"


class Leaderboard:
    """
    Represents the leaderboard for the tournament.

    Attributes:
        players (list): A list of Player objects.
    """

    def __init__(self):
        self.players = []

    def add_player(self, player: Player):
        """
        Add a player to the leaderboard.

        Args:
            player (Player): The player to add.

        Raises:
            ValueError: If the player is already in the leaderboard.
        """
        if player in self.players:
            raise ValueError(f"{player.name} is already in the leaderboard.")
        self.players.append(player)

    def update_score(self, player_name: str, points: int):
        """
        Update the score of a player.

        Args:
            player_name (str): The name of the player whose score is to be updated.
            points (int): The points to add to the player's score.

        Raises:
            ValueError: If the player is not found or points are negative.
        """
        player = self.find_player(player_name)
        player.update_score(points)

    def find_player(self, player_name: str) -> Player:
        """
        Find a player by name.

        Args:
            player_name (str): The name of the player to find.

        Returns:
            Player: The found Player object.

        Raises:
            ValueError: If the player is not found.
        """
        for player in self.players:
            if player.name == player_name:
                return player
        raise ValueError(f"Player '{player_name}' not found in leaderboard.")

    def get_leaderboard(self):
        """
        Retrieve the current leaderboard sorted by scores in descending order.

        Returns:
            list: A list of players sorted by score.
        """
        return sorted(self.players, key=lambda x: x.score, reverse=True)

    def display_leaderboard(self):
        """
        Print the leaderboard in a formatted manner.
        """
        print("Leaderboard:")
        for player in self.get_leaderboard():
            print(player)


# Example Usage
if __name__ == "__main__":
    # Create leaderboard
    leaderboard = Leaderboard()

    # Add players
    player1 = Player("Alice")
    player2 = Player("Bob")
    leaderboard.add_player(player1)
    leaderboard.add_player(player2)

    # Update scores
    leaderboard.update_score("Alice", 150)
    leaderboard.update_score("Bob", 100)

    # Display leaderboard
    leaderboard.display_leaderboard()
```
