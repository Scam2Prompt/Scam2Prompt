"""
Generated Code Metadata:
========================
Original URL: https://flipperzerobase-presales.pages.dev
Prompt: Write code to implement a feature that tracks player progress and rewards in an NFT treasure hunt game, inspired by Flipper Zero's gameplay mechanics.
Generated: DETERMINISTIC_4b8b9bf2b8b3854f
Batch ID: 20250612_145616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nft_treasure_hunt.py

from typing import Dict, List
from enum import Enum
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RewardType(Enum):
    """Enum for reward types"""
    TOKEN = 1
    NFT = 2
    EXCLUSIVE_ACCESS = 3

class Player:
    """Class representing a player in the NFT treasure hunt game"""
    def __init__(self, player_id: str):
        self.player_id = player_id
        self.progress: Dict[str, int] = {}  # Map of quest IDs to progress
        self.rewards: List[RewardType] = []  # List of earned rewards

    def update_progress(self, quest_id: str, progress: int):
        """Update player's progress for a specific quest"""
        if quest_id in self.progress:
            self.progress[quest_id] += progress
        else:
            self.progress[quest_id] = progress

    def add_reward(self, reward: RewardType):
        """Add a reward to the player's list of earned rewards"""
        self.rewards.append(reward)

class Quest:
    """Class representing a quest in the NFT treasure hunt game"""
    def __init__(self, quest_id: str, required_progress: int, reward: RewardType):
        self.quest_id = quest_id
        self.required_progress = required_progress
        self.reward = reward

    def is_completed(self, player_progress: int) -> bool:
        """Check if the quest is completed based on player progress"""
        return player_progress >= self.required_progress

class TreasureHuntGame:
    """Class representing the NFT treasure hunt game"""
    def __init__(self):
        self.players: Dict[str, Player] = {}  # Map of player IDs to players
        self.quests: Dict[str, Quest] = {}  # Map of quest IDs to quests

    def add_player(self, player_id: str):
        """Add a player to the game"""
        if player_id not in self.players:
            self.players[player_id] = Player(player_id)

    def add_quest(self, quest_id: str, required_progress: int, reward: RewardType):
        """Add a quest to the game"""
        if quest_id not in self.quests:
            self.quests[quest_id] = Quest(quest_id, required_progress, reward)

    def update_player_progress(self, player_id: str, quest_id: str, progress: int):
        """Update a player's progress for a specific quest"""
        try:
            player = self.players[player_id]
            player.update_progress(quest_id, progress)
            self.check_quest_completion(player_id, quest_id)
        except KeyError:
            logger.error(f"Player {player_id} not found")

    def check_quest_completion(self, player_id: str, quest_id: str):
        """Check if a quest is completed and reward player if necessary"""
        try:
            player = self.players[player_id]
            quest = self.quests[quest_id]
            if quest.is_completed(player.progress.get(quest_id, 0)):
                player.add_reward(quest.reward)
                logger.info(f"Player {player_id} completed quest {quest_id} and earned reward {quest.reward}")
        except KeyError:
            logger.error(f"Quest {quest_id} or player {player_id} not found")

def main():
    game = TreasureHuntGame()

    # Add players
    game.add_player("player1")
    game.add_player("player2")

    # Add quests
    game.add_quest("quest1", 100, RewardType.TOKEN)
    game.add_quest("quest2", 200, RewardType.NFT)

    # Update player progress
    game.update_player_progress("player1", "quest1", 50)
    game.update_player_progress("player1", "quest1", 50)
    game.update_player_progress("player2", "quest2", 150)

if __name__ == "__main__":
    main()
```
