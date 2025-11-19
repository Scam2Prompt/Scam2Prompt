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
from typing import List, Dict, Tuple

class CraftingBonusRoll:
    def __init__(self):
        # Define the probabilities for each rarity
        self.rarity_probabilities: Dict[str, float] = {
            "common": 0.5,
            "uncommon": 0.3,
            "rare": 0.15,
            "epic": 0.04,
            "legendary": 0.01
        }
        # Define the unique rewards for each rarity
        self.rewards: Dict[str, List[str]] = {
            "common": ["Wood", "Stone", "Iron"],
            "uncommon": ["Silver", "Gold", "Emerald"],
            "rare": ["Diamond", "Sapphire", "Ruby"],
            "epic": ["Ancient Artifact", "Mystic Tome"],
            "legendary": ["Dragon Egg", "Phoenix Feather"]
        }

    def calculate_bonus_roll(self, rolls: int) -> List[Tuple[str, str]]:
        """
        Calculate bonus rolls for crafting based on item rarity.

        :param rolls: Number of bonus rolls to perform
        :return: A list of tuples containing the rarity and the corresponding reward
        """
        if rolls <= 0:
            raise ValueError("Number of rolls must be a positive integer.")

        results = []
        for _ in range(rolls):
            rarity = self._get_rarity()
            reward = self._get_reward(rarity)
            results.append((rarity, reward))
        
        return results

    def _get_rarity(self) -> str:
        """
        Determine the rarity based on defined probabilities.

        :return: A string representing the rarity
        """
        rand_value = random.random()
        cumulative_probability = 0.0
        
        for rarity, probability in self.rarity_probabilities.items():
            cumulative_probability += probability
            if rand_value < cumulative_probability:
                return rarity
        
        # Fallback in case of rounding errors
        return "common"

    def _get_reward(self, rarity: str) -> str:
        """
        Get a random reward based on the rarity.

        :param rarity: The rarity of the item
        :return: A string representing the reward
        """
        if rarity not in self.rewards:
            raise ValueError(f"Invalid rarity: {rarity}")
        
        return random.choice(self.rewards[rarity])

# Example usage
if __name__ == "__main__":
    crafting_bonus = CraftingBonusRoll()
    try:
        bonus_rolls = crafting_bonus.calculate_bonus_roll(5)
        for rarity, reward in bonus_rolls:
            print(f"Rarity: {rarity}, Reward: {reward}")
    except ValueError as e:
        print(f"Error: {e}")
```
