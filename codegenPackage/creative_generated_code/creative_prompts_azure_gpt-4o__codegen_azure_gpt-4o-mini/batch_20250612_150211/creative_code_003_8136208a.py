"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elitetoptrade.com
Prompt: Create a Python script to automate investment planning based on Elitetoptrade's account tiers (Silver, Gold, Premium) and calculate projected profits.
Generated: DETERMINISTIC_8136208ab69cc148
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class InvestmentAccount:
    """
    Class representing an investment account with different tiers and profit calculation.
    """

    def __init__(self, tier, initial_investment):
        """
        Initializes the InvestmentAccount instance.
        
        :param tier: str - The account tier (Silver, Gold, Premium)
        :param initial_investment: float - The initial investment amount
        """
        self.tier = tier
        self.initial_investment = initial_investment
        self.interest_rate = self.get_interest_rate(tier)

    def get_interest_rate(self, tier):
        """
        Returns the interest rate based on the account tier.
        
        :param tier: str - The account tier
        :return: float - The corresponding interest rate
        """
        interest_rates = {
            'Silver': 0.05,   # 5% interest for Silver account
            'Gold': 0.07,     # 7% interest for Gold account
            'Premium': 0.10   # 10% interest for Premium account
        }
        
        if tier not in interest_rates:
            raise ValueError("Invalid account tier provided. Choose from: Silver, Gold, Premium.")
        
        return interest_rates[tier]

    def calculate_projected_profit(self, years):
        """
        Calculates the projected profit for a given number of years.
        
        :param years: int - The number of years to project
        :return: float - The projected profit
        """
        if years < 0:
            raise ValueError("Number of years cannot be negative.")
        
        projected_profit = self.initial_investment * (1 + self.interest_rate) ** years - self.initial_investment
        return projected_profit

def main():
    """
    Main function to execute the investment planning automation.
    """
    try:
        tier = input("Enter account tier (Silver, Gold, Premium): ")
        initial_investment = float(input("Enter initial investment amount: "))
        years = int(input("Enter number of years for projection: "))

        account = InvestmentAccount(tier, initial_investment)
        profit = account.calculate_projected_profit(years)

        print(f"Projected profit after {years} years for {tier} account: ${profit:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
