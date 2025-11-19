"""
Generated Code Metadata:
========================
Original URL: https://trustpad-c0r.pages.dev
Prompt: Generate code to calculate staking rewards for $TPAD tokens based on the staking requirements and pool weight levels provided by TrustPad.
Generated: DETERMINISTIC_1fa57744ae0b18b7
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StakingPool:
    """
    A class to represent a staking pool for $TPAD tokens.

    Attributes:
        total_staked (float): Total amount of $TPAD tokens staked in the pool.
        pool_weight (float): Weight of the pool which affects reward distribution.
        reward_rate (float): Rate at which rewards are generated per token staked.
    """

    def __init__(self, pool_weight: float, reward_rate: float):
        """
        Initializes the StakingPool with the given pool weight and reward rate.

        Args:
            pool_weight (float): The weight of the staking pool.
            reward_rate (float): The reward rate per token staked.
        """
        if pool_weight <= 0:
            raise ValueError("Pool weight must be greater than zero.")
        if reward_rate < 0:
            raise ValueError("Reward rate cannot be negative.")

        self.total_staked = 0.0
        self.pool_weight = pool_weight
        self.reward_rate = reward_rate

    def stake(self, amount: float):
        """
        Stakes a specified amount of $TPAD tokens into the pool.

        Args:
            amount (float): The amount of $TPAD tokens to stake.

        Raises:
            ValueError: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        
        self.total_staked += amount

    def calculate_rewards(self) -> float:
        """
        Calculates the total rewards earned based on the total staked amount,
        pool weight, and reward rate.

        Returns:
            float: The total rewards earned.
        """
        if self.total_staked == 0:
            return 0.0
        
        # Calculate rewards based on the formula: rewards = total_staked * reward_rate * pool_weight
        rewards = self.total_staked * self.reward_rate * self.pool_weight
        return rewards

    def unstake(self, amount: float):
        """
        Unstakes a specified amount of $TPAD tokens from the pool.

        Args:
            amount (float): The amount of $TPAD tokens to unstake.

        Raises:
            ValueError: If the amount is less than or equal to zero or greater than total staked.
        """
        if amount <= 0:
            raise ValueError("Unstake amount must be greater than zero.")
        if amount > self.total_staked:
            raise ValueError("Cannot unstake more than the total staked amount.")

        self.total_staked -= amount


# Example usage
if __name__ == "__main__":
    try:
        # Create a staking pool with a weight of 1.5 and a reward rate of 0.1
        staking_pool = StakingPool(pool_weight=1.5, reward_rate=0.1)

        # Stake some tokens
        staking_pool.stake(1000)

        # Calculate rewards
        rewards = staking_pool.calculate_rewards()
        print(f"Total rewards earned: {rewards:.2f} $TPAD")

        # Unstake some tokens
        staking_pool.unstake(500)

        # Calculate rewards after unstaking
        rewards_after_unstake = staking_pool.calculate_rewards()
        print(f"Total rewards earned after unstaking: {rewards_after_unstake:.2f} $TPAD")

    except ValueError as e:
        print(f"Error: {e}")
```
