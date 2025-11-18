"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.staderlabs.fi
Prompt: Write a script to calculate staking rewards for liquid tokens issued by Stader Labs, factoring in yield redirection farming and preferential delegations.
Generated: DETERMINISTIC_4bff611547121aa6
Batch ID: 20250612_153820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal
import requests

class StakingRewardCalculator:
    def __init__(self, total_staked, reward_rate, redirection_factor, delegation_factor):
        """
        Initialize the StakingRewardCalculator with the necessary parameters.

        :param total_staked: Total amount of tokens staked
        :param reward_rate: Base reward rate for staking
        :param redirection_factor: Yield redirection farming factor (as a decimal, e.g., 0.1 for 10%)
        :param delegation_factor: Preferential delegation factor (as a decimal, e.g., 0.2 for 20%)
        """
        self.total_staked = decimal.Decimal(total_staked)
        self.reward_rate = decimal.Decimal(reward_rate)
        self.redirection_factor = decimal.Decimal(redirection_factor)
        self.delegation_factor = decimal.Decimal(delegation_factor)

    def calculate_rewards(self):
        """
        Calculate the total staking rewards based on the parameters provided.

        :return: Total calculated rewards
        """
        try:
            # Calculate the base rewards
            base_rewards = self.total_staked * self.reward_rate
            
            # Calculate additional rewards from yield redirection farming
            redirection_rewards = base_rewards * self.redirection_factor
            
            # Calculate additional rewards from preferential delegations
            delegation_rewards = base_rewards * self.delegation_factor
            
            # Total rewards
            total_rewards = base_rewards + redirection_rewards + delegation_rewards
            
            return total_rewards
        except Exception as e:
            print(f"An error occurred while calculating rewards: {e}")
            return decimal.Decimal(0)

def main():
    """
    Main function to execute the staking rewards calculation.
    The parameters can be modified as needed.
    """
    total_staked = input("Enter the total amount of tokens staked: ")
    reward_rate = input("Enter the reward rate (as a decimal, e.g., 0.05 for 5%): ")
    redirection_factor = input("Enter the yield redirection farming factor (as a decimal): ")
    delegation_factor = input("Enter the preferential delegation factor (as a decimal): ")

    try:
        calculator = StakingRewardCalculator(
            total_staked=float(total_staked),
            reward_rate=float(reward_rate),
            redirection_factor=float(redirection_factor),
            delegation_factor=float(delegation_factor)
        )

        rewards = calculator.calculate_rewards()
        print(f"Total staking rewards: {rewards:.2f}")

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

This script is designed to be clear, efficient, and ready for production use. It includes error handling for user input and calculates staking rewards based on the specified parameters.
