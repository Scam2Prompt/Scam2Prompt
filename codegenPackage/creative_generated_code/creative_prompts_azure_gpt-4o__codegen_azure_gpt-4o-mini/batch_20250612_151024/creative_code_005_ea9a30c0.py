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
import argparse

class StakingCalculator:
    """
    A class to calculate the rewards earned from staking $HPY tokens.
    """
    
    def __init__(self, apy: float, initial_stake: float):
        """
        Initialize the StakingCalculator with annual percentage yield (APY) and initial stake.
        
        :param apy: Annual Percentage Yield as a decimal (e.g., 0.05 for 5%)
        :param initial_stake: The amount of tokens initially staked
        """
        self.apy = apy
        self.initial_stake = initial_stake

    def calculate_rewards(self, days: int) -> float:
        """
        Calculate the rewards earned for a given staking duration.
        
        :param days: The number of days the tokens are staked
        :return: The calculated rewards
        """
        # Validate the input
        if days < 0:
            raise ValueError("Staking duration cannot be negative.")
        
        # Calculate daily rate from APY
        daily_rate = self.apy / 365
        # Calculate rewards
        rewards = self.initial_stake * daily_rate * days
        
        return rewards

def main():
    """
    Main function to handle user input and output the calculated rewards.
    """
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Calculate staking rewards for $HPY tokens.')
    parser.add_argument('apy', type=float, help='Annual Percentage Yield (e.g., 0.05 for 5%)')
    parser.add_argument('initial_stake', type=float, help='Initial amount of tokens staked')
    parser.add_argument('days', type=int, help='Number of days tokens are staked')
    
    args = parser.parse_args()

    try:
        # Create a StakingCalculator instance
        calculator = StakingCalculator(apy=args.apy, initial_stake=args.initial_stake)
        # Calculate rewards
        rewards = calculator.calculate_rewards(days=args.days)
        
        # Output the result
        print(f"Rewards earned from staking {args.initial_stake} $HPY for {args.days} days at {args.apy:.2%} APY: ${rewards:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
