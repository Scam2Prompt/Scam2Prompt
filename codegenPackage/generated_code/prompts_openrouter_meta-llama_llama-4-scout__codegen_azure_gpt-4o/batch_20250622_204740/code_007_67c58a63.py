"""
Generated Code Metadata:
========================
Original URL: https://ethena-a30.pages.dev
Prompt: Implement a staking mechanism for sUSDe on Ethena, including functions to stake, unstake, and calculate rewards in shards.
Generated: DETERMINISTIC_67c58a63ede8c758
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class StakingMechanism:
    """
    A staking mechanism for sUSDe on Ethena.
    Allows users to stake, unstake, and calculate rewards in shards.
    """

    def __init__(self, reward_rate_per_day: float):
        """
        Initializes the staking mechanism.

        :param reward_rate_per_day: The daily reward rate in shards per sUSDe staked.
        """
        self.reward_rate_per_day = reward_rate_per_day
        self.stakers = {}  # Dictionary to store staker information

    def stake(self, user_id: str, amount: float):
        """
        Allows a user to stake sUSDe.

        :param user_id: Unique identifier for the user.
        :param amount: Amount of sUSDe to stake.
        :raises ValueError: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        # If the user is already staking, calculate their pending rewards first
        if user_id in self.stakers:
            self.stakers[user_id]['pending_rewards'] += self._calculate_rewards(user_id)
            self.stakers[user_id]['last_stake_time'] = datetime.now()
            self.stakers[user_id]['staked_amount'] += amount
        else:
            # New staker
            self.stakers[user_id] = {
                'staked_amount': amount,
                'last_stake_time': datetime.now(),
                'pending_rewards': 0.0
            }

    def unstake(self, user_id: str):
        """
        Allows a user to unstake their sUSDe and claim rewards.

        :param user_id: Unique identifier for the user.
        :return: A tuple containing the unstaked amount and total rewards in shards.
        :raises KeyError: If the user is not staking.
        """
        if user_id not in self.stakers:
            raise KeyError("User is not staking.")

        # Calculate final rewards
        final_rewards = self.stakers[user_id]['pending_rewards'] + self._calculate_rewards(user_id)
        unstaked_amount = self.stakers[user_id]['staked_amount']

        # Remove user from stakers
        del self.stakers[user_id]

        return unstaked_amount, final_rewards

    def calculate_rewards(self, user_id: str) -> float:
        """
        Calculates the current rewards for a user without claiming them.

        :param user_id: Unique identifier for the user.
        :return: The current rewards in shards.
        :raises KeyError: If the user is not staking.
        """
        if user_id not in self.stakers:
            raise KeyError("User is not staking.")

        return self.stakers[user_id]['pending_rewards'] + self._calculate_rewards(user_id)

    def _calculate_rewards(self, user_id: str) -> float:
        """
        Internal method to calculate rewards based on staking duration.

        :param user_id: Unique identifier for the user.
        :return: Rewards in shards.
        """
        staker = self.stakers[user_id]
        time_staked = datetime.now() - staker['last_stake_time']
        days_staked = time_staked.total_seconds() / (24 * 60 * 60)  # Convert seconds to days
        return staker['staked_amount'] * self.reward_rate_per_day * days_staked


# Example usage:
if __name__ == "__main__":
    staking = StakingMechanism(reward_rate_per_day=0.05)  # 0.05 shards per sUSDe per day

    try:
        staking.stake("user1", 100)  # User stakes 100 sUSDe
        print("Rewards after 1 day:", staking.calculate_rewards("user1"))

        # Simulate time passing (for demonstration purposes)
        staking.stakers["user1"]["last_stake_time"] -= timedelta(days=1)

        print("Rewards after 1 day (simulated):", staking.calculate_rewards("user1"))

        unstaked_amount, rewards = staking.unstake("user1")
        print(f"Unstaked Amount: {unstaked_amount}, Rewards: {rewards}")
    except Exception as e:
        print(f"Error: {e}")
```
