"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raca3-2.pages.dev
Prompt: Write a Python script that utilizes the RACA Game Infra SDK to create a simple game leaderboard for the USM Metaverse.
Generated: DETERMINISTIC_143a1ab57d31acc9
Batch ID: 20250612_161130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
game_leaderboard.py

This script uses the RACA Game Infra SDK to create and manage a simple game leaderboard 
for the USM Metaverse. It includes functionality to add player scores, retrieve top players, 
and handle errors appropriately.

Requirements:
- Install the RACA Game Infra SDK: pip install raca-game-infra-sdk

Usage:
- This script acts as a module that can be imported and used to interact with the leaderboard.
"""

from raca_game_infra_sdk import Leaderboard, RacaSDKError

# Constants for the leaderboard configuration
LEADERBOARD_NAME = "USM_Metaverse_Leaderboard"
MAX_PLAYERS = 10  # Maximum number of players to display in the leaderboard

class GameLeaderboard:
    """
    GameLeaderboard class to manage the game's leaderboard using the RACA Game Infra SDK.
    """
    def __init__(self):
        try:
            # Initialize the leaderboard
            self.leaderboard = Leaderboard(name=LEADERBOARD_NAME, max_entries=MAX_PLAYERS)
            print(f"Leaderboard '{LEADERBOARD_NAME}' initialized successfully.")
        except RacaSDKError as e:
            print(f"Error initializing leaderboard: {e}")
            raise

    def add_score(self, player_id, score):
        """
        Add a player's score to the leaderboard.

        Args:
            player_id (str): Unique identifier for the player.
            score (int): Player's score.

        Returns:
            None
        """
        try:
            self.leaderboard.add_entry(player_id=player_id, score=score)
            print(f"Score {score} added for player '{player_id}'.")
        except RacaSDKError as e:
            print(f"Error adding score for player '{player_id}': {e}")

    def get_top_players(self):
        """
        Retrieve the top players from the leaderboard.

        Returns:
            list: A list of top players, each represented as a dictionary 
                  with 'player_id' and 'score' keys.
        """
        try:
            top_players = self.leaderboard.get_entries()
            print("Top players retrieved successfully.")
            return top_players
        except RacaSDKError as e:
            print(f"Error retrieving top players: {e}")
            return []

    def display_leaderboard(self):
        """
        Display the current leaderboard in a formatted way.

        Returns:
            None
        """
        top_players = self.get_top_players()
        if not top_players:
            print("Leaderboard is empty.")
            return

        print(f"Leaderboard: {LEADERBOARD_NAME}")
        print("=" * 30)
        for rank, entry in enumerate(top_players, start=1):
            print(f"Rank {rank}: Player '{entry['player_id']}' with score {entry['score']}")
        print("=" * 30)

# Example usage of the GameLeaderboard class
if __name__ == "__main__":
    try:
        # Initialize the leaderboard
        game_leaderboard = GameLeaderboard()

        # Add scores for players
        game_leaderboard.add_score("player1", 150)
        game_leaderboard.add_score("player2", 200)
        game_leaderboard.add_score("player3", 180)

        # Display the leaderboard
        game_leaderboard.display_leaderboard()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

Note: Replace `raca_game_infra_sdk` with the actual package name of the RACA Game Infra SDK if it's different. Ensure the SDK is installed before running this script.
