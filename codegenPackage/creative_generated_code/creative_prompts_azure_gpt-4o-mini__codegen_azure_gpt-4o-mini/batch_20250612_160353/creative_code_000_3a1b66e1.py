"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coineehub.com
Prompt: Generate a Python script to calculate potential returns from CoineeHub's investment plans, including daily and monthly returns for different packages.
Generated: DETERMINISTIC_3a1b66e1fc6b3b30
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class InvestmentPlan:
    """Class to represent an investment plan with its characteristics."""
    
    def __init__(self, name, daily_rate, monthly_rate):
        """
        Initialize an investment plan with its name, daily rate, and monthly rate.
        
        :param name: str - Name of the investment plan
        :param daily_rate: float - Daily return rate as a percentage
        :param monthly_rate: float - Monthly return rate as a percentage
        """
        self.name = name
        self.daily_rate = daily_rate / 100  # Convert percentage to decimal
        self.monthly_rate = monthly_rate / 100  # Convert percentage to decimal

    def calculate_daily_return(self, investment_amount):
        """
        Calculate potential daily return for the investment amount.
        
        :param investment_amount: float - Amount invested
        :return: float - Daily return amount
        """
        return investment_amount * self.daily_rate

    def calculate_monthly_return(self, investment_amount):
        """
        Calculate potential monthly return for the investment amount.
        
        :param investment_amount: float - Amount invested
        :return: float - Monthly return amount
        """
        return investment_amount * self.monthly_rate

def main():
    """Main function to execute the investment return calculations."""
    # Investment plans (name, daily rate, monthly rate)
    plans = [
        InvestmentPlan("Basic Plan", 1.0, 30.0),  # 1% daily, 30% monthly
        InvestmentPlan("Premium Plan", 1.5, 40.0),  # 1.5% daily, 40% monthly
        InvestmentPlan("Elite Plan", 2.0, 50.0)  # 2% daily, 50% monthly
    ]

    try:
        # User input for investment amount
        investment_amount = float(input("Enter the investment amount: "))
        
        if investment_amount <= 0:
            raise ValueError("Investment amount must be positive.")

        print("\nPotential Returns:\n")
        for plan in plans:
            daily_return = plan.calculate_daily_return(investment_amount)
            monthly_return = plan.calculate_monthly_return(investment_amount)
            print(f"{plan.name}:")
            print(f"  Daily Return: ${daily_return:.2f}")
            print(f"  Monthly Return: ${monthly_return:.2f}\n")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

This script is designed to calculate potential returns from different investment plans with proper error handling and input validation.
