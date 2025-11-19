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
from typing import Dict, List

class Rarity(Enum):
    """Item rarity levels"""
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5

class Reward:
    """Represents a reward with its rarity and probability"""
    def __init__(self, name: str, rarity: Rarity, probability: float):
        self.name = name
        self.rarity = rarity
        self.probability = probability

def calculate_bonus_rolls(num_rolls: int, rewards: List[Reward]) -> Dict[Rarity, int]:
    """
    Calculate bonus rolls for crafting in Big Time.

    Args:
    - num_rolls (int): The number of bonus rolls.
    - rewards (List[Reward]): A list of rewards with their probabilities.

    Returns:
    - A dictionary with the count of each rarity level obtained.
    """
    # Validate input
    if num_rolls <= 0:
        raise ValueError("Number of rolls must be greater than 0")

    # Normalize probabilities to ensure they add up to 1
    total_probability = sum(reward.probability for reward in rewards)
    if abs(total_probability - 1) > 1e-6:
        raise ValueError("Probabilities do not add up to 1")

    # Initialize result dictionary
    result = {rarity: 0 for rarity in Rarity}

    # Perform bonus rolls
    for _ in range(num_rolls):
        roll = random.random()
        cumulative_probability = 0
        for reward in rewards:
            cumulative_probability += reward.probability
            if roll <= cumulative_probability:
                result[reward.rarity] += 1
                break

    return result

def main():
    # Define rewards with their probabilities
    rewards = [
        Reward("Common Item", Rarity.COMMON, 0.5),
        Reward("Uncommon Item", Rarity.UNCOMMON, 0.3),
        Reward("Rare Item", Rarity.RARE, 0.15),
        Reward("Epic Item", Rarity.EPIC, 0.05),
        Reward("Legendary Item", Rarity.LEGENDARY, 0.01),
    ]

    # Calculate bonus rolls
    num_rolls = 10000
    result = calculate_bonus_rolls(num_rolls, rewards)

    # Print result
    print("Rarity\tCount")
    for rarity, count in result.items():
        print(f"{rarity.name}\t{count} ({count / num_rolls * 100:.2f}%)")

if __name__ == "__main__":
    main()
```
