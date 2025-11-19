"""
Generated Code Metadata:
========================
Original URL: https://memeindexlive.pages.dev
Prompt: Create a Python script to calculate the potential APY for staking $MEMEX tokens during presale, considering the 25% supply dedicated to staking rewards.
Generated: DETERMINISTIC_6eab4bd9bbe72151
Batch ID: 20250622_211639
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
    def __init__(self, total_supply: float, staking_rewards_percentage: float, staking_amount: float, duration_days: int):
        """
        Initialize the StakingCalculator with the necessary parameters.

        :param total_supply: Total supply of the token.
        :param staking_rewards_percentage: Percentage of total supply dedicated to staking rewards.
        :param staking_amount: Amount of tokens being staked.
        :param duration_days: Duration of staking in days.
        """
        self.total_supply = total_supply
        self.staking_rewards_percentage = staking_rewards_percentage
        self.staking_amount = staking_amount
        self.duration_days = duration_days

    def calculate_apy(self) -> float:
        """
        Calculate the Annual Percentage Yield (APY) for staking.

        :return: The calculated APY as a percentage.
        """
        try:
            # Calculate total staking rewards available
            total_staking_rewards = self.total_supply * (self.staking_rewards_percentage / 100)

            # Calculate the potential rewards for the staked amount
            potential_rewards = (total_staking_rewards * (self.staking_amount / self.total_supply))

            # Calculate APY based on the duration of staking
            apy = (potential_rewards / self.staking_amount) * (365 / self.duration_days) * 100

            return apy
        except ZeroDivisionError:
            print("Error: Duration of staking cannot be zero.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)

def main():
    # Example parameters
    total_supply = 1000000  # Total supply of $MEMEX tokens
    staking_rewards_percentage = 25  # 25% of total supply for staking rewards
    staking_amount = 1000  # Amount of tokens being staked
    duration_days = 30  # Duration of staking in days

    # Create an instance of StakingCalculator
    calculator = StakingCalculator(total_supply, staking_rewards_percentage, staking_amount, duration_days)

    # Calculate and print the APY
    apy = calculator.calculate_apy()
    print(f"The potential APY for staking ${staking_amount} $MEMEX tokens is: {apy:.2f}%")

if __name__ == "__main__":
    main()
```
