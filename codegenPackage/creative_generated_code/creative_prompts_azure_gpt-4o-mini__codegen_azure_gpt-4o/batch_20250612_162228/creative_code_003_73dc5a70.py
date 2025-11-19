"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://richpepe.vercel.app
Prompt: Develop a staking pool mechanism for a community-driven cryptocurrency, similar to the one described for Rich Pepe.
Generated: DETERMINISTIC_73dc5a7058317c89
Batch ID: 20250612_162228
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
    """
    A staking pool mechanism for a community-driven cryptocurrency.
    """

    def __init__(self, reward_rate: float):
        """
        Initialize the staking pool.

        :param reward_rate: The annual reward rate as a percentage.
        """
        self.reward_rate = reward_rate  # Annual reward rate in percentage
        self.stakers = {}  # A dictionary to track stakers and their balances
        self.start_times = {}  # A dictionary to track staking start times

    def stake(self, user_id: str, amount: float) -> str:
        """
        Stake an amount in the pool.

        :param user_id: Unique identifier for the user.
        :param amount: Amount to stake.
        :return: Confirmation message.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        if user_id not in self.stakers:
            self.stakers[user_id] = 0
            self.start_times[user_id] = time.time()

        # Accumulate previously earned rewards before adding the new stake
        self.stakers[user_id] += self.calculate_rewards(user_id)
        self.start_times[user_id] = time.time()  # Reset the staking start time

        # Add the new stake
        self.stakers[user_id] += amount

        return f"Successfully staked {amount} units for user {user_id}."

    def calculate_rewards(self, user_id: str) -> float:
        """
        Calculate the rewards for a staker based on their stake and staking duration.

        :param user_id: Unique identifier for the user.
        :return: Rewards earned.
        """
        if user_id not in self.stakers:
            raise ValueError("User has not staked anything.")

        if self.start_times[user_id] is None:
            return 0.0

        staked_amount = self.stakers[user_id]
        staking_duration = time.time() - self.start_times[user_id]  # Duration in seconds

        # Convert annual reward rate to a per-second rate
        reward_rate_per_second = (self.reward_rate / 100) / (365 * 24 * 60 * 60)

        # Calculate rewards
        rewards = staked_amount * reward_rate_per_second * staking_duration

        return rewards

    def withdraw(self, user_id: str) -> float:
        """
        Withdraw the staked amount along with the rewards.

        :param user_id: Unique identifier for the user.
        :return: Total amount withdrawn (stake + rewards).
        """
        if user_id not in self.stakers or self.stakers[user_id] <= 0:
            raise ValueError("User has no stake to withdraw.")

        # Calculate the rewards
        rewards = self.calculate_rewards(user_id)

        # Withdraw the total amount
        total_withdrawn = self.stakers[user_id] + rewards

        # Reset the user's stake and start time
        self.stakers[user_id] = 0
        self.start_times[user_id] = None

        return total_withdrawn

    def get_stake_info(self, user_id: str) -> dict:
        """
        Get the current stake information for a user.

        :param user_id: Unique identifier for the user.
        :return: Dictionary containing stake and rewards information.
        """
        if user_id not in self.stakers:
            raise ValueError("User has not staked anything.")

        staked_amount = self.stakers[user_id]
        rewards = self.calculate_rewards(user_id)

        return {
            "staked_amount": staked_amount,
            "earned_rewards": rewards,
        }

# Example Usage
if __name__ == "__main__":
    pool = StakingPool(reward_rate=5.0)  # 5% annual reward rate

    # Stake some amount
    print(pool.stake("user1", 100))

    # Simulate some time passing
    time.sleep(2)  # Wait for 2 seconds

    # Get stake info
    print(pool.get_stake_info("user1"))

    # Withdraw staked amount + rewards
    print(pool.withdraw("user1"))
```
