"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-etuktuk.pages.dev
Prompt: Develop a function to calculate the rewards earned by staking $TUK tokens, incorporating the staking mechanics described in the eTukTuk ecosystem.
Generated: DETERMINISTIC_dfaf49d593fde487
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script provides a function to calculate rewards earned by staking $TUK tokens.
It incorporates staking mechanics described in the eTukTuk ecosystem.

Key assumptions:
1. Rewards are calculated based on a fixed Annual Percentage Yield (APY).
2. The staking duration is provided by the user in days.
3. Rewards are compounded annually.
4. Error handling for invalid inputs is included.

"""

def calculate_staking_rewards(staked_amount, staking_days, apy, days_in_year=365):
    """
    Calculates the rewards earned from staking $TUK tokens.

    Parameters:
        staked_amount (float): The amount of $TUK tokens staked by the user.
        staking_days (int): The number of days the tokens are staked.
        apy (float): The annual percentage yield (APY) as a percentage (e.g., pass 5.0 for 5% APY).
        days_in_year (int): Number of days in a year (default is 365).

    Returns:
        float: Total rewards earned during the staking period.

    Raises:
        ValueError: If staked_amount is negative, staking_days is not positive, or apy is negative.
    """
    # Input validation
    if staked_amount < 0:
        raise ValueError("Staked amount must be non-negative.")
    if staking_days <= 0:
        raise ValueError("Staking days must be positive.")
    if apy < 0:
        raise ValueError("APY must be non-negative.")

    # Convert APY percentage to a decimal for calculations
    apy_decimal = apy / 100

    # Calculate rewards
    # Formula: rewards = staked_amount * apy_decimal * (staking_days / days_in_year)
    rewards = staked_amount * apy_decimal * (staking_days / days_in_year)

    return rewards


# Example usage
if __name__ == "__main__":
    try:
        # User input (example values)
        staked_amount = 1000  # Amount of $TUK tokens staked
        staking_days = 90     # Duration of staking in days
        apy = 5.0             # Annual Percentage Yield (APY) in percentage

        # Calculate rewards
        rewards = calculate_staking_rewards(staked_amount, staking_days, apy)
        
        # Display results
        print(f"Rewards earned for staking {staked_amount} $TUK tokens for {staking_days} days at {apy}% APY: {rewards:.2f} $TUK")
    except ValueError as e:
        print(f"Error: {e}")
```
