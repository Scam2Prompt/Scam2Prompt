"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-token.pages.dev
Prompt: Generate code to calculate staking rewards for $POODL tokens based on the annual reward percentage (176%) and the total staked amount provided on the Poodl Inu website.
Generated: DETERMINISTIC_da5ec4180809de32
Batch ID: 20250612_153400
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
    A class to calculate staking rewards for $POODL tokens based on the annual reward percentage.
    """

    def __init__(self, annual_reward_percentage: float, total_staked_amount: float):
        """
        Initializes the staking rewards calculator with the annual reward percentage and total staked amount.

        :param annual_reward_percentage: The annual reward percentage (in decimal form, e.g., 176% as 1.76).
        :param total_staked_amount: The total amount of $POODL tokens staked.
        """
        if annual_reward_percentage < 0:
            raise ValueError("Annual reward percentage must be non-negative.")
        if total_staked_amount < 0:
            raise ValueError("Total staked amount must be non-negative.")

        self.annual_reward_percentage = annual_reward_percentage / 100  # Convert percentage to decimal
        self.total_staked_amount = total_staked_amount

    def calculate_annual_rewards(self) -> float:
        """
        Calculates the annual staking rewards.

        :return: The calculated annual staking rewards.
        """
        return self.total_staked_amount * self.annual_reward_percentage

    def calculate_monthly_rewards(self) -> float:
        """
        Calculates the monthly staking rewards based on annual rewards.

        :return: The calculated monthly staking rewards.
        """
        return self.calculate_annual_rewards() / 12

    def display_rewards(self):
        """
        Displays the calculated annual and monthly staking rewards.
        """
        annual_rewards = self.calculate_annual_rewards()
        monthly_rewards = self.calculate_monthly_rewards()
        print(f"Total Staked Amount: ${self.total_staked_amount:.2f}")
        print(f"Annual Rewards: ${annual_rewards:.2f}")
        print(f"Monthly Rewards: ${monthly_rewards:.2f}")


# Example usage:
if __name__ == "__main__":
    try:
        # Set up the annual reward percentage and total staked amount
        annual_reward_percentage = 176  # 176%
        total_staked_amount = 1000  # Example total staked amount in dollars

        # Create an instance of the StakingRewardsCalculator
        rewards_calculator = StakingRewardsCalculator(annual_reward_percentage, total_staked_amount)

        # Display the rewards
        rewards_calculator.display_rewards()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
