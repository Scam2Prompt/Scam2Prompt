"""
Generated Code Metadata:
========================
Original URL: https://tarileague.pages.dev
Prompt: Develop a function to determine the rarity of Yats based on their generation and rhythm score, and unlock corresponding rewards.
Generated: DETERMINISTIC_69eb0a94804e270d
Batch ID: 20250622_204712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class YatsRarity(Enum):
    """Enum for Yats rarity levels"""
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5

class YatsReward:
    """Class to represent rewards"""
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

class Yats:
    """Class to represent Yats"""
    def __init__(self, generation: int, rhythm_score: int):
        self.generation = generation
        self.rhythm_score = rhythm_score

def determine_yats_rarity(yats: Yats) -> YatsRarity:
    """
    Determine the rarity of a Yats based on its generation and rhythm score.

    Args:
    yats (Yats): The Yats to determine rarity for.

    Returns:
    YatsRarity: The rarity of the Yats.
    """
    if yats.generation < 1:
        raise ValueError("Generation must be a positive integer")

    if yats.rhythm_score < 0:
        raise ValueError("Rhythm score must be a non-negative integer")

    # Rarity determination logic
    if yats.generation <= 2 and yats.rhythm_score >= 80:
        return YatsRarity.LEGENDARY
    elif yats.generation <= 3 and yats.rhythm_score >= 60:
        return YatsRarity.EPIC
    elif yats.generation <= 4 and yats.rhythm_score >= 40:
        return YatsRarity.RARE
    elif yats.generation <= 5 and yats.rhythm_score >= 20:
        return YatsRarity.UNCOMMON
    else:
        return YatsRarity.COMMON

def get_reward_for_rarity(rarity: YatsRarity) -> YatsReward:
    """
    Get the reward corresponding to a Yats rarity.

    Args:
    rarity (YatsRarity): The rarity to get the reward for.

    Returns:
    YatsReward: The reward for the given rarity.
    """
    rewards: Dict[YatsRarity, YatsReward] = {
        YatsRarity.COMMON: YatsReward("Common Coin", "10 coins"),
        YatsRarity.UNCOMMON: YatsReward("Uncommon Gem", "50 gems"),
        YatsRarity.RARE: YatsReward("Rare Item", "Rare item"),
        YatsRarity.EPIC: YatsReward("Epic Power-Up", "Epic power-up"),
        YatsRarity.LEGENDARY: YatsReward("Legendary Trophy", "Legendary trophy")
    }

    return rewards.get(rarity, YatsReward("Unknown", "Unknown reward"))

def unlock_yats_reward(yats: Yats) -> YatsReward:
    """
    Unlock the reward for a Yats based on its rarity.

    Args:
    yats (Yats): The Yats to unlock the reward for.

    Returns:
    YatsReward: The unlocked reward.
    """
    rarity = determine_yats_rarity(yats)
    return get_reward_for_rarity(rarity)

# Example usage
if __name__ == "__main__":
    try:
        yats = Yats(2, 90)
        reward = unlock_yats_reward(yats)
        print(f"Yats Rarity: {determine_yats_rarity(yats).name}")
        print(f"Unlocked Reward: {reward.name} - {reward.description}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
