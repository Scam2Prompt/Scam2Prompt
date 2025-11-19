"""
Generated Code Metadata:
========================
Original URL: https://moontropica-rewards.web.app
Prompt: Develop a quest and challenge system for a game like Moon Tropica, with rewards and XP progression for players.
Generated: DETERMINISTIC_39d61b3a6c31c7e0
Batch ID: 20250622_205039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from typing import List, Dict, Optional, Union

class QuestType(Enum):
    """Enumeration of quest types."""
    MAIN = "Main"
    SIDE = "Side"
    DAILY = "Daily"
    WEEKLY = "Weekly"

class RewardType(Enum):
    """Enumeration of reward types."""
    XP = "XP"
    CURRENCY = "Currency"
    ITEM = "Item"

class QuestStatus(Enum):
    """Enumeration of quest statuses."""
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    FAILED = "Failed"

class Challenge:
    """Represents a challenge within a quest."""
    def __init__(self, challenge_id: str, description: str, target: int, progress: int = 0):
        self.challenge_id = challenge_id
        self.description = description
        self.target = target
        self.progress = progress
    
    def update_progress(self, amount: int = 1) -> bool:
        """Update challenge progress and check for completion."""
        self.progress += amount
        return self.progress >= self.target
    
    def reset(self) -> None:
        """Reset challenge progress."""
        self.progress = 0

class Reward:
    """Represents a reward for completing a quest."""
    def __init__(self, reward_type: RewardType, value: Union[int, str], quantity: int = 1):
        self.reward_type = reward_type
        self.value = value
        self.quantity = quantity
    
    def __str__(self) -> str:
        return f"{self.quantity} {self.reward_type.value}(s): {self.value}"

class Quest:
    """Represents a quest with challenges and rewards."""
    def __init__(
        self,
        quest_id: str,
        title: str,
        description: str,
        quest_type: QuestType,
        challenges: List[Challenge],
        rewards: List[Reward],
        required_level: int = 1
    ):
        self.quest_id = quest_id
        self.title = title
        self.description = description
        self.quest_type = quest_type
        self.challenges = challenges
        self.rewards = rewards
        self.required_level = required_level
        self.status = QuestStatus.NOT_STARTED
    
    def start_quest(self) -> bool:
        """Start the quest if requirements are met."""
        if self.status == QuestStatus.NOT_STARTED:
            self.status = QuestStatus.IN_PROGRESS
            return True
        return False
    
    def update_challenge(self, challenge_id: str, amount: int = 1) -> bool:
        """Update progress for a specific challenge."""
        if self.status != QuestStatus.IN_PROGRESS:
            return False
        
        for challenge in self.challenges:
            if challenge.challenge_id == challenge_id:
                if challenge.update_progress(amount):
                    if self._check_completion():
                        self.status = QuestStatus.COMPLETED
                        return True
                return True
        return False
    
    def _check_completion(self) -> bool:
        """Check if all challenges are completed."""
        return all(challenge.progress >= challenge.target for challenge in self.challenges)
    
    def reset(self) -> None:
        """Reset quest progress."""
        self.status = QuestStatus.NOT_STARTED
        for challenge in self.challenges:
            challenge.reset()
    
    def get_rewards(self) -> List[Reward]:
        """Get rewards if quest is completed."""
        if self.status == QuestStatus.COMPLETED:
            return self.rewards
        return []

class Player:
    """Represents a player with quest progression."""
    def __init__(self, player_id: str, name: str, level: int = 1, xp: int = 0):
        self.player_id = player_id
        self.name = name
        self.level = level
        self.xp = xp
        self.active_quests: Dict[str, Quest] = {}
        self.completed_quests: Dict[str, Quest] = {}
    
    def can_accept_quest(self, quest: Quest) -> bool:
        """Check if player can accept the quest."""
        return (
            quest.quest_id not in self.active_quests
            and quest.quest_id not in self.completed_quests
            and quest.required_level <= self.level
        )
    
    def accept_quest(self, quest: Quest) -> bool:
        """Accept a quest if possible."""
        if not self.can_accept_quest(quest):
            return False
        
        if quest.start_quest():
            self.active_quests[quest.quest_id] = quest
            return True
        return False
    
    def update_quest_progress(self, quest_id: str, challenge_id: str, amount: int = 1) -> bool:
        """Update progress for a quest challenge."""
        if quest_id not in self.active_quests:
            return False
        
        quest = self.active_quests[quest_id]
        if quest.update_challenge(challenge_id, amount):
            if quest.status == QuestStatus.COMPLETED:
                self._complete_quest(quest)
            return True
        return False
    
    def _complete_quest(self, quest: Quest) -> None:
        """Complete a quest and grant rewards."""
        rewards = quest.get_rewards()
        self._grant_rewards(rewards)
        self.completed_quests[quest.quest_id] = quest
        del self.active_quests[quest.quest_id]
    
    def _grant_rewards(self, rewards: List[Reward]) -> None:
        """Grant rewards to the player."""
        for reward in rewards:
            if reward.reward_type == RewardType.XP:
                self.xp += reward.quantity
                self._check_level_up()
    
    def _check_level_up(self) -> bool:
        """Check if player should level up."""
        xp_needed = self.level * 100
        if self.xp >= xp_needed:
            self.level += 1
            self.xp -= xp_needed
            return True
        return False

class QuestSystem:
    """Manages all quests in the game."""
    def __init__(self):
        self.quests: Dict[str, Quest] = {}
    
    def add_quest(self, quest: Quest) -> None:
        """Add a quest to the system."""
        self.quests[quest.quest_id] = quest
    
    def get_quest(self, quest_id: str) -> Optional[Quest]:
        """Get a quest by ID."""
        return self.quests.get(quest_id)
    
    def generate_daily_quest(self) -> Quest:
        """Generate a random daily quest."""
        quest_id = f"daily_{random.randint(1000, 9999)}"
        challenges = [
            Challenge("collect", "Collect 10 moon crystals", 10),
            Challenge("defeat", "Defeat 5 space pirates", 5)
        ]
        rewards = [Reward(RewardType.XP, "Experience", 50)]
        return Quest(
            quest_id,
            "Daily Moon Mission",
            "Complete daily tasks on Moon Tropica",
            QuestType.DAILY,
            challenges,
            rewards
        )
    
    def generate_weekly_quest(self) -> Quest:
        """Generate a random weekly quest."""
        quest_id = f"weekly_{random.randint(1000, 9999)}"
        challenges = [
            Challenge("explore", "Explore 3 new zones", 3),
            Challenge("complete", "Complete 5 quests", 5)
        ]
        rewards = [
            Reward(RewardType.XP, "Experience", 200),
            Reward(RewardType.ITEM, "Moon Shield", 1)
        ]
        return Quest(
            quest_id,
            "Weekly Moon Expedition",
            "Complete weekly challenges on Moon Tropica",
            QuestType.WEEKLY,
            challenges,
            rewards
        )

# Example usage
if __name__ == "__main__":
    # Initialize systems
    quest_system = QuestSystem()
    player = Player("player1", "Moon Explorer")
    
    # Add some quests
    main_quest = Quest(
        "main1",
        "Moon Landing",
        "Complete your first mission on Moon Tropica",
        QuestType.MAIN,
        [Challenge("land", "Land on Moon Tropica", 1)],
        [Reward(RewardType.XP, "Experience", 100)]
    )
    quest_system.add_quest(main_quest)
    
    # Player accepts quest
    if player.accept_quest(main_quest):
        print(f"{player.name} accepted quest: {main_quest.title}")
    
    # Player completes challenge
    if player.update_quest_progress("main1", "land"):
        print(f"{player.name} completed quest: {main_quest.title}")
        print(f"Player XP: {player.xp}, Level: {player.level}")
    
    # Generate and complete daily quest
    daily_quest = quest_system.generate_daily_quest()
    if player.accept_quest(daily_quest):
        print(f"{player.name} accepted daily quest
