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
from typing import Dict, Tuple

class RewardCalculator:
    def __init__(self, apr_evm: float, apr_solana: float) -> None:
        """
        Initializes the RewardCalculator with given APY values for EVM and Solana.

        :param apr_evm: Annual Percentage Rate (APR) for EVM rewards as a float.
        :param apr_solana: Annual Percentage Rate (APR) for Solana rewards as a float.
        """
        self.apr_evm = apr_evm
        self.apr_solana = apr_solana

    def calculate_rewards(self, principal: float, time_periods: Dict[str, int], banana_price: float) -> Dict[str, float]:
        """
        Calculate the total rewards earned in $BANANA and USD after specified time periods
        using both EVM and Solana APR values.

        :param principal: The initial investment amount as a float.
        :param time_periods: A dictionary specifying time periods in days for reward calculation.
        :param banana_price: The price of $BANANA in USD as a float.
        :return: A dictionary containing total $BANANA and USD values of rewards.
        """
        if principal < 0 or banana_price <= 0:
            raise ValueError("Principal and banana price must be greater than zero.")

        rewards = {
            "total_banana": 0.0,
            "total_usd": 0.0
        }

        for period_name, days in time_periods.items():
            if days < 0:
                raise ValueError(f"Days for {period_name} must be non-negative.")

            # Calculate rewards for EVM
            evm_reward = principal * (self.apr_evm / 100) * (days / 365)
            # Calculate rewards for Solana
            solana_reward = principal * (self.apr_solana / 100) * (days / 365)
            
            # Accumulate rewards
            rewards["total_banana"] += evm_reward + solana_reward

        # Convert total rewards to USD
        rewards["total_usd"] = rewards["total_banana"] * banana_price

        return rewards


# Example usage
if __name__ == "__main__":
    calculator = RewardCalculator(apr_evm=12.0, apr_solana=10.0)
    
    # Define time periods in days
    time_periods = {
        "30_days": 30,
        "90_days": 90,
        "365_days": 365
    }
    
    principal_amount = 1000.0  # Investment amount
    banana_price = 5.0  # Price of $BANANA in USD

    try:
        rewards = calculator.calculate_rewards(principal=principal_amount, time_periods=time_periods, banana_price=banana_price)
        print(f"Total Rewards in $BANANA: {rewards['total_banana']:.2f}")
        print(f"Total Rewards in USD: {rewards['total_usd']:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
