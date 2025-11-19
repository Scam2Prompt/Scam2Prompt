"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimdoge20live.pages.dev
Prompt: How can I implement a staking mechanism for DOGE20 that calculates rewards based on user percentage in the staking pool?
Generated: DETERMINISTIC_8f5f79d21f48a69f
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class StakingPool:
    def __init__(self):
        """
        Initializes the staking pool.
        """
        self.total_staked = 0.0
        self.user_stakes = {}
        self.reward_rate = 0.1  # Example reward rate: 10% of the staked amount
        self.last_update_time = time.time()

    def stake(self, user_id, amount):
        """
        Allows a user to stake an amount of DOGE20 tokens.

        :param user_id: The unique identifier for the user staking tokens.
        :param amount: The amount of DOGE20 tokens to stake.
        :raises ValueError: If the stake amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be positive.")

        # Update total staked and user stake
        self.total_staked += amount
        if user_id in self.user_stakes:
            self.user_stakes[user_id] += amount
        else:
            self.user_stakes[user_id] = amount

        # Log staking event
        print(f"User {user_id} staked {amount} DOGE20 tokens.")

    def calculate_rewards(self, user_id):
        """
        Calculates and returns the rewards for a given user based on their stake.

        :param user_id: The unique identifier for the user.
        :return: The calculated rewards for the user.
        :raises KeyError: If the user has no stakes.
        """
        if user_id not in self.user_stakes:
            raise KeyError("User has no stakes in the pool.")
        
        # Calculate time since last update
        current_time = time.time()
        time_elapsed = current_time - self.last_update_time

        # Calculate rewards based on the user's percentage of the total stake
        user_stake = self.user_stakes[user_id]
        user_percentage = user_stake / self.total_staked
        rewards = user_percentage * self.reward_rate * time_elapsed

        # Update last update time
        self.last_update_time = current_time
        
        return rewards

    def withdraw(self, user_id):
        """
        Allows a user to withdraw their staked amount along with their rewards.

        :param user_id: The unique identifier for the user.
        :raises KeyError: If the user has no stakes.
        """
        if user_id not in self.user_stakes:
            raise KeyError("User has no stakes in the pool.")

        # Calculate user's rewards and total withdrawal amount
        rewards = self.calculate_rewards(user_id)
        total_withdrawal = self.user_stakes[user_id] + rewards
        
        # Remove user from stakes
        del self.user_stakes[user_id]
        self.total_staked -= total_withdrawal - rewards

        # Log withdrawal event
        print(f"User {user_id} withdrew {total_withdrawal} DOGE20 tokens (including {rewards} rewards).")

# Example usage:
if __name__ == "__main__":
    pool = StakingPool()
    
    # Users staking DOGE20
    pool.stake('user1', 100)
    time.sleep(1)  # Simulate time passing
    pool.stake('user2', 200)

    # Calculate rewards for user1
    rewards_user1 = pool.calculate_rewards('user1')
    print(f"User1 rewards: {rewards_user1}")

    # User1 withdraws
    pool.withdraw('user1')
```
