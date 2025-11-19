"""
Generated Code Metadata:
========================
Original URL: https://ev-io.now.sh
Prompt: Generate code for a basic leaderboard system that tracks player XP and performance metrics, as seen in ev.io.
Generated: DETERMINISTIC_4d81fd4082eaed15
Batch ID: 20250622_204809
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
from typing import Dict, List, Optional

class Player:
    """Represents a player with XP and performance metrics."""
    
    def __init__(self, player_id: str, name: str, xp: int = 0, kills: int = 0, deaths: int = 0):
        """
        Initialize a player with default or provided stats.
        
        Args:
            player_id: Unique identifier for the player
            name: Player's display name
            xp: Initial XP points (default: 0)
            kills: Initial kill count (default: 0)
            deaths: Initial death count (default: 0)
        """
        self.player_id = player_id
        self.name = name
        self.xp = xp
        self.kills = kills
        self.deaths = deaths
    
    @property
    def kd_ratio(self) -> float:
        """Calculate kill/death ratio."""
        return self.kills / max(1, self.deaths)
    
    def add_xp(self, amount: int) -> None:
        """Add XP to player's total."""
        if amount < 0:
            raise ValueError("XP amount cannot be negative")
        self.xp += amount
    
    def add_kill(self) -> None:
        """Increment kill count."""
        self.kills += 1
    
    def add_death(self) -> None:
        """Increment death count."""
        self.deaths += 1
    
    def to_dict(self) -> Dict:
        """Convert player data to dictionary for serialization."""
        return {
            'player_id': self.player_id,
            'name': self.name,
            'xp': self.xp,
            'kills': self.kills,
            'deaths': self.deaths
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Player':
        """Create Player instance from dictionary."""
        return cls(
            player_id=data['player_id'],
            name=data['name'],
            xp=data.get('xp', 0),
            kills=data.get('kills', 0),
            deaths=data.get('deaths', 0)
        )

class Leaderboard:
    """Manages player rankings and persistence."""
    
    def __init__(self, storage_file: str = 'leaderboard.json'):
        """
        Initialize leaderboard with storage file.
        
        Args:
            storage_file: Path to JSON file for data persistence
        """
        self.storage_file = storage_file
        self.players: Dict[str, Player] = {}
        self._load_data()
    
    def _load_data(self) -> None:
        """Load player data from storage file if it exists."""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as f:
                    data = json.load(f)
                    self.players = {
                        player_id: Player.from_dict(player_data)
                        for player_id, player_data in data.items()
                    }
            except (json.JSONDecodeError, IOError) as e:
                raise RuntimeError(f"Failed to load leaderboard data: {str(e)}")
    
    def _save_data(self) -> None:
        """Save current player data to storage file."""
        try:
            with open(self.storage_file, 'w') as f:
                json.dump(
                    {player_id: player.to_dict() for player_id, player in self.players.items()},
                    f,
                    indent=2
                )
        except IOError as e:
            raise RuntimeError(f"Failed to save leaderboard data: {str(e)}")
    
    def add_player(self, player_id: str, name: str) -> None:
        """
        Add a new player to the leaderboard.
        
        Args:
            player_id: Unique identifier for the player
            name: Player's display name
        """
        if player_id in self.players:
            raise ValueError("Player ID already exists")
        self.players[player_id] = Player(player_id, name)
        self._save_data()
    
    def get_player(self, player_id: str) -> Optional[Player]:
        """Retrieve a player by ID."""
        return self.players.get(player_id)
    
    def update_player_xp(self, player_id: str, amount: int) -> None:
        """
        Update a player's XP.
        
        Args:
            player_id: ID of player to update
            amount: XP to add (can be negative)
        """
        player = self.players.get(player_id)
        if not player:
            raise ValueError("Player not found")
        player.add_xp(amount)
        self._save_data()
    
    def record_kill(self, killer_id: str, victim_id: str) -> None:
        """
        Record a kill between two players.
        
        Args:
            killer_id: ID of the killing player
            victim_id: ID of the killed player
        """
        killer = self.players.get(killer_id)
        victim = self.players.get(victim_id)
        
        if not killer or not victim:
            raise ValueError("One or both players not found")
        
        killer.add_kill()
        victim.add_death()
        self._save_data()
    
    def get_top_players_by_xp(self, limit: int = 10) -> List[Player]:
        """
        Get top players sorted by XP.
        
        Args:
            limit: Number of top players to return
            
        Returns:
            List of Player objects sorted by XP (descending)
        """
        return sorted(
            self.players.values(),
            key=lambda p: p.xp,
            reverse=True
        )[:limit]
    
    def get_top_players_by_kd(self, limit: int = 10) -> List[Player]:
        """
        Get top players sorted by kill/death ratio.
        
        Args:
            limit: Number of top players to return
            
        Returns:
            List of Player objects sorted by KD ratio (descending)
        """
        return sorted(
            self.players.values(),
            key=lambda p: p.kd_ratio,
            reverse=True
        )[:limit]
    
    def reset_leaderboard(self) -> None:
        """Reset all player stats (for testing purposes)."""
        self.players = {}
        self._save_data()
```
