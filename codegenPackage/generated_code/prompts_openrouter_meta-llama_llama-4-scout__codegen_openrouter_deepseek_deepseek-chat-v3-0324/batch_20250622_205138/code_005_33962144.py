"""
Generated Code Metadata:
========================
Original URL: https://bigtimecodes.pages.dev
Prompt: Develop a system for tracking and displaying player progress and achievements in a game, including features like prestige portals and adventure instances, similar to Big Time.
Generated: DETERMINISTIC_33962144e6a99f4d
Batch ID: 20250622_205138
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
from enum import Enum, auto
from typing import Dict, List, Optional, Tuple


class AchievementType(Enum):
    """Enumeration of achievement types."""
    QUEST_COMPLETION = auto()
    ITEM_COLLECTION = auto()
    BOSS_DEFEAT = auto()
    LEVEL_REACHED = auto()
    PRESTIGE_REACHED = auto()


class Achievement:
    """Represents a game achievement."""
    
    def __init__(self, achievement_id: str, name: str, description: str, 
                 achievement_type: AchievementType, reward: Dict):
        """
        Initialize an Achievement.
        
        Args:
            achievement_id: Unique identifier for the achievement.
            name: Name of the achievement.
            description: Description of the achievement.
            achievement_type: Type of achievement (from AchievementType enum).
            reward: Dictionary containing reward details.
        """
        self.achievement_id = achievement_id
        self.name = name
        self.description = description
        self.type = achievement_type
        self.reward = reward
        self.unlocked = False
        self.unlock_date = None

    def unlock(self) -> None:
        """Mark the achievement as unlocked with the current timestamp."""
        if not self.unlocked:
            self.unlocked = True
            self.unlock_date = datetime.now()

    def to_dict(self) -> Dict:
        """Convert the achievement to a dictionary for serialization."""
        return {
            'achievement_id': self.achievement_id,
            'name': self.name,
            'description': self.description,
            'type': self.type.name,
            'reward': self.reward,
            'unlocked': self.unlocked,
            'unlock_date': self.unlock_date.isoformat() if self.unlock_date else None
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Achievement':
        """Create an Achievement from a dictionary."""
        achievement = cls(
            data['achievement_id'],
            data['name'],
            data['description'],
            AchievementType[data['type']],
            data['reward']
        )
        achievement.unlocked = data['unlocked']
        if data['unlock_date']:
            achievement.unlock_date = datetime.fromisoformat(data['unlock_date'])
        return achievement


class PlayerProgress:
    """Tracks and manages player progress and achievements."""
    
    def __init__(self, player_id: str):
        """
        Initialize player progress tracker.
        
        Args:
            player_id: Unique identifier for the player.
        """
        self.player_id = player_id
        self.level = 1
        self.experience = 0
        self.prestige_level = 0
        self.achievements: Dict[str, Achievement] = {}
        self.completed_quests: List[str] = []
        self.completed_instances: List[str] = []
        self.portal_entries: Dict[str, int] = {}  # portal_id: entry_count

    def add_experience(self, amount: int) -> Tuple[int, bool]:
        """
        Add experience points to the player.
        
        Args:
            amount: Amount of experience to add.
            
        Returns:
            Tuple of (new_level, level_up) indicating if a level up occurred.
        """
        self.experience += amount
        new_level = self.calculate_level()
        level_up = new_level > self.level
        if level_up:
            self.level = new_level
        return new_level, level_up

    def calculate_level(self) -> int:
        """Calculate the player's level based on experience."""
        return self.experience // 1000 + 1  # Simplified level calculation

    def prestige(self) -> bool:
        """
        Prestige the player if they meet requirements.
        
        Returns:
            True if prestiged successfully, False otherwise.
        """
        if self.level >= 50 and self.prestige_level < 10:
            self.prestige_level += 1
            self.level = 1
            self.experience = 0
            return True
        return False

    def complete_quest(self, quest_id: str) -> None:
        """Mark a quest as completed."""
        if quest_id not in self.completed_quests:
            self.completed_quests.append(quest_id)

    def complete_instance(self, instance_id: str) -> None:
        """Mark an adventure instance as completed."""
        if instance_id not in self.completed_instances:
            self.completed_instances.append(instance_id)

    def enter_portal(self, portal_id: str) -> None:
        """Record a portal entry."""
        self.portal_entries[portal_id] = self.portal_entries.get(portal_id, 0) + 1

    def add_achievement(self, achievement: Achievement) -> None:
        """Add an achievement to the player's collection."""
        self.achievements[achievement.achievement_id] = achievement

    def unlock_achievement(self, achievement_id: str) -> Optional[Achievement]:
        """
        Unlock an achievement if it exists and isn't already unlocked.
        
        Returns:
            The unlocked achievement if successful, None otherwise.
        """
        achievement = self.achievements.get(achievement_id)
        if achievement and not achievement.unlocked:
            achievement.unlock()
            return achievement
        return None

    def get_unlocked_achievements(self) -> List[Achievement]:
        """Get all unlocked achievements."""
        return [a for a in self.achievements.values() if a.unlocked]

    def get_locked_achievements(self) -> List[Achievement]:
        """Get all locked achievements."""
        return [a for a in self.achievements.values() if not a.unlocked]

    def to_dict(self) -> Dict:
        """Convert the player progress to a dictionary for serialization."""
        return {
            'player_id': self.player_id,
            'level': self.level,
            'experience': self.experience,
            'prestige_level': self.prestige_level,
            'achievements': {k: v.to_dict() for k, v in self.achievements.items()},
            'completed_quests': self.completed_quests,
            'completed_instances': self.completed_instances,
            'portal_entries': self.portal_entries
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'PlayerProgress':
        """Create a PlayerProgress from a dictionary."""
        progress = cls(data['player_id'])
        progress.level = data['level']
        progress.experience = data['experience']
        progress.prestige_level = data['prestige_level']
        progress.achievements = {
            k: Achievement.from_dict(v) for k, v in data['achievements'].items()
        }
        progress.completed_quests = data['completed_quests']
        progress.completed_instances = data['completed_instances']
        progress.portal_entries = data['portal_entries']
        return progress


class AchievementSystem:
    """Manages all achievements and player progress in the game."""
    
    def __init__(self):
        """Initialize the achievement system."""
        self.players: Dict[str, PlayerProgress] = {}
        self.available_achievements: Dict[str, Achievement] = {}

    def register_player(self, player_id: str) -> PlayerProgress:
        """Register a new player with the system."""
        if player_id not in self.players:
            self.players[player_id] = PlayerProgress(player_id)
        return self.players[player_id]

    def add_achievement(self, achievement: Achievement) -> None:
        """Add an achievement to the available achievements pool."""
        self.available_achievements[achievement.achievement_id] = achievement

    def initialize_player_achievements(self, player_id: str) -> None:
        """Initialize a player with all available achievements (locked)."""
        if player_id in self.players:
            for achievement in self.available_achievements.values():
                self.players[player_id].add_achievement(achievement)

    def save_to_file(self, filename: str) -> None:
        """Save the achievement system state to a file."""
        data = {
            'players': {k: v.to_dict() for k, v in self.players.items()},
            'achievements': {k: v.to_dict() for k, v in self.available_achievements.items()}
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, filename: str) -> None:
        """Load the achievement system state from a file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.players = {
            k: PlayerProgress.from_dict(v) for k, v in data['players'].items()
        }
        self.available_achievements = {
            k: Achievement.from_dict(v) for k, v in data['achievements'].items()
        }

    def check_achievements(self, player_id: str, trigger_type: AchievementType, 
                          trigger_data: Dict) -> List[Achievement]:
        """
        Check for achievements that should be unlocked based on a trigger.
        
        Args:
            player_id: ID of
