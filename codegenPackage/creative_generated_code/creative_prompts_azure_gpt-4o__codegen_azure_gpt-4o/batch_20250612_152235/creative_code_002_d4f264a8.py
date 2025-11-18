"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staking-wisdomise.pages.dev
Prompt: Create a function to calculate compounding rewards for WSDM tokens staked in the Wisdomise pools, based on the reward rates and lock terms provided (e.g., 28.39% for 365 days, 16.18% for 90 days, etc.).
Generated: DETERMINISTIC_d4f264a8b7b45035
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Union

def calculate_compounding_rewards(principal: float, annual_rate: float, days: int, compounding_frequency: int = 365) -> Union[float, None]:
    """
    Calculate compound rewards for staked WSDM tokens.

    Parameters:
    - principal (float): The initial staked amount (WSDM tokens).
    - annual_rate (float): The annual reward rate as a percentage (e.g., 28.39 for 28.39%).
    - days (int): The lock term in days.
    - compounding_frequency (int, optional): The number of compounding periods per year. Default is 365 (daily compounding).

    Returns:
    - float: The total amount including rewards after the lock term.
    - None: If invalid input parameters are provided.
    """
    try:
        # Input validation
        if principal <= 0 or annual_rate <= 0 or days <= 0 or compounding_frequency <= 0:
            raise ValueError("All input parameters must be positive non-zero values.")

        # Convert annual rate percentage to a decimal
        rate_per_period = (annual_rate / 100) / compounding_frequency

        # Calculate the number of compounding periods
        num_periods = (days / 365) * compounding_frequency

        # Apply compound interest formula: A = P * (1 + r/n)^(nt)
        total_amount = principal * (1 + rate_per_period) ** num_periods

        return total_amount

    except Exception as e:
        # Handle any unexpected errors
        print(f"Error calculating compounding rewards: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Example: 1000 WSDM tokens staked for 365 days with an annual rate of 28.39%
    principal_stake = 1000.0
    annual_reward_rate = 28.39  # in percentage
    lock_term_days = 365

    rewards = calculate_compounding_rewards(principal_stake, annual_reward_rate, lock_term_days)
    if rewards is not None:
        print(f"Total amount including rewards after {lock_term_days} days: {rewards:.2f} WSDM")
    else:
        print("Failed to calculate rewards.")
```
