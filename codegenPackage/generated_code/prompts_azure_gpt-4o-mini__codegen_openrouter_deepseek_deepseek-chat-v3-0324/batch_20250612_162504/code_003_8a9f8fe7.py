"""
Generated Code Metadata:
========================
Original URL: https://promo-ps44.github.io
Prompt: Generate a function that calculates the probability of winning for different tokens in the Degen Toy Machine.
Generated: DETERMINISTIC_8a9f8fe793383c73
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import Dict, List, Union

def calculate_win_probability(
    token_counts: Dict[str, int],
    rarity_weights: Dict[str, float],
    boost_factors: Union[Dict[str, float], None] = None
) -> Dict[str, float]:
    """
    Calculate the probability of winning for different tokens in the Degen Toy Machine.

    Args:
        token_counts: A dictionary mapping token names to their counts in the machine.
        rarity_weights: A dictionary mapping token names to their base rarity weights.
        boost_factors: Optional dictionary mapping token names to boost factors (default is None).

    Returns:
        A dictionary mapping token names to their win probabilities.

    Raises:
        ValueError: If token_counts or rarity_weights are empty, or if they have mismatched keys.
    """
    # Input validation
    if not token_counts or not rarity_weights:
        raise ValueError("token_counts and rarity_weights cannot be empty")
    
    if set(token_counts.keys()) != set(rarity_weights.keys()):
        raise ValueError("token_counts and rarity_weights must have the same keys")

    # Apply boost factors if provided (default to 1.0 if not provided)
    effective_weights = {}
    for token, count in token_counts.items():
        base_weight = rarity_weights[token]
        boost = boost_factors[token] if boost_factors and token in boost_factors else 1.0
        effective_weights[token] = base_weight * boost * count

    # Calculate total weight
    total_weight = sum(effective_weights.values())
    if total_weight <= 0:
        raise ValueError("Total effective weight must be positive")

    # Calculate probabilities
    probabilities = {
        token: weight / total_weight
        for token, weight in effective_weights.items()
    }

    return probabilities

# Example usage:
if __name__ == "__main__":
    # Example data
    token_counts = {
        "common": 100,
        "uncommon": 50,
        "rare": 10,
        "legendary": 5
    }
    
    rarity_weights = {
        "common": 1.0,
        "uncommon": 2.0,
        "rare": 5.0,
        "legendary": 10.0
    }
    
    boost_factors = {
        "legendary": 1.5  # 50% boost for legendary tokens
    }
    
    try:
        probabilities = calculate_win_probability(token_counts, rarity_weights, boost_factors)
        print("Win Probabilities:")
        for token, prob in probabilities.items():
            print(f"{token}: {prob:.2%}")
    except ValueError as e:
        print(f"Error calculating probabilities: {e}")
```
