"""
Generated Code Metadata:
========================
Original URL: https://yifistake.finance
Prompt: Create a script that calculates the annual percentage yield (APY) for YI12 staking based on the provided data.
Generated: DETERMINISTIC_6f28d529e98384f6
Batch ID: 20250612_162409
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates the annual percentage yield (APY) for YI12 staking.

This script takes into account the total value locked, the amount of YI12 staked,
and the reward rate to calculate the APY.
"""

def calculate_apy(total_value_locked: float, total_staked: float, reward_rate: float) -> float:
    """
    Calculates the annual percentage yield (APY) for YI12 staking.

    Args:
    - total_value_locked (float): The total value locked in the staking pool.
    - total_staked (float): The total amount of YI12 staked.
    - reward_rate (float): The reward rate for the staking pool.

    Returns:
    - apy (float): The calculated annual percentage yield.

    Raises:
    - ZeroDivisionError: If total_staked is zero.
    - ValueError: If any input value is negative.
    """

    # Check for negative input values
    if total_value_locked < 0 or total_staked < 0 or reward_rate < 0:
        raise ValueError("Input values cannot be negative.")

    # Check for division by zero
    if total_staked == 0:
        raise ZeroDivisionError("Total staked cannot be zero.")

    # Calculate the APY
    apy = (reward_rate / total_staked) * (total_value_locked / total_staked) * 100

    return apy


def main():
    try:
        # Example usage
        total_value_locked = 1000000.0  # Total value locked in the staking pool
        total_staked = 500000.0  # Total amount of YI12 staked
        reward_rate = 0.05  # Reward rate for the staking pool

        apy = calculate_apy(total_value_locked, total_staked, reward_rate)

        print(f"The calculated APY is: {apy:.2f}%")

    except (ZeroDivisionError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
