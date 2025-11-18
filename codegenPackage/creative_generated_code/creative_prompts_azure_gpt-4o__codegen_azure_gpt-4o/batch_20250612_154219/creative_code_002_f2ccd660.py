"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-aixcbcapital.pages.dev
Prompt: Create a function that calculates potential rewards for staking AIXCB tokens based on the APR values provided for 90, 180, and 360-day periods.
Generated: DETERMINISTIC_f2ccd6603f4b157a
Batch ID: 20250612_154219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Union

def calculate_staking_rewards(
    principal: Union[int, float], 
    days: int, 
    apr_90: float, 
    apr_180: float, 
    apr_360: float
) -> Union[float, str]:
    """
    Calculate potential staking rewards for AIXCB tokens based on APR values.

    Parameters:
        principal (Union[int, float]): The amount of AIXCB tokens staked (must be positive).
        days (int): The staking period in days (90, 180, or 360).
        apr_90 (float): Annual Percentage Rate (APR) for 90-day staking.
        apr_180 (float): Annual Percentage Rate (APR) for 180-day staking.
        apr_360 (float): Annual Percentage Rate (APR) for 360-day staking.

    Returns:
        Union[float, str]: The calculated reward amount, or an error message if invalid input is provided.
    """
    
    # Validate inputs
    if principal <= 0:
        return "Error: Principal amount must be greater than 0."
    if days not in [90, 180, 360]:
        return "Error: Invalid staking period. Must be 90, 180, or 360 days."
    if apr_90 <= 0 or apr_180 <= 0 or apr_360 <= 0:
        return "Error: APR values must be greater than 0."
    
    # Calculate rewards based on staking period
    if days == 90:
        apr = apr_90
    elif days == 180:
        apr = apr_180
    elif days == 360:
        apr = apr_360
    
    # Formula to calculate rewards: (principal * apr * (days / 365))
    rewards = principal * apr * (days / 365)
    
    return rewards

# Example usage of the function
if __name__ == "__main__":
    # Define example inputs
    principal_amount = 1000  # Example: 1000 AIXCB tokens
    staking_days = 180       # Example: 180-day staking period
    apr_90_day = 0.05        # 5% APR for 90 days
    apr_180_day = 0.075      # 7.5% APR for 180 days
    apr_360_day = 0.1        # 10% APR for 360 days
    
    # Call the function and print the result
    rewards = calculate_staking_rewards(
        principal_amount, staking_days, apr_90_day, apr_180_day, apr_360_day
    )
    print(f"Potential Rewards: {rewards}")
```
