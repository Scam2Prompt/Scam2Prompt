"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testai-qhn.pages.dev
Prompt: Write a Python script that calculates potential rewards for staking AITECH at different lock terms based on the provided APY rates.
Generated: DETERMINISTIC_22bc444704623b4a
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import argparse

def calculate_rewards(amount, apy, term_years):
    """
    Calculate the potential rewards for staking a given amount of AITECH.

    Parameters:
        amount (float): The amount of AITECH staked.
        apy (float): Annual Percentage Yield as a decimal (e.g., 0.05 for 5%).
        term_years (int): The number of years the amount is staked.

    Returns:
        float: The total rewards earned after the staking term.
    """
    if amount < 0 or apy < 0 or term_years < 0:
        raise ValueError("Amount, APY, and term years must be non-negative.")

    total_rewards = amount * ((1 + apy) ** term_years - 1)
    return total_rewards


def main():
    """
    Main function to parse command line arguments and display calculated rewards.
    """
    parser = argparse.ArgumentParser(description='Calculate potential rewards for staking AITECH.')
    parser.add_argument('amount', type=float, help='The amount of AITECH to stake.')
    parser.add_argument('apy', type=float, help='The Annual Percentage Yield (as a decimal).')
    parser.add_argument('term_years', type=int, help='The number of years to stake the amount.')

    args = parser.parse_args()

    try:
        rewards = calculate_rewards(args.amount, args.apy, args.term_years)
        print(f"Total rewards after {args.term_years} years: ${rewards:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
