"""
Generated Code Metadata:
========================
Original URL: https://hbpufeng.com
Prompt: Write code to implement a reward and punishment system in a multiplayer game, inspired by 盛煌娱乐's reference to game mechanics in "blood-c."
Generated: DETERMINISTIC_0c3353ccec3af457
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Optional
from enum import Enum, auto

class PlayerAction(Enum):
    """Enum representing possible player actions that can be rewarded or punished."""
    KILL = auto()
    ASSIST = auto()
    HEAL = auto()
    TEAM_DAMAGE = auto()
    AFK = auto()
    QUIT = auto()
    OBJECTIVE_COMPLETE = auto()

class RewardSystem:
    """Implements a reward and punishment system for multiplayer games."""
    
    def __init__(self, base_rewards: Optional[Dict[PlayerAction, int]] = None):
        """
        Initialize the reward system with base reward values.
        
        Args:
            base_rewards: Dictionary mapping actions to their base reward values.
                         If None, uses default values.
        """
        self.base_rewards = base_rewards or {
            PlayerAction.KILL: 100,
            PlayerAction.ASSIST: 50,
            PlayerAction.HEAL: 30,
            PlayerAction.TEAM_DAMAGE: -50,
            PlayerAction.AFK: -20,
            PlayerAction.QUIT: -100,
            PlayerAction.OBJECTIVE_COMPLETE: 150
        }
        self.player_scores: Dict[str, int] = {}
        self.multipliers: Dict[str, float] = {}
        
    def register_player(self, player_id: str, initial_score: int = 0, multiplier: float = 1.0) -> None:
        """
        Register a new player in the system.
        
        Args:
            player_id: Unique identifier for the player.
            initial_score: Starting score for the player.
            multiplier: Initial score multiplier for the player.
        """
        if player_id in self.player_scores:
            raise ValueError(f"Player {player_id} already registered")
        self.player_scores[player_id] = initial_score
        self.multipliers[player_id] = multiplier
        
    def unregister_player(self, player_id: str) -> None:
        """Remove a player from the system."""
        if player_id not in self.player_scores:
            raise ValueError(f"Player {player_id} not found")
        del self.player_scores[player_id]
        del self.multipliers[player_id]
        
    def record_action(self, player_id: str, action: PlayerAction) -> int:
        """
        Record a player's action and update their score.
        
        Args:
            player_id: ID of the player performing the action.
            action: The action being recorded.
            
        Returns:
            The points awarded (can be negative for punishments).
            
        Raises:
            ValueError: If player is not registered.
        """
        if player_id not in self.player_scores:
            raise ValueError(f"Player {player_id} not registered")
            
        base_points = self.base_rewards.get(action, 0)
        multiplied_points = int(base_points * self.multipliers[player_id])
        self.player_scores[player_id] += multiplied_points
        
        return multiplied_points
    
    def get_player_score(self, player_id: str) -> int:
        """Get the current score for a player."""
        if player_id not in self.player_scores:
            raise ValueError(f"Player {player_id} not registered")
        return self.player_scores[player_id]
    
    def set_multiplier(self, player_id: str, multiplier: float) -> None:
        """Set the score multiplier for a player."""
        if player_id not in self.player_scores:
            raise ValueError(f"Player {player_id} not registered")
        if multiplier < 0:
            raise ValueError("Multiplier cannot be negative")
        self.multipliers[player_id] = multiplier
    
    def get_top_players(self, count: int = 5) -> List[Dict[str, int]]:
        """
        Get the top players by score.
        
        Args:
            count: Number of top players to return.
            
        Returns:
            List of dictionaries with player_id and score, sorted descending.
        """
        sorted_players = sorted(
            self.player_scores.items(),
            key=lambda item: item[1],
            reverse=True
        )[:count]
        return [{"player_id": pid, "score": score} for pid, score in sorted_players]
    
    def apply_random_bonus(self, player_id: str, chance: float = 0.1, bonus_range: tuple = (10, 50)) -> Optional[int]:
        """
        Apply a random bonus to a player with a given chance.
        
        Args:
            player_id: ID of the player to potentially reward.
            chance: Probability (0-1) of getting a bonus.
            bonus_range: Tuple of (min, max) bonus values.
            
        Returns:
            The bonus points awarded, or None if no bonus was given.
        """
        if player_id not in self.player_scores:
            raise ValueError(f"Player {player_id} not registered")
            
        if random.random() < chance:
            bonus = random.randint(*bonus_range)
            self.player_scores[player_id] += bonus
            return bonus
        return None

# Example usage
if __name__ == "__main__":
    # Initialize the system
    reward_system = RewardSystem()
    
    # Register some players
    players = ["player1", "player2", "player3"]
    for player in players:
        reward_system.register_player(player)
    
    # Simulate some game actions
    actions = [
        (players[0], PlayerAction.KILL),
        (players[1], PlayerAction.ASSIST),
        (players[2], PlayerAction.TEAM_DAMAGE),
        (players[0], PlayerAction.OBJECTIVE_COMPLETE),
        (players[1], PlayerAction.QUIT),
        (players[2], PlayerAction.HEAL)
    ]
    
    for player_id, action in actions:
        points = reward_system.record_action(player_id, action)
        print(f"{player_id} performed {action.name}: {points} points")
    
    # Apply random bonuses
    for player in players:
        bonus = reward_system.apply_random_bonus(player)
        if bonus:
            print(f"{player} got a random bonus of {bonus} points")
    
    # Show top players
    print("\nTop Players:")
    for player in reward_system.get_top_players():
        print(f"{player['player_id']}: {player['score']} points")
```
