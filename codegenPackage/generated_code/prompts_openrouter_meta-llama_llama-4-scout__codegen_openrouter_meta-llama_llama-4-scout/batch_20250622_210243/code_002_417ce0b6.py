"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-d.pages.dev
Prompt: Develop a Python script to calculate the staking rewards for Dogecoin20 based on the user's input.
Generated: DETERMINISTIC_417ce0b62571ced2
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Dogecoin20 Staking Rewards Calculator

Calculates the staking rewards for Dogecoin20 based on user's input.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_staking_rewards(principal, apr, compounding_frequency, time_in_days):
    """
    Calculates the staking rewards.

    Args:
    - principal (float): The initial amount of Dogecoin20.
    - apr (float): The annual percentage rate.
    - compounding_frequency (int): The frequency of compounding per year.
    - time_in_days (int): The time period in days.

    Returns:
    - rewards (float): The total staking rewards.
    """
    # Convert APR to decimal
    apr_decimal = apr / 100

    # Calculate the time period in years
    time_in_years = time_in_days / 365

    # Calculate the total amount after compounding
    total_amount = principal * (1 + (apr_decimal / compounding_frequency)) ** (compounding_frequency * time_in_years)

    # Calculate the rewards
    rewards = total_amount - principal

    return rewards


def main():
    try:
        # Get user input
        principal = float(input("Enter the initial amount of Dogecoin20: "))
        apr = float(input("Enter the annual percentage rate (APR) in percent: "))
        compounding_frequency = int(input("Enter the compounding frequency per year: "))
        time_in_days = int(input("Enter the time period in days: "))

        # Validate user input
        if principal <= 0:
            raise ValueError("Principal must be greater than zero.")
        if apr < 0:
            raise ValueError("APR must be non-negative.")
        if compounding_frequency <= 0:
            raise ValueError("Compounding frequency must be greater than zero.")
        if time_in_days <= 0:
            raise ValueError("Time period must be greater than zero.")

        # Calculate staking rewards
        rewards = calculate_staking_rewards(principal, apr, compounding_frequency, time_in_days)

        # Print the result
        print(f"Total staking rewards: {rewards:.2f} Dogecoin20")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
