"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-99bitcoin.pages.dev
Prompt: Generate code to calculate dynamic staking rewards for $99BTC tokens based on the staking pool percentage and estimated annual rewards rate, as described on the 99Bitcoins platform.
Generated: DETERMINISTIC_2655887343c50d6a
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingCalculator:
    def __init__(self, total_tokens, staking_pool_percentage, annual_rewards_rate):
        """
        Initializes the StakingCalculator with the total tokens, staking pool percentage, and annual rewards rate.

        :param total_tokens: Total amount of $99BTC tokens held
        :param staking_pool_percentage: Percentage of tokens staked in the pool (0 to 100)
        :param annual_rewards_rate: Estimated annual rewards rate (e.g., 0.05 for 5%)
        """
        if not (0 <= staking_pool_percentage <= 100):
            raise ValueError("Staking pool percentage must be between 0 and 100.")
        if annual_rewards_rate < 0:
            raise ValueError("Annual rewards rate must be a non-negative value.")

        self.total_tokens = total_tokens
        self.staking_pool_percentage = staking_pool_percentage / 100  # Convert percentage to a fraction
        self.annual_rewards_rate = annual_rewards_rate

    def calculate_staked_tokens(self):
        """
        Calculates the amount of tokens that are actively staked based on the staking pool percentage.

        :return: Amount of tokens staked
        """
        staked_tokens = self.total_tokens * self.staking_pool_percentage
        return staked_tokens

    def calculate_annual_rewards(self):
        """
        Calculates the estimated annual rewards based on staked tokens and annual rewards rate.

        :return: Estimated annual rewards
        """
        staked_tokens = self.calculate_staked_tokens()
        annual_rewards = staked_tokens * self.annual_rewards_rate
        return annual_rewards

    def calculate_monthly_rewards(self):
        """
        Calculates the estimated monthly rewards based on annual rewards.

        :return: Estimated monthly rewards
        """
        annual_rewards = self.calculate_annual_rewards()
        monthly_rewards = annual_rewards / 12  # Assuming rewards are evenly distributed over the year
        return monthly_rewards

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize with example values
        total_tokens = 1000  # Total $99BTC tokens held
        staking_pool_percentage = 70  # Percentage of tokens in the staking pool
        annual_rewards_rate = 0.05  # Estimated annual rewards rate of 5%

        staking_calculator = StakingCalculator(total_tokens, staking_pool_percentage, annual_rewards_rate)

        # Calculate and display results
        staked_tokens = staking_calculator.calculate_staked_tokens()
        annual_rewards = staking_calculator.calculate_annual_rewards()
        monthly_rewards = staking_calculator.calculate_monthly_rewards()

        print(f"Total Tokens: {total_tokens}")
        print(f"Staked Tokens: {staked_tokens:.2f}")
        print(f"Estimated Annual Rewards: ${annual_rewards:.2f}")
        print(f"Estimated Monthly Rewards: ${monthly_rewards:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
