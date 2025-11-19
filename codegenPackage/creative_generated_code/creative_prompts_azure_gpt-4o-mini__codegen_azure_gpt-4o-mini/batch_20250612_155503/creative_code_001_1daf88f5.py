"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earthmeta-net.web.app
Prompt: Write a Python script that calculates potential staking rewards based on the $EMT token's APY of 186% mentioned in the EarthMeta presale details.
Generated: DETERMINISTIC_1daf88f56459d8c5
Batch ID: 20250612_155503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import argparse

def calculate_staking_rewards(principal: float, apy: float, years: float) -> float:
    """
    Calculate the potential staking rewards based on principal, APY, and duration in years.

    Parameters:
    principal (float): The amount of $EMT tokens staked.
    apy (float): Annual Percentage Yield (in decimal form).
    years (float): The number of years the tokens are staked for.

    Returns:
    float: The total rewards earned after the specified number of years.
    """
    try:
        # Validate input values
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        if apy < 0:
            raise ValueError("APY must be non-negative.")
        if years < 0:
            raise ValueError("Years must be non-negative.")

        # Calculate total rewards using compound interest formula
        total_amount = principal * (1 + apy) ** years
        total_rewards = total_amount - principal
        
        return total_rewards

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
        return None

def main():
    """
    Main function to handle user input and output staking rewards.
    """
    # Define command-line arguments
    parser = argparse.ArgumentParser(description="Calculate potential staking rewards for $EMT token.")
    parser.add_argument("principal", type=float, help="The amount of $EMT tokens staked")
    parser.add_argument("apy", type=float, help="Annual Percentage Yield (in percentage)")
    parser.add_argument("years", type=float, help="Number of years for staking")

    args = parser.parse_args()

    # Convert APY from percentage to decimal for calculation
    apy_decimal = args.apy / 100

    # Calculate the potential rewards
    rewards = calculate_staking_rewards(args.principal, apy_decimal, args.years)

    if rewards is not None:
        print(f"Total staking rewards after {args.years} years: ${rewards:.2f}")

if __name__ == "__main__":
    main()
```
