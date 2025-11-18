"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supercore-7hg.pages.dev
Prompt: Write a script to enable staking functionality for PLS and 9MM tokens, including tracking rewards and pool stats.
Generated: DETERMINISTIC_4dbf89691fc35158
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from decimal import Decimal

# Configure logging to track events and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class StakingPool:
    def __init__(self, token_name):
        """
        Initialize the staking pool for a specified token.
        
        :param token_name: The name of the token (e.g., 'PLS', '9MM')
        """
        self.token_name = token_name
        self.stakers = {}  # Dictionary to track staker balances and rewards
        self.total_staked = Decimal('0.0')  # Total amount staked in the pool
        self.reward_rate = Decimal('0.05')  # Rewards rate (5% per cycle)
        
    def stake(self, user, amount):
        """
        Allow a user to stake a specified amount of tokens.
        
        :param user: The user staking the tokens
        :param amount: The amount of tokens to stake
        :raises ValueError: If the amount is less than or equal to zero
        """
        if amount <= 0:
            raise ValueError("Amount to stake must be greater than zero.")
        
        if user not in self.stakers:
            self.stakers[user] = {'balance': Decimal('0.0'), 'rewards': Decimal('0.0')}
        
        self.stakers[user]['balance'] += Decimal(amount)
        self.total_staked += Decimal(amount)
        logging.info(f"{user} has staked {amount} {self.token_name}. Total staked: {self.total_staked}")

    def unstake(self, user, amount):
        """
        Allow a user to unstake a specified amount of tokens.
        
        :param user: The user unstaking the tokens
        :param amount: The amount of tokens to unstake
        :raises ValueError: If the user has insufficient balance or amount is invalid
        """
        if user not in self.stakers or self.stakers[user]['balance'] < amount:
            raise ValueError("Insufficient balance to unstake.")
        
        if amount <= 0:
            raise ValueError("Amount to unstake must be greater than zero.")
        
        self.stakers[user]['balance'] -= Decimal(amount)
        self.total_staked -= Decimal(amount)
        logging.info(f"{user} has unstaked {amount} {self.token_name}. Total staked: {self.total_staked}")

    def calculate_rewards(self, user):
        """
        Calculate and distribute rewards for a user based on their staked balance.
        
        :param user: The user for whom to calculate rewards
        :raises ValueError: If the user has no stake in the pool
        """
        if user not in self.stakers:
            raise ValueError("User has no stake in the pool.")
        
        staked_amount = self.stakers[user]['balance']
        rewards = staked_amount * self.reward_rate
        self.stakers[user]['rewards'] += rewards
        logging.info(f"{user} has earned {rewards} rewards. Total rewards: {self.stakers[user]['rewards']}")

    def get_pool_stats(self):
        """
        Retrieve the current stats of the staking pool.
        
        :return: A dictionary containing total staked amount and number of stakers
        """
        return {
            'total_staked': str(self.total_staked),
            'number_of_stakers': len(self.stakers)
        }

# Example usage
if __name__ == "__main__":
    try:
        pls_staking_pool = StakingPool('PLS')
        pls_staking_pool.stake('Alice', 100)
        pls_staking_pool.stake('Bob', 200)
        pls_staking_pool.calculate_rewards('Alice')
        
        stats = pls_staking_pool.get_pool_stats()
        logging.info(f"Pool Stats: {stats}")
        
        pls_staking_pool.unstake('Alice', 50)
        pls_staking_pool.calculate_rewards('Bob')
        
    except ValueError as e:
        logging.error(f"An error occurred: {e}")
```
