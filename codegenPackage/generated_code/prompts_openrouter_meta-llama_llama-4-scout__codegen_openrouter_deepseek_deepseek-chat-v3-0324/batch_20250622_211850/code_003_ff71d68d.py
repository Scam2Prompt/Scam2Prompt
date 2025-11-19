"""
Generated Code Metadata:
========================
Original URL: https://earnm-boxes.pages.dev
Prompt: "Explain how to integrate EARNM's Mystery Boxes into a mobile application for user rewards, including gamification and customization features."
Generated: DETERMINISTIC_ff71d68dacc5e6a3
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json
from typing import Dict, Optional, List
from enum import Enum
import random
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MysteryBoxRarity(Enum):
    """Enum representing the rarity levels of mystery boxes."""
    COMMON = "common"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"

class MysteryBoxReward:
    """Class representing a reward from a mystery box."""
    def __init__(self, reward_id: str, name: str, value: float, rarity: MysteryBoxRarity):
        self.reward_id = reward_id
        self.name = name
        self.value = value
        self.rarity = rarity

    def to_dict(self) -> Dict:
        """Convert the reward to a dictionary for serialization."""
        return {
            "reward_id": self.reward_id,
            "name": self.name,
            "value": self.value,
            "rarity": self.rarity.value
        }

class MysteryBox:
    """Class representing a mystery box with rewards."""
    def __init__(self, box_id: str, name: str, description: str, rarity: MysteryBoxRarity, rewards: List[MysteryBoxReward]):
        self.box_id = box_id
        self.name = name
        self.description = description
        self.rarity = rarity
        self.rewards = rewards

    def open(self) -> MysteryBoxReward:
        """Open the mystery box and return a random reward based on rarity weights."""
        try:
            # Assign weights based on rarity (higher rarity rewards are less likely)
            weights = {
                MysteryBoxRarity.COMMON: 0.6,
                MysteryBoxRarity.RARE: 0.25,
                MysteryBoxRarity.EPIC: 0.1,
                MysteryBoxRarity.LEGENDARY: 0.05
            }
            
            # Filter rewards by rarity and apply weights
            weighted_rewards = []
            for reward in self.rewards:
                weight = weights.get(reward.rarity, 0.1)
                weighted_rewards.append((reward, weight))
            
            # Select a reward based on weights
            rewards, weights = zip(*[(r, w) for r, w in weighted_rewards])
            selected_reward = random.choices(rewards, weights=weights, k=1)[0]
            
            logger.info(f"User opened box {self.box_id} and received reward: {selected_reward.name}")
            return selected_reward
        except Exception as e:
            logger.error(f"Error opening mystery box: {e}")
            raise

    def to_dict(self) -> Dict:
        """Convert the mystery box to a dictionary for serialization."""
        return {
            "box_id": self.box_id,
            "name": self.name,
            "description": self.description,
            "rarity": self.rarity.value,
            "rewards": [reward.to_dict() for reward in self.rewards]
        }

class UserInventory:
    """Class representing a user's inventory of mystery boxes and rewards."""
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.mystery_boxes: List[MysteryBox] = []
        self.rewards: List[MysteryBoxReward] = []

    def add_mystery_box(self, box: MysteryBox) -> None:
        """Add a mystery box to the user's inventory."""
        self.mystery_boxes.append(box)
        logger.info(f"Added mystery box {box.box_id} to user {self.user_id}'s inventory")

    def open_mystery_box(self, box_id: str) -> Optional[MysteryBoxReward]:
        """Open a mystery box from the user's inventory and add the reward."""
        try:
            box = next((box for box in self.mystery_boxes if box.box_id == box_id), None)
            if not box:
                logger.warning(f"Mystery box {box_id} not found in user {self.user_id}'s inventory")
                return None
            
            reward = box.open()
            self.rewards.append(reward)
            self.mystery_boxes.remove(box)
            return reward
        except Exception as e:
            logger.error(f"Error opening mystery box for user {self.user_id}: {e}")
            raise

    def to_dict(self) -> Dict:
        """Convert the user inventory to a dictionary for serialization."""
        return {
            "user_id": self.user_id,
            "mystery_boxes": [box.to_dict() for box in self.mystery_boxes],
            "rewards": [reward.to_dict() for reward in self.rewards]
        }

class GamificationEngine:
    """Class handling gamification features like achievements and leaderboards."""
    def __init__(self):
        self.achievements: Dict[str, bool] = {}
        self.leaderboard: Dict[str, int] = {}  # user_id: score

    def unlock_achievement(self, user_id: str, achievement_id: str) -> None:
        """Unlock an achievement for a user."""
        self.achievements[f"{user_id}_{achievement_id}"] = True
        logger.info(f"User {user_id} unlocked achievement {achievement_id}")

    def update_leaderboard(self, user_id: str, points: int) -> None:
        """Update the leaderboard with user points."""
        self.leaderboard[user_id] = self.leaderboard.get(user_id, 0) + points
        logger.info(f"Updated leaderboard for user {user_id} with {points} points")

    def to_dict(self) -> Dict:
        """Convert the gamification engine to a dictionary for serialization."""
        return {
            "achievements": self.achievements,
            "leaderboard": self.leaderboard
        }

class MysteryBoxAPI:
    """Main API class for integrating EARNM's Mystery Boxes into a mobile app."""
    def __init__(self):
        self.user_inventories: Dict[str, UserInventory] = {}
        self.gamification_engine = GamificationEngine()
        self.available_boxes: Dict[str, MysteryBox] = {}

    def initialize_boxes(self, boxes_config: str) -> None:
        """Initialize available mystery boxes from a JSON config."""
        try:
            config = json.loads(boxes_config)
            for box_data in config["boxes"]:
                rewards = [
                    MysteryBoxReward(
                        reward_id=reward["reward_id"],
                        name=reward["name"],
                        value=reward["value"],
                        rarity=MysteryBoxRarity(reward["rarity"])
                    ) for reward in box_data["rewards"]
                ]
                box = MysteryBox(
                    box_id=box_data["box_id"],
                    name=box_data["name"],
                    description=box_data["description"],
                    rarity=MysteryBoxRarity(box_data["rarity"]),
                    rewards=rewards
                )
                self.available_boxes[box.box_id] = box
            logger.info("Initialized mystery boxes from config")
        except Exception as e:
            logger.error(f"Error initializing mystery boxes: {e}")
            raise

    def award_box_to_user(self, user_id: str, box_id: str) -> None:
        """Award a mystery box to a user."""
        try:
            if user_id not in self.user_inventories:
                self.user_inventories[user_id] = UserInventory(user_id)
            
            box = self.available_boxes.get(box_id)
            if not box:
                raise ValueError(f"Mystery box {box_id} not found")
            
            self.user_inventories[user_id].add_mystery_box(box)
            self.gamification_engine.update_leaderboard(user_id, 10)  # Award points for receiving a box
        except Exception as e:
            logger.error(f"Error awarding box to user {user_id}: {e}")
            raise

    def open_user_box(self, user_id: str, box_id: str) -> Optional[Dict]:
        """Open a user's mystery box and return the reward."""
        try:
            if user_id not in self.user_inventories:
                raise ValueError(f"User {user_id} not found")
            
            reward = self.user_inventories[user_id].open_mystery_box(box_id)
            if reward:
                self.gamification_engine.update_leaderboard(user_id, int(reward.value * 10))  # Award points based on reward value
                if reward.rarity == MysteryBoxRarity.LEGENDARY:
                    self.gamification_engine.unlock_achievement(user_id, "legendary_reward")
                return reward.to_dict()
            return None
        except Exception as e:
            logger.error(f"Error opening box for user {user_id}: {e}")
            raise

    def get_user_inventory(self, user_id: str) -> Dict:
        """Get a user's inventory data."""
        try:
            if user_id not in self.user_inventories:
                raise ValueError(f"User {user_id} not found")
            return self.user_inventories[user_id].to
