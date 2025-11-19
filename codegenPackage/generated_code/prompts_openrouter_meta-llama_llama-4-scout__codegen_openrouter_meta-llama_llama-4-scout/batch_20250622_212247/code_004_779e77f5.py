"""
Generated Code Metadata:
========================
Original URL: https://onbeam.live
Prompt: Create a function to calculate rewards for staking BEAM and Node Tokens on the Beam Network, considering commission rates and staked amounts.
Generated: DETERMINISTIC_779e77f593195758
Batch ID: 20250622_212247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

class StakingRewardsCalculator:
    """
    Calculates rewards for staking BEAM and Node Tokens on the Beam Network.

    Attributes:
    beam_stake (float): The amount of BEAM staked.
    node_token_stake (float): The amount of Node Tokens staked.
    commission_rate (float): The commission rate as a decimal.
    beam_reward_per_block (float): The reward per block for BEAM staking.
    node_token_reward_per_block (float): The reward per block for Node Token staking.
    """

    def __init__(self, 
                 beam_stake: float, 
                 node_token_stake: float, 
                 commission_rate: float, 
                 beam_reward_per_block: float, 
                 node_token_reward_per_block: float):
        """
        Initializes the StakingRewardsCalculator.

        Args:
        beam_stake (float): The amount of BEAM staked.
        node_token_stake (float): The amount of Node Tokens staked.
        commission_rate (float): The commission rate as a decimal.
        beam_reward_per_block (float): The reward per block for BEAM staking.
        node_token_reward_per_block (float): The reward per block for Node Token staking.
        """
        self.beam_stake = beam_stake
        self.node_token_stake = node_token_stake
        self.commission_rate = commission_rate
        self.beam_reward_per_block = beam_reward_per_block
        self.node_token_reward_per_block = node_token_reward_per_block

    def calculate_beam_rewards(self) -> float:
        """
        Calculates the rewards for BEAM staking.

        Returns:
        float: The rewards for BEAM staking.
        """
        # Calculate BEAM rewards without commission
        beam_rewards = self.beam_stake * self.beam_reward_per_block
        
        # Apply commission
        beam_rewards_after_commission = beam_rewards * (1 - self.commission_rate)
        
        return beam_rewards_after_commission

    def calculate_node_token_rewards(self) -> float:
        """
        Calculates the rewards for Node Token staking.

        Returns:
        float: The rewards for Node Token staking.
        """
        # Calculate Node Token rewards without commission
        node_token_rewards = self.node_token_stake * self.node_token_reward_per_block
        
        # Apply commission
        node_token_rewards_after_commission = node_token_rewards * (1 - self.commission_rate)
        
        return node_token_rewards_after_commission

    def calculate_total_rewards(self) -> Dict[str, float]:
        """
        Calculates the total rewards for both BEAM and Node Token staking.

        Returns:
        Dict[str, float]: A dictionary containing the rewards for BEAM and Node Token staking.
        """
        beam_rewards = self.calculate_beam_rewards()
        node_token_rewards = self.calculate_node_token_rewards()
        
        return {
            "beam_rewards": beam_rewards,
            "node_token_rewards": node_token_rewards,
            "total_rewards": beam_rewards + node_token_rewards
        }


def main():
    try:
        # Example usage
        beam_stake = 1000.0
        node_token_stake = 500.0
        commission_rate = 0.1  # 10% commission
        beam_reward_per_block = 0.01
        node_token_reward_per_block = 0.005

        calculator = StakingRewardsCalculator(beam_stake, 
                                              node_token_stake, 
                                              commission_rate, 
                                              beam_reward_per_block, 
                                              node_token_reward_per_block)

        rewards = calculator.calculate_total_rewards()
        
        print("Rewards:")
        for reward_type, amount in rewards.items():
            print(f"{reward_type.capitalize().replace('_', ' ')}: {amount}")
    
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
