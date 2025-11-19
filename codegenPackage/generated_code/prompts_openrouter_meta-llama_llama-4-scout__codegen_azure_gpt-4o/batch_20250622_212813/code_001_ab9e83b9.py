"""
Generated Code Metadata:
========================
Original URL: https://sayloud.io
Prompt: Describe the fee distribution mechanics of Loud, including the 4% fee and how rewards are calculated and distributed in SOL.
Generated: DETERMINISTIC_ab9e83b9ca0e0725
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import List, Dict

# Constants
TRANSACTION_FEE_PERCENTAGE = 4  # Fee percentage (4%)
REWARD_POOL_PERCENTAGE = 50  # Percentage of the fee allocated to rewards pool (50%)
TREASURY_PERCENTAGE = 50  # Percentage of the fee allocated to treasury (50%)

# Function to calculate fee distribution
def calculate_fee_distribution(transaction_amount: float) -> Dict[str, float]:
    """
    Calculate the fee distribution for a given transaction amount.

    Args:
        transaction_amount (float): The total amount of the transaction in SOL.

    Returns:
        Dict[str, float]: A dictionary containing the fee breakdown:
            - total_fee: Total fee deducted from the transaction.
            - reward_pool: Amount allocated to the rewards pool.
            - treasury: Amount allocated to the treasury.
    """
    if transaction_amount <= 0:
        raise ValueError("Transaction amount must be greater than zero.")

    # Calculate total fee
    total_fee = (TRANSACTION_FEE_PERCENTAGE / 100) * transaction_amount

    # Calculate distribution
    reward_pool = (REWARD_POOL_PERCENTAGE / 100) * total_fee
    treasury = (TREASURY_PERCENTAGE / 100) * total_fee

    return {
        "total_fee": total_fee,
        "reward_pool": reward_pool,
        "treasury": treasury
    }

# Function to distribute rewards to users
def distribute_rewards(reward_pool: float, user_weights: Dict[str, float]) -> Dict[str, float]:
    """
    Distribute rewards from the reward pool to users based on their weights.

    Args:
        reward_pool (float): Total amount in the reward pool in SOL.
        user_weights (Dict[str, float]): A dictionary where keys are user IDs and values are their weights.

    Returns:
        Dict[str, float]: A dictionary containing the rewards distributed to each user.
    """
    if reward_pool <= 0:
        raise ValueError("Reward pool must be greater than zero.")
    if not user_weights or sum(user_weights.values()) == 0:
        raise ValueError("User weights must be non-empty and sum to a positive value.")

    # Calculate total weight
    total_weight = sum(user_weights.values())

    # Distribute rewards based on weights
    rewards = {}
    for user_id, weight in user_weights.items():
        rewards[user_id] = (weight / total_weight) * reward_pool

    return rewards

# Example usage
if __name__ == "__main__":
    try:
        # Example transaction amount in SOL
        transaction_amount = 100.0  # 100 SOL

        # Calculate fee distribution
        fee_distribution = calculate_fee_distribution(transaction_amount)
        print("Fee Distribution:", fee_distribution)

        # Example user weights for reward distribution
        user_weights = {
            "user1": 10,
            "user2": 20,
            "user3": 30
        }

        # Distribute rewards
        rewards = distribute_rewards(fee_distribution["reward_pool"], user_weights)
        print("Rewards Distribution:", rewards)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
