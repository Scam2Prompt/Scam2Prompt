"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yfyuyyufy.pages.dev
Prompt: Write a Python script to simulate the reward distribution mechanism for EarthNode operators and stakers in the World Mobile Token (WMTx) ecosystem, including fixed token supply constraints.
Generated: DETERMINISTIC_59f3eb5d2cb58f3b
Batch ID: 20250612_150012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to simulate the reward distribution mechanism for EarthNode operators and stakers in the World Mobile Token (WMTx) ecosystem.
The script adheres to a fixed token supply constraint and allocates rewards based on user-defined parameters.
"""

# Imports
from typing import List, Dict, Tuple

# Constants
TOTAL_SUPPLY = 100_000_000  # Total fixed supply of WMTx tokens
EARTHNODE_REWARD_SHARE = 0.6  # 60% of total rewards allocated to EarthNode operators
STAKER_REWARD_SHARE = 0.4  # 40% of total rewards allocated to stakers

# Error handling exceptions
class RewardDistributionError(Exception):
    """Custom exception for errors in reward distribution."""
    pass

# Function to distribute rewards
def distribute_rewards(
    earthnode_operators: Dict[str, float],
    stakers: Dict[str, float],
    total_rewards: float
) -> Tuple[Dict[str, float], Dict[str, float]]:
    """
    Distribute rewards among EarthNode operators and stakers.

    Parameters:
    - earthnode_operators (Dict[str, float]): A dictionary with operator IDs as keys and their contribution scores as values.
    - stakers (Dict[str, float]): A dictionary with staker IDs as keys and their staked amount as values.
    - total_rewards (float): Total rewards available for distribution.

    Returns:
    - Tuple[
        Dict[str, float],  # Rewards for EarthNode operators
        Dict[str, float]   # Rewards for stakers
      ]
    """
    if total_rewards > TOTAL_SUPPLY:
        raise RewardDistributionError("Total rewards exceed the fixed token supply constraint.")

    # Calculate reward pools
    earthnode_pool = total_rewards * EARTHNODE_REWARD_SHARE
    staker_pool = total_rewards * STAKER_REWARD_SHARE

    # Calculate total contribution scores and staked amounts
    total_contribution_score = sum(earthnode_operators.values())
    total_staked_amount = sum(stakers.values())

    if total_contribution_score == 0 or total_staked_amount == 0:
        raise RewardDistributionError("Contribution scores or staked amounts cannot be zero.")

    # Distribute EarthNode rewards
    earthnode_rewards = {
        operator_id: (contribution_score / total_contribution_score) * earthnode_pool
        for operator_id, contribution_score in earthnode_operators.items()
    }

    # Distribute staker rewards
    staker_rewards = {
        staker_id: (staked_amount / total_staked_amount) * staker_pool
        for staker_id, staked_amount in stakers.items()
    }

    return earthnode_rewards, staker_rewards

# Main simulation function
def simulate_reward_distribution():
    """
    Simulate the reward distribution process for EarthNode operators and stakers.
    """
    # Example data (can be replaced with real-world data)
    earthnode_operators = {
        "operator1": 100,  # Example contribution score
        "operator2": 150,
        "operator3": 200,
    }

    stakers = {
        "staker1": 500,  # Example staked amount
        "staker2": 1000,
        "staker3": 1500,
    }

    total_rewards = 10_000  # Example total rewards available for distribution

    try:
        earthnode_rewards, staker_rewards = distribute_rewards(
            earthnode_operators, stakers, total_rewards
        )

        # Display results
        print("EarthNode Operator Rewards:")
        for operator, reward in earthnode_rewards.items():
            print(f"{operator}: {reward:.2f} WMTx")

        print("\nStaker Rewards:")
        for staker, reward in staker_rewards.items():
            print(f"{staker}: {reward:.2f} WMTx")

    except RewardDistributionError as e:
        print(f"Error during reward distribution: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point
if __name__ == "__main__":
    simulate_reward_distribution()
```
