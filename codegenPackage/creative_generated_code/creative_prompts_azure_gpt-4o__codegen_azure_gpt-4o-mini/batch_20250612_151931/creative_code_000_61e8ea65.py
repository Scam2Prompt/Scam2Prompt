"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bananagunn.io
Prompt: Write a script to calculate rewards for holding $BANANA tokens based on the APR and epoch duration, including separate calculations for EVM and Solana rewards as described on the Bananagun Rewards page.
Generated: DETERMINISTIC_61e8ea65122281a0
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time


class TokenRewardsCalculator:
    """
    A class to calculate rewards for holding $BANANA tokens based on APR and epoch duration.
    Supports calculations for both EVM and Solana rewards.
    """

    def __init__(self, apr, epoch_duration, token_amount):
        """
        Initializes the rewards calculator with the given parameters.

        :param apr: Annual Percentage Rate (as a decimal, e.g., 0.05 for 5%)
        :param epoch_duration: Duration of each epoch in seconds
        :param token_amount: Amount of $BANANA tokens held
        """
        self.apr = apr
        self.epoch_duration = epoch_duration
        self.token_amount = token_amount

    def calculate_rewards(self):
        """
        Calculates the rewards for the given token amount based on APR and epoch duration.

        :return: A dictionary with rewards for EVM and Solana
        """
        try:
            # Rewards calculation
            rewards_per_epoch = self.token_amount * (self.apr / 365) * (self.epoch_duration / 86400)
            return {
                "EVM_rewards": rewards_per_epoch,
                "Solana_rewards": rewards_per_epoch * 1.2  # Example multiplier for Solana
            }
        except ZeroDivisionError:
            raise ValueError("Epoch duration must be greater than zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating rewards: {e}")


if __name__ == "__main__":
    # Example usage of the TokenRewardsCalculator class
    try:
        # Input parameters
        apr = 0.05  # 5% APR
        epoch_duration = 604800  # 1 week in seconds
        token_amount = 1000  # Amount of $BANANA tokens

        # Initialize the calculator
        rewards_calculator = TokenRewardsCalculator(apr, epoch_duration, token_amount)

        # Calculate rewards
        rewards = rewards_calculator.calculate_rewards()
        print("Rewards calculated:")
        print(f"EVM Rewards: {rewards['EVM_rewards']:.4f} $BANANA")
        print(f"Solana Rewards: {rewards['Solana_rewards']:.4f} $BANANA")
    except Exception as e:
        print(f"Error: {e}")
```
