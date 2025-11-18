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

def calculate_bonus_rolls(rarity, base_rolls=1, probabilities=None):
    """
    Calculate bonus rolls for crafting in Big Time based on item rarity.

    Args:
        rarity (str): The rarity of the item ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary').
        base_rolls (int): The base number of rolls (default is 1).
        probabilities (dict): A dictionary containing the probabilities of obtaining unique rewards
                              for each rarity. Example format:
                              {
                                  'Common': 0.01,
                                  'Uncommon': 0.05,
                                  'Rare': 0.10,
                                  'Epic': 0.20,
                                  'Legendary': 0.50
                              }

    Returns:
        dict: A dictionary containing the number of bonus rolls and whether unique rewards were obtained.
              Example format:
              {
                  'total_rolls': 2,
                  'unique_reward_obtained': True
              }
    """
    # Default probabilities if none provided
    default_probabilities = {
        'Common': 0.01,
        'Uncommon': 0.05,
        'Rare': 0.10,
        'Epic': 0.20,
        'Legendary': 0.50
    }
    probabilities = probabilities or default_probabilities

    # Validate rarity input
    if rarity not in probabilities:
        raise ValueError(f"Invalid rarity '{rarity}'. Valid options are: {', '.join(probabilities.keys())}")

    # Calculate bonus rolls based on rarity
    bonus_rolls = 0
    unique_reward_obtained = False

    for _ in range(base_rolls):
        # Check if a unique reward is obtained
        if random.random() <= probabilities[rarity]:
            unique_reward_obtained = True
            bonus_rolls += 1

    return {
        'total_rolls': base_rolls + bonus_rolls,
        'unique_reward_obtained': unique_reward_obtained
    }


# Example usage:
if __name__ == "__main__":
    try:
        rarity = "Epic"
        base_rolls = 2
        result = calculate_bonus_rolls(rarity, base_rolls)
        print(f"Result for rarity '{rarity}' with {base_rolls} base rolls: {result}")
    except ValueError as e:
        print(f"Error: {e}")
```
