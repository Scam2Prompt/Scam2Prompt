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
import random

def calculate_meowgon_rarity(elements, drop_rates):
    """
    Calculate the rarity of a Meowgon creature based on its elements and drop rates.

    Args:
        elements (list): A list of elements associated with the Meowgon (e.g., ['Fire', 'Water']).
        drop_rates (dict): A dictionary containing rarity levels and their respective drop rates.
                           Example: {'Supreme': 0.00137, 'Legendary': 0.01235, 'Epic': 0.05, 'Rare': 0.2, 'Common': 0.73628}

    Returns:
        str: The rarity level of the Meowgon.
    """
    # Validate input
    if not isinstance(elements, list) or not all(isinstance(e, str) for e in elements):
        raise ValueError("Elements must be a list of strings.")
    if not isinstance(drop_rates, dict) or not all(isinstance(k, str) and isinstance(v, (int, float)) for k, v in drop_rates.items()):
        raise ValueError("Drop rates must be a dictionary with string keys and numeric values.")
    if sum(drop_rates.values()) > 1:
        raise ValueError("Drop rates must sum to 1 or less.")

    # Normalize drop rates to ensure they sum to 1
    total_rate = sum(drop_rates.values())
    if total_rate < 1:
        drop_rates['Common'] = drop_rates.get('Common', 0) + (1 - total_rate)

    # Generate a random number to determine rarity
    random_number = random.random()

    # Determine rarity based on drop rates
    cumulative_probability = 0
    for rarity, rate in sorted(drop_rates.items(), key=lambda x: x[1], reverse=True):
        cumulative_probability += rate
        if random_number <= cumulative_probability:
            return rarity

    # Fallback (should not occur if drop rates are properly normalized)
    return "Unknown"

# Example usage
if __name__ == "__main__":
    elements = ['Fire', 'Water']
    drop_rates = {
        'Supreme': 0.00137,
        'Legendary': 0.01235,
        'Epic': 0.05,
        'Rare': 0.2,
        'Common': 0.73628
    }

    try:
        rarity = calculate_meowgon_rarity(elements, drop_rates)
        print(f"The Meowgon rarity is: {rarity}")
    except ValueError as e:
        print(f"Error: {e}")
```
