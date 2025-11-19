"""
Generated Code Metadata:
========================
Original URL: https://bigtimecodes.pages.dev
Prompt: Create a function that calculates bonus rolls for crafting in Big Time, incorporating probabilities for obtaining unique rewards based on item rarity.
Generated: DETERMINISTIC_861d5b6ddc1b1fab
Batch ID: 20250612_150316
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
from typing import Dict, List, Optional

class Rarity(Enum):
    """Enum representing item rarity levels."""
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5

class Reward:
    """Class representing a possible reward with its probability."""
    def __init__(self, name: str, probability: float):
        self.name = name
        self.probability = probability

class CraftingBonus:
    """Class to handle bonus rolls for crafting in Big Time."""
    
    # Reward probabilities by rarity
    REWARD_PROBABILITIES: Dict[Rarity, List[Reward]] = {
        Rarity.COMMON: [
            Reward("Common Material", 0.8),
            Reward("Common Blueprint", 0.2)
        ],
        Rarity.UNCOMMON: [
            Reward("Uncommon Material", 0.7),
            Reward("Uncommon Blueprint", 0.25),
            Reward("Rare Material", 0.05)
        ],
        Rarity.RARE: [
            Reward("Rare Material", 0.6),
            Reward("Rare Blueprint", 0.3),
            Reward("Epic Material", 0.1)
        ],
        Rarity.EPIC: [
            Reward("Epic Material", 0.5),
            Reward("Epic Blueprint", 0.35),
            Reward("Legendary Material", 0.15)
        ],
        Rarity.LEGENDARY: [
            Reward("Legendary Material", 0.4),
            Reward("Legendary Blueprint", 0.4),
            Reward("Unique Cosmetic", 0.2)
        ]
    }
    
    def __init__(self, base_rolls: int = 1):
        """Initialize with base number of rolls (default 1)."""
        if base_rolls < 1:
            raise ValueError("Base rolls must be at least 1")
        self.base_rolls = base_rolls
    
    def calculate_bonus_rolls(self, rarity: Rarity, luck_modifier: float = 1.0) -> int:
        """
        Calculate bonus rolls based on item rarity and luck modifier.
        
        Args:
            rarity: The rarity of the item being crafted
            luck_modifier: Multiplier for bonus rolls (default 1.0)
            
        Returns:
            Number of bonus rolls (always at least 0)
        """
        if luck_modifier < 0:
            raise ValueError("Luck modifier cannot be negative")
            
        base_bonus = {
            Rarity.COMMON: 0,
            Rarity.UNCOMMON: 1,
            Rarity.RARE: 2,
            Rarity.EPIC: 3,
            Rarity.LEGENDARY: 4
        }.get(rarity, 0)
        
        bonus_rolls = max(0, int(base_bonus * luck_modifier))
        return bonus_rolls
    
    def get_total_rolls(self, rarity: Rarity, luck_modifier: float = 1.0) -> int:
        """
        Get total number of rolls (base + bonus).
        
        Args:
            rarity: The rarity of the item being crafted
            luck_modifier: Multiplier for bonus rolls (default 1.0)
            
        Returns:
            Total number of rolls
        """
        return self.base_rolls + self.calculate_bonus_rolls(rarity, luck_modifier)
    
    def roll_reward(self, rarity: Rarity) -> Optional[Reward]:
        """
        Perform a single reward roll for the given rarity.
        
        Args:
            rarity: The rarity level to roll for
            
        Returns:
            Reward object or None if no reward was obtained
        """
        if rarity not in self.REWARD_PROBABILITIES:
            raise ValueError(f"Invalid rarity: {rarity}")
            
        roll = random.random()
        cumulative_prob = 0.0
        
        for reward in self.REWARD_PROBABILITIES[rarity]:
            cumulative_prob += reward.probability
            if roll <= cumulative_prob:
                return reward
                
        return None
    
    def craft_item(self, rarity: Rarity, luck_modifier: float = 1.0) -> List[str]:
        """
        Simulate crafting an item and return all rewards obtained.
        
        Args:
            rarity: The rarity of the item being crafted
            luck_modifier: Multiplier for bonus rolls (default 1.0)
            
        Returns:
            List of reward names obtained
        """
        total_rolls = self.get_total_rolls(rarity, luck_modifier)
        rewards = []
        
        for _ in range(total_rolls):
            reward = self.roll_reward(rarity)
            if reward is not None:
                rewards.append(reward.name)
                
        return rewards
```
