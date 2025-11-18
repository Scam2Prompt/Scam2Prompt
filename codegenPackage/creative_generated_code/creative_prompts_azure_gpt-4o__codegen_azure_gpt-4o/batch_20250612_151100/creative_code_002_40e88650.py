"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thehuskyinu-io.pages.dev
Prompt: Generate a Python script to calculate the staking rewards for $HINU tokens based on APY rates provided by the Husky Inu platform.
Generated: DETERMINISTIC_40e8865013fd3356
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import argparse
import sys

def calculate_staking_rewards(principal, apy_rate, days_staked):
    """
    Calculate staking rewards for $HINU tokens based on given parameters.

    :param principal: The initial amount of $HINU tokens staked.
    :param apy_rate: Annual Percentage Yield (APY) rate as a percentage (e.g., 12 for 12% APY).
    :param days_staked: Number of days the tokens are staked.
    :return: Total rewards accrued from staking.
    """
    try:
        # APY rate converted to daily rate
        daily_rate = apy_rate / 100 / 365  
        
        # Total rewards calculation
        rewards = principal * daily_rate * days_staked
        
        return rewards
    
    except Exception as e:
        raise ValueError(f"Error calculating staking rewards: {str(e)}")

def main():
    """
    Main function to parse user input and calculate staking rewards.
    """
    parser = argparse.ArgumentParser(description="Calculate staking rewards for $HINU tokens.")
    parser.add_argument(
        "-p", "--principal", type=float, required=True,
        help="Initial amount of $HINU tokens staked."
    )
    parser.add_argument(
        "-r", "--apy_rate", type=float, required=True,
        help="Annual Percentage Yield (APY) rate as a percentage (e.g., 12 for 12% APY)."
    )
    parser.add_argument(
        "-d", "--days_staked", type=int, required=True,
        help="Number of days the tokens are staked."
    )
    
    args = parser.parse_args()

    try:
        # Validate input
        if args.principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if args.apy_rate <= 0:
            raise ValueError("APY rate must be greater than zero.")
        if args.days_staked <= 0:
            raise ValueError("Days staked must be greater than zero.")
        
        # Calculate rewards
        rewards = calculate_staking_rewards(args.principal, args.apy_rate, args.days_staked)
        print(f"\nStaking Rewards Calculation:")
        print(f"Principal: {args.principal} $HINU")
        print(f"APY Rate: {args.apy_rate}%")
        print(f"Days Staked: {args.days_staked}")
        print(f"Rewards Accrued: {rewards:.2f} $HINU")
    
    except ValueError as ve:
        print(f"Input Error: {str(ve)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
