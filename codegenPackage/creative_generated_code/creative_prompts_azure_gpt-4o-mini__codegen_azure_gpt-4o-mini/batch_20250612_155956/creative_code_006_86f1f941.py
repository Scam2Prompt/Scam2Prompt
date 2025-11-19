"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nexus-mutual.xyz
Prompt: Create a function that calculates the rewards for members staking NXM tokens based on the risk level of smart contracts in Nexus Mutual.
Generated: DETERMINISTIC_86f1f94191ae62ee
Batch ID: 20250612_155956
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingRewardsCalculator:
    """
    A class to calculate staking rewards for members based on the risk level of smart contracts in Nexus Mutual.
    """

    def __init__(self, base_reward_rate: float):
        """
        Initializes the StakingRewardsCalculator with a base reward rate.

        :param base_reward_rate: The base reward rate for staking NXM tokens.
        """
        if base_reward_rate <= 0:
            raise ValueError("Base reward rate must be a positive value.")
        self.base_reward_rate = base_reward_rate

    def calculate_rewards(self, staked_amount: float, risk_level: str) -> float:
        """
        Calculates the staking rewards based on the staked amount and the risk level of the smart contract.

        :param staked_amount: The amount of NXM tokens staked.
        :param risk_level: The risk level of the smart contract ("low", "medium", "high").
        :return: The calculated rewards.
        """
        if staked_amount <= 0:
            raise ValueError("Staked amount must be a positive value.")
        
        risk_multiplier = self.get_risk_multiplier(risk_level)

        # Calculate rewards
        rewards = staked_amount * self.base_reward_rate * risk_multiplier
        return rewards

    def get_risk_multiplier(self, risk_level: str) -> float:
        """
        Retrieves the risk multiplier based on the risk level.

        :param risk_level: The risk level of the smart contract ("low", "medium", "high").
        :return: The corresponding risk multiplier.
        """
        risk_multipliers = {
            "low": 1.0,
            "medium": 1.5,
            "high": 2.0
        }

        # Check for valid risk level
        if risk_level not in risk_multipliers:
            raise ValueError(f"Invalid risk level: {risk_level}. Valid options are: {', '.join(risk_multipliers.keys())}")

        return risk_multipliers[risk_level]


# Example usage:
if __name__ == "__main__":
    try:
        calculator = StakingRewardsCalculator(base_reward_rate=0.1)  # 10% base reward
        staked_amount = 1000  # Amount of NXM tokens staked
        risk_level = "medium"  # Risk level of the smart contract

        # Calculate the rewards
        rewards = calculator.calculate_rewards(staked_amount, risk_level)
        print(f"Calculated rewards for staking {staked_amount} NXM with {risk_level} risk level: {rewards} NXM")
    except ValueError as e:
        print(f"Error: {e}")
```
