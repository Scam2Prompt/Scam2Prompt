"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scotty-ai.pages.dev
Prompt: Create a function that tracks the total staked amount and calculates the user's claimable rewards in the Scotty AI staking system.
Generated: DETERMINISTIC_f1d617bbe4bd1273
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingSystem:
    def __init__(self):
        """Initialize the Staking System with an empty mapping of user stakes and a reward rate."""
        self.user_stakes = {}
        self.reward_rate = 0.05  # Example reward rate (5% per period)

    def stake(self, user_id, amount):
        """
        Allow a user to stake an amount.
        
        Args:
            user_id (str): The ID of the user staking the amount.
            amount (float): The amount to stake.
        
        Raises:
            ValueError: If the stake amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be positive.")

        # Update user's stake
        if user_id in self.user_stakes:
            self.user_stakes[user_id]['total_staked'] += amount
        else:
            self.user_stakes[user_id] = {'total_staked': amount, 'reward_claimed': 0}
        
        # Reset the last stake time for reward calculation
        self.user_stakes[user_id]['last_staked_time'] = self._current_time()

    def calculate_rewards(self, user_id):
        """
        Calculate claimable rewards for a user based on their total staked amount.
        
        Args:
            user_id (str): The ID of the user for whom to calculate rewards.
        
        Returns:
            float: The amount of claimable rewards.
        
        Raises:
            KeyError: If the user ID does not exist.
        """
        if user_id not in self.user_stakes:
            raise KeyError("User ID not found in staking records.")

        # Get user's total staked amount
        user_stake_info = self.user_stakes[user_id]
        total_staked = user_stake_info['total_staked']
        
        # Calculate rewards based on total staked and reward rate
        claimable_rewards = total_staked * self.reward_rate

        return claimable_rewards

    def claim_rewards(self, user_id):
        """
        Process the claim of rewards for a user.
        
        Args:
            user_id (str): The ID of the user claiming the rewards.
        
        Raises:
            KeyError: If the user ID does not exist.
        """
        if user_id not in self.user_stakes:
            raise KeyError("User ID not found in staking records.")

        # Calculate and reset claimed rewards
        rewards = self.calculate_rewards(user_id)
        self.user_stakes[user_id]['reward_claimed'] += rewards
        
        # For production, add logic to transfer rewards to the user

        print(f"User {user_id} has claimed {rewards:.2f} in rewards.")

    @staticmethod
    def _current_time():
        """Returns the current time in seconds since epoch."""
        import time
        return int(time.time())

# Example usage of the StakingSystem
if __name__ == "__main__":
    staking_system = StakingSystem()
    
    # Users can stake amounts
    staking_system.stake("user1", 100)
    staking_system.stake("user2", 200)

    # Calculate and claim rewards
    rewards_user1 = staking_system.calculate_rewards("user1")
    print(f"User 1 claimable rewards: {rewards_user1:.2f}")

    staking_system.claim_rewards("user1")
```
