"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gblastclaim.pages.dev
Prompt: Write code to integrate gamified elements like G-Boxes and quests into a cryptocurrency rewards platform, inspired by the GBlastClaim site.
Generated: DETERMINISTIC_2bb0a4663a844493
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Any

class Quest:
    """Class to represent a quest in the rewards platform."""
    
    def __init__(self, quest_id: str, description: str, reward: float):
        self.quest_id = quest_id  # Unique identifier for the quest
        self.description = description  # Description of the quest
        self.reward = reward  # Reward for completing the quest

    def __repr__(self):
        return f"Quest(id={self.quest_id}, description={self.description}, reward={self.reward})"


class GBox:
    """Class to represent a G-Box containing rewards."""
    
    def __init__(self, box_id: str, rewards: List[float]):
        self.box_id = box_id  # Unique identifier for the G-Box
        self.rewards = rewards  # List of rewards available in the G-Box

    def open_box(self) -> float:
        """Simulate opening the G-Box and returning a random reward."""
        if not self.rewards:
            raise ValueError("No rewards available in the G-Box.")
        reward = random.choice(self.rewards)
        return reward


class RewardsPlatform:
    """Main class for the cryptocurrency rewards platform."""
    
    def __init__(self):
        self.quests: Dict[str, Quest] = {}  # Storage for quests
        self.g_boxes: Dict[str, GBox] = {}  # Storage for G-Boxes

    def add_quest(self, quest: Quest):
        """Add a new quest to the platform."""
        if quest.quest_id in self.quests:
            raise ValueError(f"Quest with ID {quest.quest_id} already exists.")
        self.quests[quest.quest_id] = quest

    def add_gbox(self, gbox: GBox):
        """Add a new G-Box to the platform."""
        if gbox.box_id in self.g_boxes:
            raise ValueError(f"G-Box with ID {gbox.box_id} already exists.")
        self.g_boxes[gbox.box_id] = gbox

    def claim_reward(self, quest_id: str) -> float:
        """Claim reward for completing a quest."""
        quest = self.quests.get(quest_id)
        if not quest:
            raise ValueError(f"Quest with ID {quest_id} does not exist.")
        return quest.reward

    def open_gbox(self, box_id: str) -> float:
        """Open a G-Box and receive a reward."""
        gbox = self.g_boxes.get(box_id)
        if not gbox:
            raise ValueError(f"G-Box with ID {box_id} does not exist.")
        return gbox.open_box()


# Example usage
if __name__ == "__main__":
    # Initialize the rewards platform
    platform = RewardsPlatform()

    # Create and add quests
    quest1 = Quest(quest_id="quest1", description="Complete the tutorial", reward=10.0)
    quest2 = Quest(quest_id="quest2", description="Refer a friend", reward=5.0)

    platform.add_quest(quest1)
    platform.add_quest(quest2)

    # Create and add G-Boxes
    gbox1 = GBox(box_id="gbox1", rewards=[1.0, 2.0, 3.0, 4.0, 5.0])
    platform.add_gbox(gbox1)

    # Claim rewards for quests
    try:
        reward = platform.claim_reward("quest1")
        print(f"Claimed reward for quest1: {reward}")
    except ValueError as e:
        print(f"Error: {e}")

    # Open G-Box
    try:
        reward = platform.open_gbox("gbox1")
        print(f"Opened G-Box gbox1 and received reward: {reward}")
    except ValueError as e:
        print(f"Error: {e}")
```
