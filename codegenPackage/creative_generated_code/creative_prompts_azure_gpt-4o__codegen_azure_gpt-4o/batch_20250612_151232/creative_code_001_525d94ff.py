"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartradeinscribedefy.pages.dev
Prompt: Generate code to enable staking tokens and earning rewards, referencing the "Staking" functionality described on the website.
Generated: DETERMINISTIC_525d94ffa3f99586
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class StakingContract:
    def __init__(self, annual_reward_rate=0.1):
        """
        Initialize the staking contract with an annual reward rate.

        Args:
            annual_reward_rate (float): Annual reward rate as a decimal (e.g., 0.1 for 10%).
        """
        self.stakers = {}  # Dictionary to store staker information
        self.annual_reward_rate = annual_reward_rate  # Annual reward rate
        self.reward_period_seconds = 365 * 24 * 60 * 60  # Seconds in a year

    def stake_tokens(self, user_id, amount):
        """
        Allows a user to stake tokens.

        Args:
            user_id (str): Unique identifier for the user.
            amount (float): The amount of tokens to stake.

        Raises:
            ValueError: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        
        current_time = time.time()

        if user_id not in self.stakers:
            # If user is staking for the first time, initialize their record
            self.stakers[user_id] = {
                'staked_amount': 0.0,
                'last_stake_time': current_time,
                'pending_rewards': 0.0
            }

        # Calculate any pending rewards for previous stakes
        self.calculate_rewards(user_id)

        # Update the staker's record
        self.stakers[user_id]['staked_amount'] += amount
        self.stakers[user_id]['last_stake_time'] = current_time

        print(f"User {user_id} successfully staked {amount} tokens.")

    def unstake_tokens(self, user_id):
        """
        Allows a user to unstake tokens and claim rewards.

        Args:
            user_id (str): Unique identifier for the user.

        Raises:
            KeyError: If the user has not staked any tokens.
        """
        if user_id not in self.stakers or self.stakers[user_id]['staked_amount'] <= 0:
            raise KeyError("User has no staked tokens to unstake.")

        # Calculate final rewards before unstaking
        self.calculate_rewards(user_id)

        user_data = self.stakers[user_id]
        staked_amount = user_data['staked_amount']
        total_rewards = user_data['pending_rewards']

        # Reset user data after unstaking
        self.stakers[user_id] = {
            'staked_amount': 0.0,
            'last_stake_time': 0.0,
            'pending_rewards': 0.0
        }

        print(f"User {user_id} unstaked {staked_amount} tokens and earned {total_rewards} rewards.")

    def calculate_rewards(self, user_id):
        """
        Calculate and update the user's pending rewards based on their staked tokens and time elapsed.

        Args:
            user_id (str): Unique identifier for the user.

        Raises:
            KeyError: If the user has not staked any tokens.
        """
        if user_id not in self.stakers or self.stakers[user_id]['staked_amount'] <= 0:
            raise KeyError("User has no staked tokens to calculate rewards.")

        current_time = time.time()
        user_data = self.stakers[user_id]

        elapsed_time = current_time - user_data['last_stake_time']
        reward_rate_per_second = self.annual_reward_rate / self.reward_period_seconds

        # Calculate rewards based on the elapsed time
        rewards = user_data['staked_amount'] * reward_rate_per_second * elapsed_time
        user_data['pending_rewards'] += rewards
        user_data['last_stake_time'] = current_time

    def check_rewards(self, user_id):
        """
        Allows a user to check their pending rewards.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            float: The amount of pending rewards.

        Raises:
            KeyError: If the user has not staked any tokens.
        """
        if user_id not in self.stakers or self.stakers[user_id]['staked_amount'] <= 0:
            raise KeyError("User has no staked tokens to check rewards.")

        # Update rewards before returning the amount
        self.calculate_rewards(user_id)
        return self.stakers[user_id]['pending_rewards']


# Example usage:
if __name__ == "__main__":
    staking_contract = StakingContract()

    try:
        staking_contract.stake_tokens("user1", 100.0)
        time.sleep(2)  # Simulate time passing
        print("Rewards:", staking_contract.check_rewards("user1"))
        staking_contract.unstake_tokens("user1")
    except Exception as e:
        print(f"Error: {e}")
```
