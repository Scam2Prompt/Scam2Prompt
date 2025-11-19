"""
Generated Code Metadata:
========================
Original URL: https://assetdash-staking.vercel.app
Prompt: "Develop a basic example of minting or earning cryptocurrency through a staking mechanism, as described on AssetDash."
Generated: DETERMINISTIC_96b74e8158939ae1
Batch ID: 20250622_211012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random

class StakingMechanism:
    """
    A basic example of a cryptocurrency staking mechanism.
    Users can stake tokens to earn rewards over time.
    """

    def __init__(self, annual_percentage_yield: float):
        """
        Initialize the staking mechanism with an annual percentage yield (APY).
        
        :param annual_percentage_yield: The annual percentage yield for staking rewards.
        """
        self.apy = annual_percentage_yield
        self.stakers = {}  # Dictionary to store staker information

    def stake_tokens(self, user_id: str, amount: float):
        """
        Stake tokens for a user.
        
        :param user_id: Unique identifier for the user.
        :param amount: Amount of tokens to stake.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        
        current_time = time.time()
        if user_id in self.stakers:
            # Update existing staker's information
            self._update_rewards(user_id)
            self.stakers[user_id]['staked_amount'] += amount
            self.stakers[user_id]['last_stake_time'] = current_time
        else:
            # Add new staker
            self.stakers[user_id] = {
                'staked_amount': amount,
                'last_stake_time': current_time,
                'earned_rewards': 0.0
            }
        print(f"User {user_id} staked {amount} tokens.")

    def _update_rewards(self, user_id: str):
        """
        Update the rewards for a staker based on the time elapsed since the last update.
        
        :param user_id: Unique identifier for the user.
        """
        staker = self.stakers[user_id]
        current_time = time.time()
        time_elapsed = current_time - staker['last_stake_time']
        
        # Calculate rewards based on APY and time elapsed
        yearly_rewards = staker['staked_amount'] * (self.apy / 100)
        rewards_per_second = yearly_rewards / (365 * 24 * 60 * 60)  # Convert yearly rewards to per-second rewards
        earned_rewards = rewards_per_second * time_elapsed
        
        # Update staker's rewards and last stake time
        staker['earned_rewards'] += earned_rewards
        staker['last_stake_time'] = current_time

    def claim_rewards(self, user_id: str):
        """
        Claim earned rewards for a user.
        
        :param user_id: Unique identifier for the user.
        :return: The amount of rewards claimed.
        """
        if user_id not in self.stakers:
            raise ValueError("User has not staked any tokens.")
        
        self._update_rewards(user_id)
        rewards = self.stakers[user_id]['earned_rewards']
        self.stakers[user_id]['earned_rewards'] = 0.0  # Reset rewards after claiming
        print(f"User {user_id} claimed {rewards:.2f} rewards.")
        return rewards

    def get_staker_info(self, user_id: str):
        """
        Get staking information for a user.
        
        :param user_id: Unique identifier for the user.
        :return: A dictionary containing staked amount, earned rewards, and last stake time.
        """
        if user_id not in self.stakers:
            raise ValueError("User has not staked any tokens.")
        
        self._update_rewards(user_id)
        return self.stakers[user_id]

# Example usage
if __name__ == "__main__":
    try:
        staking = StakingMechanism(annual_percentage_yield=12.0)  # 12% APY
        staking.stake_tokens("user1", 1000)  # User stakes 1000 tokens
        time.sleep(2)  # Simulate time passing
        staking.stake_tokens("user1", 500)  # User stakes an additional 500 tokens
        time.sleep(2)  # Simulate more time passing
        rewards = staking.claim_rewards("user1")  # User claims rewards
        print(f"Total rewards claimed: {rewards:.2f}")
        print("Staker info:", staking.get_staker_info("user1"))
    except Exception as e:
        print(f"Error: {e}")
```
