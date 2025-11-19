"""
Generated Code Metadata:
========================
Original URL: https://moontropica.pages.dev
Prompt: Develop a system for rewarding players with XP progression, quests, and challenges in a game like Moon Tropica.
Generated: DETERMINISTIC_b6bcb55d4b9df0cc
Batch ID: 20250622_204603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum, auto
from typing import Dict, List, Optional, Tuple


class QuestType(Enum):
    """Enumeration of quest types."""
    MAIN = auto()
    SIDE = auto()
    DAILY = auto()
    WEEKLY = auto()
    CHALLENGE = auto()


class RewardType(Enum):
    """Enumeration of reward types."""
    XP = auto()
    CURRENCY = auto()
    ITEM = auto()
    UNLOCK = auto()


@dataclass
class Reward:
    """Class representing a reward."""
    reward_type: RewardType
    amount: int
    item_id: Optional[str] = None


@dataclass
class Quest:
    """Class representing a quest."""
    quest_id: str
    title: str
    description: str
    quest_type: QuestType
    required_level: int
    objectives: Dict[str, int]  # key: objective, value: target
    rewards: List[Reward]
    is_repeatable: bool = False
    is_completed: bool = False
    progress: Dict[str, int] = field(default_factory=dict)  # key: objective, value: current


@dataclass
class Challenge:
    """Class representing a challenge."""
    challenge_id: str
    title: str
    description: str
    objectives: Dict[str, int]
    rewards: List[Reward]
    duration_hours: int
    start_time: Optional[datetime] = None
    is_active: bool = False
    is_completed: bool = False
    progress: Dict[str, int] = field(default_factory=dict)


class PlayerProgression:
    """Class handling player progression including XP, leveling, and quests."""
    
    def __init__(self, player_id: str):
        self.player_id = player_id
        self.xp = 0
        self.level = 1
        self.quests: Dict[str, Quest] = {}
        self.active_challenges: Dict[str, Challenge] = {}
        self.completed_quests: List[str] = []
        self.completed_challenges: List[str] = []
        self.level_thresholds = self._calculate_level_thresholds()
        
    def _calculate_level_thresholds(self) -> Dict[int, int]:
        """Calculate XP thresholds for each level."""
        thresholds = {}
        base_xp = 1000
        for level in range(1, 101):
            thresholds[level] = base_xp * level
        return thresholds
    
    def add_xp(self, amount: int) -> Tuple[int, bool]:
        """Add XP to player and check for level up.
        
        Returns:
            Tuple of (new_level, leveled_up)
        """
        self.xp += amount
        leveled_up = False
        
        while self.level < 100 and self.xp >= self.level_thresholds[self.level]:
            self.xp -= self.level_thresholds[self.level]
            self.level += 1
            leveled_up = True
            
        return self.level, leveled_up
    
    def add_quest(self, quest: Quest) -> None:
        """Add a quest to player's quest log."""
        if quest.quest_id in self.quests:
            raise ValueError(f"Quest {quest.quest_id} already exists")
        
        quest.progress = {obj: 0 for obj in quest.objectives}
        self.quests[quest.quest_id] = quest
    
    def update_quest_progress(self, quest_id: str, objective: str, amount: int = 1) -> bool:
        """Update progress for a quest objective.
        
        Returns:
            True if quest was completed, False otherwise
        """
        if quest_id not in self.quests:
            raise ValueError(f"Quest {quest_id} not found")
        
        quest = self.quests[quest_id]
        
        if objective not in quest.objectives:
            raise ValueError(f"Objective {objective} not found in quest {quest_id}")
        
        quest.progress[objective] += amount
        
        if quest.progress[objective] >= quest.objectives[objective]:
            quest.progress[objective] = quest.objectives[objective]
        
        if all(quest.progress[obj] >= quest.objectives[obj] for obj in quest.objectives):
            quest.is_completed = True
            self._complete_quest(quest)
            return True
        return False
    
    def _complete_quest(self, quest: Quest) -> None:
        """Handle quest completion rewards and cleanup."""
        for reward in quest.rewards:
            if reward.reward_type == RewardType.XP:
                self.add_xp(reward.amount)
        
        self.completed_quests.append(quest.quest_id)
        
        if not quest.is_repeatable:
            del self.quests[quest.quest_id]
        else:
            quest.is_completed = False
            quest.progress = {obj: 0 for obj in quest.objectives}
    
    def start_challenge(self, challenge: Challenge) -> None:
        """Start a challenge for the player."""
        if challenge.challenge_id in self.active_challenges:
            raise ValueError(f"Challenge {challenge.challenge_id} already active")
        
        challenge.start_time = datetime.now()
        challenge.is_active = True
        challenge.progress = {obj: 0 for obj in challenge.objectives}
        self.active_challenges[challenge.challenge_id] = challenge
    
    def update_challenge_progress(self, challenge_id: str, objective: str, amount: int = 1) -> bool:
        """Update progress for a challenge objective.
        
        Returns:
            True if challenge was completed, False otherwise
        """
        if challenge_id not in self.active_challenges:
            raise ValueError(f"Challenge {challenge_id} not found")
        
        challenge = self.active_challenges[challenge_id]
        
        if objective not in challenge.objectives:
            raise ValueError(f"Objective {objective} not found in challenge {challenge_id}")
        
        challenge.progress[objective] += amount
        
        if challenge.progress[objective] >= challenge.objectives[objective]:
            challenge.progress[objective] = challenge.objectives[objective]
        
        if all(challenge.progress[obj] >= challenge.objectives[obj] for obj in challenge.objectives):
            challenge.is_completed = True
            self._complete_challenge(challenge)
            return True
        return False
    
    def _complete_challenge(self, challenge: Challenge) -> None:
        """Handle challenge completion rewards and cleanup."""
        for reward in challenge.rewards:
            if reward.reward_type == RewardType.XP:
                self.add_xp(reward.amount)
        
        self.completed_challenges.append(challenge.challenge_id)
        del self.active_challenges[challenge.challenge_id]
    
    def check_expired_challenges(self) -> None:
        """Check and remove expired challenges."""
        current_time = datetime.now()
        expired = []
        
        for challenge_id, challenge in self.active_challenges.items():
            if challenge.start_time and (current_time - challenge.start_time) > timedelta(hours=challenge.duration_hours):
                expired.append(challenge_id)
        
        for challenge_id in expired:
            del self.active_challenges[challenge_id]
    
    def to_dict(self) -> Dict:
        """Serialize player progression to dictionary."""
        return {
            "player_id": self.player_id,
            "xp": self.xp,
            "level": self.level,
            "quests": [vars(q) for q in self.quests.values()],
            "active_challenges": [vars(c) for c in self.active_challenges.values()],
            "completed_quests": self.completed_quests,
            "completed_challenges": self.completed_challenges
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'PlayerProgression':
        """Deserialize player progression from dictionary."""
        player = cls(data["player_id"])
        player.xp = data["xp"]
        player.level = data["level"]
        player.completed_quests = data["completed_quests"]
        player.completed_challenges = data["completed_challenges"]
        
        for q_data in data["quests"]:
            rewards = [Reward(**r) for r in q_data["rewards"]]
            quest = Quest(
                quest_id=q_data["quest_id"],
                title=q_data["title"],
                description=q_data["description"],
                quest_type=QuestType[q_data["quest_type"]],
                required_level=q_data["required_level"],
                objectives=q_data["objectives"],
                rewards=rewards,
                is_repeatable=q_data["is_repeatable"],
                is_completed=q_data["is_completed"],
                progress=q_data["progress"]
            )
            player.quests[quest.quest_id] = quest
        
        for c_data in data["active_challenges"]:
            rewards = [Reward(**r) for r in c_data["rewards"]]
            challenge = Challenge(
                challenge_id=c_data["challenge_id"],
                title=c_data["title"],
                description=c_data["description"],
                objectives=c_data["objectives"],
                rewards=rewards,
                duration_hours=c_data["duration_h
