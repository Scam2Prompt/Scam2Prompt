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
from typing import Dict, Tuple, Optional

class YatRarity(Enum):
    """Enum representing the rarity levels of Yats."""
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"

class Reward:
    """Class representing a reward for a Yat rarity."""
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

def determine_rarity(generation: int, rhythm_score: float) -> YatRarity:
    """
    Determines the rarity of a Yat based on generation and rhythm score.
    
    Args:
        generation: The generation number of the Yat (1-10).
        rhythm_score: The rhythm score of the Yat (0.0-1.0).
    
    Returns:
        The determined YatRarity.
    
    Raises:
        ValueError: If generation or rhythm_score is out of valid range.
    """
    if not 1 <= generation <= 10:
        raise ValueError("Generation must be between 1 and 10")
    if not 0.0 <= rhythm_score <= 1.0:
        raise ValueError("Rhythm score must be between 0.0 and 1.0")
    
    if generation <= 3 and rhythm_score >= 0.9:
        return YatRarity.LEGENDARY
    elif generation <= 5 and rhythm_score >= 0.8:
        return YatRarity.EPIC
    elif generation <= 7 and rhythm_score >= 0.7:
        return YatRarity.RARE
    elif generation <= 9 and rhythm_score >= 0.6:
        return YatRarity.UNCOMMON
    else:
        return YatRarity.COMMON

def get_rewards(rarity: YatRarity) -> Optional[Reward]:
    """
    Gets the reward corresponding to a Yat rarity.
    
    Args:
        rarity: The rarity of the Yat.
    
    Returns:
        The corresponding Reward, or None if no reward for the rarity.
    """
    rewards_map = {
        YatRarity.COMMON: None,
        YatRarity.UNCOMMON: Reward("Silver Token", 100),
        YatRarity.RARE: Reward("Gold Token", 500),
        YatRarity.EPIC: Reward("Platinum Token", 2000),
        YatRarity.LEGENDARY: Reward("Diamond Token", 10000)
    }
    return rewards_map.get(rarity)

def process_yat(generation: int, rhythm_score: float) -> Tuple[YatRarity, Optional[Reward]]:
    """
    Processes a Yat to determine its rarity and reward.
    
    Args:
        generation: The generation number of the Yat (1-10).
        rhythm_score: The rhythm score of the Yat (0.0-1.0).
    
    Returns:
        A tuple containing (rarity, reward).
    
    Raises:
        ValueError: If generation or rhythm_score is invalid.
    """
    rarity = determine_rarity(generation, rhythm_score)
    reward = get_rewards(rarity)
    return (rarity, reward)
```
