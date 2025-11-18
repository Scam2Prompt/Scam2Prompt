"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syncexperttrade.com
Prompt: Write a Python script to automate investment planning based on SyncExpertTrade's account tiers (Bronze, Silver, Gold, Premium) and their respective profit margins.
Generated: DETERMINISTIC_42a3c0d16c6af8e3
Batch ID: 20250612_154622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class InvestmentPlanner:
    """
    A class to handle automated investment planning based on account tiers 
    and their respective profit margins.
    """
    def __init__(self):
        # Define account tiers and their profit margins
        self.account_tiers = {
            "Bronze": 0.03,  # 3% profit margin
            "Silver": 0.05,  # 5% profit margin
            "Gold": 0.08,    # 8% profit margin
            "Premium": 0.12  # 12% profit margin
        }

    def calculate_profit(self, tier, investment_amount):
        """
        Calculate the expected profit based on the account tier and investment amount.

        :param tier: str: Account tier (Bronze, Silver, Gold, Premium)
        :param investment_amount: float: Amount to be invested
        :return: float: Expected profit
        :raises ValueError: If the account tier is invalid or investment amount is negative
        """
        if tier not in self.account_tiers:
            raise ValueError(f"Invalid account tier: {tier}")
        if investment_amount < 0:
            raise ValueError("Investment amount cannot be negative.")
        
        # Calculate profit
        profit_margin = self.account_tiers[tier]
        expected_profit = investment_amount * profit_margin
        return expected_profit

def get_user_input():
    """
    Get user input for account tier and investment amount.

    :return: tuple: (tier, investment_amount)
    :raises ValueError: If input is invalid
    """
    try:
        tier = input("Enter your account tier (Bronze, Silver, Gold, Premium): ").capitalize()
        investment_amount = float(input("Enter the amount you wish to invest: "))
        return tier, investment_amount
    except ValueError as e:
        raise ValueError("Invalid input. Please ensure you enter valid data.") from e

def main():
    """
    Main function to execute investment planning.
    """
    print("Welcome to SyncExpertTrade Investment Planner!")
    planner = InvestmentPlanner()

    try:
        # Get user input
        tier, investment_amount = get_user_input()

        # Calculate profit
        profit = planner.calculate_profit(tier, investment_amount)
        print(f"\nAccount Tier: {tier}")
        print(f"Investment Amount: ${investment_amount:.2f}")
        print(f"Expected Profit: ${profit:.2f}")
    except ValueError as ve:
        # Handle invalid input or computation errors
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        # Catch-all for unforeseen errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
