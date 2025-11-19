"""
Generated Code Metadata:
========================
Original URL: https://magpiexyz.pages.dev
Prompt: Create a function to calculate the profitability of staking and locking MGP tokens on Magpie XYZ, including rewards in WOM and additional MGP.
Generated: DETERMINISTIC_84aa19fd356051e6
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

def calculate_staking_profitability(
    mgp_staked: float, 
    lock_duration: int, 
    wom_rewards: Dict[int, float], 
    additional_mgp_rewards: Dict[int, float], 
    mgp_price: float, 
    wom_price: float
) -> Dict[str, float]:
    """
    Calculate the profitability of staking and locking MGP tokens on Magpie XYZ.

    Args:
    - mgp_staked (float): The amount of MGP tokens staked.
    - lock_duration (int): The duration of the lock in days.
    - wom_rewards (Dict[int, float]): A dictionary of WOM rewards for different lock durations.
    - additional_mgp_rewards (Dict[int, float]): A dictionary of additional MGP rewards for different lock durations.
    - mgp_price (float): The current price of MGP.
    - wom_price (float): The current price of WOM.

    Returns:
    - A dictionary containing the profitability metrics.
    """

    # Check if lock duration is valid
    if lock_duration not in wom_rewards or lock_duration not in additional_mgp_rewards:
        raise ValueError("Invalid lock duration")

    # Calculate WOM rewards
    wom_reward = wom_rewards[lock_duration]

    # Calculate additional MGP rewards
    additional_mgp_reward = additional_mgp_rewards[lock_duration]

    # Calculate total rewards in USD
    total_wom_rewards_usd = wom_reward * wom_price
    total_additional_mgp_rewards_usd = additional_mgp_reward * mgp_price

    # Calculate profitability metrics
    total_rewards_usd = total_wom_rewards_usd + total_additional_mgp_rewards_usd
    roi = (total_rewards_usd / (mgp_staked * mgp_price)) * 100 if mgp_staked > 0 else 0

    # Return profitability metrics
    return {
        "wom_rewards": wom_reward,
        "additional_mgp_rewards": additional_mgp_reward,
        "total_rewards_usd": total_rewards_usd,
        "roi": roi
    }


def main():
    # Example usage
    mgp_staked = 1000
    lock_duration = 30
    wom_rewards = {30: 100, 60: 200, 90: 300}
    additional_mgp_rewards = {30: 50, 60: 100, 90: 150}
    mgp_price = 10.0
    wom_price = 5.0

    try:
        profitability = calculate_staking_profitability(
            mgp_staked, 
            lock_duration, 
            wom_rewards, 
            additional_mgp_rewards, 
            mgp_price, 
            wom_price
        )
        print("Profitability Metrics:")
        for metric, value in profitability.items():
            print(f"{metric.capitalize().replace('_', ' ')}: {value}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
