"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egld.pages.dev
Prompt: Write a Python script to calculate EGLD staking rewards based on the formula provided by MultiversX.
Generated: DETERMINISTIC_64053bd550638dd6
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate EGLD staking rewards based on the formula provided by MultiversX.

Assumptions:
- Rewards are calculated based on a fixed annual percentage rate (APR).
- Compound interest is applied daily.
- User provides initial staked amount, APR, and staking duration in days.

Author: Expert Programmer
"""

import argparse
from typing import Optional

def calculate_staking_rewards(initial_stake: float, apr: float, days: int) -> Optional[float]:
    """
    Calculate EGLD staking rewards.

    Parameters:
        initial_stake (float): The amount of EGLD staked.
        apr (float): Annual Percentage Rate (APR) in percentage. (e.g., 10 for 10%).
        days (int): Duration of staking in days.

    Returns:
        float: Total rewards after staking duration.
    """
    try:
        # Convert APR to daily interest rate (APR / 365)
        daily_rate = apr / 100 / 365

        # Calculate rewards using compound interest formula
        # Total = Principal * (1 + DailyRate)^(Days)
        total_amount = initial_stake * ((1 + daily_rate) ** days)

        # Rewards = Total Amount - Initial Stake
        rewards = total_amount - initial_stake

        return rewards
    except Exception as e:
        print(f"Error calculating staking rewards: {e}")
        return None

def parse_arguments():
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments containing initial stake, APR, and duration.
    """
    parser = argparse.ArgumentParser(description="Calculate EGLD staking rewards.")
    parser.add_argument(
        "--initial-stake",
        type=float,
        required=True,
        help="Initial amount of EGLD staked."
    )
    parser.add_argument(
        "--apr",
        type=float,
        required=True,
        help="Annual Percentage Rate (APR) in percentage (e.g., 10 for 10%)."
    )
    parser.add_argument(
        "--days",
        type=int,
        required=True,
        help="Staking duration in days."
    )
    return parser.parse_args()

def main():
    """
    Main function to handle user input and display staking rewards.
    """
    try:
        # Parse command-line arguments
        args = parse_arguments()

        # Calculate rewards
        rewards = calculate_staking_rewards(args.initial_stake, args.apr, args.days)

        # Display results
        if rewards is not None:
            print(f"Initial Stake: {args.initial_stake:.4f} EGLD")
            print(f"APR: {args.apr:.2f}%")
            print(f"Staking Duration: {args.days} days")
            print(f"Estimated Rewards: {rewards:.4f} EGLD")
        else:
            print("Failed to calculate staking rewards.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
