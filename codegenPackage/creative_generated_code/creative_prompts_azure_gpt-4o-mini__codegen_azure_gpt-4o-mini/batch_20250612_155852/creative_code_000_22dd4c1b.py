"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centraltraderz.com
Prompt: Generate a Python script that calculates potential profits based on the investment plans offered by Centraltraderz, including the minimum deposit and expected returns for each plan.
Generated: DETERMINISTIC_22dd4c1b89175ec4
Batch ID: 20250612_155852
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
    """Class to represent an investment plan with a minimum deposit and expected returns."""
    
    def __init__(self, name, min_deposit, expected_return_rate):
        """
        Initialize an InvestmentPlan instance.
        
        Args:
            name (str): The name of the investment plan.
            min_deposit (float): The minimum deposit required for the plan.
            expected_return_rate (float): The expected return rate as a percentage.
        """
        self.name = name
        self.min_deposit = min_deposit
        self.expected_return_rate = expected_return_rate
    
    def calculate_profit(self, deposit_amount):
        """
        Calculate the potential profit based on the deposit amount.
        
        Args:
            deposit_amount (float): The amount being deposited.
        
        Returns:
            float: The calculated profit based on the deposit and expected return rate.
        
        Raises:
            ValueError: If deposit_amount is less than the minimum deposit.
        """
        if deposit_amount < self.min_deposit:
            raise ValueError(f"Deposit amount must be at least {self.min_deposit} for the {self.name} plan.")
        
        profit = deposit_amount * (self.expected_return_rate / 100)
        return profit


def main():
    """Main function to execute the investment profit calculations."""
    # Define investment plans offered by Centraltraderz
    plans = [
        InvestmentPlan("Basic Plan", 1000, 5.0),
        InvestmentPlan("Standard Plan", 5000, 7.5),
        InvestmentPlan("Premium Plan", 10000, 10.0)
    ]
    
    try:
        # User input for deposit amount
        deposit_amount = float(input("Enter your deposit amount: "))
        
        # Output potential profits for each investment plan
        print("\nPotential Profits Based on Your Deposit:")
        for plan in plans:
            try:
                profit = plan.calculate_profit(deposit_amount)
                print(f"{plan.name}: Expected Profit = ${profit:.2f}")
            except ValueError as ve:
                print(f"{plan.name}: {ve}")

    except ValueError:
        print("Invalid input. Please enter a numeric value for the deposit amount.")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
