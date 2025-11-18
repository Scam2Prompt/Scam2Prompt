"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casinotg.pages.dev
Prompt: Generate code to calculate staking rewards for `$TGC` tokens based on TG.Casino's tokenomics, including daily reward distribution.
Generated: DETERMINISTIC_f7766862f9255ffc
Batch ID: 20250612_150435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class StakingCalculator:
    """
    A class to calculate staking rewards for $TGC tokens based on TG.Casino's tokenomics.
    """

    def __init__(self, total_supply: int, reward_per_day: float, staking_duration: int):
        """
        Initializes the StakingCalculator with the required parameters.

        :param total_supply: Total supply of $TGC tokens.
        :param reward_per_day: Daily reward distributed to stakers.
        :param staking_duration: Duration for which tokens are staked (in days).
        """
        self.total_supply = total_supply
        self.reward_per_day = reward_per_day
        self.staking_duration = staking_duration

    def calculate_total_rewards(self) -> float:
        """
        Calculates the total rewards earned over the staking duration.

        :return: Total staking rewards.
        """
        if self.staking_duration <= 0:
            raise ValueError("Staking duration must be greater than zero.")
        
        total_rewards = self.reward_per_day * self.staking_duration
        return total_rewards

    def calculate_rewards_for_amount(self, staked_amount: float) -> float:
        """
        Calculates the rewards based on the amount of tokens staked.

        :param staked_amount: Amount of $TGC tokens being staked.
        :return: Total rewards for the staked amount.
        """
        if staked_amount < 0:
            raise ValueError("Staked amount cannot be negative.")
        if staked_amount > self.total_supply:
            raise ValueError("Staked amount cannot exceed total supply.")

        # Calculate the reward proportionate to the staked amount
        total_rewards = self.calculate_total_rewards()
        rewards_for_amount = (staked_amount / self.total_supply) * total_rewards
        
        return rewards_for_amount

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the staking calculator with hypothetical parameters
        total_supply = 1_000_000  # Total supply of $TGC tokens
        reward_per_day = 500  # Daily reward distributed
        staking_duration = 30  # Staking duration in days
        
        # Create an instance of the StakingCalculator
        staking_calculator = StakingCalculator(total_supply, reward_per_day, staking_duration)
        
        # Calculate rewards for a specific staked amount
        staked_amount = 10_000  # Amount of $TGC tokens being staked
        rewards = staking_calculator.calculate_rewards_for_amount(staked_amount)
        
        print(f"Total rewards for staking {staked_amount} $TGC over {staking_duration} days: ${rewards:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
