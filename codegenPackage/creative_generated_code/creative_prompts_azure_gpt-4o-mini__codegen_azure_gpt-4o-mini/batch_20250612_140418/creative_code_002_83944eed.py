"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-ai.web.app
Prompt: Create a function that calculates the potential rewards from staking $QUBE tokens based on the provided tokenomics details.
Generated: DETERMINISTIC_83944eedb0277a62
Batch ID: 20250612_140418
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
    A class to calculate potential rewards from staking $QUBE tokens based on tokenomics details.
    """

    def __init__(self, total_supply, circulating_supply, rewards_per_block, blocks_per_day, staking_percentage):
        """
        Initializes the staking calculator with necessary tokenomics details.

        :param total_supply: Total supply of $QUBE tokens
        :param circulating_supply: Circulating supply of $QUBE tokens
        :param rewards_per_block: Total rewards distributed per block
        :param blocks_per_day: Number of blocks produced in a day
        :param staking_percentage: Percentage of tokens staked
        """
        self.total_supply = total_supply
        self.circulating_supply = circulating_supply
        self.rewards_per_block = rewards_per_block
        self.blocks_per_day = blocks_per_day
        self.staking_percentage = staking_percentage / 100.0  # Convert percentage to decimal

    def calculate_staked_tokens(self, staked_amount):
        """
        Calculates the amount of tokens that are staked.

        :param staked_amount: Amount of $QUBE tokens staked
        :return: Amount of tokens staked in the system
        """
        if staked_amount < 0:
            raise ValueError("Staked amount cannot be negative.")
        return staked_amount * self.staking_percentage

    def calculate_daily_rewards(self, staked_amount):
        """
        Calculates the potential daily rewards for staked $QUBE tokens.

        :param staked_amount: Amount of $QUBE tokens staked
        :return: Estimated daily rewards
        """
        staked_tokens = self.calculate_staked_tokens(staked_amount)
        if staked_tokens > self.circulating_supply:
            raise ValueError("Staked tokens exceed circulating supply.")
        
        # Calculate the daily rewards based on the proportion of staked tokens
        daily_rewards = (staked_tokens / self.circulating_supply) * self.rewards_per_block * self.blocks_per_day
        return daily_rewards

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the staking calculator with example tokenomics data
        staking_calculator = StakingCalculator(
            total_supply=100_000_000,  # Total supply of $QUBE
            circulating_supply=75_000_000,  # Circulating supply of $QUBE
            rewards_per_block=1000,  # Rewards per block
            blocks_per_day=720,  # Blocks per day
            staking_percentage=30  # 30% of tokens are staked
        )

        # Calculate potential daily rewards for a given staked amount
        staked_amount = 10_000  # Amount of $QUBE tokens staked
        daily_rewards = staking_calculator.calculate_daily_rewards(staked_amount)
        print(f"Estimated Daily Rewards for {staked_amount} staked QUBE: {daily_rewards:.2f} tokens")

    except Exception as e:
        print(f"An error occurred: {e}")
```
