"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rocketspool.github.io
Prompt: Write code to simulate staking ETH in Rocket Pool's protocol, demonstrating the differences between tokenized staking and node operation in terms of rewards and requirements.
Generated: DETERMINISTIC_703ddfec541e88e9
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RocketPoolStaking:
    def __init__(self, eth_staked, is_node_operator=False):
        """
        Initialize the RocketPoolStaking class.

        :param eth_staked: Amount of ETH staked (in whole ETH)
        :param is_node_operator: Boolean indicating if the user is a node operator
        """
        self.eth_staked = eth_staked
        self.is_node_operator = is_node_operator
        self.reward_rate = 0.05  # 5% reward rate for tokenized staking
        self.node_reward_rate = 0.1  # 10% reward rate for node operators
        self.minimum_stake = 16  # Minimum stake for node operation in ETH

    def calculate_rewards(self):
        """
        Calculate the rewards based on the staking type.

        :return: Total rewards earned
        """
        if self.is_node_operator:
            if self.eth_staked < self.minimum_stake:
                raise ValueError("Minimum staking requirement for node operation is 16 ETH.")
            rewards = self.eth_staked * self.node_reward_rate
        else:
            rewards = self.eth_staked * self.reward_rate

        return rewards

    def staking_summary(self):
        """
        Provide a summary of the staking details.

        :return: A dictionary containing staking information
        """
        try:
            rewards = self.calculate_rewards()
            summary = {
                "ETH Staked": self.eth_staked,
                "Is Node Operator": self.is_node_operator,
                "Total Rewards Earned": rewards
            }
            return summary
        except ValueError as e:
            return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Example for tokenized staking
    tokenized_staking = RocketPoolStaking(eth_staked=10, is_node_operator=False)
    print(tokenized_staking.staking_summary())

    # Example for node operation (should succeed)
    node_operator_staking = RocketPoolStaking(eth_staked=20, is_node_operator=True)
    print(node_operator_staking.staking_summary())

    # Example for node operation (should raise error)
    try:
        insufficient_node_staking = RocketPoolStaking(eth_staked=10, is_node_operator=True)
        print(insufficient_node_staking.staking_summary())
    except ValueError as e:
        print(f"Error: {e}")
```
