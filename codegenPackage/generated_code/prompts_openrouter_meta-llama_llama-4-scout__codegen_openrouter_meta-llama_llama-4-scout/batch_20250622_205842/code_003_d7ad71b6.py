"""
Generated Code Metadata:
========================
Original URL: https://allthingslemon-io.pages.dev
Prompt: Design a function to calculate NFT rewards for a user who has staked a certain amount of Aluminum (ALUM) and Natural Gas (NATG) NFTs on the LEMON platform.
Generated: DETERMINISTIC_d7ad71b68fef8359
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

def calculate_nft_rewards(alum_staked: float, natg_staked: float, 
                          alum_reward_rate: float, natg_reward_rate: float, 
                          total_alum_staked: float, total_natg_staked: float) -> Dict[str, float]:
    """
    Calculates NFT rewards for a user who has staked a certain amount of Aluminum (ALUM) and Natural Gas (NATG) NFTs on the LEMON platform.

    Args:
    - alum_staked (float): The amount of ALUM NFTs staked by the user.
    - natg_staked (float): The amount of NATG NFTs staked by the user.
    - alum_reward_rate (float): The reward rate for ALUM NFTs.
    - natg_reward_rate (float): The reward rate for NATG NFTs.
    - total_alum_staked (float): The total amount of ALUM NFTs staked on the platform.
    - total_natg_staked (float): The total amount of NATG NFTs staked on the platform.

    Returns:
    - A dictionary containing the rewards for ALUM and NATG NFTs.

    Raises:
    - ValueError: If any of the input values are negative.
    - ZeroDivisionError: If the total amount of staked NFTs is zero.
    """

    # Check for negative input values
    if alum_staked < 0 or natg_staked < 0 or alum_reward_rate < 0 or natg_reward_rate < 0:
        raise ValueError("Input values cannot be negative.")

    # Calculate rewards
    try:
        alum_reward = (alum_staked / total_alum_staked) * alum_reward_rate if total_alum_staked > 0 else 0
        natg_reward = (natg_staked / total_natg_staked) * natg_reward_rate if total_natg_staked > 0 else 0
    except ZeroDivisionError:
        raise ZeroDivisionError("Total amount of staked NFTs cannot be zero.")

    # Return rewards as a dictionary
    return {
        "alum_reward": alum_reward,
        "natg_reward": natg_reward
    }


def main():
    try:
        alum_staked = 100.0
        natg_staked = 50.0
        alum_reward_rate = 10.0
        natg_reward_rate = 5.0
        total_alum_staked = 1000.0
        total_natg_staked = 500.0

        rewards = calculate_nft_rewards(alum_staked, natg_staked, alum_reward_rate, natg_reward_rate, total_alum_staked, total_natg_staked)
        print("ALUM Reward:", rewards["alum_reward"])
        print("NATG Reward:", rewards["natg_reward"])
    except (ValueError, ZeroDivisionError) as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
```
