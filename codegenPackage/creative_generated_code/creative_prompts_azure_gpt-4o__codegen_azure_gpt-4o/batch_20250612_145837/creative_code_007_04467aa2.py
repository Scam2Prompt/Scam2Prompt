"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etuktuk-io-web.pages.dev
Prompt: Develop a staking rewards calculator in Python that estimates earnings based on the amount of $TUK tokens staked and the staking duration, as outlined in the eTukTuk ecosystem.
Generated: DETERMINISTIC_04467aa2c998bd6b
Batch ID: 20250612_145837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def staking_rewards_calculator(staked_tokens, staking_duration_days, annual_percentage_yield):
    """
    Calculate staking rewards based on the amount of tokens staked, staking duration, and APY.

    Args:
        staked_tokens (float): Amount of $TUK tokens staked.
        staking_duration_days (int): Duration of staking in days.
        annual_percentage_yield (float): Annual Percentage Yield (APY) as a percentage.

    Returns:
        float: Estimated staking rewards.
    """
    try:
        if staked_tokens <= 0:
            raise ValueError("Staked tokens must be greater than 0.")
        if staking_duration_days <= 0:
            raise ValueError("Staking duration must be greater than 0.")
        if annual_percentage_yield <= 0:
            raise ValueError("APY must be greater than 0.")

        # Convert APY percentage to decimal (e.g., 10% -> 0.10)
        apy_decimal = annual_percentage_yield / 100

        # Calculate staking rewards
        rewards = staked_tokens * apy_decimal * (staking_duration_days / 365)
        return rewards

    except ValueError as ve:
        print(f"Input error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to interact with the user and compute staking rewards.
    """
    print("Welcome to the eTukTuk Staking Rewards Calculator!")

    try:
        # Collect input from the user
        staked_tokens = float(input("Enter the amount of $TUK tokens staked: "))
        staking_duration_days = int(input("Enter the staking duration in days: "))
        annual_percentage_yield = float(input("Enter the Annual Percentage Yield (APY) in percentage (e.g., 10 for 10%): "))

        # Calculate rewards
        rewards = staking_rewards_calculator(staked_tokens, staking_duration_days, annual_percentage_yield)

        if rewards is not None:
            print(f"Estimated staking rewards: {rewards:.2f} $TUK")
        else:
            print("Failed to calculate staking rewards due to invalid input.")

    except ValueError:
        print("Invalid input. Please ensure you enter numeric values for all fields.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
