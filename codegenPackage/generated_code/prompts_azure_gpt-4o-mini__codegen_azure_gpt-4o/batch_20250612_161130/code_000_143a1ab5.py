"""
Generated Code Metadata:
========================
Original URL: https://raca3-2.pages.dev
Prompt: Write a Python script that utilizes the RACA Game Infra SDK to create a simple game leaderboard for the USM Metaverse.
Generated: DETERMINISTIC_143a1ab57d31acc9
Batch ID: 20250612_161130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Python Script: Game Leaderboard for USM Metaverse using RACA Game Infra SDK

This script creates a simple game leaderboard using the RACA Game Infra SDK.
It allows players to submit their scores and displays the top players in the leaderboard.

Requirements:
- Install the RACA Game Infra SDK (ensure it's properly installed in your environment).
"""

# Import necessary modules from the RACA Game Infra SDK
from raca_game_infra_sdk import Leaderboard, Player, GameInfraError

# Constants
LEADERBOARD_NAME = "USM_Metaverse_Leaderboard"
MAX_LEADERBOARD_ENTRIES = 10  # Maximum number of players to display in the leaderboard

def create_leaderboard():
    """
    Creates a new leaderboard for the USM Metaverse game.
    Returns:
        Leaderboard object if successful, None otherwise.
    """
    try:
        # Initialize the leaderboard
        leaderboard = Leaderboard(name=LEADERBOARD_NAME, max_entries=MAX_LEADERBOARD_ENTRIES)
        print(f"Leaderboard '{LEADERBOARD_NAME}' created successfully.")
        return leaderboard
    except GameInfraError as e:
        print(f"Error creating leaderboard: {e}")
        return None

def add_player_score(leaderboard, player_name, score):
    """
    Adds a player's score to the leaderboard.
    Args:
        leaderboard (Leaderboard): The leaderboard object.
        player_name (str): Name of the player.
        score (int): Player's score.
    """
    try:
        # Create a new player object
        player = Player(name=player_name, score=score)
        # Add the player to the leaderboard
        leaderboard.add_player(player)
        print(f"Player '{player_name}' with score {score} added to the leaderboard.")
    except GameInfraError as e:
        print(f"Error adding player score: {e}")

def display_leaderboard(leaderboard):
    """
    Displays the current leaderboard.
    Args:
        leaderboard (Leaderboard): The leaderboard object.
    """
    try:
        # Fetch the top players from the leaderboard
        top_players = leaderboard.get_top_players()
        print(f"\n--- {LEADERBOARD_NAME} ---")
        print("Rank | Player Name | Score")
        print("--------------------------")
        for rank, player in enumerate(top_players, start=1):
            print(f"{rank}    | {player.name}       | {player.score}")
    except GameInfraError as e:
        print(f"Error displaying leaderboard: {e}")

def main():
    """
    Main function to run the leaderboard script.
    """
    # Create the leaderboard
    leaderboard = create_leaderboard()
    if not leaderboard:
        return

    # Add sample player scores
    add_player_score(leaderboard, "Alice", 1500)
    add_player_score(leaderboard, "Bob", 1200)
    add_player_score(leaderboard, "Charlie", 1800)

    # Display the leaderboard
    display_leaderboard(leaderboard)

if __name__ == "__main__":
    main()
```
