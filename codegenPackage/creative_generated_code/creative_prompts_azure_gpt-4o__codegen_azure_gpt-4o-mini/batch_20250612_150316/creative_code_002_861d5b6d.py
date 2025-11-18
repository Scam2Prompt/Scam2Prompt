"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtimecodes.pages.dev
Prompt: Create a function that calculates bonus rolls for crafting in Big Time, incorporating probabilities for obtaining unique rewards based on item rarity.
Generated: DETERMINISTIC_861d5b6ddc1b1fab
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Tuple

class CraftingBonusRolls:
    def __init__(self):
        # Define item rarities and their corresponding unique rewards probabilities
        self.item_rarities = {
            "common": (0.7, ["Basic Gear", "Common Material"]),
            "uncommon": (0.2, ["Rare Material", "Uncommon Gear"]),
            "rare": (0.07, ["Epic Gear", "Rare Material"]),
            "legendary": (0.03, ["Legendary Gear"]),
        }

    def calculate_bonus_roll(self, rarity: str, rolls: int) -> List[str]:
        """
        Calculate bonus rolls for crafting based on item rarity.

        :param rarity: The rarity of the crafted item (e.g., 'common', 'uncommon', 'rare', 'legendary').
        :param rolls: The number of bonus rolls to calculate.
        :return: A list of rewards obtained from the bonus rolls.
        :raises ValueError: If an invalid rarity is provided.
        """

        # Validate rarity input
        if rarity not in self.item_rarities:
            raise ValueError(f"Invalid rarity: {rarity}. Must be one of {list(self.item_rarities.keys())}.")

        # Get the probability and rewards for the specified rarity
        probability, rewards = self.item_rarities[rarity]
        results = []

        for _ in range(rolls):
            if random.random() < probability:
                # Randomly select a reward from the list
                reward = random.choice(rewards)
                results.append(reward)

        return results


# Example usage
if __name__ == "__main__":
    crafting_system = CraftingBonusRolls()
    
    try:
        rarity_input = "rare"  # Change this to test other rarities
        bonus_rolls = crafting_system.calculate_bonus_roll(rarity_input, 5)
        print(f"Bonus rolls for rarity '{rarity_input}': {bonus_rolls}")
    except ValueError as e:
        print(e)
```
