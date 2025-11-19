"""
Generated Code Metadata:
========================
Original URL: https://moontropica.pages.dev
Prompt: Generate code for a quest system that allows players to earn XP and rewards in a game similar to Moon Tropica.
Generated: DETERMINISTIC_7bc70731c976115d
Batch ID: 20250612_163518
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

class QuestStatus(Enum):
    """Enum representing the status of a quest."""
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class Reward:
    """Class representing a quest reward."""
    def __init__(self, xp: int, items: Optional[Dict[str, int]] = None):
        """
        Initialize a Reward object.
        
        Args:
            xp (int): Experience points awarded.
            items (Optional[Dict[str, int]]): Dictionary of item names and quantities.
        """
        self.xp = xp
        self.items = items if items else {}

    def to_dict(self) -> Dict:
        """Convert the Reward object to a dictionary."""
        return {
            "xp": self.xp,
            "items": self.items
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Reward':
        """Create a Reward object from a dictionary."""
        return cls(
            xp=data["xp"],
            items=data.get("items", {})
        )

class Quest:
    """Class representing a quest."""
    def __init__(
        self,
        quest_id: str,
        title: str,
        description: str,
        objectives: List[str],
        reward: Reward,
        required_level: int = 1
    ):
        """
        Initialize a Quest object.
        
        Args:
            quest_id (str): Unique identifier for the quest.
            title (str): Title of the quest.
            description (str): Description of the quest.
            objectives (List[str]): List of objectives to complete the quest.
            reward (Reward): Reward for completing the quest.
            required_level (int): Minimum level required to start the quest.
        """
        self.quest_id = quest_id
        self.title = title
        self.description = description
        self.objectives = objectives
        self.reward = reward
        self.required_level = required_level
        self.status = QuestStatus.NOT_STARTED
        self.completed_objectives = []

    def start_quest(self) -> None:
        """Mark the quest as started if not already started."""
        if self.status == QuestStatus.NOT_STARTED:
            self.status = QuestStatus.IN_PROGRESS

    def complete_objective(self, objective: str) -> bool:
        """
        Mark an objective as completed.
        
        Args:
            objective (str): The objective to complete.
            
        Returns:
            bool: True if the objective was completed, False otherwise.
        """
        if (
            self.status == QuestStatus.IN_PROGRESS
            and objective in self.objectives
            and objective not in self.completed_objectives
        ):
            self.completed_objectives.append(objective)
            return True
        return False

    def complete_quest(self) -> bool:
        """
        Mark the quest as completed if all objectives are done.
        
        Returns:
            bool: True if the quest was completed, False otherwise.
        """
        if (
            self.status == QuestStatus.IN_PROGRESS
            and set(self.completed_objectives) == set(self.objectives)
        ):
            self.status = QuestStatus.COMPLETED
            return True
        return False

    def to_dict(self) -> Dict:
        """Convert the Quest object to a dictionary."""
        return {
            "quest_id": self.quest_id,
            "title": self.title,
            "description": self.description,
            "objectives": self.objectives,
            "reward": self.reward.to_dict(),
            "required_level": self.required_level,
            "status": self.status.value,
            "completed_objectives": self.completed_objectives
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Quest':
        """Create a Quest object from a dictionary."""
        quest = cls(
            quest_id=data["quest_id"],
            title=data["title"],
            description=data["description"],
            objectives=data["objectives"],
            reward=Reward.from_dict(data["reward"]),
            required_level=data.get("required_level", 1)
        )
        quest.status = QuestStatus(data["status"])
        quest.completed_objectives = data.get("completed_objectives", [])
        return quest

class Player:
    """Class representing a player."""
    def __init__(self, player_id: str, name: str, level: int = 1, xp: int = 0):
        """
        Initialize a Player object.
        
        Args:
            player_id (str): Unique identifier for the player.
            name (str): Name of the player.
            level (int): Current level of the player.
            xp (int): Current experience points of the player.
        """
        self.player_id = player_id
        self.name = name
        self.level = level
        self.xp = xp
        self.inventory = {}
        self.active_quests = {}
        self.completed_quests = []

    def add_xp(self, xp: int) -> None:
        """Add experience points to the player."""
        self.xp += xp
        self._check_level_up()

    def _check_level_up(self) -> None:
        """Check if the player has enough XP to level up."""
        xp_needed = self.level * 100
        if self.xp >= xp_needed:
            self.level += 1
            self.xp -= xp_needed

    def add_to_inventory(self, item: str, quantity: int = 1) -> None:
        """Add an item to the player's inventory."""
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

    def start_quest(self, quest: Quest) -> bool:
        """
        Start a quest if the player meets the requirements.
        
        Args:
            quest (Quest): The quest to start.
            
        Returns:
            bool: True if the quest was started, False otherwise.
        """
        if (
            quest.quest_id not in self.active_quests
            and quest.quest_id not in self.completed_quests
            and self.level >= quest.required_level
        ):
            quest.start_quest()
            self.active_quests[quest.quest_id] = quest
            return True
        return False

    def complete_quest(self, quest_id: str) -> bool:
        """
        Complete a quest and grant rewards to the player.
        
        Args:
            quest_id (str): The ID of the quest to complete.
            
        Returns:
            bool: True if the quest was completed, False otherwise.
        """
        if quest_id in self.active_quests:
            quest = self.active_quests[quest_id]
            if quest.complete_quest():
                self.add_xp(quest.reward.xp)
                for item, quantity in quest.reward.items.items():
                    self.add_to_inventory(item, quantity)
                self.completed_quests.append(quest_id)
                del self.active_quests[quest_id]
                return True
        return False

    def to_dict(self) -> Dict:
        """Convert the Player object to a dictionary."""
        return {
            "player_id": self.player_id,
            "name": self.name,
            "level": self.level,
            "xp": self.xp,
            "inventory": self.inventory,
            "active_quests": {k: v.to_dict() for k, v in self.active_quests.items()},
            "completed_quests": self.completed_quests
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Player':
        """Create a Player object from a dictionary."""
        player = cls(
            player_id=data["player_id"],
            name=data["name"],
            level=data["level"],
            xp=data["xp"]
        )
        player.inventory = data.get("inventory", {})
        player.active_quests = {
            k: Quest.from_dict(v) for k, v in data.get("active_quests", {}).items()
        }
        player.completed_quests = data.get("completed_quests", [])
        return player

class QuestSystem:
    """Class representing a quest system."""
    def __init__(self):
        """Initialize the QuestSystem."""
        self.quests = {}
        self.players = {}

    def add_quest(self, quest: Quest) -> None:
        """Add a quest to the system."""
        self.quests[quest.quest_id] = quest

    def register_player(self, player: Player) -> None:
        """Register a player to the system."""
        self.players[player.player_id] = player

    def save_state(self, file_path: str) -> bool:
        """
        Save the current state of the quest system to a file.
        
        Args:
            file_path (str): Path to the save file.
            
        Returns:
            bool: True if the save was successful, False otherwise.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump({
                    "quests": {k: v.to_dict() for k, v in self.quest
