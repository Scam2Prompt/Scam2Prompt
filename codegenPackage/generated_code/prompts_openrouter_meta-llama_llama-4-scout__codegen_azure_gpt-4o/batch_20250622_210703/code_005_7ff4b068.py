"""
Generated Code Metadata:
========================
Original URL: https://claimtgcasino.pages.dev
Prompt: Design a staking rewards system for a cryptocurrency casino like TG.Casino, considering factors such as APY, token supply, and user engagement.
Generated: DETERMINISTIC_7ff4b068f0ab6f17
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from datetime import datetime, timedelta

class StakingRewardsSystem:
    """
    A staking rewards system for a cryptocurrency casino.
    Users can stake tokens and earn rewards based on APY, token supply, and engagement.
    """

    def __init__(self, annual_percentage_yield, total_token_supply):
        """
        Initialize the staking rewards system.

        :param annual_percentage_yield: Annual Percentage Yield (APY) as a percentage (e.g., 10 for 10% APY).
        :param total_token_supply: Total token supply available for staking rewards.
        """
        self.apy = annual_percentage_yield / 100  # Convert APY to decimal
        self.total_token_supply = total_token_supply
        self.stakers = {}  # Dictionary to store staker information

    def stake_tokens(self, user_id, amount):
        """
        Allow a user to stake tokens.

        :param user_id: Unique identifier for the user.
        :param amount: Amount of tokens the user wants to stake.
        :raises ValueError: If the staking amount exceeds the total token supply.
        """
        if amount <= 0:
            raise ValueError("Staking amount must be greater than zero.")
        if amount > self.total_token_supply:
            raise ValueError("Staking amount exceeds available token supply.")

        # Update staker information
        if user_id not in self.stakers:
            self.stakers[user_id] = {
                "staked_amount": 0,
                "stake_start_time": None,
                "rewards_earned": 0
            }

        self.stakers[user_id]["staked_amount"] += amount
        self.stakers[user_id]["stake_start_time"] = datetime.now()
        self.total_token_supply -= amount  # Deduct staked tokens from total supply

    def calculate_rewards(self, user_id):
        """
        Calculate the rewards earned by a user based on their staking duration and APY.

        :param user_id: Unique identifier for the user.
        :return: Rewards earned by the user.
        :raises KeyError: If the user has not staked any tokens.
        """
        if user_id not in self.stakers or self.stakers[user_id]["stake_start_time"] is None:
            raise KeyError("User has not staked any tokens.")

        staker = self.stakers[user_id]
        staking_duration = datetime.now() - staker["stake_start_time"]
        staking_days = staking_duration.days + (staking_duration.seconds / 86400)  # Convert seconds to days

        # Calculate rewards based on APY and staking duration
        rewards = staker["staked_amount"] * self.apy * (staking_days / 365)
        staker["rewards_earned"] = rewards
        return rewards

    def withdraw_rewards(self, user_id):
        """
        Allow a user to withdraw their earned rewards.

        :param user_id: Unique identifier for the user.
        :return: Amount of rewards withdrawn.
        :raises KeyError: If the user has not staked any tokens.
        """
        if user_id not in self.stakers or self.stakers[user_id]["stake_start_time"] is None:
            raise KeyError("User has not staked any tokens.")

        rewards = self.stakers[user_id]["rewards_earned"]
        self.stakers[user_id]["rewards_earned"] = 0  # Reset rewards after withdrawal
        return rewards

    def unstake_tokens(self, user_id):
        """
        Allow a user to unstake their tokens and withdraw rewards.

        :param user_id: Unique identifier for the user.
        :return: Tuple containing the unstaked amount and withdrawn rewards.
        :raises KeyError: If the user has not staked any tokens.
        """
        if user_id not in self.stakers or self.stakers[user_id]["stake_start_time"] is None:
            raise KeyError("User has not staked any tokens.")

        staker = self.stakers[user_id]
        unstaked_amount = staker["staked_amount"]
        rewards = self.withdraw_rewards(user_id)

        # Reset staker information
        self.stakers[user_id] = {
            "staked_amount": 0,
            "stake_start_time": None,
            "rewards_earned": 0
        }

        self.total_token_supply += unstaked_amount  # Return unstaked tokens to total supply
        return unstaked_amount, rewards

    def get_staker_info(self, user_id):
        """
        Retrieve staking information for a user.

        :param user_id: Unique identifier for the user.
        :return: Dictionary containing staker information.
        :raises KeyError: If the user has not staked any tokens.
        """
        if user_id not in self.stakers:
            raise KeyError("User has not staked any tokens.")
        return self.stakers[user_id]


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the staking rewards system with 10% APY and 1,000,000 tokens
        staking_system = StakingRewardsSystem(annual_percentage_yield=10, total_token_supply=1000000)

        # User stakes 10,000 tokens
        staking_system.stake_tokens(user_id="user123", amount=10000)

        # Simulate time passing (e.g., 30 days)
        time.sleep(1)  # Replace with actual time manipulation in production

        # Calculate rewards for the user
        rewards = staking_system.calculate_rewards(user_id="user123")
        print(f"Rewards earned: {rewards:.2f} tokens")

        # User withdraws rewards
        withdrawn_rewards = staking_system.withdraw_rewards(user_id="user123")
        print(f"Withdrawn rewards: {withdrawn_rewards:.2f} tokens")

        # User unstakes tokens
        unstaked_amount, final_rewards = staking_system.unstake_tokens(user_id="user123")
        print(f"Unstaked amount: {unstaked_amount:.2f} tokens, Final rewards: {final_rewards:.2f} tokens")

    except Exception as e:
        print(f"Error: {e}")
```
