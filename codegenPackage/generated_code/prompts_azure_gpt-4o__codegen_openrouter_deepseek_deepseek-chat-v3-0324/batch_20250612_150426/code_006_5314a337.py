"""
Generated Code Metadata:
========================
Original URL: https://geno-pets.net
Prompt: Write code to implement a leaderboard system for ranking players based on their activity and achievements, as described in Genopets Phase 1 roadmap.
Generated: DETERMINISTIC_5314a3376bf202aa
Batch ID: 20250612_150426
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
from datetime import datetime
import heapq
import uuid
import os

# Constants
LEADERBOARD_SIZE = 100
SCORE_WEIGHTS = {
    'activity': 0.4,
    'achievements': 0.6
}

@dataclass
class Player:
    """Represents a player in the Genopets game."""
    player_id: str
    username: str
    activity_score: float = 0.0
    achievement_score: float = 0.0
    last_updated: datetime = field(default_factory=datetime.utcnow)

    @property
    def total_score(self) -> float:
        """Calculate weighted total score."""
        return (self.activity_score * SCORE_WEIGHTS['activity'] + 
                self.achievement_score * SCORE_WEIGHTS['achievements'])

    def to_dict(self) -> Dict:
        """Convert Player object to dictionary for serialization."""
        return {
            'player_id': self.player_id,
            'username': self.username,
            'activity_score': self.activity_score,
            'achievement_score': self.achievement_score,
            'last_updated': self.last_updated.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Player':
        """Create Player object from dictionary."""
        return cls(
            player_id=data['player_id'],
            username=data['username'],
            activity_score=data['activity_score'],
            achievement_score=data['achievement_score'],
            last_updated=datetime.fromisoformat(data['last_updated'])
        )

class Leaderboard:
    """Implements a leaderboard system for ranking players."""
    
    def __init__(self, storage_path: str = 'leaderboard_data.json'):
        self.storage_path = storage_path
        self.players: Dict[str, Player] = {}  # player_id -> Player
        self.top_players: List[Player] = []   # Min-heap of top players
        self._initialize()

    def _initialize(self) -> None:
        """Initialize leaderboard from storage if available."""
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, 'r') as f:
                    data = json.load(f)
                    self.players = {pid: Player.from_dict(pdata) 
                                  for pid, pdata in data['players'].items()}
                    self.top_players = [Player.from_dict(pdata) 
                                      for pdata in data['top_players']]
            except (json.JSONDecodeError, KeyError, IOError) as e:
                print(f"Error loading leaderboard data: {e}")
                self._reset()

    def _reset(self) -> None:
        """Reset leaderboard to empty state."""
        self.players = {}
        self.top_players = []
        self._save()

    def _save(self) -> None:
        """Save leaderboard data to storage."""
        try:
            data = {
                'players': {pid: player.to_dict() 
                          for pid, player in self.players.items()},
                'top_players': [player.to_dict() for player in self.top_players]
            }
            with open(self.storage_path, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving leaderboard data: {e}")

    def add_or_update_player(self, username: str, 
                           activity_delta: float = 0.0, 
                           achievement_delta: float = 0.0,
                           player_id: Optional[str] = None) -> str:
        """
        Add or update a player's scores.
        Returns the player_id (new or existing).
        """
        if player_id is None:
            player_id = str(uuid.uuid4())
        
        if player_id in self.players:
            player = self.players[player_id]
            player.activity_score += activity_delta
            player.achievement_score += achievement_delta
            player.last_updated = datetime.utcnow()
        else:
            player = Player(
                player_id=player_id,
                username=username,
                activity_score=activity_delta,
                achievement_score=achievement_delta
            )
            self.players[player_id] = player
        
        self._update_top_players(player)
        self._save()
        return player_id

    def _update_top_players(self, player: Player) -> None:
        """Maintain the top players heap."""
        if len(self.top_players) < LEADERBOARD_SIZE:
            heapq.heappush(self.top_players, player)
        elif player.total_score > self.top_players[0].total_score:
            heapq.heappushpop(self.top_players, player)

    def get_leaderboard(self, limit: int = 10) -> List[Dict]:
        """
        Get the top players ranked by total score.
        Returns list of player dictionaries sorted in descending order.
        """
        sorted_players = sorted(
            self.top_players, 
            key=lambda p: p.total_score, 
            reverse=True
        )[:limit]
        return [
            {
                'rank': i + 1,
                'username': player.username,
                'total_score': player.total_score,
                'activity_score': player.activity_score,
                'achievement_score': player.achievement_score
            }
            for i, player in enumerate(sorted_players)
        ]

    def get_player_rank(self, player_id: str) -> Optional[int]:
        """
        Get a player's current rank in the leaderboard.
        Returns None if player is not in top players.
        """
        sorted_players = sorted(
            self.top_players, 
            key=lambda p: p.total_score, 
            reverse=True
        )
        for rank, player in enumerate(sorted_players, 1):
            if player.player_id == player_id:
                return rank
        return None

    def get_player_stats(self, player_id: str) -> Optional[Dict]:
        """Get detailed stats for a specific player."""
        player = self.players.get(player_id)
        if player:
            return {
                'player_id': player.player_id,
                'username': player.username,
                'total_score': player.total_score,
                'activity_score': player.activity_score,
                'achievement_score': player.achievement_score,
                'last_updated': player.last_updated.isoformat(),
                'rank': self.get_player_rank(player_id)
            }
        return None

# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Add some players
    player1 = leaderboard.add_or_update_player("Alice", 50.0, 30.0)
    player2 = leaderboard.add_or_update_player("Bob", 40.0, 40.0)
    player3 = leaderboard.add_or_update_player("Charlie", 60.0, 20.0)
    
    # Update scores
    leaderboard.add_or_update_player("Alice", 10.0, 5.0, player1)
    
    # Get leaderboard
    top_players = leaderboard.get_leaderboard()
    print("Top Players:")
    for player in top_players:
        print(f"{player['rank']}. {player['username']} - {player['total_score']:.2f}")
    
    # Get player stats
    alice_stats = leaderboard.get_player_stats(player1)
    print("\nAlice's Stats:")
    print(alice_stats)
```
