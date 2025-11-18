"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bananarewards.pages.dev
Prompt: Create a function to calculate rewards using the APR extrapolated over different time ranges, combining EVM and Solana rewards into total $BANANA and USD values.
Generated: DETERMINISTIC_c87d79d9f560259f
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict, Union
import datetime

def calculate_rewards(
    evm_rewards: Dict[str, Union[float, int]],
    solana_rewards: Dict[str, Union[float, int]],
    apr: float,
    price_per_banana: float,
    duration_days: int
) -> Dict[str, Union[float, str]]:
    """
    Calculate total rewards based on EVM and Solana rewards, APR, and price.

    Args:
        evm_rewards (dict): Dictionary containing reward details from EVM (keys: 'BANANA', 'USD').
        solana_rewards (dict): Dictionary containing reward details from Solana (keys: 'BANANA', 'USD').
        apr (float): Annual Percentage Rate (APR) as a percentage (e.g., 12.5 for 12.5% APR).
        price_per_banana (float): Current price per $BANANA in USD.
        duration_days (int): Duration in days to calculate the rewards.

    Returns:
        dict: Dictionary containing total rewards in $BANANA and USD,
              and a description of the calculated duration.
    """
    try:
        # Validate inputs
        if duration_days <= 0:
            raise ValueError("Duration_days must be greater than 0.")
        if apr < 0:
            raise ValueError("APR must be a non-negative value.")
        if price_per_banana <= 0:
            raise ValueError("Price per BANANA must be greater than 0.")

        # Calculate extrapolated APR rewards for the given time range
        annual_rewards_banana = (evm_rewards['BANANA'] + solana_rewards['BANANA']) * (apr / 100)
        daily_rewards_banana = annual_rewards_banana / 365
        rewards_banana = daily_rewards_banana * duration_days

        # Calculate USD values based on $BANANA price
        rewards_usd = rewards_banana * price_per_banana

        # Combine EVM and Solana rewards
        total_rewards_banana = evm_rewards['BANANA'] + solana_rewards['BANANA'] + rewards_banana
        total_rewards_usd = evm_rewards['USD'] + solana_rewards['USD'] + rewards_usd

        # Prepare results
        result = {
            "total_banana": round(total_rewards_banana, 4),
            "total_usd": round(total_rewards_usd, 2),
            "duration": f"{duration_days} days ({datetime.timedelta(days=duration_days)})"
        }

        return result

    except KeyError as e:
        raise KeyError(f"Missing key in reward dictionaries: {e}")
    except Exception as e:
        raise RuntimeError(f"An error occurred while calculating rewards: {e}")

# Example usage
if __name__ == "__main__":
    evm_rewards_example = {"BANANA": 100, "USD": 200}
    solana_rewards_example = {"BANANA": 50, "USD": 100}
    apr_example = 12.5  # 12.5% APR
    price_per_banana_example = 1.5  # $1.5 per BANANA
    duration_days_example = 30  # 30 days

    try:
        rewards = calculate_rewards(
            evm_rewards=evm_rewards_example,
            solana_rewards=solana_rewards_example,
            apr=apr_example,
            price_per_banana=price_per_banana_example,
            duration_days=duration_days_example
        )
        print(f"Calculated Rewards: {rewards}")
    except Exception as e:
        print(f"Error: {e}")
```
