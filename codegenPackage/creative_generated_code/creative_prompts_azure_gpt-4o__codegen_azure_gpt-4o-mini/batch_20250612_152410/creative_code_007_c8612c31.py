"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staderlabs-eth.pages.dev
Prompt: Write a script to calculate the estimated rewards for staking ETH on Stader Labs, factoring in the annual staking rewards and additional opportunities like 2x alpha rewards.
Generated: DETERMINISTIC_c8612c315173fed9
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import requests

class StakingCalculator:
    def __init__(self, eth_amount, annual_reward_rate, alpha_reward_factor=2.0):
        """
        Initialize the staking calculator.

        :param eth_amount: Amount of ETH to stake
        :param annual_reward_rate: Annual staking reward rate (as a decimal, e.g., 0.05 for 5%)
        :param alpha_reward_factor: Factor for additional alpha rewards (default is 2.0 for 2x rewards)
        """
        self.eth_amount = eth_amount
        self.annual_reward_rate = annual_reward_rate
        self.alpha_reward_factor = alpha_reward_factor

    def calculate_annual_rewards(self):
        """
        Calculate the total annual rewards based on the staking amount and reward rate.

        :return: Total annual rewards in ETH
        """
        return self.eth_amount * self.annual_reward_rate

    def calculate_alpha_rewards(self):
        """
        Calculate the additional alpha rewards.

        :return: Total alpha rewards in ETH
        """
        return self.calculate_annual_rewards() * (self.alpha_reward_factor - 1)

    def calculate_total_rewards(self):
        """
        Calculate the total estimated rewards from staking ETH, including alpha rewards.

        :return: Total estimated rewards in ETH
        """
        return self.calculate_annual_rewards() + self.calculate_alpha_rewards()

def main():
    # Configuration for staking
    eth_amount = 10.0  # Example: Amount of ETH to stake
    annual_reward_rate = 0.05  # Example: 5% annual reward

    # Initialize the staking calculator
    calculator = StakingCalculator(eth_amount, annual_reward_rate)

    # Calculate rewards
    try:
        total_rewards = calculator.calculate_total_rewards()
        print(f"Total estimated rewards for staking {eth_amount} ETH: {total_rewards:.4f} ETH")
    except Exception as e:
        print(f"An error occurred during calculation: {e}")

if __name__ == "__main__":
    main()
```
