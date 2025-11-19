"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tgcasino-app.pages.dev
Prompt: Write a Python script that calculates the potential staking rewards for $TGC tokens based on the current APY mentioned on TG.Casino.
Generated: DETERMINISTIC_4cd5d228881bc112
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import argparse

def calculate_staking_rewards(amount, apy, duration_days):
    """
    Calculate the potential staking rewards for $TGC tokens.

    Parameters:
        amount (float): The amount of $TGC tokens being staked.
        apy (float): The annual percentage yield (APY) in percent (e.g., 10.5 for 10.5% APY).
        duration_days (int): The staking duration in days.

    Returns:
        float: The calculated staking rewards.
    """
    try:
        # Convert APY into a daily yield by dividing by 100 (to convert percentage to fraction) and 365 days
        daily_yield_rate = (apy / 100) / 365
        
        # Calculate the rewards based on staking duration
        rewards = amount * daily_yield_rate * duration_days
        
        return rewards
    except Exception as e:
        # Catch unexpected errors during calculation
        raise ValueError(f"Error calculating staking rewards: {str(e)}")


def main():
    """
    Main function to handle script execution.
    """
    try:
        # Set up argument parser for command-line inputs
        parser = argparse.ArgumentParser(description="Calculate potential staking rewards for $TGC tokens.")
        parser.add_argument(
            "-a", "--amount", type=float, required=True,
            help="Amount of $TGC tokens to be staked."
        )
        parser.add_argument(
            "-apy", "--annual-percentage-yield", type=float, required=True,
            help="Annual Percentage Yield (APY) in percent (e.g., 10.5 for 10.5% APY)."
        )
        parser.add_argument(
            "-d", "--days", type=int, required=True,
            help="Staking duration in days."
        )
        
        # Parse arguments
        args = parser.parse_args()
        amount = args.amount
        apy = args.annual_percentage_yield
        duration_days = args.days
        
        # Validate inputs
        if amount <= 0 or apy <= 0 or duration_days <= 0:
            raise ValueError("All input values must be positive numbers.")
        
        # Calculate staking rewards
        rewards = calculate_staking_rewards(amount, apy, duration_days)
        
        # Print the results
        print(f"Staking Amount: {amount} TGC")
        print(f"APY: {apy}%")
        print(f"Staking Duration: {duration_days} days")
        print(f"Potential Rewards: {rewards:.6f} TGC")
    
    except Exception as e:
        # Handle errors and print the message
        print(f"Error: {str(e)}")


# Entry point for script execution
if __name__ == "__main__":
    main()
```
