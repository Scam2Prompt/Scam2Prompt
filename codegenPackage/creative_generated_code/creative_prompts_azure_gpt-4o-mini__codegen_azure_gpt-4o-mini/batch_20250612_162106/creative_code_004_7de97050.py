"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rockketpool.github.io
Prompt: Describe the process of earning staking rewards through Rocket Pool and how to calculate them based on node performance.
Generated: DETERMINISTIC_7de97050379fa2d1
Batch ID: 20250612_162106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class RocketPoolStaking:
    def __init__(self, total_eth_staked, node_performance, reward_rate):
        """
        Initialize the RocketPoolStaking instance.

        Parameters:
        total_eth_staked (float): Total ETH staked in the Rocket Pool.
        node_performance (float): Performance of the node as a percentage (0-100).
        reward_rate (float): Base reward rate as a percentage (0-100).
        """
        if total_eth_staked < 0:
            raise ValueError("Total ETH staked cannot be negative.")
        if not (0 <= node_performance <= 100):
            raise ValueError("Node performance must be between 0 and 100.")
        if not (0 <= reward_rate <= 100):
            raise ValueError("Reward rate must be between 0 and 100.")
        
        self.total_eth_staked = total_eth_staked
        self.node_performance = node_performance
        self.reward_rate = reward_rate

    def calculate_rewards(self, period_years):
        """
        Calculate the staking rewards based on node performance and period.

        Parameters:
        period_years (float): The staking period in years.

        Returns:
        float: The calculated rewards in ETH.
        """
        if period_years < 0:
            raise ValueError("Staking period cannot be negative.")

        # Effective reward rate based on node performance
        effective_reward_rate = (self.reward_rate / 100) * (self.node_performance / 100)
        
        # Total rewards calculation
        rewards = self.total_eth_staked * effective_reward_rate * period_years
        
        return rewards

    def display_rewards(self, period_years):
        """
        Display the calculated rewards in a formatted way.

        Parameters:
        period_years (float): The staking period in years.
        """
        try:
            rewards = self.calculate_rewards(period_years)
            print(f"Total ETH staked: {self.total_eth_staked:.2f}")
            print(f"Node Performance: {self.node_performance:.2f}%")
            print(f"Reward Rate: {self.reward_rate:.2f}%")
            print(f"Staking Period: {period_years:.2f} years")
            print(f"Calculated Rewards: {rewards:.4f} ETH")
        except ValueError as e:
            print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of RocketPoolStaking with example values
        staking = RocketPoolStaking(total_eth_staked=10.0, node_performance=95.0, reward_rate=5.0)
        
        # Display rewards for a staking period of 3 years
        staking.display_rewards(period_years=3.0)
    except Exception as e:
        print(f"Error initializing RocketPoolStaking: {e}")
```
