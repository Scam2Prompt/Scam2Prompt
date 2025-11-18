"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yfyuyyufy.pages.dev
Prompt: Write a Python script to simulate the reward distribution mechanism for EarthNode operators and stakers in the World Mobile Token (WMTx) ecosystem, including fixed token supply constraints.
Generated: DETERMINISTIC_59f3eb5d2cb58f3b
Batch ID: 20250612_150012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from decimal import Decimal, getcontext

# Set the precision for Decimal operations
getcontext().prec = 18

class WMTxRewardDistributor:
    def __init__(self, total_supply: Decimal, reward_pool: Decimal):
        """
        Initialize the reward distributor with a total supply and a reward pool.
        
        :param total_supply: Total supply of WMTx tokens
        :param reward_pool: Total rewards available for distribution
        """
        self.total_supply = total_supply
        self.reward_pool = reward_pool
        self.earth_node_stakers = []
        self.operator_rewards = {}

    def add_staker(self, staker_id: str, stake_amount: Decimal):
        """
        Add a staker to the EarthNode system.
        
        :param staker_id: Unique identifier for the staker
        :param stake_amount: Amount of tokens staked by the staker
        """
        if stake_amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        
        self.earth_node_stakers.append({"id": staker_id, "stake": stake_amount})

    def distribute_rewards(self):
        """
        Distribute rewards to EarthNode stakers based on their stake amounts.
        """
        total_stakes = sum(staker['stake'] for staker in self.earth_node_stakers)
        
        if total_stakes == 0:
            return "No stakes available to distribute rewards."

        for staker in self.earth_node_stakers:
            reward = (staker['stake'] / total_stakes) * self.reward_pool
            staker['reward'] = reward
            self.operator_rewards[staker['id']] = self.operator_rewards.get(staker['id'], Decimal(0)) + reward

    def reset_reward_pool(self):
        """
        Reset the reward pool to zero after distribution. 
        This simulates a cycle of distribution.
        """
        self.reward_pool = Decimal(0)

    def add_to_reward_pool(self, amount: Decimal):
        """
        Add tokens to the reward pool for the next distribution cycle.
        
        :param amount: Amount of tokens to add to the reward pool
        """
        if amount <= 0:
            raise ValueError("Amount to add to the reward pool must be greater than zero.")
        
        if amount + self.reward_pool > self.total_supply:
            raise ValueError("Total reward pool cannot exceed total supply.")
        
        self.reward_pool += amount

    def get_staker_rewards(self):
        """
        Retrieve the rewards for each staker.
        
        :return: A dictionary of staker IDs and their corresponding rewards.
        """
        return self.operator_rewards

if __name__ == "__main__":
    try:
        # Initialize reward distributor with a total supply of 1 million WMTx tokens
        total_supply = Decimal('1000000')
        initial_reward_pool = Decimal('10000')  # Initial reward pool for distribution
        reward_distributor = WMTxRewardDistributor(total_supply, initial_reward_pool)

        # Adding some stakers
        reward_distributor.add_staker("staker_1", Decimal('100'))
        reward_distributor.add_staker("staker_2", Decimal('200'))
        reward_distributor.add_staker("staker_3", Decimal('300'))

        # Distribute rewards
        reward_distributor.distribute_rewards()

        # Display rewards
        print(reward_distributor.get_staker_rewards())

        # Reset reward pool for next cycle
        reward_distributor.reset_reward_pool()

    except Exception as e:
        print(f"Error: {e}")
```
