"""
Generated Code Metadata:
========================
Original URL: https://mememoguls-en.pages.dev
Prompt: Implement a leaderboard system in Python that tracks and ranks Meme Moguls players based on their earnings and trading activity, using the wealth leaderboard feature described on the site.
Generated: DETERMINISTIC_9d96a26a40996936
Batch ID: 20250612_152924
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
from dataclasses import dataclass, field
import heapq
from datetime import datetime
import os
import uuid

@dataclass(order=True)
class Player:
    """Represents a Meme Moguls player with their earnings and trading activity."""
    player_id: str = field(compare=False)
    username: str = field(compare=False)
    total_earnings: float = field(compare=True)
    trading_volume: float = field(compare=False)
    last_active: datetime = field(compare=False)

    def to_dict(self) -> Dict:
        """Convert Player object to dictionary for serialization."""
        return {
            "player_id": self.player_id,
            "username": self.username,
            "total_earnings": self.total_earnings,
            "trading_volume": self.trading_volume,
            "last_active": self.last_active.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Player':
        """Create Player object from dictionary."""
        return cls(
            player_id=data["player_id"],
            username=data["username"],
            total_earnings=data["total_earnings"],
            trading_volume=data["trading_volume"],
            last_active=datetime.fromisoformat(data["last_active"])
        )

class Leaderboard:
    """Implements a leaderboard system for Meme Moguls players."""
    
    def __init__(self, storage_path: str = "leaderboard_data.json"):
        """Initialize the leaderboard with optional persistent storage."""
        self.storage_path = storage_path
        self.players: Dict[str, Player] = {}  # player_id -> Player
        self._load_data()
    
    def _load_data(self) -> None:
        """Load player data from persistent storage if available."""
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, 'r') as f:
                    data = json.load(f)
                    self.players = {
                        player_id: Player.from_dict(player_data)
                        for player_id, player_data in data.items()
                    }
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading leaderboard data: {e}")
    
    def _save_data(self) -> None:
        """Save player data to persistent storage."""
        try:
            with open(self.storage_path, 'w') as f:
                json.dump(
                    {player_id: player.to_dict() for player_id, player in self.players.items()},
                    f,
                    indent=2
                )
        except IOError as e:
            print(f"Error saving leaderboard data: {e}")
    
    def add_or_update_player(
        self,
        username: str,
        earnings_delta: float,
        volume_delta: float,
        player_id: Optional[str] = None
    ) -> str:
        """
        Add a new player or update an existing player's stats.
        Returns the player_id (new or existing).
        """
        if player_id is None:
            player_id = str(uuid.uuid4())
        
        if player_id in self.players:
            player = self.players[player_id]
            player.total_earnings += earnings_delta
            player.trading_volume += volume_delta
            player.last_active = datetime.now()
        else:
            self.players[player_id] = Player(
                player_id=player_id,
                username=username,
                total_earnings=earnings_delta,
                trading_volume=volume_delta,
                last_active=datetime.now()
            )
        
        self._save_data()
        return player_id
    
    def get_top_players_by_earnings(self, limit: int = 10) -> List[Player]:
        """Return top N players ranked by total earnings."""
        # Use max-heap by inverting earnings to negative values
        heap = []
        for player in self.players.values():
            heapq.heappush(heap, (-player.total_earnings, player))
        
        top_players = []
        for _ in range(min(limit, len(heap))):
            if heap:
                _, player = heapq.heappop(heap)
                top_players.append(player)
        
        return top_players
    
    def get_top_players_by_volume(self, limit: int = 10) -> List[Player]:
        """Return top N players ranked by trading volume."""
        heap = []
        for player in self.players.values():
            heapq.heappush(heap, (-player.trading_volume, player))
        
        top_players = []
        for _ in range(min(limit, len(heap))):
            if heap:
                _, player = heapq.heappop(heap)
                top_players.append(player)
        
        return top_players
    
    def get_player_rank(self, player_id: str) -> Optional[int]:
        """
        Get a player's rank based on earnings.
        Returns None if player not found.
        """
        if player_id not in self.players:
            return None
        
        sorted_players = sorted(
            self.players.values(),
            key=lambda p: (-p.total_earnings, p.last_active)
        )
        
        for rank, player in enumerate(sorted_players, start=1):
            if player.player_id == player_id:
                return rank
        
        return None
    
    def get_player_stats(self, player_id: str) -> Optional[Player]:
        """Get a player's stats by their ID."""
        return self.players.get(player_id)
    
    def remove_inactive_players(self, days_inactive: int = 30) -> int:
        """
        Remove players who haven't been active for specified days.
        Returns number of players removed.
        """
        cutoff = datetime.now() - timedelta(days=days_inactive)
        inactive_ids = [
            player_id for player_id, player in self.players.items()
            if player.last_active < cutoff
        ]
        
        for player_id in inactive_ids:
            del self.players[player_id]
        
        if inactive_ids:
            self._save_data()
        
        return len(inactive_ids)

# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Add/update players
    leaderboard.add_or_update_player("meme_king", 1000.50, 500.25)
    leaderboard.add_or_update_player("dank_lord", 750.25, 1000.75)
    leaderboard.add_or_update_player("pepe_farmer", 1500.75, 300.50)
    
    # Get top players
    print("Top players by earnings:")
    for i, player in enumerate(leaderboard.get_top_players_by_earnings(), start=1):
        print(f"{i}. {player.username} - ${player.total_earnings:,.2f}")
    
    print("\nTop players by trading volume:")
    for i, player in enumerate(leaderboard.get_top_players_by_volume(), start=1):
        print(f"{i}. {player.username} - {player.trading_volume:,.2f} volume")
```
