"""
Generated Code Metadata:
========================
Original URL: https://bananarewards.pages.dev
Prompt: Create a function to calculate rewards using the APR extrapolated over different time ranges, combining EVM and Solana rewards into total $BANANA and USD values.
Generated: DETERMINISTIC_c87d79d9f560259f
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

def calculate_rewards(apr: float, 
                      evm_rewards: Dict[str, float], 
                      solana_rewards: Dict[str, float], 
                      time_range: str, 
                      banana_price: float) -> Dict[str, float]:
    """
    Calculate total rewards in $BANANA and USD.

    Args:
    - apr (float): The annual percentage rate.
    - evm_rewards (Dict[str, float]): EVM rewards.
    - solana_rewards (Dict[str, float]): Solana rewards.
    - time_range (str): Time range to extrapolate APR over. 
                        Can be 'day', 'week', 'month', 'year'.
    - banana_price (float): Current price of $BANANA in USD.

    Returns:
    - Dict[str, float]: Total rewards in $BANANA and USD.
    """

    # Define time range conversion to years
    time_range_conversion = {
        'day': 1 / 365,
        'week': 1 / 52,
        'month': 1 / 12,
        'year': 1
    }

    # Check if time range is valid
    if time_range not in time_range_conversion:
        raise ValueError("Invalid time range. Must be 'day', 'week', 'month', or 'year'.")

    try:
        # Calculate total rewards in $BANANA
        total_banana_rewards = sum(evm_rewards.values()) + sum(solana_rewards.values())

        # Extrapolate APR over time range
        apr_over_time_range = apr * time_range_conversion[time_range]

        # Calculate total rewards in $BANANA
        total_banana_rewards *= apr_over_time_range

        # Calculate total rewards in USD
        total_usd_rewards = total_banana_rewards * banana_price

        # Return total rewards
        return {
            'total_banana_rewards': total_banana_rewards,
            'total_usd_rewards': total_usd_rewards
        }

    except Exception as e:
        # Log and re-raise exception
        print(f"An error occurred: {str(e)}")
        raise


# Example usage:
if __name__ == "__main__":
    evm_rewards = {'reward1': 100, 'reward2': 200}
    solana_rewards = {'reward3': 50, 'reward4': 75}
    apr = 0.05  # 5%
    time_range = 'month'
    banana_price = 10.0  # $10 per $BANANA

    rewards = calculate_rewards(apr, evm_rewards, solana_rewards, time_range, banana_price)
    print(rewards)
```
