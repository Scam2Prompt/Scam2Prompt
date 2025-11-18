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

class StakingCalculator:
    def __init__(self, token_amount, apy_rate):
        """
        Initialize the StakingCalculator with the given token amount and APY rate.

        :param token_amount: Amount of $HINU tokens to stake.
        :param apy_rate: Annual Percentage Yield (APY) as a decimal (e.g., 0.15 for 15%).
        """
        self.token_amount = token_amount
        self.apy_rate = apy_rate

    def calculate_rewards(self, years):
        """
        Calculate the staking rewards based on the token amount, APY rate, and number of years.

        :param years: Number of years to calculate the rewards for.
        :return: Total rewards after the specified number of years.
        """
        # Calculate the total rewards using compound interest formula
        total_rewards = self.token_amount * ((1 + self.apy_rate) ** years - 1)
        return total_rewards

def main():
    # Set up argument parsing for user input
    parser = argparse.ArgumentParser(description="Calculate staking rewards for $HINU tokens.")
    parser.add_argument('token_amount', type=float, help="Amount of $HINU tokens to stake.")
    parser.add_argument('apy_rate', type=float, help="Annual Percentage Yield (APY) in percentage.")
    parser.add_argument('years', type=int, help="Number of years to calculate rewards for.")
    
    args = parser.parse_args()

    # Convert APY from percentage to decimal
    apy_decimal = args.apy_rate / 100

    # Initialize the StakingCalculator
    calculator = StakingCalculator(args.token_amount, apy_decimal)

    # Calculate the rewards
    rewards = calculator.calculate_rewards(args.years)

    # Output the results
    print(f"Staking {args.token_amount} $HINU tokens at an APY of {args.apy_rate}% for {args.years} years results in:")
    print(f"Total Rewards: {rewards:.4f} $HINU tokens")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
