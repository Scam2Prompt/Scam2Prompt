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
import os
from typing import List, Dict, Optional
from raca_sdk import RacaClient, RacaException

class USMLeaderboard:
    """
    A simple leaderboard implementation for the USM Metaverse using RACA Game Infra SDK.
    """
    
    def __init__(self, game_id: str, api_key: str):
        """
        Initialize the leaderboard with game credentials.
        
        Args:
            game_id: The unique identifier for the game
            api_key: The API key for authentication
        """
        try:
            self.client = RacaClient(game_id=game_id, api_key=api_key)
            self.leaderboard_name = "usm_metaverse_leaderboard"
        except RacaException as e:
            raise RuntimeError(f"Failed to initialize RACA client: {str(e)}")

    def add_score(self, player_id: str, score: float) -> bool:
        """
        Add or update a player's score in the leaderboard.
        
        Args:
            player_id: Unique identifier for the player
            score: The score to be recorded
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.client.update_leaderboard(
                leaderboard_name=self.leaderboard_name,
                player_id=player_id,
                score=score
            )
            return True
        except RacaException as e:
            print(f"Error updating score: {str(e)}")
            return False

    def get_top_players(self, limit: int = 10) -> List[Dict[str, float]]:
        """
        Retrieve the top players from the leaderboard.
        
        Args:
            limit: Number of top players to retrieve (default: 10)
            
        Returns:
            List of dictionaries containing player_id and score
        """
        try:
            leaderboard = self.client.get_leaderboard(
                leaderboard_name=self.leaderboard_name,
                limit=limit
            )
            return [
                {"player_id": entry.player_id, "score": entry.score}
                for entry in leaderboard.entries
            ]
        except RacaException as e:
            print(f"Error fetching leaderboard: {str(e)}")
            return []

    def get_player_rank(self, player_id: str) -> Optional[int]:
        """
        Get a player's current rank in the leaderboard.
        
        Args:
            player_id: The player to look up
            
        Returns:
            int: The player's rank if found, None otherwise
        """
        try:
            rank = self.client.get_player_rank(
                leaderboard_name=self.leaderboard_name,
                player_id=player_id
            )
            return rank
        except RacaException as e:
            print(f"Error fetching player rank: {str(e)}")
            return None

def main():
    # Load configuration from environment variables
    game_id = os.getenv("RACA_GAME_ID")
    api_key = os.getenv("RACA_API_KEY")
    
    if not game_id or not api_key:
        raise ValueError("Missing RACA_GAME_ID or RACA_API_KEY environment variables")
    
    # Initialize leaderboard
    leaderboard = USMLeaderboard(game_id=game_id, api_key=api_key)
    
    # Example usage
    leaderboard.add_score("player1", 100.5)
    leaderboard.add_score("player2", 200.0)
    leaderboard.add_score("player3", 150.75)
    
    print("Top Players:")
    for player in leaderboard.get_top_players(3):
        print(f"{player['player_id']}: {player['score']}")
    
    player_rank = leaderboard.get_player_rank("player1")
    if player_rank is not None:
        print(f"Player1 rank: {player_rank}")

if __name__ == "__main__":
    main()
```
