"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rangersprotocol.gitbook.io
Prompt: Can you write a function to calculate the block rewards for proposal nodes based on the RPG staking ratio in the Rangers Protocol?
Generated: DETERMINISTIC_1b1ba9393fd37a5e
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Union

def calculate_block_rewards(total_rewards: Union[int, float], staking_ratio: float) -> Union[int, float]:
    """
    Calculate the block rewards for proposal nodes based on the RPG staking ratio.

    Parameters:
        total_rewards (Union[int, float]): The total reward pool for the block.
        staking_ratio (float): The RPG staking ratio (should be between 0 and 1 inclusive).

    Returns:
        Union[int, float]: The calculated block rewards for proposal nodes.

    Raises:
        ValueError: If staking_ratio is not between 0 and 1 inclusive.
        TypeError: If total_rewards or staking_ratio are not of the correct type.
    """
    # Input validation
    if not isinstance(total_rewards, (int, float)):
        raise TypeError("total_rewards must be an int or float.")

    if not isinstance(staking_ratio, float):
        raise TypeError("staking_ratio must be a float.")

    if not (0 <= staking_ratio <= 1):
        raise ValueError("staking_ratio must be between 0 and 1 inclusive.")

    # Calculate block rewards based on staking ratio
    block_rewards = total_rewards * staking_ratio

    return block_rewards

# Example usage
if __name__ == "__main__":
    try:
        total_rewards = 1000  # Example total rewards for a block
        staking_ratio = 0.25  # Example staking ratio (25%)

        rewards = calculate_block_rewards(total_rewards, staking_ratio)
        print(f"Block rewards for proposal nodes: {rewards}")
    
    except (ValueError, TypeError) as e:
        print(f"Error calculating block rewards: {e}")
```
