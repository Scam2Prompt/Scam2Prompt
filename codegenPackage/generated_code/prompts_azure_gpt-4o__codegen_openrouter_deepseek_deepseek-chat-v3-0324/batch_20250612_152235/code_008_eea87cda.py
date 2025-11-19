"""
Generated Code Metadata:
========================
Original URL: https://galaxyfox-in.pages.dev
Prompt: Create a Python script that calculates rewards for players based on their participation in a play-to-earn game, using the mechanics described for $GFOX tokens.
Generated: DETERMINISTIC_eea87cda5e565132
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import List, Dict, Optional
from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 18

@dataclass
class Player:
    """Represents a player in the play-to-earn game."""
    player_id: str
    total_xp: Decimal = Decimal('0')
    total_tokens_earned: Decimal = Decimal('0')
    last_activity_timestamp: int = 0
    active_days: int = 0

@dataclass
class GameSession:
    """Represents a game session with XP earned."""
    player_id: str
    xp_earned: Decimal
    timestamp: int

class RewardCalculator:
    """Calculates rewards for players based on their participation."""
    
    def __init__(self, config_path: str = 'config.json'):
        """Initialize with configuration."""
        self.config = self._load_config(config_path)
        self.players: Dict[str, Player] = {}
        
    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from JSON file."""
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file not found at {config_path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON configuration file")
    
    def _calculate_daily_bonus(self, player: Player) -> Decimal:
        """Calculate daily active bonus based on consecutive active days."""
        bonus_multiplier = min(
            player.active_days / self.config['max_active_days_for_bonus'],
            Decimal('1')
        )
        return self.config['daily_bonus'] * bonus_multiplier
    
    def _calculate_xp_to_tokens(self, xp: Decimal) -> Decimal:
        """Convert XP to tokens based on conversion rate."""
        return xp * self.config['xp_to_token_rate']
    
    def _update_player_activity(self, player: Player, timestamp: int) -> None:
        """Update player's active days streak."""
        if timestamp - player.last_activity_timestamp > self.config['daily_reset_seconds']:
            player.active_days = 1
        else:
            player.active_days += 1
        player.last_activity_timestamp = timestamp
    
    def process_session(self, session: GameSession) -> Player:
        """Process a game session and update player rewards."""
        if session.player_id not in self.players:
            self.players[session.player_id] = Player(player_id=session.player_id)
        
        player = self.players[session.player_id]
        
        # Update player activity
        self._update_player_activity(player, session.timestamp)
        
        # Calculate base tokens from XP
        base_tokens = self._calculate_xp_to_tokens(session.xp_earned)
        
        # Calculate daily bonus
        daily_bonus = self._calculate_daily_bonus(player)
        
        # Calculate total tokens for this session
        session_tokens = base_tokens + daily_bonus
        
        # Update player totals
        player.total_xp += session.xp_earned
        player.total_tokens_earned += session_tokens
        
        return player
    
    def batch_process_sessions(self, sessions: List[GameSession]) -> Dict[str, Player]:
        """Process multiple game sessions efficiently."""
        results = {}
        for session in sessions:
            player = self.process_session(session)
            results[session.player_id] = player
        return results
    
    def get_player_rewards(self, player_id: str) -> Optional[Decimal]:
        """Get total tokens earned by a player."""
        player = self.players.get(player_id)
        return player.total_tokens_earned if player else None
    
    def save_player_data(self, output_path: str = 'player_data.json') -> None:
        """Save player data to JSON file."""
        try:
            serializable_data = {
                pid: {
                    'player_id': p.player_id,
                    'total_xp': str(p.total_xp),
                    'total_tokens_earned': str(p.total_tokens_earned),
                    'last_activity_timestamp': p.last_activity_timestamp,
                    'active_days': p.active_days
                }
                for pid, p in self.players.items()
            }
            
            with open(output_path, 'w') as f:
                json.dump(serializable_data, f, indent=2)
        except Exception as e:
            raise IOError(f"Failed to save player data: {str(e)}")

# Example configuration (would normally be in config.json)
DEFAULT_CONFIG = {
    "xp_to_token_rate": Decimal('0.01'),
    "daily_bonus": Decimal('5'),
    "max_active_days_for_bonus": 7,
    "daily_reset_seconds": 86400  # 24 hours in seconds
}
```
