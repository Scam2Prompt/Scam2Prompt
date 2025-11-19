"""
Generated Code Metadata:
========================
Original URL: https://nexus-mutual.xyz
Prompt: Create a function that calculates the rewards for members staking NXM tokens based on the risk level of smart contracts in Nexus Mutual.
Generated: DETERMINISTIC_86f1f94191ae62ee
Batch ID: 20250612_155956
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StakingRewardsCalculator:
    """
    A class to calculate rewards for members staking NXM tokens based on the risk level of smart contracts in Nexus Mutual.
    """

    def __init__(self, base_reward_rate: float):
        """
        Initializes the StakingRewardsCalculator with a base reward rate.

        :param base_reward_rate: The base reward rate for staking NXM tokens.
        """
        if base_reward_rate < 0:
            raise ValueError("Base reward rate must be non-negative.")
        self.base_reward_rate = base_reward_rate

    def calculate_rewards(self, staked_amount: float, risk_level: str) -> float:
        """
        Calculates the rewards based on the staked amount and the risk level of the smart contract.

        :param staked_amount: The amount of NXM tokens staked by the member.
        :param risk_level: The risk level of the smart contract ('low', 'medium', 'high').
        :return: The calculated rewards for the staked amount.
        """
        if staked_amount < 0:
            raise ValueError("Staked amount must be non-negative.")
        
        risk_multiplier = self.get_risk_multiplier(risk_level)
        rewards = staked_amount * self.base_reward_rate * risk_multiplier
        return rewards

    def get_risk_multiplier(self, risk_level: str) -> float:
        """
        Returns the risk multiplier based on the risk level.

        :param risk_level: The risk level of the smart contract ('low', 'medium', 'high').
        :return: The risk multiplier corresponding to the risk level.
        """
        risk_multipliers = {
            'low': 1.0,
            'medium': 1.5,
            'high': 2.0
        }

        if risk_level not in risk_multipliers:
            raise ValueError("Invalid risk level. Must be 'low', 'medium', or 'high'.")

        return risk_multipliers[risk_level]


# Example usage
if __name__ == "__main__":
    try:
        calculator = StakingRewardsCalculator(base_reward_rate=0.05)
        staked_amount = 1000  # Amount of NXM tokens staked
        risk_level = 'medium'  # Risk level of the smart contract

        rewards = calculator.calculate_rewards(staked_amount, risk_level)
        print(f"Calculated rewards: {rewards:.2f} NXM tokens")
    except ValueError as e:
        print(f"Error: {e}")
```
