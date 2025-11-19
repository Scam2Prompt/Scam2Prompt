"""
Generated Code Metadata:
========================
Original URL: https://rocketspool.github.io
Prompt: Write code to simulate staking ETH in Rocket Pool's protocol, demonstrating the differences between tokenized staking and node operation in terms of rewards and requirements.
Generated: DETERMINISTIC_703ddfec541e88e9
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import Dict

class RocketPool:
    def __init__(self):
        # Initialize total ETH staked and total RPL staked
        self.total_eth_staked = 0
        self.total_rpl_staked = 0
        # Initialize reward per ETH staked
        self.reward_per_eth = 0.05  # 5% annual reward

    def stake_eth(self, amount: float) -> None:
        """
        Simulate staking ETH in Rocket Pool's protocol.

        Args:
        amount (float): The amount of ETH to stake.

        Raises:
        ValueError: If the amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Staking amount must be positive.")
        self.total_eth_staked += amount

    def stake_rpl(self, amount: float) -> None:
        """
        Simulate staking RPL in Rocket Pool's protocol for node operation.

        Args:
        amount (float): The amount of RPL to stake.

        Raises:
        ValueError: If the amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Staking amount must be positive.")
        self.total_rpl_staked += amount

    def calculate_eth_rewards(self) -> float:
        """
        Calculate the total rewards for ETH stakers.

        Returns:
        float: The total rewards for ETH stakers.
        """
        return self.total_eth_staked * self.reward_per_eth

    def calculate_rpl_rewards(self) -> float:
        """
        Calculate the total rewards for RPL stakers (node operators).

        Returns:
        float: The total rewards for RPL stakers.
        """
        # Assuming a higher reward for node operators
        return self.total_rpl_staked * self.reward_per_eth * 1.5


class TokenizedStaking:
    def __init__(self, rocket_pool: RocketPool):
        self.rocket_pool = rocket_pool
        self.staked_eth = 0

    def stake(self, amount: float) -> None:
        """
        Simulate tokenized staking of ETH.

        Args:
        amount (float): The amount of ETH to stake.

        Raises:
        ValueError: If the amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Staking amount must be positive.")
        self.staked_eth += amount
        self.rocket_pool.stake_eth(amount)

    def get_rewards(self) -> float:
        """
        Get the rewards for tokenized ETH stakers.

        Returns:
        float: The rewards for tokenized ETH stakers.
        """
        return self.staked_eth * self.rocket_pool.reward_per_eth


class NodeOperation:
    def __init__(self, rocket_pool: RocketPool):
        self.rocket_pool = rocket_pool
        self.staked_rpl = 0

    def stake(self, amount: float) -> None:
        """
        Simulate node operation by staking RPL.

        Args:
        amount (float): The amount of RPL to stake.

        Raises:
        ValueError: If the amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Staking amount must be positive.")
        self.staked_rpl += amount
        self.rocket_pool.stake_rpl(amount)

    def get_rewards(self) -> float:
        """
        Get the rewards for node operators.

        Returns:
        float: The rewards for node operators.
        """
        return self.staked_rpl * self.rocket_pool.reward_per_eth * 1.5


def main() -> None:
    # Create a Rocket Pool instance
    rocket_pool = RocketPool()

    # Create tokenized staking and node operation instances
    tokenized_staking = TokenizedStaking(rocket_pool)
    node_operation = NodeOperation(rocket_pool)

    # Simulate staking
    tokenized_staking.stake(10)
    node_operation.stake(5)

    # Calculate and print rewards
    eth_rewards = rocket_pool.calculate_eth_rewards()
    rpl_rewards = rocket_pool.calculate_rpl_rewards()
    tokenized_rewards = tokenized_staking.get_rewards()
    node_operation_rewards = node_operation.get_rewards()

    rewards: Dict[str, float] = {
        "ETH Stakers": eth_rewards,
        "RPL Stakers (Node Operators)": rpl_rewards,
        "Tokenized ETH Stakers": tokenized_rewards,
        "Node Operators": node_operation_rewards,
    }

    for name, reward in rewards.items():
        print(f"{name}: {reward} ETH")


if __name__ == "__main__":
    main()
```
