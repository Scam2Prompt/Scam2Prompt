"""
Generated Code Metadata:
========================
Original URL: https://hehe-com.pages.dev
Prompt: Explain how to implement staking for $HEHE tokens to earn rewards, based on the staking details provided in the HEHE ecosystem.
Generated: DETERMINISTIC_3fe1cc621d62aaa0
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Staking Implementation for $HEHE Tokens
This script allows users to stake $HEHE tokens and earn rewards based on the staking details provided in the HEHE ecosystem.
"""

import time

class StakingContract:
    def __init__(self, reward_rate_per_second: float):
        """
        Initialize the staking contract.

        :param reward_rate_per_second: The rate at which rewards are earned per second.
        """
        self.reward_rate_per_second = reward_rate_per_second  # Rewards per second
        self.stakers = {}  # Dictionary to store staker information

    def stake_tokens(self, user: str, amount: float):
        """
        Stake $HEHE tokens for a user.

        :param user: The user's identifier (e.g., wallet address).
        :param amount: The amount of $HEHE tokens to stake.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        current_time = time.time()

        # If the user is already staking, calculate their pending rewards first
        if user in self.stakers:
            self._update_rewards(user)

        # Update the user's staking information
        self.stakers[user] = {
            "amount": self.stakers.get(user, {}).get("amount", 0) + amount,
            "last_stake_time": current_time,
            "pending_rewards": self.stakers.get(user, {}).get("pending_rewards", 0)
        }

    def unstake_tokens(self, user: str):
        """
        Unstake all $HEHE tokens for a user and return their rewards.

        :param user: The user's identifier (e.g., wallet address).
        :return: A tuple containing the unstaked amount and the total rewards earned.
        """
        if user not in self.stakers:
            raise ValueError("User has no staked tokens.")

        # Update rewards before unstaking
        self._update_rewards(user)

        staked_info = self.stakers.pop(user)
        staked_amount = staked_info["amount"]
        total_rewards = staked_info["pending_rewards"]

        return staked_amount, total_rewards

    def _update_rewards(self, user: str):
        """
        Update the pending rewards for a user based on the time elapsed since their last stake.

        :param user: The user's identifier (e.g., wallet address).
        """
        if user not in self.stakers:
            raise ValueError("User has no staked tokens.")

        current_time = time.time()
        staked_info = self.stakers[user]

        # Calculate rewards based on time elapsed
        time_elapsed = current_time - staked_info["last_stake_time"]
        rewards_earned = time_elapsed * self.reward_rate_per_second * staked_info["amount"]

        # Update the user's pending rewards and last stake time
        staked_info["pending_rewards"] += rewards_earned
        staked_info["last_stake_time"] = current_time

    def get_staker_info(self, user: str):
        """
        Get staking information for a user.

        :param user: The user's identifier (e.g., wallet address).
        :return: A dictionary containing the staked amount, pending rewards, and last stake time.
        """
        if user not in self.stakers:
            return {"amount": 0, "pending_rewards": 0, "last_stake_time": None}

        self._update_rewards(user)
        return self.stakers[user]


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the staking contract with a reward rate of 0.01 $HEHE per second
        staking_contract = StakingContract(reward_rate_per_second=0.01)

        # User stakes 100 $HEHE tokens
        staking_contract.stake_tokens(user="user1", amount=100)

        # Simulate some time passing
        time.sleep(5)

        # Get user staking info
        user_info = staking_contract.get_staker_info(user="user1")
        print(f"User Info: {user_info}")

        # User unstakes their tokens
        unstaked_amount, rewards = staking_contract.unstake_tokens(user="user1")
        print(f"Unstaked Amount: {unstaked_amount}, Rewards Earned: {rewards}")

    except Exception as e:
        print(f"Error: {e}")
```
