"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustpad-c0r.pages.dev
Prompt: Create a function to calculate potential returns based on the staking levels and weights provided by TrustPad.
Generated: DETERMINISTIC_88b2504cac712c82
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary module
from typing import Dict, Union

def calculate_staking_returns(staking_levels: Dict[str, Union[int, float]], weights: Dict[str, Union[int, float]], total_rewards: Union[int, float]) -> Dict[str, float]:
    """
    Calculate potential staking returns for each staking level based on provided weights.
    
    Parameters:
    staking_levels (Dict[str, Union[int, float]]): A dictionary where keys are staking levels and values are staking amounts.
    weights (Dict[str, Union[int, float]]): A dictionary where keys are staking levels and values are weights assigned to those levels.
    total_rewards (Union[int, float]): The total rewards to be distributed across the staking levels.

    Returns:
    Dict[str, float]: A dictionary where keys are staking levels and values are the calculated rewards for each level.
    """
    # Validate input types
    if not isinstance(staking_levels, dict) or not isinstance(weights, dict):
        raise ValueError("`staking_levels` and `weights` must be dictionaries.")
    if not isinstance(total_rewards, (int, float)) or total_rewards < 0:
        raise ValueError("`total_rewards` must be a positive number.")

    # Validate that keys in staking_levels and weights match
    if set(staking_levels.keys()) != set(weights.keys()):
        raise ValueError("Keys in `staking_levels` and `weights` must match.")

    # Calculate total weighted contributions
    total_weighted_contributions = 0
    for level, staking_amount in staking_levels.items():
        if staking_amount < 0:
            raise ValueError(f"Staking amount for level {level} cannot be negative.")
        weight = weights.get(level)
        total_weighted_contributions += staking_amount * weight

    # Handle case where total weighted contributions is zero
    if total_weighted_contributions == 0:
        raise ValueError("Total weighted contributions cannot be zero.")

    # Calculate returns for each staking level
    staking_returns = {}
    for level, staking_amount in staking_levels.items():
        weight = weights[level]
        level_contribution = staking_amount * weight
        staking_returns[level] = (level_contribution / total_weighted_contributions) * total_rewards

    return staking_returns


# Example usage:
if __name__ == "__main__":
    # Define example staking levels and weights
    staking_levels = {"level_1": 1000, "level_2": 500, "level_3": 1500}
    weights = {"level_1": 1.0, "level_2": 0.8, "level_3": 1.2}
    total_rewards = 10000

    # Calculate staking returns
    try:
        returns = calculate_staking_returns(staking_levels, weights, total_rewards)
        print("Staking Returns:", returns)
    except ValueError as e:
        print("Error:", e)
```
