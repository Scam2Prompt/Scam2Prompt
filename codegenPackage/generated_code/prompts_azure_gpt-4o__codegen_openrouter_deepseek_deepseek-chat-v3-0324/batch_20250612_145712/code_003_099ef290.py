"""
Generated Code Metadata:
========================
Original URL: https://minerswiss.com
Prompt: Implement a leaderboard system in Python that ranks players based on their coin balance, as outlined in the Khaby Lame Coin game. Include functionality for displaying the top players.
Generated: DETERMINISTIC_099ef290bc5387de
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict, Optional

class Leaderboard:
    """
    A leaderboard system that ranks players based on their coin balance.
    """
    
    def __init__(self, file_path: str = "leaderboard.json"):
        """
        Initialize the leaderboard with a JSON file for data persistence.
        
        Args:
            file_path: Path to the JSON file storing leaderboard data.
        """
        self.file_path = file_path
        self.players = self._load_leaderboard()
    
    def _load_leaderboard(self) -> Dict[str, int]:
        """
        Load leaderboard data from JSON file. Create file if it doesn't exist.
        
        Returns:
            Dictionary of player names and their coin balances.
        """
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as f:
                    return json.load(f)
            return {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading leaderboard: {e}")
            return {}
    
    def _save_leaderboard(self) -> None:
        """
        Save the current leaderboard state to the JSON file.
        """
        try:
            with open(self.file_path, 'w') as f:
                json.dump(self.players, f, indent=4)
        except IOError as e:
            print(f"Error saving leaderboard: {e}")
    
    def update_player(self, player_name: str, coins: int) -> None:
        """
        Update a player's coin balance in the leaderboard.
        
        Args:
            player_name: Name of the player to update.
            coins: New coin balance for the player.
        """
        if not isinstance(coins, int) or coins < 0:
            raise ValueError("Coins must be a non-negative integer")
            
        self.players[player_name] = coins
        self._save_leaderboard()
    
    def get_top_players(self, n: int = 10) -> List[Dict[str, int]]:
        """
        Get the top N players ranked by their coin balance.
        
        Args:
            n: Number of top players to return.
            
        Returns:
            List of dictionaries containing player names and their coin balances,
            sorted in descending order.
        """
        if n <= 0:
            return []
            
        sorted_players = sorted(
            self.players.items(),
            key=lambda item: item[1],
            reverse=True
        )
        
        return [{"name": name, "coins": coins} for name, coins in sorted_players[:n]]
    
    def get_player_rank(self, player_name: str) -> Optional[int]:
        """
        Get the rank of a specific player (1-based index).
        
        Args:
            player_name: Name of the player to check.
            
        Returns:
            Rank of the player if found, None otherwise.
        """
        if player_name not in self.players:
            return None
            
        sorted_players = sorted(
            self.players.items(),
            key=lambda item: item[1],
            reverse=True
        )
        
        for rank, (name, _) in enumerate(sorted_players, start=1):
            if name == player_name:
                return rank
                
        return None

# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Update some players
    leaderboard.update_player("Khaby", 1000)
    leaderboard.update_player("Player1", 500)
    leaderboard.update_player("Player2", 750)
    leaderboard.update_player("Player3", 1200)
    
    # Get top players
    top_players = leaderboard.get_top_players(3)
    print("Top 3 Players:")
    for player in top_players:
        print(f"{player['name']}: {player['coins']} coins")
    
    # Get a player's rank
    rank = leaderboard.get_player_rank("Khaby")
    print(f"\nKhaby's rank: {rank}")
```
