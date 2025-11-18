"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-inqubeta-ai.pages.dev
Prompt: Generate code to stake QUBE tokens and calculate staking rewards based on the 5% sell tax reward pool described in InQubeta's tokenomics.
Generated: DETERMINISTIC_290de2f10c147219
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class QubeStaking:
    """
    Class for staking QUBE tokens and calculating rewards based on a 5% sell tax reward pool.
    """

    def __init__(self, reward_pool=0.0, annual_percentage_rate=5.0):
        """
        Initializes the staking system.

        :param reward_pool: Initial reward pool (default is 0.0 QUBE tokens).
        :param annual_percentage_rate: Annual reward rate from the sell tax pool (default is 5%).
        """
        self.reward_pool = reward_pool
        self.apr = annual_percentage_rate
        self.stakers = {}  # Dictionary to hold staking information

    def stake_tokens(self, user_address, amount):
        """
        Allows users to stake tokens.

        :param user_address: Unique identifier for the user (e.g., wallet address).
        :param amount: Amount of QUBE tokens to stake.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        
        # Record the staking details
        current_time = time.time()
        if user_address not in self.stakers:
            self.stakers[user_address] = {
                "staked_amount": 0.0,
                "stake_time": current_time,
                "reward_earned": 0.0
            }
        self.stakers[user_address]["staked_amount"] += amount
        self.stakers[user_address]["stake_time"] = current_time

        print(f"User {user_address} successfully staked {amount} QUBE tokens.")

    def calculate_rewards(self, user_address):
        """
        Calculates staking rewards for a specific user.

        :param user_address: Unique identifier for the user (e.g., wallet address).
        :return: Reward earned by the user.
        """
        if user_address not in self.stakers or self.stakers[user_address]["staked_amount"] <= 0:
            raise ValueError("No tokens staked for the given user address.")

        # Calculate time-based rewards
        user_data = self.stakers[user_address]
        current_time = time.time()
        time_elapsed = current_time - user_data["stake_time"]  # Time elapsed in seconds
        time_elapsed_in_days = time_elapsed / (60 * 60 * 24)  # Convert seconds to days

        # Calculate reward based on APR and elapsed time
        reward = (user_data["staked_amount"] * self.apr / 100) * (time_elapsed_in_days / 365)

        # Ensure reward does not exceed the reward pool
        reward = min(reward, self.reward_pool)

        user_data["reward_earned"] = reward
        return reward

    def withdraw_rewards(self, user_address):
        """
        Allows users to withdraw their staking rewards.

        :param user_address: Unique identifier for the user (e.g., wallet address).
        :return: Amount of rewards withdrawn.
        """
        if user_address not in self.stakers:
            raise ValueError("No staking data found for the given user address.")

        user_data = self.stakers[user_address]
        reward_to_withdraw = user_data["reward_earned"]

        if reward_to_withdraw <= 0:
            raise ValueError("No rewards available for withdrawal.")

        # Deduct the reward from the pool and reset user's reward
        self.reward_pool -= reward_to_withdraw
        user_data["reward_earned"] = 0.0

        print(f"User {user_address} successfully withdrew {reward_to_withdraw} QUBE tokens.")
        return reward_to_withdraw

    def add_to_reward_pool(self, amount):
        """
        Adds QUBE tokens to the reward pool (e.g., from sell tax).

        :param amount: Amount to add to the reward pool.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        self.reward_pool += amount
        print(f"Added {amount} QUBE tokens to the reward pool.")

# Example usage
if __name__ == "__main__":
    staking_system = QubeStaking(reward_pool=1000.0)  # Initialize with 1000 QUBE tokens in the reward pool

    # Simulate staking and reward calculation
    staking_system.stake_tokens("user1", 500)
    time.sleep(2)  # Simulate some time passing
    reward = staking_system.calculate_rewards("user1")
    print(f"Reward for user1: {reward} QUBE tokens")

    # Withdraw rewards
    withdrawn_reward = staking_system.withdraw_rewards("user1")
    print(f"User1 withdrew: {withdrawn_reward} QUBE tokens")

    # Add to reward pool
    staking_system.add_to_reward_pool(200)
```
