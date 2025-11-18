"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://invistribe.com
Prompt: Develop a Python program to calculate potential earnings based on the Fortunity reward tiers (Bronze, Silver, Gold) and simulate the growth of income over time.
Generated: DETERMINISTIC_162771cb25bcce89
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List

class RewardTier:
    """
    Class to represent a reward tier with specific earning multipliers.
    """
    def __init__(self, name: str, multiplier: float):
        self.name = name
        self.multiplier = multiplier

class FortunityEarningsCalculator:
    """
    A calculator for potential earnings based on Fortunity reward tiers.
    Simulates income growth over a given period of time.
    """
    def __init__(self):
        # Define reward tiers with their multipliers
        self.tiers = {
            'Bronze': RewardTier('Bronze', 1.0),
            'Silver': RewardTier('Silver', 1.5),
            'Gold': RewardTier('Gold', 2.0)
        }

    def calculate_monthly_earnings(self, base_income: float, tier_name: str) -> float:
        """
        Calculate monthly earnings based on the reward tier multiplier.
        :param base_income: The base income amount.
        :param tier_name: The name of the reward tier.
        :return: Monthly earnings after applying the multiplier.
        """
        if tier_name not in self.tiers:
            raise ValueError(f"Invalid tier name: {tier_name}. Valid tiers are: {', '.join(self.tiers.keys())}")
        
        tier = self.tiers[tier_name]
        return base_income * tier.multiplier

    def simulate_income_growth(self, base_income: float, tier_name: str, months: int) -> List[float]:
        """
        Simulate the growth of income over a specified number of months.
        :param base_income: The base income amount.
        :param tier_name: The name of the reward tier.
        :param months: The number of months to simulate.
        :return: A list of cumulative income for each month.
        """
        if months <= 0:
            raise ValueError("Number of months must be greater than 0.")
        
        monthly_earning = self.calculate_monthly_earnings(base_income, tier_name)
        cumulative_income = []
        total_income = 0.0

        for month in range(1, months + 1):
            total_income += monthly_earning
            cumulative_income.append(total_income)

        return cumulative_income

def main():
    """
    Main function to run the Fortunity Earnings Calculator.
    """
    print("Welcome to the Fortunity Earnings Calculator!")
    
    try:
        # Get user input for base income, reward tier, and number of months
        base_income = float(input("Enter your base monthly income: "))
        tier_name = input("Enter your reward tier (Bronze, Silver, Gold): ").capitalize()
        months = int(input("Enter the number of months for income simulation: "))

        # Instantiate the calculator
        calculator = FortunityEarningsCalculator()

        # Calculate earnings and simulate growth
        earnings = calculator.simulate_income_growth(base_income, tier_name, months)
        
        print("\nIncome Growth Simulation:")
        for month, income in enumerate(earnings, start=1):
            print(f"Month {month}: ${income:.2f}")

    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
