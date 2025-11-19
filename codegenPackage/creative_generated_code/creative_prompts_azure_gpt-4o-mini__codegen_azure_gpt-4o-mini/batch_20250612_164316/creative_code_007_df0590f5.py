"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-dapps.pages.dev
Prompt: Create a function that calculates potential staking rewards based on the gamified model used by Green Bitcoin.
Generated: DETERMINISTIC_df0590f50787e5b6
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingRewardCalculator:
    """
    A class to calculate potential staking rewards based on the gamified model used by Green Bitcoin.
    """

    def __init__(self, total_supply: float, staked_amount: float, reward_rate: float, staking_period: int):
        """
        Initializes the StakingRewardCalculator with the necessary parameters.

        :param total_supply: Total supply of the cryptocurrency.
        :param staked_amount: Amount of cryptocurrency being staked.
        :param reward_rate: Annual reward rate as a decimal (e.g., 0.05 for 5%).
        :param staking_period: Duration of staking in years.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if staked_amount < 0:
            raise ValueError("Staked amount cannot be negative.")
        if not (0 <= reward_rate <= 1):
            raise ValueError("Reward rate must be between 0 and 1.")
        if staking_period < 0:
            raise ValueError("Staking period cannot be negative.")

        self.total_supply = total_supply
        self.staked_amount = staked_amount
        self.reward_rate = reward_rate
        self.staking_period = staking_period

    def calculate_rewards(self) -> float:
        """
        Calculates the potential staking rewards over the specified staking period.

        :return: The total rewards earned after the staking period.
        """
        rewards = self.staked_amount * self.reward_rate * self.staking_period
        return rewards

    def calculate_percentage_of_supply(self) -> float:
        """
        Calculates the percentage of total supply that is being staked.

        :return: The percentage of the total supply that is staked.
        """
        if self.total_supply == 0:
            return 0.0
        return (self.staked_amount / self.total_supply) * 100

    def display_results(self):
        """
        Displays the results of the staking calculations.
        """
        try:
            rewards = self.calculate_rewards()
            staking_percentage = self.calculate_percentage_of_supply()

            print(f"Staked Amount: {self.staked_amount} BTC")
            print(f"Potential Rewards over {self.staking_period} years: {rewards:.6f} BTC")
            print(f"Percentage of Total Supply Staked: {staking_percentage:.2f}%")
        except Exception as e:
            print(f"An error occurred while calculating rewards: {e}")

# Example of usage
if __name__ == "__main__":
    try:
        # Parameters: total_supply, staked_amount, reward_rate, staking_period
        calculator = StakingRewardCalculator(total_supply=21000000, staked_amount=0.5, reward_rate=0.05, staking_period=5)
        calculator.display_results()
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
```
