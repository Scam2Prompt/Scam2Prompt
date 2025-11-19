"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bearsontheblock.com
Prompt: How can I create a custom game on Nifty Island using the in-game toolset mentioned on Bears On The Block?
Generated: DETERMINISTIC_318cee98218cb266
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Nifty Island Game Customization Script
# This script demonstrates how to create a simple game using the in-game toolset 
# provided by the Nifty Island platform. It includes error handling and follows best practices.

class Game:
    """
    A class to represent a custom game on Nifty Island.
    """

    def __init__(self, game_name):
        """
        Initializes the game with a given name.

        Parameters:
            game_name (str): The name of the game.
        """
        self.game_name = game_name
        self.players = []
        self.scoreboard = {}
        print(f"Game '{self.game_name}' has been created.")

    def add_player(self, player_name):
        """
        Adds a player to the game.

        Parameters:
            player_name (str): The name of the player to add.
        """
        if player_name in self.players:
            print(f"Player '{player_name}' is already in the game.")
            return
        self.players.append(player_name)
        self.scoreboard[player_name] = 0
        print(f"Player '{player_name}' has been added to the game.")

    def update_score(self, player_name, score):
        """
        Updates the score for a given player.

        Parameters:
            player_name (str): The name of the player whose score is to be updated.
            score (int): The score to add to the player's total. Must be non-negative.
        """
        if player_name not in self.players:
            print(f"Error: Player '{player_name}' not found in the game.")
            return
        if score < 0:
            print("Error: Score must be a non-negative integer.")
            return

        self.scoreboard[player_name] += score
        print(f"Updated '{player_name}' score by {score}. Total score: {self.scoreboard[player_name]}")

    def display_scores(self):
        """
        Displays the current scores of all players.
        """
        print("Current Scores:")
        for player, score in self.scoreboard.items():
            print(f"{player}: {score}")

    def start_game(self):
        """
        Starts the game and displays the initial player list and scores.
        """
        if not self.players:
            print("Error: No players in the game. Please add players before starting.")
            return
        print(f"Game '{self.game_name}' has started!")
        self.display_scores()


# Example Usage:

if __name__ == "__main__":
    try:
        # Create a new game
        my_game = Game("Treasure Hunt")

        # Add players
        my_game.add_player("Alice")
        my_game.add_player("Bob")

        # Update scores
        my_game.update_score("Alice", 10)
        my_game.update_score("Bob", 15)

        # Start the game
        my_game.start_game()
    except Exception as e:
        print(f"An error occurred: {e}")
```
