"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnm-boxes.pages.dev
Prompt: Create a function that calculates the potential earnings from opening a Mystery Box based on its rarity and contents in the $EARNM system.
Generated: DETERMINISTIC_157b993db82cce2e
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict

# Define constants for rarity multipliers
RARITY_MULTIPLIERS = {
    "common": 1.0,
    "uncommon": 1.5,
    "rare": 2.0,
    "epic": 3.0,
    "legendary": 5.0
}

def calculate_potential_earnings(rarity: str, contents: List[Dict[str, float]]) -> float:
    """
    Calculate the potential earnings from opening a Mystery Box.

    Args:
        rarity (str): The rarity level of the Mystery Box. Accepted values are:
                      'common', 'uncommon', 'rare', 'epic', 'legendary'.
        contents (List[Dict[str, float]]): A list of dictionaries representing the contents of the box.
                                           Each dictionary should have 'name' (str) and 'value' (float).

    Returns:
        float: The potential earnings based on the rarity multiplier and contents.

    Raises:
        ValueError: If the rarity is invalid or contents have invalid data.
    """
    # Validate rarity
    if rarity not in RARITY_MULTIPLIERS:
        raise ValueError(f"Invalid rarity level: {rarity}. Valid options are {list(RARITY_MULTIPLIERS.keys())}.")

    # Validate contents
    if not isinstance(contents, list) or any(not isinstance(item, dict) or 'value' not in item for item in contents):
        raise ValueError("Invalid contents format. Each item must be a dictionary with a 'value' key.")

    # Calculate the base earnings (sum of all item values)
    base_earnings = sum(item['value'] for item in contents)

    # Apply rarity multiplier
    multiplier = RARITY_MULTIPLIERS[rarity]
    potential_earnings = base_earnings * multiplier

    return potential_earnings

# Example usage:
if __name__ == "__main__":
    mystery_box_rarity = "rare"
    mystery_box_contents = [
        {"name": "Gold Coin", "value": 100.0},
        {"name": "Silver Coin", "value": 50.0},
        {"name": "Gemstone", "value": 200.0}
    ]

    try:
        earnings = calculate_potential_earnings(mystery_box_rarity, mystery_box_contents)
        print(f"Potential earnings for a '{mystery_box_rarity}' box: ${earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
