"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://incubetaipo.pages.dev
Prompt: Write a code snippet to calculate potential rewards from staking $QUBE tokens based on the 5% sell tax and the dedicated reward pool mentioned on the InQubeta platform.
Generated: DETERMINISTIC_5d2b76032d793fde
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingCalculator:
    """
    A class to calculate potential rewards from staking $QUBE tokens.
    """

    def __init__(self, total_tokens_staked: float, reward_pool: float, sell_tax_rate: float = 0.05):
        """
        Initializes the StakingCalculator with the total tokens staked,
        the reward pool amount, and the sell tax rate.

        :param total_tokens_staked: Total amount of $QUBE tokens staked
        :param reward_pool: Total amount of rewards available in the pool
        :param sell_tax_rate: Tax rate applied to selling $QUBE tokens
        """
        self.total_tokens_staked = total_tokens_staked
        self.reward_pool = reward_pool
        self.sell_tax_rate = sell_tax_rate

    def calculate_rewards(self) -> float:
        """
        Calculate the potential rewards from staking based on the provided 
        stake and reward pool.

        :return: The potential reward amount
        """
        if self.total_tokens_staked <= 0:
            raise ValueError("Total tokens staked must be greater than zero.")
        if self.reward_pool < 0:
            raise ValueError("Reward pool must not be negative.")

        # Calculate the effective reward pool after considering the sell tax
        effective_reward_pool = self.reward_pool * (1 - self.sell_tax_rate)

        # Calculate the reward based on the proportion of tokens staked
        rewards = (self.total_tokens_staked / self.total_tokens_staked) * effective_reward_pool

        return rewards

# Example usage
if __name__ == "__main__":
    try:
        # Assume an example where 1000 $QUBE tokens are staked and the reward pool is $5000
        total_staked = 1000.0  # Example: 1000 tokens
        reward_pool = 5000.0    # Example: $5000 in the reward pool

        staking_calculator = StakingCalculator(total_staked, reward_pool)
        potential_rewards = staking_calculator.calculate_rewards()

        print(f"Potential rewards from staking: ${potential_rewards:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
