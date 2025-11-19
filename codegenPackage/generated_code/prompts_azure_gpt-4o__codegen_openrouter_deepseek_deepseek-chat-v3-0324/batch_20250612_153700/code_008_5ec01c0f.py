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
import json
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
from datetime import datetime
import heapq

@dataclass
class Player:
    """Represents a player with their balloon height achievements."""
    player_id: str
    username: str
    highest_balloon_height: float
    last_updated: datetime

    def to_dict(self) -> Dict:
        """Convert Player object to dictionary for serialization."""
        data = asdict(self)
        data['last_updated'] = self.last_updated.isoformat()
        return data

    @classmethod
    def from_dict(cls, data: Dict) -> 'Player':
        """Create Player object from dictionary."""
        data['last_updated'] = datetime.fromisoformat(data['last_updated'])
        return cls(**data)

class Leaderboard:
    """A leaderboard system that ranks players based on balloon height achievements."""
    
    def __init__(self, storage_file: str = 'leaderboard.json'):
        """
        Initialize the leaderboard.
        
        Args:
            storage_file: Path to the JSON file for persistent storage.
        """
        self.storage_file = storage_file
        self.players: Dict[str, Player] = {}  # player_id -> Player
        self._load_data()

    def _load_data(self) -> None:
        """Load player data from storage file."""
        try:
            with open(self.storage_file, 'r') as f:
                data = json.load(f)
                self.players = {pid: Player.from_dict(pdata) for pid, pdata in data.items()}
        except FileNotFoundError:
            self.players = {}
        except json.JSONDecodeError:
            raise ValueError("Corrupted leaderboard data file")

    def _save_data(self) -> None:
        """Save player data to storage file."""
        data = {pid: player.to_dict() for pid, player in self.players.items()}
        with open(self.storage_file, 'w') as f:
            json.dump(data, f, indent=2)

    def add_or_update_player(self, player_id: str, username: str, height: float) -> None:
        """
        Add or update a player's balloon height achievement.
        
        Args:
            player_id: Unique identifier for the player
            username: Display name of the player
            height: New balloon height achievement
        """
        now = datetime.now()
        
        if player_id in self.players:
            if height > self.players[player_id].highest_balloon_height:
                self.players[player_id].highest_balloon_height = height
                self.players[player_id].last_updated = now
        else:
            self.players[player_id] = Player(
                player_id=player_id,
                username=username,
                highest_balloon_height=height,
                last_updated=now
            )
        
        self._save_data()

    def get_top_players(self, n: int = 10) -> List[Player]:
        """
        Get top N players by balloon height.
        
        Args:
            n: Number of top players to return
            
        Returns:
            List of top N players sorted by height (descending)
        """
        # Use min-heap to efficiently get top N players
        heap = []
        for player in self.players.values():
            if len(heap) < n:
                heapq.heappush(heap, (player.highest_balloon_height, player))
            else:
                heapq.heappushpop(heap, (player.highest_balloon_height, player))
        
        # Sort the top players in descending order
        top_players = [player for (height, player) in sorted(heap, reverse=True)]
        return top_players

    def get_player_rank(self, player_id: str) -> Optional[int]:
        """
        Get a player's rank based on their balloon height.
        
        Args:
            player_id: ID of the player to check
            
        Returns:
            Player's rank (1-based) or None if player not found
        """
        if player_id not in self.players:
            return None
            
        player_height = self.players[player_id].highest_balloon_height
        sorted_players = sorted(
            self.players.values(),
            key=lambda p: p.highest_balloon_height,
            reverse=True
        )
        
        for rank, player in enumerate(sorted_players, start=1):
            if player.player_id == player_id:
                return rank
                
        return None

    def get_player_position(self, player_id: str) -> Optional[Dict]:
        """
        Get detailed position information for a player.
        
        Args:
            player_id: ID of the player to check
            
        Returns:
            Dictionary with player's rank, height, and username or None if not found
        """
        if player_id not in self.players:
            return None
            
        player = self.players[player_id]
        rank = self.get_player_rank(player_id)
        
        return {
            'rank': rank,
            'height': player.highest_balloon_height,
            'username': player.username,
            'last_updated': player.last_updated.isoformat()
        }

    def reset_leaderboard(self) -> None:
        """Clear all leaderboard data."""
        self.players = {}
        self._save_data()
```
