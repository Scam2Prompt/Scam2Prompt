"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ayeaye-pro.pages.dev
Prompt: Write code to calculate and distribute rewards among early investors in a cryptocurrency project, based on the principles outlined by Aye Aye Coin.
Generated: DETERMINISTIC_4f3c5856fbba60da
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EarlyInvestorRewardDistribution:
    def __init__(self, total_rewards, investors):
        """
        Initialize the reward distribution system.

        :param total_rewards: Total amount of rewards to be distributed (float).
        :param investors: List of tuples, each containing (investor_address, investment_amount).
        """
        self.total_rewards = total_rewards
        self.investors = investors
        self.total_investment = sum(amount for _, amount in investors)

        # Check that the total investment is greater than zero to avoid division by zero.
        if self.total_investment <= 0:
            raise ValueError("Total investment must be greater than zero.")

    def calculate_rewards(self):
        """
        Calculate the rewards for each investor based on their investment amount.

        :return: A list of tuples containing (investor_address, reward_amount).
        """
        rewards = []
        for address, investment in self.investors:
            # Calculate individual reward based on proportional investment
            reward_amount = (investment / self.total_investment) * self.total_rewards
            rewards.append((address, reward_amount))
        return rewards

    def distribute_rewards(self):
        """
        Distribute rewards to the investors.

        :return: A dictionary with investor addresses as keys and their corresponding reward amounts.
        """
        rewards = self.calculate_rewards()
        reward_distribution = {}
        
        for address, reward in rewards:
            # Simulate the distribution of rewards, in a real scenario this would involve transactions
            reward_distribution[address] = reward
        
        return reward_distribution

if __name__ == "__main__":
    try:
        # Example list of investors and their investment amounts
        investors_data = [
            ("0xInvestorA", 1000.0),
            ("0xInvestorB", 2000.0),
            ("0xInvestorC", 3000.0)
        ]
        total_reward_amount = 600.0  # Total rewards to be distributed

        # Initialize the reward distribution system
        distribution_system = EarlyInvestorRewardDistribution(total_reward_amount, investors_data)
        
        # Distribute rewards
        rewards = distribution_system.distribute_rewards()
        
        # Display the rewards
        for address, reward in rewards.items():
            print(f"Investor Address: {address} | Reward Amount: {reward:.2f}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
