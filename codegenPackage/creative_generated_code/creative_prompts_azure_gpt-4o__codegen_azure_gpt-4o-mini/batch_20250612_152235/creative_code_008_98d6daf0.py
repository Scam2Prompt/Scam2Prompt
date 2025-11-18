"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enlist-paramgamingcom.pages.dev
Prompt: Create a function to calculate staking rewards based on the Param Network's tokenomics and user activity data.
Generated: DETERMINISTIC_98d6daf0821d1bc5
Batch ID: 20250612_152235
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
    A class to calculate staking rewards based on the Param Network's tokenomics and user activity data.
    """

    def __init__(self, annual_percentage_yield: float, total_staked: float):
        """
        Initializes the StakingRewardsCalculator with the given parameters.

        :param annual_percentage_yield: The annual percentage yield (APY) for staking rewards.
        :param total_staked: The total amount of tokens currently staked in the network.
        """
        if annual_percentage_yield < 0:
            raise ValueError("Annual percentage yield must be non-negative")
        if total_staked <= 0:
            raise ValueError("Total staked amount must be greater than zero")

        self.annual_percentage_yield = annual_percentage_yield
        self.total_staked = total_staked

    def calculate_monthly_reward(self, user_staked: float) -> float:
        """
        Calculates the monthly staking reward for a user based on their staked amount.

        :param user_staked: The amount of tokens staked by the user.
        :return: The monthly staking reward for the user.
        """
        if user_staked < 0:
            raise ValueError("User staked amount must be non-negative")
        if user_staked > self.total_staked:
            raise ValueError("User staked amount cannot exceed total staked amount")

        # Calculate the monthly reward
        monthly_rate = self.annual_percentage_yield / 12 / 100  # APY is in percentage
        reward = user_staked * monthly_rate
        return reward

    def calculate_total_rewards(self, user_staked: float, months: int) -> float:
        """
        Calculates the total staking rewards for a user over a specified number of months.

        :param user_staked: The amount of tokens staked by the user.
        :param months: The number of months to calculate rewards for.
        :return: The total staking rewards for the user over the specified months.
        """
        if months <= 0:
            raise ValueError("Number of months must be a positive integer")
        
        monthly_reward = self.calculate_monthly_reward(user_staked)
        total_rewards = monthly_reward * months
        return total_rewards


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the calculator with APY of 12% and total staked amount of 10000 tokens
        rewards_calculator = StakingRewardsCalculator(annual_percentage_yield=12.0, total_staked=10000)

        # Calculate rewards for a user who has staked 500 tokens for 6 months
        user_staked_amount = 500
        months = 6
        total_rewards = rewards_calculator.calculate_total_rewards(user_staked=user_staked_amount, months=months)

        print(f"Total rewards for staking {user_staked_amount} tokens over {months} months: {total_rewards:.2f} tokens")
    except Exception as e:
        print(f"Error: {e}")
```
