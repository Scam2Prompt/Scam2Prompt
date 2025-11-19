"""
Generated Code Metadata:
========================
Original URL: https://web-tpad.pages.dev
Prompt: Develop a script to calculate the allocation of TPAD tokens for a user participating in an IDO, considering the staking requirements and pool weights for different levels.
Generated: DETERMINISTIC_162d6b19df48ade4
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tpad_allocation.py

from typing import Dict, List

class TPADAllocator:
    def __init__(self, pool_weights: Dict[str, float], staking_requirements: Dict[str, int]):
        """
        Initialize the TPADAllocator with pool weights and staking requirements.

        Args:
        - pool_weights (Dict[str, float]): A dictionary of pool levels and their corresponding weights.
        - staking_requirements (Dict[str, int]): A dictionary of pool levels and their corresponding staking requirements.
        """
        self.pool_weights = pool_weights
        self.staking_requirements = staking_requirements

    def calculate_allocation(self, user_stake: int, user_level: str) -> float:
        """
        Calculate the TPAD token allocation for a user.

        Args:
        - user_stake (int): The user's stake amount.
        - user_level (str): The user's level in the pool.

        Returns:
        - float: The calculated TPAD token allocation.

        Raises:
        - ValueError: If the user's level is not found in the pool weights or staking requirements.
        """
        if user_level not in self.pool_weights:
            raise ValueError(f"User level '{user_level}' not found in pool weights")

        if user_level not in self.staking_requirements:
            raise ValueError(f"User level '{user_level}' not found in staking requirements")

        required_stake = self.staking_requirements[user_level]
        if user_stake < required_stake:
            return 0.0  # No allocation if staking requirement is not met

        pool_weight = self.pool_weights[user_level]
        # Assuming total TPAD tokens available for allocation
        total_tpad_tokens = 1000000.0  # Example value

        allocation = (user_stake / required_stake) * pool_weight * total_tpad_tokens
        return allocation


def main():
    # Example usage
    pool_weights = {
        "level1": 0.2,
        "level2": 0.3,
        "level3": 0.5
    }

    staking_requirements = {
        "level1": 100,
        "level2": 500,
        "level3": 1000
    }

    allocator = TPADAllocator(pool_weights, staking_requirements)

    user_stake = 750
    user_level = "level2"

    try:
        allocation = allocator.calculate_allocation(user_stake, user_level)
        print(f"TPAD token allocation for user: {allocation:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
