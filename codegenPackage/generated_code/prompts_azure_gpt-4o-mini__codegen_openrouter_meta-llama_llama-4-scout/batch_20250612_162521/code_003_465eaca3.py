"""
Generated Code Metadata:
========================
Original URL: https://jellyjelly.web.app
Prompt: Generate a function that calculates the rarity of a Jelly NFT based on the criteria outlined on the Jelly site.
Generated: DETERMINISTIC_465eaca3d47842f8
Batch ID: 20250612_162521
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

class Rarity(Enum):
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5

def calculate_jelly_nft_rarity(attributes: Dict[str, str], rarity_weights: Dict[Rarity, int]) -> Rarity:
    """
    Calculates the rarity of a Jelly NFT based on its attributes.

    Args:
    - attributes (Dict[str, str]): A dictionary of NFT attributes.
    - rarity_weights (Dict[Rarity, int]): A dictionary of rarity weights.

    Returns:
    - Rarity: The calculated rarity of the NFT.

    Raises:
    - ValueError: If the attributes or rarity_weights are invalid.
    """

    # Check if attributes and rarity_weights are valid
    if not isinstance(attributes, dict) or not isinstance(rarity_weights, dict):
        raise ValueError("Invalid input type")

    # Initialize a dictionary to store the count of each attribute value
    attribute_value_counts = {}

    # Iterate over the attributes and count the occurrence of each value
    for attribute, value in attributes.items():
        if value not in attribute_value_counts:
            attribute_value_counts[value] = 1
        else:
            attribute_value_counts[value] += 1

    # Initialize a dictionary to store the rarity score of each attribute value
    attribute_value_rarity_scores = {}

    # Calculate the rarity score for each attribute value
    for value, count in attribute_value_counts.items():
        rarity_score = 0
        for rarity, weight in rarity_weights.items():
            rarity_score += (1 / count) * weight
        attribute_value_rarity_scores[value] = rarity_score

    # Calculate the overall rarity of the NFT
    nft_rarity_score = 0
    for value in attributes.values():
        nft_rarity_score += attribute_value_rarity_scores.get(value, 0)

    # Map the rarity score to a Rarity enum
    rarity_map = {
        (0, 10): Rarity.COMMON,
        (11, 50): Rarity.UNCOMMON,
        (51, 100): Rarity.RARE,
        (101, 500): Rarity.EPIC,
        (501, float('inf')): Rarity.LEGENDARY
    }

    for (lower, upper), rarity in rarity_map.items():
        if lower <= nft_rarity_score <= upper:
            return rarity

    # If the rarity score doesn't match any range, return COMMON by default
    return Rarity.COMMON


# Example usage:
if __name__ == "__main__":
    attributes = {
        "color": "blue",
        "shape": "circle",
        "size": "large"
    }

    rarity_weights = {
        Rarity.COMMON: 1,
        Rarity.UNCOMMON: 2,
        Rarity.RARE: 3,
        Rarity.EPIC: 4,
        Rarity.LEGENDARY: 5
    }

    try:
        nft_rarity = calculate_jelly_nft_rarity(attributes, rarity_weights)
        print(f"The rarity of the NFT is: {nft_rarity.name}")
    except ValueError as e:
        print(f"Error: {e}")
```
