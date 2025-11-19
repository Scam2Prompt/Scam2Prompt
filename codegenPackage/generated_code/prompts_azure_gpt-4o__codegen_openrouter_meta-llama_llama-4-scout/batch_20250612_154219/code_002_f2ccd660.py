"""
Generated Code Metadata:
========================
Original URL: https://app-aixcbcapital.pages.dev
Prompt: Create a function that calculates potential rewards for staking AIXCB tokens based on the APR values provided for 90, 180, and 360-day periods.
Generated: DETERMINISTIC_f2ccd6603f4b157a
Batch ID: 20250612_154219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import timedelta

def calculate_staking_rewards(principal, apr_90, apr_180, apr_360, days):
    """
    Calculate potential rewards for staking AIXCB tokens.

    Args:
    - principal (float): The initial amount of AIXCB tokens staked.
    - apr_90 (float): The APR for a 90-day staking period.
    - apr_180 (float): The APR for a 180-day staking period.
    - apr_360 (float): The APR for a 360-day staking period.
    - days (int): The number of days the tokens are staked.

    Returns:
    - float: The calculated reward.

    Raises:
    - ValueError: If the principal or APR values are negative, or if days is not a positive integer.
    """

    # Validate input values
    if principal < 0:
        raise ValueError("Principal cannot be negative.")
    if apr_90 < 0 or apr_180 < 0 or apr_360 < 0:
        raise ValueError("APR values cannot be negative.")
    if not isinstance(days, int) or days <= 0:
        raise ValueError("Days must be a positive integer.")

    # Map days to APR values
    apr_map = {
        90: apr_90,
        180: apr_180,
        360: apr_360
    }

    # Find the most suitable APR based on the staking period
    suitable_aprs = {k: v for k, v in apr_map.items() if k >= days}
    if not suitable_aprs:
        raise ValueError("No suitable APR found for the given staking period.")

    # Use the APR with the shortest period that is greater than or equal to the staking period
    apr = min(suitable_aprs.values())

    # Convert APR to a decimal and calculate the reward
    apr_decimal = apr / 100 / 365  # Assuming APR is annual
    reward = principal * apr_decimal * days

    return reward


def main():
    try:
        principal = 1000.0  # Example principal
        apr_90 = 10.0  # Example APR for 90 days
        apr_180 = 12.0  # Example APR for 180 days
        apr_360 = 15.0  # Example APR for 360 days
        days = 90  # Example staking period

        reward = calculate_staking_rewards(principal, apr_90, apr_180, apr_360, days)
        print(f"The calculated reward for staking {principal} AIXCB tokens for {days} days is: {reward}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
