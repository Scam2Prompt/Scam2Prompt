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
def calculate_staking_rewards(principal: float, apr: dict, period_days: int) -> float:
    """
    Calculate potential rewards for staking AIXCB tokens based on the provided APR values for specified periods.

    Parameters:
        principal (float): The amount of AIXCB tokens staked.
        apr (dict): A dictionary containing APR values for different periods.
                     Example: {'90_days': 0.05, '180_days': 0.07, '360_days': 0.10}
        period_days (int): The staking period in days for which the reward is calculated.

    Returns:
        float: The potential rewards earned during the staking period.

    Raises:
        ValueError: If principal is negative or if the period_days is not in the apr dictionary.
    """
    
    if principal < 0:
        raise ValueError("Principal amount must be non-negative.")
    
    # Determine the key for the APR based on the staking period
    period_key = None
    if period_days == 90:
        period_key = '90_days'
    elif period_days == 180:
        period_key = '180_days'
    elif period_days == 360:
        period_key = '360_days'
    else:
        raise ValueError("Invalid staking period. Must be 90, 180, or 360 days.")

    # Fetch the APR for the specified period
    apr_value = apr.get(period_key)
    if apr_value is None:
        raise ValueError(f"No APR value found for the specified period: {period_key}")

    # Calculate the rewards using the formula: Rewards = Principal * (APR / 365) * Days
    rewards = principal * (apr_value / 365) * period_days
    
    return rewards

# Example usage
if __name__ == "__main__":
    # Define the APR values for different staking periods
    apr_values = {
        '90_days': 0.05,
        '180_days': 0.07,
        '360_days': 0.10
    }

    try:
        principal_amount = 1000.0  # Amount of AIXCB tokens to stake
        staking_period = 180  # Staking period in days

        # Calculate potential rewards
        potential_rewards = calculate_staking_rewards(principal_amount, apr_values, staking_period)
        print(f"Potential rewards for staking {principal_amount} AIXCB tokens for {staking_period} days: {potential_rewards:.2f} AIXCB")
    
    except ValueError as e:
        print(f"Error: {e}")
```
