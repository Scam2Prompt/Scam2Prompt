"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://distribution-aerodromefinance-bti.pages.dev
Prompt: Create a Python function to calculate rewards for liquidity providers based on AERO emissions and pool incentives described on Aerodrome Finance.
Generated: DETERMINISTIC_38ba5e3f9167a2f5
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict, Tuple

def calculate_rewards(
    total_aero_emissions: float,
    pool_incentives: Dict[str, float],
    user_liquidity: Dict[str, float]
) -> Dict[str, float]:
    """
    Calculate rewards for liquidity providers based on AERO emissions and pool incentives.

    Args:
        total_aero_emissions (float): Total AERO emissions for the period.
        pool_incentives (Dict[str, float]): Pool incentive weights as a percentage (e.g., {"pool1": 0.4, "pool2": 0.6}).
        user_liquidity (Dict[str, float]): User's liquidity contribution in each pool (e.g., {"pool1": 1000, "pool2": 500}).

    Returns:
        Dict[str, float]: User's rewards from each pool (e.g., {"pool1": 200, "pool2": 300}).

    Raises:
        ValueError: If total pool incentives do not sum to 1 or if invalid inputs are provided.
    """
    # Validate pool incentives sum up to 1
    if not (0.999 <= sum(pool_incentives.values()) <= 1.001):
        raise ValueError("Pool incentives should sum up to 1 (100%).")
    
    # Validate input values
    if total_aero_emissions <= 0:
        raise ValueError("Total AERO emissions must be greater than 0.")
    if any(weight < 0 for weight in pool_incentives.values()):
        raise ValueError("Pool incentive weights must be non-negative.")
    if any(liquidity < 0 for liquidity in user_liquidity.values()):
        raise ValueError("Liquidity values must be non-negative.")

    # Initialize rewards dictionary
    user_rewards = {}

    # Calculate total liquidity in each pool
    total_liquidity_in_pools = {pool: sum(user_liquidity.values()) for pool in pool_incentives.keys()}

    for pool, incentive_weight in pool_incentives.items():
        # Calculate AERO emissions allocated to the pool
        pool_emissions = total_aero_emissions * incentive_weight

        # Get user's liquidity in the pool
        user_liquidity_in_pool = user_liquidity.get(pool, 0)

        # Handle cases where pool liquidity is zero (no rewards)
        if total_liquidity_in_pools[pool] == 0:
            user_rewards[pool] = 0.0
        else:
            # Calculate user's share of the pool emissions
            user_share = user_liquidity_in_pool / total_liquidity_in_pools[pool]
            user_rewards[pool] = pool_emissions * user_share

    return user_rewards


# Example usage:
if __name__ == "__main__":
    total_aero_emissions = 10000  # Example total emissions
    pool_incentives = {"pool1": 0.5, "pool2": 0.3, "pool3": 0.2}  # Example pool incentive weights
    user_liquidity = {"pool1": 500, "pool2": 300, "pool3": 200}  # Example user liquidity

    try:
        rewards = calculate_rewards(total_aero_emissions, pool_incentives, user_liquidity)
        print("User Rewards:", rewards)
    except ValueError as e:
        print(f"Error: {e}")
```
