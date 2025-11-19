"""
Generated Code Metadata:
========================
Original URL: https://stellar-neurongate.xyz
Prompt: Write code to implement a leaderboard system for casino games, inspired by the community-driven features of Zeus Fortune.
Generated: DETERMINISTIC_7d6e2901842c302e
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Optional
import uuid
import os
from abc import ABC, abstractmethod

# Exception classes
class LeaderboardError(Exception):
    """Base exception for leaderboard-related errors."""
    pass

class PlayerNotFoundError(LeaderboardError):
    """Raised when a player is not found in the leaderboard."""
    pass

class InvalidScoreError(LeaderboardError):
    """Raised when an invalid score is provided."""
    pass

# Abstract base class for storage
class LeaderboardStorage(ABC):
    @abstractmethod
    def save_leaderboard(self, leaderboard: List[Dict]) -> None:
        pass
    
    @abstractmethod
    def load_leaderboard(self) -> List[Dict]:
        pass

# JSON file-based storage implementation
class JSONLeaderboardStorage(LeaderboardStorage):
    def __init__(self, file_path: str = 'leaderboard.json'):
        self.file_path = file_path
        self._ensure_file_exists()
    
    def _ensure_file_exists(self) -> None:
        """Ensure the storage file exists, create if it doesn't."""
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)
    
    def save_leaderboard(self, leaderboard: List[Dict]) -> None:
        """Save leaderboard data to JSON file."""
        try:
            with open(self.file_path, 'w') as f:
                json.dump(leaderboard, f, indent=2)
        except (IOError, json.JSONDecodeError) as e:
            raise LeaderboardError(f"Failed to save leaderboard: {str(e)}")
    
    def load_leaderboard(self) -> List[Dict]:
        """Load leaderboard data from JSON file."""
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            raise LeaderboardError(f"Failed to load leaderboard: {str(e)}")

# Leaderboard service
class LeaderboardService:
    def __init__(self, storage: LeaderboardStorage):
        self.storage = storage
    
    def add_or_update_player(self, player_id: str, player_name: str, score: int, game_type: str) -> None:
        """Add or update a player's score in the leaderboard."""
        if not isinstance(score, int) or score < 0:
            raise InvalidScoreError("Score must be a non-negative integer")
        
        leaderboard = self.storage.load_leaderboard()
        current_time = datetime.utcnow().isoformat()
        
        # Check if player exists
        player_found = False
        for entry in leaderboard:
            if entry['player_id'] == player_id and entry['game_type'] == game_type:
                entry['score'] = score
                entry['last_updated'] = current_time
                player_found = True
                break
        
        if not player_found:
            leaderboard.append({
                'player_id': player_id,
                'player_name': player_name,
                'score': score,
                'game_type': game_type,
                'last_updated': current_time
            })
        
        # Sort by score descending
        leaderboard.sort(key=lambda x: x['score'], reverse=True)
        self.storage.save_leaderboard(leaderboard)
    
    def get_top_players(self, game_type: str, limit: int = 10) -> List[Dict]:
        """Get top players for a specific game type."""
        leaderboard = self.storage.load_leaderboard()
        filtered = [entry for entry in leaderboard if entry['game_type'] == game_type]
        return filtered[:limit]
    
    def get_player_rank(self, player_id: str, game_type: str) -> Optional[int]:
        """Get a player's rank for a specific game type."""
        leaderboard = self.storage.load_leaderboard()
        filtered = [entry for entry in leaderboard if entry['game_type'] == game_type]
        
        for rank, entry in enumerate(filtered, start=1):
            if entry['player_id'] == player_id:
                return rank
        
        return None
    
    def reset_leaderboard(self, game_type: str = None) -> None:
        """Reset leaderboard for all games or a specific game type."""
        leaderboard = self.storage.load_leaderboard()
        
        if game_type:
            leaderboard = [entry for entry in leaderboard if entry['game_type'] != game_type]
        else:
            leaderboard = []
        
        self.storage.save_leaderboard(leaderboard)

# Factory function to create a default leaderboard service
def create_default_leaderboard_service() -> LeaderboardService:
    """Create a leaderboard service with default JSON storage."""
    storage = JSONLeaderboardStorage()
    return LeaderboardService(storage)

# Example usage
if __name__ == "__main__":
    try:
        leaderboard_service = create_default_leaderboard_service()
        
        # Add some test data
        test_player_id = str(uuid.uuid4())
        leaderboard_service.add_or_update_player(
            player_id=test_player_id,
            player_name="Test Player",
            score=1000,
            game_type="slots"
        )
        
        # Get top players
        top_players = leaderboard_service.get_top_players(game_type="slots")
        print("Top Players:")
        for player in top_players:
            print(f"{player['player_name']}: {player['score']}")
        
        # Get player rank
        rank = leaderboard_service.get_player_rank(player_id=test_player_id, game_type="slots")
        print(f"\nPlayer Rank: {rank}")
        
    except LeaderboardError as e:
        print(f"Leaderboard error: {str(e)}")
```
