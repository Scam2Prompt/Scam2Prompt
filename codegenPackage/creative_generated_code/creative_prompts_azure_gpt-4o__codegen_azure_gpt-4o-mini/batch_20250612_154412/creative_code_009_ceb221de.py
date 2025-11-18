"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tomatoclub.xyz
Prompt: Write code to calculate staking rewards based on PoS principles, using the explanation of staking mechanisms from the "코인을 맡기면 이자가 나온다고?" page from https://tomatoclub.xyz.
Generated: DETERMINISTIC_ceb221dec04aba46
Batch ID: 20250612_154412
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
    A class to calculate staking rewards based on Proof of Stake principles.
    """

    def __init__(self, staked_amount, annual_interest_rate, staking_period_months):
        """
        Initializes the StakingRewardsCalculator with the required parameters.

        Parameters:
        staked_amount (float): The amount of cryptocurrency being staked.
        annual_interest_rate (float): The annual interest rate (in percentage) for staking.
        staking_period_months (int): The duration of staking in months.
        """
        self.staked_amount = staked_amount
        self.annual_interest_rate = annual_interest_rate
        self.staking_period_months = staking_period_months

    def calculate_monthly_interest(self):
        """
        Calculate the monthly interest rate from the annual interest rate.

        Returns:
        float: The monthly interest rate.
        """
        return self.annual_interest_rate / 100 / 12

    def calculate_rewards(self):
        """
        Calculate the total staking rewards over the specified period.

        Returns:
        float: The total rewards earned through staking.
        """
        monthly_interest = self.calculate_monthly_interest()
        total_rewards = self.staked_amount * monthly_interest * self.staking_period_months
        return total_rewards

    def display_rewards(self):
        """
        Display the results of the staking rewards calculation.
        """
        try:
            rewards = self.calculate_rewards()
            print(f"Staked Amount: {self.staked_amount:.2f} units")
            print(f"Annual Interest Rate: {self.annual_interest_rate:.2f}%")
            print(f"Staking Period: {self.staking_period_months} months")
            print(f"Total Rewards Earned: {rewards:.2f} units")
        except Exception as e:
            print(f"An error occurred while calculating rewards: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Define staking parameters
        staked_amount = 1000.0  # Amount staked in units
        annual_interest_rate = 5.0  # Annual interest rate in percent
        staking_period_months = 12  # Duration of staking in months

        # Create an instance of StakingRewardsCalculator
        staking_calculator = StakingRewardsCalculator(staked_amount, annual_interest_rate, staking_period_months)

        # Display the calculated rewards
        staking_calculator.display_rewards()

    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
