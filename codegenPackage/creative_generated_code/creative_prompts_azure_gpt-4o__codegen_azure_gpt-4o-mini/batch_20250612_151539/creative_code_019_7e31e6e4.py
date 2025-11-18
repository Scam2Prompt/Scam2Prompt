"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casinouniswap.com
Prompt: Write code to display RTP percentages for different casino games, including slots, blackjack, and roulette, as explained on Santa Claus Casino.
Generated: DETERMINISTIC_7e31e6e4da477968
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class CasinoGame:
    """
    A class to represent a casino game with its Return to Player (RTP) percentage.
    """

    def __init__(self, name: str, rtp: float):
        """
        Initializes a new CasinoGame instance.

        Args:
            name (str): The name of the casino game.
            rtp (float): The RTP percentage of the game.

        Raises:
            ValueError: If rtp is not between 0 and 100.
        """
        if not (0 <= rtp <= 100):
            raise ValueError("RTP must be between 0 and 100.")
        
        self.name = name
        self.rtp = rtp

    def display_info(self) -> str:
        """
        Returns a string representation of the game and its RTP.

        Returns:
            str: The formatted string with game information.
        """
        return f"{self.name}: {self.rtp}% RTP"


class Casino:
    """
    A class to manage a collection of casino games.
    """

    def __init__(self):
        """Initializes an empty list of casino games."""
        self.games = []

    def add_game(self, game: CasinoGame):
        """
        Adds a new game to the casino.

        Args:
            game (CasinoGame): The game to add.
        """
        self.games.append(game)

    def display_games(self):
        """Displays the RTP percentages for all games in the casino."""
        if not self.games:
            print("No games available.")
            return
        
        print("Casino Games RTP Percentages:")
        for game in self.games:
            print(game.display_info())


if __name__ == "__main__":
    # Initialize the casino
    santa_claus_casino = Casino()

    # Game data with RTP percentages
    game_data = [
        {"name": "Slots", "rtp": 95.0},
        {"name": "Blackjack", "rtp": 99.5},
        {"name": "Roulette", "rtp": 97.3},
    ]

    # Adding games to the casino with error handling
    for data in game_data:
        try:
            game = CasinoGame(name=data["name"], rtp=data["rtp"])
            santa_claus_casino.add_game(game)
        except ValueError as e:
            print(f"Error adding game {data['name']}: {e}")

    # Display the RTP percentages
    santa_claus_casino.display_games()
```
