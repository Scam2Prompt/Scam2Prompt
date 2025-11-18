"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-scorpion-casino.pages.dev
Prompt: Write a Python script to calculate daily staking rewards for $SCORP token holders, factoring in the automatic token burn and buy-back system described in the Scorpion Casino ecosystem.
Generated: DETERMINISTIC_ddfc0dd99d50489c
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class StakingRewardsCalculator:
    def __init__(self, total_supply, staking_pool, burn_rate, buy_back_rate):
        """
        Initialize the staking rewards calculator with key parameters.

        :param total_supply: Total supply of $SCORP tokens
        :param staking_pool: Total amount of $SCORP tokens staked
        :param burn_rate: Percentage of tokens burned daily (0 to 1)
        :param buy_back_rate: Percentage of tokens bought back daily (0 to 1)
        """
        self.total_supply = total_supply
        self.staking_pool = staking_pool
        self.burn_rate = burn_rate
        self.buy_back_rate = buy_back_rate

    def calculate_daily_rewards(self, staked_tokens):
        """
        Calculate the daily staking rewards for a given amount of staked tokens.

        :param staked_tokens: Amount of tokens staked by the user
        :return: Daily rewards amount
        """
        if staked_tokens < 0:
            raise ValueError("Staked tokens cannot be negative.")
        if staked_tokens > self.staking_pool:
            raise ValueError("Cannot stake more tokens than are in the staking pool.")
        
        # Calculate total daily rewards based on staking pool size
        daily_rewards_pool = self.staking_pool * (1 - self.burn_rate) * (1 - self.buy_back_rate)
        
        # Calculate user rewards based on their share of the staking pool
        user_share = staked_tokens / self.staking_pool
        daily_rewards = daily_rewards_pool * user_share
        
        return daily_rewards

    def apply_burn_and_buyback(self):
        """
        Simulate the burning and buying back of tokens based on the rates defined.
        
        This method updates the staking pool and total supply after applying
        the burn and buy-back rates.
        """
        # Calculate tokens to be burned and bought back
        tokens_to_burn = self.staking_pool * self.burn_rate
        tokens_to_buyback = self.staking_pool * self.buy_back_rate
        
        # Update total supply and staking pool
        self.total_supply -= tokens_to_burn
        self.staking_pool -= tokens_to_buyback
        
        # Log the changes
        print(f"{datetime.datetime.now()}: Burned {tokens_to_burn} tokens.")
        print(f"{datetime.datetime.now()}: Bought back {tokens_to_buyback} tokens.")

def main():
    # Configuration for the staking rewards calculator
    total_supply = 1_000_000  # Total supply of $SCORP tokens
    staking_pool = 500_000     # Total amount of $SCORP tokens staked
    burn_rate = 0.01           # Daily burn rate: 1%
    buy_back_rate = 0.02       # Daily buy-back rate: 2%

    # Create a rewards calculator instance
    rewards_calculator = StakingRewardsCalculator(total_supply, staking_pool, burn_rate, buy_back_rate)

    # Simulate daily staking rewards calculation for a user who staked 10,000 tokens
    try:
        staked_tokens = 10_000
        daily_rewards = rewards_calculator.calculate_daily_rewards(staked_tokens)
        print(f"Daily rewards for staking {staked_tokens} tokens: {daily_rewards}")

        # Apply burn and buy-back for the day
        rewards_calculator.apply_burn_and_buyback()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
