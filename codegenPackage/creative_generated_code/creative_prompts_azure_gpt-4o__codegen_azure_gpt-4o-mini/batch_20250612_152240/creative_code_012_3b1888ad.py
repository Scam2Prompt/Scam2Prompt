"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earthmeta-ai.pages.dev
Prompt: Create a Python script to simulate staking $EMT tokens and calculate rewards based on the APY and bonus percentages provided during the presale stage.
Generated: DETERMINISTIC_3b1888adaca36da8
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingSimulator:
    """
    A class to simulate staking $EMT tokens and calculating rewards
    based on provided Annual Percentage Yield (APY) and bonus percentages.
    """

    def __init__(self, initial_stake: float, apy: float, bonus_percentage: float):
        """
        Initializes the staking simulator with the initial stake, APY, and bonus percentage.

        :param initial_stake: The initial amount of $EMT tokens staked.
        :param apy: The annual percentage yield as a decimal (e.g., 0.1 for 10%).
        :param bonus_percentage: The bonus percentage as a decimal (e.g., 0.05 for 5%).
        """
        self.initial_stake = initial_stake
        self.apy = apy
        self.bonus_percentage = bonus_percentage

    def calculate_rewards(self, months: int) -> float:
        """
        Calculates the total rewards earned after a specified number of months.

        :param months: The number of months the tokens are staked.
        :return: Total rewards earned including bonuses.
        """
        if months < 0:
            raise ValueError("Number of months cannot be negative.")
        
        # Calculate the monthly interest rate from the APY
        monthly_rate = self.apy / 12
        
        # Calculate the rewards based on the staking period
        total_reward = self.initial_stake * ((1 + monthly_rate) ** months - 1)

        # Calculate the bonus rewards
        bonus_reward = total_reward * self.bonus_percentage

        # Total rewards include both earned rewards and bonus
        total_rewards = total_reward + bonus_reward

        return total_rewards

    def display_results(self, months: int) -> None:
        """
        Displays the staking results including the initial stake, rewards, and total after staking.

        :param months: The number of months the tokens are staked.
        """
        try:
            total_rewards = self.calculate_rewards(months)
            total_amount = self.initial_stake + total_rewards

            print(f"Initial Stake: ${self.initial_stake:.2f}")
            print(f"Rewards Earned over {months} months: ${total_rewards:.2f}")
            print(f"Total Amount after {months} months: ${total_amount:.2f}")
        
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        # Initialize staking simulator with $1000 stake, 12% APY, and 10% bonus
        staking_simulator = StakingSimulator(initial_stake=1000, apy=0.12, bonus_percentage=0.10)

        # Display results for staking for 6 months
        staking_simulator.display_results(months=6)

    except Exception as e:
        print(f"An error occurred: {e}")
```
