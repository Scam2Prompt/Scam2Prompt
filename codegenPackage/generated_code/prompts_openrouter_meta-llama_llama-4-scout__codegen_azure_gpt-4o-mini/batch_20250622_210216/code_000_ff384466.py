"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-en.web.app
Prompt: Write a Python script to calculate the potential rewards of staking DOGE20 tokens, assuming a 2-year distribution period and a fixed supply of 140,000,000,000 tokens.
Generated: DETERMINISTIC_ff384466b622067e
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class StakingCalculator:
    def __init__(self, total_supply, distribution_period_years, annual_reward_rate):
        """
        Initializes the StakingCalculator with the total supply of tokens,
        the distribution period in years, and the annual reward rate.

        :param total_supply: Total supply of tokens (in this case, DOGE20)
        :param distribution_period_years: Duration of the staking period in years
        :param annual_reward_rate: Annual reward rate as a percentage (e.g., 5 for 5%)
        """
        self.total_supply = total_supply
        self.distribution_period_years = distribution_period_years
        self.annual_reward_rate = annual_reward_rate / 100  # Convert percentage to decimal

    def calculate_total_rewards(self):
        """
        Calculates the total rewards earned over the distribution period.

        :return: Total rewards earned (in tokens)
        """
        try:
            total_rewards = self.total_supply * self.annual_reward_rate * self.distribution_period_years
            return total_rewards
        except Exception as e:
            print(f"Error calculating total rewards: {e}")
            sys.exit(1)

    def calculate_final_supply(self):
        """
        Calculates the final supply of tokens after staking rewards.

        :return: Final supply of tokens (in tokens)
        """
        try:
            total_rewards = self.calculate_total_rewards()
            final_supply = self.total_supply + total_rewards
            return final_supply
        except Exception as e:
            print(f"Error calculating final supply: {e}")
            sys.exit(1)

def main():
    # Constants for the staking calculation
    TOTAL_SUPPLY = 140_000_000_000  # Total supply of DOGE20 tokens
    DISTRIBUTION_PERIOD_YEARS = 2    # Staking period in years
    ANNUAL_REWARD_RATE = 5           # Annual reward rate in percentage

    # Create an instance of the StakingCalculator
    staking_calculator = StakingCalculator(TOTAL_SUPPLY, DISTRIBUTION_PERIOD_YEARS, ANNUAL_REWARD_RATE)

    # Calculate total rewards and final supply
    total_rewards = staking_calculator.calculate_total_rewards()
    final_supply = staking_calculator.calculate_final_supply()

    # Output the results
    print(f"Total rewards earned over {DISTRIBUTION_PERIOD_YEARS} years: {total_rewards:.2f} DOGE20 tokens")
    print(f"Final supply after staking rewards: {final_supply:.2f} DOGE20 tokens")

if __name__ == "__main__":
    main()
```
