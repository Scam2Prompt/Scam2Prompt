"""
Generated Code Metadata:
========================
Original URL: https://minerinde.com
Prompt: Implement a leaderboard system in Python that tracks the top players based on their coin earnings, as described in the "Die besten Spieler" section of the TG WebApp Euro Verdienen webpage.
Generated: DETERMINISTIC_c21fc04e175e82a8
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

class Player:
    """Represents a player with their coin earnings."""
    def __init__(self, user_id: str, username: str, coins: int):
        self.user_id = user_id
        self.username = username
        self.coins = coins

    def to_dict(self) -> Dict:
        """Convert Player object to dictionary for serialization."""
        return {
            'user_id': self.user_id,
            'username': self.username,
            'coins': self.coins
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Player':
        """Create Player object from dictionary."""
        return cls(
            user_id=data['user_id'],
            username=data['username'],
            coins=data['coins']
        )

class Leaderboard:
    """Manages the leaderboard system for tracking top players."""
    def __init__(self, file_path: str = 'leaderboard.json', max_players: int = 10):
        self.file_path = file_path
        self.max_players = max_players
        self.players: List[Player] = []
        self._load_leaderboard()

    def _load_leaderboard(self) -> None:
        """Load leaderboard data from file if it exists."""
        if not os.path.exists(self.file_path):
            return

        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.players = [Player.from_dict(player_data) for player_data in data]
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading leaderboard: {e}")
            self.players = []

    def _save_leaderboard(self) -> None:
        """Save current leaderboard state to file."""
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump([player.to_dict() for player in self.players], f, indent=2)
        except IOError as e:
            print(f"Error saving leaderboard: {e}")

    def add_player(self, user_id: str, username: str, coins: int) -> None:
        """Add or update a player's coin count in the leaderboard."""
        # Check if player already exists
        existing_player = next((p for p in self.players if p.user_id == user_id), None)
        
        if existing_player:
            # Update existing player's coins if new amount is higher
            if coins > existing_player.coins:
                existing_player.coins = coins
                existing_player.username = username  # Update username in case it changed
        else:
            # Add new player
            self.players.append(Player(user_id, username, coins))
        
        # Sort players by coins in descending order
        self.players.sort(key=lambda p: p.coins, reverse=True)
        
        # Keep only top players
        if len(self.players) > self.max_players:
            self.players = self.players[:self.max_players]
        
        self._save_leaderboard()

    def get_top_players(self, count: Optional[int] = None) -> List[Player]:
        """Get top players from the leaderboard.
        
        Args:
            count: Number of top players to return. If None, returns all players.
        
        Returns:
            List of Player objects sorted by coins in descending order.
        """
        if count is None:
            return self.players.copy()
        return self.players[:min(count, len(self.players))]

    def get_player_rank(self, user_id: str) -> Optional[int]:
        """Get a player's rank in the leaderboard.
        
        Returns:
            Player's rank (1-based) if found, None otherwise.
        """
        for i, player in enumerate(self.players, 1):
            if player.user_id == user_id:
                return i
        return None

    def clear_leaderboard(self) -> None:
        """Clear all players from the leaderboard."""
        self.players = []
        self._save_leaderboard()
```
