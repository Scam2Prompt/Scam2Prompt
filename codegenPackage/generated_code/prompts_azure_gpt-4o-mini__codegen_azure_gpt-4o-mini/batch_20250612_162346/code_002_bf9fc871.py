"""
Generated Code Metadata:
========================
Original URL: https://realis.pages.dev
Prompt: Generate a Python function that calculates the drop rate for different rarities of Meowgon NFTs based on the provided percentages.
Generated: DETERMINISTIC_bf9fc871e874d195
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, Tuple

def calculate_drop_rate(rarities: Dict[str, float], total_drops: int) -> Dict[str, int]:
    """
    Calculate the number of drops for each rarity of Meowgon NFTs based on provided percentages.

    Args:
        rarities (Dict[str, float]): A dictionary where keys are rarity names and values are their drop percentages.
        total_drops (int): The total number of NFT drops to distribute among the rarities.

    Returns:
        Dict[str, int]: A dictionary with rarity names as keys and the calculated number of drops as values.

    Raises:
        ValueError: If the total drop percentage does not equal 100 or if total_drops is negative.
    """
    
    # Validate input
    if total_drops < 0:
        raise ValueError("Total drops must be a non-negative integer.")
    
    total_percentage = sum(rarities.values())
    if total_percentage != 100:
        raise ValueError("Total drop percentages must equal 100.")

    # Calculate drops for each rarity
    drop_counts = {}
    for rarity, percentage in rarities.items():
        drop_count = int((percentage / 100) * total_drops)
        drop_counts[rarity] = drop_count

    return drop_counts

# Example usage
if __name__ == "__main__":
    try:
        rarities = {
            "Common": 50.0,
            "Rare": 30.0,
            "Epic": 15.0,
            "Legendary": 5.0
        }
        total_drops = 1000
        drop_rates = calculate_drop_rate(rarities, total_drops)
        print(drop_rates)
    except ValueError as e:
        print(f"Error: {e}")
```
