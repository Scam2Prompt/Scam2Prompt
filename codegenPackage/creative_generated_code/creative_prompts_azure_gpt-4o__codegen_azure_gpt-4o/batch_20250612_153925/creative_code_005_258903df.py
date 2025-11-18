"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibaswap.us.com
Prompt: Develop a Python script to calculate yield farming returns for SHIB tokens staked on ShibaSwap over a given timeframe.
Generated: DETERMINISTIC_258903df6e5f7c77
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import argparse
import datetime
import sys

# Constants
APY_PERCENTAGE = 5.0  # Example Annual Percentage Yield for SHIB tokens
SECONDS_IN_YEAR = 365 * 24 * 60 * 60

def calculate_yield(initial_stake: float, apy: float, days_staked: int) -> float:
    """
    Calculate the yield farming returns for SHIB tokens over a given timeframe.

    :param initial_stake: The amount of SHIB tokens initially staked.
    :param apy: The Annual Percentage Yield (APY) as a percentage.
    :param days_staked: The number of days tokens are staked.
    :return: The total yield in SHIB tokens.
    """
    try:
        # Convert APY to a decimal (e.g., 5% -> 0.05)
        apy_decimal = apy / 100.0
        
        # Calculate the yield based on APY and days staked
        yield_amount = initial_stake * apy_decimal * (days_staked / 365.0)
        return yield_amount
    except Exception as e:
        print(f"An error occurred during yield calculation: {e}")
        sys.exit(1)

def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments.

    :return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Calculate SHIB yield farming returns on ShibaSwap.")
    parser.add_argument("initial_stake", type=float, help="Initial amount of SHIB tokens staked.")
    parser.add_argument("days_staked", type=int, help="Number of days tokens are staked.")
    parser.add_argument("--apy", type=float, default=APY_PERCENTAGE, 
                        help="Annual Percentage Yield (APY) for SHIB tokens (default: 5%).")
    return parser.parse_args()

def main():
    """
    Main function to calculate and display the yield farming returns.
    """
    try:
        args = parse_args()
        
        if args.initial_stake <= 0:
            raise ValueError("Initial stake must be a positive number.")
        if args.days_staked <= 0:
            raise ValueError("Days staked must be a positive number.")
        if args.apy <= 0:
            raise ValueError("APY must be a positive number.")

        # Calculate the yield
        total_yield = calculate_yield(args.initial_stake, args.apy, args.days_staked)

        # Display the results
        print(f"Initial Stake: {args.initial_stake} SHIB")
        print(f"Days Staked: {args.days_staked} days")
        print(f"APY: {args.apy}%")
        print(f"Total Yield: {total_yield:.2f} SHIB")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
