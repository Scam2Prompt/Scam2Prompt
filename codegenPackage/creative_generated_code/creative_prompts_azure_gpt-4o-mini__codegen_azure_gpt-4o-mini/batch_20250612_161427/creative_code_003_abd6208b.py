"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paal.vercel.app
Prompt: Generate a function that calculates total ETH rewards based on staking amounts, inspired by the Paal AI rewards campaign.
Generated: DETERMINISTIC_abd6208b0d359b3f
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EthRewardsCalculator:
    """
    A class to calculate total ETH rewards based on staking amounts.
    Inspired by the Paal AI rewards campaign.
    """

    def __init__(self, staking_amounts, reward_rate):
        """
        Initializes the EthRewardsCalculator with staking amounts and a reward rate.

        :param staking_amounts: List of staking amounts for each participant.
        :param reward_rate: The reward rate as a decimal (e.g., 0.05 for 5%).
        """
        if not isinstance(staking_amounts, list) or not all(isinstance(amount, (int, float)) for amount in staking_amounts):
            raise ValueError("staking_amounts must be a list of numbers.")
        if not isinstance(reward_rate, (int, float)) or reward_rate < 0:
            raise ValueError("reward_rate must be a non-negative number.")
        
        self.staking_amounts = staking_amounts
        self.reward_rate = reward_rate

    def calculate_total_rewards(self):
        """
        Calculates the total ETH rewards based on the staking amounts and reward rate.

        :return: Total ETH rewards as a float.
        """
        total_rewards = 0.0
        for amount in self.staking_amounts:
            reward = amount * self.reward_rate
            total_rewards += reward
        return total_rewards

    def display_rewards(self):
        """
        Displays the staking amounts and their corresponding rewards.
        """
        print("Staking Amounts and Corresponding Rewards:")
        for amount in self.staking_amounts:
            reward = amount * self.reward_rate
            print(f"Staking Amount: {amount} ETH -> Reward: {reward:.4f} ETH")
        print(f"Total Rewards: {self.calculate_total_rewards():.4f} ETH")


# Example usage
if __name__ == "__main__":
    try:
        staking_amounts = [1.0, 2.5, 0.75, 3.0]  # Example staking amounts in ETH
        reward_rate = 0.05  # Example reward rate (5%)

        rewards_calculator = EthRewardsCalculator(staking_amounts, reward_rate)
        rewards_calculator.display_rewards()
    except ValueError as e:
        print(f"Error: {e}")
```
