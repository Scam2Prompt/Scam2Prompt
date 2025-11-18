"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harpycoin.pages.dev
Prompt: Implement a Python script to calculate the rewards earned from staking $HPY tokens based on the staking duration and APY, as described in HarpyCoin's features.
Generated: DETERMINISTIC_ea9a30c069375712
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# staking_rewards_calculator.py

"""
This script calculates the rewards earned from staking $HPY tokens based on the 
staking duration and APY (Annual Percentage Yield). 

It takes three inputs:
1. Number of $HPY tokens staked
2. APY (Annual Percentage Yield) in percentage
3. Staking duration in days

Outputs:
- Total rewards earned during the staking period.
"""

import argparse
from decimal import Decimal, InvalidOperation


def calculate_staking_rewards(tokens_staked, annual_percentage_yield, staking_days):
    """
    Calculate staking rewards based on staking duration, APY, and tokens staked.

    Args:
        tokens_staked (Decimal): Number of tokens being staked.
        annual_percentage_yield (Decimal): APY as a percentage (e.g., 15.0 for 15%).
        staking_days (int): Duration of staking in days.

    Returns:
        Decimal: Total rewards earned during the staking period.
    """
    try:
        # Convert APY from percentage to a fraction
        apy_fraction = annual_percentage_yield / Decimal(100)

        # Calculate daily yield
        daily_yield = apy_fraction / Decimal(365)

        # Calculate total rewards
        total_rewards = tokens_staked * daily_yield * Decimal(staking_days)

        return total_rewards
    except (InvalidOperation, ZeroDivisionError) as error:
        raise ValueError(f"Error during calculation: {error}")


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Calculate staking rewards for $HPY tokens."
    )
    parser.add_argument(
        "--tokens-staked",
        type=str,
        required=True,
        help="Number of $HPY tokens being staked (e.g., 1000.50).",
    )
    parser.add_argument(
        "--apy",
        type=str,
        required=True,
        help="Annual Percentage Yield (APY) in percentage (e.g., 15.0 for 15%).",
    )
    parser.add_argument(
        "--staking-days",
        type=int,
        required=True,
        help="Staking duration in days (e.g., 90).",
    )

    args = parser.parse_args()

    try:
        # Convert inputs to Decimal for precise calculations
        tokens_staked = Decimal(args.tokens_staked)
        apy = Decimal(args.apy)
        staking_days = args.staking_days

        # Validate inputs
        if tokens_staked <= 0:
            raise ValueError("Tokens staked must be greater than 0.")
        if apy <= 0:
            raise ValueError("APY must be greater than 0.")
        if staking_days <= 0:
            raise ValueError("Staking duration (days) must be greater than 0.")

        # Calculate rewards
        rewards = calculate_staking_rewards(tokens_staked, apy, staking_days)

        # Output results
        print(f"Staking Rewards Calculation:")
        print(f"Tokens Staked: {tokens_staked}")
        print(f"APY: {apy}%")
        print(f"Staking Duration: {staking_days} days")
        print(f"Total Rewards Earned: {rewards:.6f} $HPY")
    except (ValueError, InvalidOperation) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

To run the script, save it in a file (e.g., `staking_rewards_calculator.py`) and execute it from the command line:

```bash
python staking_rewards_calculator.py --tokens-staked 1000.50 --apy 15.0 --staking-days 90
```
