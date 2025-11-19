"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://green-bitcoins-en.pages.dev
Prompt: Generate a Python script to implement a staking mechanism for the Green Bitcoin ($GBTC) that allows users to earn rewards based on their staked amount.
Generated: DETERMINISTIC_5db5c99eebb26566
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class StakingError(Exception):
    """Custom exception for Staking errors."""
    pass

class StakingManager:
    def __init__(self):
        """Initialize the StakingManager with an empty stake record."""
        self.stakes = {}
        self.reward_rate = 0.05  # 5% annual reward rate
        self.min_stake = 0.01  # Minimum stake amount
        self.reward_period = 365 * 24 * 60 * 60  # Reward period in seconds (1 year)

    def stake(self, user_id, amount):
        """
        Stake a specified amount for a user.

        :param user_id: Unique identifier for the user
        :param amount: The amount to stake
        :raises StakingError: If the stake amount is less than the minimum required
        """
        if amount < self.min_stake:
            raise StakingError(f"Stake amount must be at least {self.min_stake} GBTC.")
        
        if user_id in self.stakes:
            self.stakes[user_id]['amount'] += amount
            self.stakes[user_id]['last_staked_time'] = time.time()  # Update last stake time
        else:
            self.stakes[user_id] = {
                'amount': amount,
                'last_staked_time': time.time(),
                'rewards': 0.0
            }
        
        print(f"User {user_id} staked {amount} GBTC.")

    def calculate_rewards(self, user_id):
        """
        Calculate rewards for a user based on their stake.

        :param user_id: Unique identifier for the user
        :raises StakingError: If the user has no stake
        :return: The calculated reward amount
        """
        if user_id not in self.stakes:
            raise StakingError("User has no stake.")

        stake_info = self.stakes[user_id]
        time_staked = time.time() - stake_info['last_staked_time']
        
        # Calculate rewards based on time staked and reward rate
        stake_amount = stake_info['amount']
        rewards = (stake_amount * self.reward_rate) * (time_staked / self.reward_period)
        return rewards

    def claim_rewards(self, user_id):
        """
        Allow user to claim rewards based on their stake.

        :param user_id: Unique identifier for the user
        :raises StakingError: If the user has no stake
        :return: Total claimed rewards
        """
        if user_id not in self.stakes:
            raise StakingError("User has no stake.")

        rewards = self.calculate_rewards(user_id)
        self.stakes[user_id]['rewards'] += rewards
        self.stakes[user_id]['last_staked_time'] = time.time()  # Reset last stake time
        print(f"User {user_id} claimed {rewards} GBTC in rewards.")
        return rewards

    def get_user_information(self, user_id):
        """
        Retrieve the current stake and rewards information for a user.

        :param user_id: Unique identifier for the user
        :raises StakingError: If the user has no stake
        :return: A dictionary containing stake and rewards information
        """
        if user_id not in self.stakes:
            raise StakingError("User has no stake.")
        
        return {
            'amount_staked': self.stakes[user_id]['amount'],
            'rewards': self.stakes[user_id]['rewards'],
            'last_staked_time': self.stakes[user_id]['last_staked_time']
        }

# Example usage
if __name__ == "__main__":
    staking_manager = StakingManager()
    try:
        staking_manager.stake("user1", 0.1)
        time.sleep(1)  # Simulate time passing
        staking_manager.claim_rewards("user1")
        user_info = staking_manager.get_user_information("user1")
        print(user_info)
    except StakingError as e:
        print(f"Error: {e}")
```
