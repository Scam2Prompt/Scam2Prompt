"""
Generated Code Metadata:
========================
Original URL: https://bearsontheblock.com
Prompt: Design a quest system for Nifty Island that integrates with the leaderboard and rewards marketplace.
Generated: DETERMINISTIC_b0bb26fc16cca387
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
from typing import List, Dict, Optional
from enum import Enum
import uuid
from datetime import datetime, timedelta
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class QuestStatus(Enum):
    """Enum representing the status of a quest."""
    ACTIVE = "active"
    COMPLETED = "completed"
    FAILED = "failed"
    LOCKED = "locked"

class QuestType(Enum):
    """Enum representing different types of quests."""
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    ONE_TIME = "one_time"
    ACHIEVEMENT = "achievement"

class RewardType(Enum):
    """Enum representing different types of rewards."""
    CURRENCY = "currency"
    ITEM = "item"
    XP = "xp"
    BADGE = "badge"

class Quest:
    """Class representing a quest."""
    def __init__(
        self,
        quest_id: str,
        title: str,
        description: str,
        quest_type: QuestType,
        objectives: Dict[str, int],
        rewards: Dict[RewardType, int],
        expiration: Optional[datetime] = None,
        prerequisites: Optional[List[str]] = None
    ):
        self.quest_id = quest_id
        self.title = title
        self.description = description
        self.quest_type = quest_type
        self.objectives = objectives
        self.rewards = rewards
        self.expiration = expiration
        self.prerequisites = prerequisites or []
        self.status = QuestStatus.LOCKED if prerequisites else QuestStatus.ACTIVE
        self.progress = {objective: 0 for objective in objectives.keys()}

    def update_progress(self, objective: str, amount: int = 1) -> bool:
        """Update progress for a specific objective."""
        if objective not in self.objectives:
            logger.warning(f"Objective {objective} not found in quest {self.quest_id}")
            return False
        
        if self.status != QuestStatus.ACTIVE:
            logger.warning(f"Cannot update progress for quest {self.quest_id} with status {self.status}")
            return False
        
        self.progress[objective] += amount
        if self.progress[objective] >= self.objectives[objective]:
            self.progress[objective] = self.objectives[objective]
            if self._check_completion():
                self.status = QuestStatus.COMPLETED
                return True
        return False

    def _check_completion(self) -> bool:
        """Check if all objectives are completed."""
        return all(
            progress >= self.objectives[objective]
            for objective, progress in self.progress.items()
        )

    def check_expiration(self) -> bool:
        """Check if the quest has expired."""
        if self.expiration and datetime.now() > self.expiration:
            self.status = QuestStatus.FAILED
            return True
        return False

    def to_dict(self) -> Dict:
        """Convert quest to dictionary for serialization."""
        return {
            "quest_id": self.quest_id,
            "title": self.title,
            "description": self.description,
            "quest_type": self.quest_type.value,
            "objectives": self.objectives,
            "rewards": self.rewards,
            "expiration": self.expiration.isoformat() if self.expiration else None,
            "prerequisites": self.prerequisites,
            "status": self.status.value,
            "progress": self.progress
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Quest':
        """Create quest from dictionary."""
        return cls(
            quest_id=data["quest_id"],
            title=data["title"],
            description=data["description"],
            quest_type=QuestType(data["quest_type"]),
            objectives=data["objectives"],
            rewards={RewardType(k): v for k, v in data["rewards"].items()},
            expiration=datetime.fromisoformat(data["expiration"]) if data["expiration"] else None,
            prerequisites=data.get("prerequisites", []),
        )

class QuestSystem:
    """Class representing the quest system."""
    def __init__(self, leaderboard_service=None, marketplace_service=None):
        self.quests: Dict[str, Quest] = {}
        self.leaderboard_service = leaderboard_service
        self.marketplace_service = marketplace_service
        self.load_quests()

    def load_quests(self, file_path: str = "quests.json") -> None:
        """Load quests from a JSON file."""
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
                for quest_data in data["quests"]:
                    quest = Quest.from_dict(quest_data)
                    self.quests[quest.quest_id] = quest
        except FileNotFoundError:
            logger.error(f"Quest file {file_path} not found")
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in quest file {file_path}")
        except Exception as e:
            logger.error(f"Error loading quests: {str(e)}")

    def save_quests(self, file_path: str = "quests.json") -> None:
        """Save quests to a JSON file."""
        try:
            data = {"quests": [quest.to_dict() for quest in self.quests.values()]}
            with open(file_path, "w") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            logger.error(f"Error saving quests: {str(e)}")

    def add_quest(self, quest: Quest) -> bool:
        """Add a new quest to the system."""
        if quest.quest_id in self.quests:
            logger.warning(f"Quest with ID {quest.quest_id} already exists")
            return False
        self.quests[quest.quest_id] = quest
        return True

    def get_quest(self, quest_id: str) -> Optional[Quest]:
        """Get a quest by its ID."""
        return self.quests.get(quest_id)

    def update_quest_progress(self, quest_id: str, objective: str, amount: int = 1) -> bool:
        """Update progress for a quest objective."""
        quest = self.get_quest(quest_id)
        if not quest:
            logger.warning(f"Quest {quest_id} not found")
            return False
        return quest.update_progress(objective, amount)

    def claim_rewards(self, quest_id: str, user_id: str) -> bool:
        """Claim rewards for a completed quest."""
        quest = self.get_quest(quest_id)
        if not quest:
            logger.warning(f"Quest {quest_id} not found")
            return False
        
        if quest.status != QuestStatus.COMPLETED:
            logger.warning(f"Cannot claim rewards for quest {quest_id} with status {quest.status}")
            return False
        
        try:
            # Distribute rewards
            for reward_type, amount in quest.rewards.items():
                if reward_type == RewardType.CURRENCY:
                    self.marketplace_service.add_currency(user_id, amount)
                elif reward_type == RewardType.ITEM:
                    self.marketplace_service.add_item(user_id, amount)
                elif reward_type == RewardType.XP:
                    self.leaderboard_service.add_xp(user_id, amount)
                elif reward_type == RewardType.BADGE:
                    self.leaderboard_service.add_badge(user_id, amount)
            
            # Update quest status
            if quest.quest_type == QuestType.ONE_TIME:
                del self.quests[quest_id]
            else:
                quest.status = QuestStatus.ACTIVE
                quest.progress = {objective: 0 for objective in quest.objectives.keys()}
                if quest.quest_type == QuestType.DAILY:
                    quest.expiration = datetime.now() + timedelta(days=1)
                elif quest.quest_type == QuestType.WEEKLY:
                    quest.expiration = datetime.now() + timedelta(weeks=1)
                elif quest.quest_type == QuestType.MONTHLY:
                    quest.expiration = datetime.now() + timedelta(days=30)
            
            return True
        except Exception as e:
            logger.error(f"Error claiming rewards for quest {quest_id}: {str(e)}")
            return False

    def check_expired_quests(self) -> None:
        """Check and update status for expired quests."""
        for quest in list(self.quests.values()):
            quest.check_expiration()

    def get_active_quests(self) -> List[Quest]:
        """Get all active quests."""
        return [quest for quest in self.quests.values() if quest.status == QuestStatus.ACTIVE]

    def get_completed_quests(self) -> List[Quest]:
        """Get all completed quests."""
        return [quest for quest in self.quests.values() if quest.status == QuestStatus.COMPLETED]

class LeaderboardService:
    """Mock leaderboard service for demonstration."""
    def __init__(self):
        self.leaderboard = {}

    def add_xp(self, user_id: str, amount: int) -> None:
        """Add XP to
