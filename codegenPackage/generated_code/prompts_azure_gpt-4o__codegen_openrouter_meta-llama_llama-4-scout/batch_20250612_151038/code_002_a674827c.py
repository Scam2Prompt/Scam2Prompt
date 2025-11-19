"""
Generated Code Metadata:
========================
Original URL: https://pepeunchainedclaims.pages.dev
Prompt: Generate code to calculate double staking rewards for $PEPU tokens on Pepe Unchained Layer 2, based on the provided annual rewards rate of 307%.
Generated: DETERMINISTIC_a674827cb79b3010
Batch ID: 20250612_151038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates double staking rewards for $PEPU tokens on Pepe Unchained Layer 2.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_staking_rewards(principal_amount: float, annual_rewards_rate: float, time_in_years: float) -> float:
    """
    Calculates the staking rewards based on the principal amount, annual rewards rate, and time in years.

    Args:
    - principal_amount (float): The initial amount of $PEPU tokens staked.
    - annual_rewards_rate (float): The annual rewards rate as a decimal (e.g., 307% = 3.07).
    - time_in_years (float): The time the tokens are staked for, in years.

    Returns:
    - float: The total staking rewards.
    """
    try:
        # Validate inputs
        if principal_amount < 0:
            raise ValueError("Principal amount cannot be negative.")
        if annual_rewards_rate <= 0:
            raise ValueError("Annual rewards rate must be greater than zero.")
        if time_in_years < 0:
            raise ValueError("Time in years cannot be negative.")

        # Calculate staking rewards using compound interest formula
        rewards = principal_amount * ((1 + annual_rewards_rate) ** time_in_years - 1)
        return rewards

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def calculate_double_staking_rewards(principal_amount: float, annual_rewards_rate: float, time_in_years: float) -> float:
    """
    Calculates the double staking rewards based on the principal amount, annual rewards rate, and time in years.

    Args:
    - principal_amount (float): The initial amount of $PEPU tokens staked.
    - annual_rewards_rate (float): The annual rewards rate as a decimal (e.g., 307% = 3.07).
    - time_in_years (float): The time the tokens are staked for, in years.

    Returns:
    - float: The total double staking rewards.
    """
    try:
        # Calculate double staking rewards by doubling the annual rewards rate
        double_annual_rewards_rate = annual_rewards_rate * 2
        double_staking_rewards = calculate_staking_rewards(principal_amount, double_annual_rewards_rate, time_in_years)
        return double_staking_rewards

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    # Provided annual rewards rate of 307%
    annual_rewards_rate = 3.07

    # Example usage
    principal_amount = 1000.0  # Initial amount of $PEPU tokens staked
    time_in_years = 1.0  # Time the tokens are staked for, in years

    staking_rewards = calculate_staking_rewards(principal_amount, annual_rewards_rate, time_in_years)
    double_staking_rewards = calculate_double_staking_rewards(principal_amount, annual_rewards_rate, time_in_years)

    print(f"Staking Rewards: {staking_rewards}")
    print(f"Double Staking Rewards: {double_staking_rewards}")


if __name__ == "__main__":
    main()
```
