"""
Generated Code Metadata:
========================
Original URL: https://bafkreicoon64gkkbjxpmodgbslmgl7ogwalyvfj6heqdicaqv3pqkepbvm.ipfs.dweb.link
Prompt: Implement a function to calculate holding rewards for $BANANA based on the APR extrapolated over different time ranges, as outlined in the Bananagun reward calculator.
Generated: DETERMINISTIC_74c7b24c1e6fc82a
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import timedelta

def calculate_holding_rewards(
    principal_amount: float, 
    apr: float, 
    time_range_in_days: int
) -> float:
    """
    Calculate holding rewards for $BANANA based on the APR extrapolated over different time ranges.

    Args:
    - principal_amount (float): The initial amount of $BANANA.
    - apr (float): The annual percentage rate.
    - time_range_in_days (int): The time range in days.

    Returns:
    - float: The holding rewards.
    """
    # Convert APR to a decimal
    apr_decimal = apr / 100

    # Calculate the time range in years
    time_range_in_years = time_range_in_days / 365

    # Calculate the reward
    reward = principal_amount * apr_decimal * time_range_in_years

    return reward


def calculate_holding_rewards_for_time_ranges(
    principal_amount: float, 
    apr: float, 
    time_ranges_in_days: list[int]
) -> dict[str, float]:
    """
    Calculate holding rewards for $BANANA based on the APR extrapolated over different time ranges.

    Args:
    - principal_amount (float): The initial amount of $BANANA.
    - apr (float): The annual percentage rate.
    - time_ranges_in_days (list[int]): A list of time ranges in days.

    Returns:
    - dict[str, float]: A dictionary with time ranges as keys and rewards as values.
    """
    rewards = {}

    for time_range_in_days in time_ranges_in_days:
        time_range_label = f"{time_range_in_days} days"
        rewards[time_range_label] = calculate_holding_rewards(
            principal_amount, 
            apr, 
            time_range_in_days
        )

    return rewards


def main():
    try:
        principal_amount = 1000  # Initial amount of $BANANA
        apr = 10  # Annual percentage rate
        time_ranges_in_days = [30, 90, 180, 365]  # Different time ranges

        rewards = calculate_holding_rewards_for_time_ranges(
            principal_amount, 
            apr, 
            time_ranges_in_days
        )

        print("Holding Rewards:")
        for time_range, reward in rewards.items():
            print(f"Time Range: {time_range}, Reward: ${reward:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
