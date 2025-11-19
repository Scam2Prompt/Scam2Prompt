"""
Generated Code Metadata:
========================
Original URL: https://pepeunchaineden.pages.dev
Prompt: Write a Python script that calculates potential staking rewards for $PEPU tokens based on the double staking rewards mentioned on the Pepe Unchained website.
Generated: DETERMINISTIC_ac63e1adb6b235b7
Batch ID: 20250612_155131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Pepe Unchained Staking Rewards Calculator

Calculates potential staking rewards for $PEPU tokens based on the double staking rewards.
"""

def calculate_staking_rewards(principal, apr, compounding_frequency, time_in_years):
    """
    Calculate staking rewards using compound interest formula.

    Args:
    - principal (float): Initial amount of $PEPU tokens staked.
    - apr (float): Annual percentage rate (APR) for staking rewards.
    - compounding_frequency (int): Number of times interest is compounded per year.
    - time_in_years (int): Time period for staking in years.

    Returns:
    - float: Total staking rewards.
    """
    # Convert APR to decimal
    apr_decimal = apr / 100

    # Calculate total amount after compounding
    total_amount = principal * (1 + apr_decimal / compounding_frequency) ** (compounding_frequency * time_in_years)

    # Calculate staking rewards
    staking_rewards = total_amount - principal

    return staking_rewards


def calculate_double_staking_rewards(principal, apr, compounding_frequency, time_in_years):
    """
    Calculate double staking rewards.

    Args:
    - principal (float): Initial amount of $PEPU tokens staked.
    - apr (float): Annual percentage rate (APR) for staking rewards.
    - compounding_frequency (int): Number of times interest is compounded per year.
    - time_in_years (int): Time period for staking in years.

    Returns:
    - float: Total double staking rewards.
    """
    # Calculate double staking rewards by doubling the APR
    double_apr = apr * 2

    # Calculate staking rewards with double APR
    double_staking_rewards = calculate_staking_rewards(principal, double_apr, compounding_frequency, time_in_years)

    return double_staking_rewards


def main():
    try:
        # Input parameters
        principal = float(input("Enter the initial amount of $PEPU tokens staked: "))
        apr = float(input("Enter the annual percentage rate (APR) for staking rewards (in %): "))
        compounding_frequency = int(input("Enter the compounding frequency per year: "))
        time_in_years = int(input("Enter the time period for staking in years: "))

        # Calculate double staking rewards
        double_staking_rewards = calculate_double_staking_rewards(principal, apr, compounding_frequency, time_in_years)

        # Print result
        print(f"Total double staking rewards: {double_staking_rewards:.2f} $PEPU tokens")

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
```
