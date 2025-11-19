"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-earthmeta.pages.dev
Prompt: Write a Python script that calculates potential staking rewards for $EMT tokens based on the current presale stage and bonus percentages.
Generated: DETERMINISTIC_d9e28e79df02d82a
Batch ID: 20250612_163630
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class StakingCalculator:
    """
    A class to calculate potential staking rewards for $EMT tokens based on the current presale stage and bonus percentages.
    """

    def __init__(self, initial_investment, presale_stage, staking_duration_months):
        """
        Initialize the StakingCalculator with the investment amount, presale stage, and duration.
        
        :param initial_investment: The initial amount of $EMT tokens invested.
        :param presale_stage: The current presale stage (1, 2, or 3).
        :param staking_duration_months: The duration for which the tokens are staked, in months.
        """
        self.initial_investment = initial_investment
        self.presale_stage = presale_stage
        self.staking_duration_months = staking_duration_months
        self.bonus_percentage = self.get_bonus_percentage()

    def get_bonus_percentage(self):
        """
        Get the bonus percentage based on the presale stage.
        
        :return: Bonus percentage as a decimal.
        :raises ValueError: If the presale stage is invalid.
        """
        if self.presale_stage == 1:
            return 0.20  # 20% bonus for stage 1
        elif self.presale_stage == 2:
            return 0.15  # 15% bonus for stage 2
        elif self.presale_stage == 3:
            return 0.10  # 10% bonus for stage 3
        else:
            raise ValueError("Presale stage must be 1, 2, or 3.")

    def calculate_rewards(self):
        """
        Calculate the potential staking rewards based on the initial investment and bonus percentage.
        
        :return: Total rewards after staking duration.
        """
        # Calculate total rewards
        total_investment_with_bonus = self.initial_investment * (1 + self.bonus_percentage)
        total_rewards = total_investment_with_bonus * (self.staking_duration_months / 12)  # Assuming annual staking
        return total_rewards

def main():
    """
    Main function to run the staking calculator.
    """
    try:
        initial_investment = float(input("Enter your initial investment in $EMT tokens: "))
        presale_stage = int(input("Enter the presale stage (1, 2, or 3): "))
        staking_duration_months = int(input("Enter the staking duration in months: "))
        
        # Create an instance of StakingCalculator
        calculator = StakingCalculator(initial_investment, presale_stage, staking_duration_months)
        
        # Calculate and display the rewards
        rewards = calculator.calculate_rewards()
        print(f"Total potential staking rewards: {rewards:.2f} $EMT tokens")
        
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
