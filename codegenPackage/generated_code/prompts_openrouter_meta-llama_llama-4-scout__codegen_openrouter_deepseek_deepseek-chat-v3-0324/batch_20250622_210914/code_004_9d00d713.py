"""
Generated Code Metadata:
========================
Original URL: https://realis.pages.dev
Prompt: Develop a function to calculate the rarity of a Meowgon creature based on its elements and the provided drop rates (e.g., Supreme: 0.137%, Legendary: 1.235%, etc.).
Generated: DETERMINISTIC_9d00d7138c4959a6
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List, Optional

def calculate_rarity(
    elements: List[str],
    drop_rates: Dict[str, float],
    element_weights: Optional[Dict[str, float]] = None
) -> str:
    """
    Calculate the rarity of a Meowgon creature based on its elements and drop rates.
    
    Args:
        elements: List of elements the creature possesses.
        drop_rates: Dictionary mapping rarity names to their base drop rates (as percentages).
        element_weights: Optional dictionary mapping elements to their weight multipliers.
                        If not provided, all elements are treated equally.
    
    Returns:
        The calculated rarity name (e.g., "Supreme", "Legendary").
    
    Raises:
        ValueError: If elements list is empty or drop_rates is empty.
    """
    if not elements:
        raise ValueError("Elements list cannot be empty")
    if not drop_rates:
        raise ValueError("Drop rates dictionary cannot be empty")
    
    # Default weights to 1.0 if not provided
    if element_weights is None:
        element_weights = {element: 1.0 for element in elements}
    
    # Calculate total weight
    total_weight = sum(element_weights.get(element, 1.0) for element in elements)
    
    # Calculate adjusted drop rates
    adjusted_rates = {
        rarity: rate * total_weight
        for rarity, rate in drop_rates.items()
    }
    
    # Find the highest rarity where adjusted rate is >= random threshold
    # In practice, you would compare against a random number, but for this
    # function we'll return the highest possible rarity based on the calculation
    max_rarity = max(adjusted_rates.items(), key=lambda x: x[1])[0]
    
    return max_rarity

# Example usage:
if __name__ == "__main__":
    # Example drop rates (percentages)
    DROP_RATES = {
        "Common": 45.678,
        "Uncommon": 30.123,
        "Rare": 15.456,
        "Epic": 6.789,
        "Legendary": 1.235,
        "Supreme": 0.137
    }
    
    # Example element weights
    ELEMENT_WEIGHTS = {
        "Fire": 1.2,
        "Water": 1.1,
        "Earth": 1.0,
        "Air": 0.9,
        "Light": 1.5,
        "Dark": 1.5
    }
    
    # Test creature with elements
    creature_elements = ["Fire", "Light", "Dark"]
    
    rarity = calculate_rarity(
        elements=creature_elements,
        drop_rates=DROP_RATES,
        element_weights=ELEMENT_WEIGHTS
    )
    
    print(f"Creature rarity: {rarity}")
```
