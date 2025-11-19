"""
Generated Code Metadata:
========================
Original URL: https://apexdiginvcompany.com
Prompt: Generate a Python script that calculates potential profits based on the investment plans offered by Apex Digital Limited, including Beginner, Standard, Gold, Ambassador, and VIP plans.
Generated: DETERMINISTIC_8c9628ea73b55b3e
Batch ID: 20250612_160124
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import Dict, List, Tuple

class InvestmentPlan:
    """
    Represents an investment plan with its details and profit calculation logic.
    """
    def __init__(self, name: str, min_amount: float, max_amount: float, duration_days: int, profit_rate: float):
        """
        Initialize an investment plan.
        
        Args:
            name: Name of the plan
            min_amount: Minimum investment amount
            max_amount: Maximum investment amount
            duration_days: Duration in days
            profit_rate: Daily profit rate (as decimal)
        """
        self.name = name
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.duration_days = duration_days
        self.profit_rate = profit_rate

    def calculate_profit(self, amount: float) -> Tuple[float, float]:
        """
        Calculate total profit and return on investment.
        
        Args:
            amount: Investment amount
            
        Returns:
            Tuple of (total_profit, roi_percentage)
            
        Raises:
            ValueError: If amount is outside plan limits
        """
        if not (self.min_amount <= amount <= self.max_amount):
            raise ValueError(f"Amount must be between ${self.min_amount:,.2f} and ${self.max_amount:,.2f} for {self.name} plan")
        
        total_profit = amount * self.profit_rate * self.duration_days
        roi_percentage = (total_profit / amount) * 100
        return total_profit, roi_percentage

class ApexDigitalInvestmentCalculator:
    """
    Calculator for Apex Digital Limited investment plans.
    """
    def __init__(self):
        self.plans = {
            "Beginner": InvestmentPlan("Beginner", 50, 499, 7, 0.05),
            "Standard": InvestmentPlan("Standard", 500, 4999, 14, 0.07),
            "Gold": InvestmentPlan("Gold", 5000, 19999, 21, 0.10),
            "Ambassador": InvestmentPlan("Ambassador", 20000, 49999, 28, 0.15),
            "VIP": InvestmentPlan("VIP", 50000, 1000000, 30, 0.20)
        }

    def get_available_plans(self) -> List[str]:
        """Return list of available plan names."""
        return list(self.plans.keys())

    def calculate_profits(self, plan_name: str, amount: float) -> Dict[str, float]:
        """
        Calculate investment profits for a given plan and amount.
        
        Args:
            plan_name: Name of the investment plan
            amount: Investment amount
            
        Returns:
            Dictionary containing profit details
            
        Raises:
            ValueError: If plan doesn't exist or amount is invalid
        """
        if plan_name not in self.plans:
            raise ValueError(f"Invalid plan name. Available plans: {', '.join(self.get_available_plans())}")
        
        if amount <= 0:
            raise ValueError("Investment amount must be positive")
            
        plan = self.plans[plan_name]
        total_profit, roi = plan.calculate_profit(amount)
        
        return {
            "plan": plan_name,
            "investment": amount,
            "duration_days": plan.duration_days,
            "total_profit": total_profit,
            "roi_percentage": roi,
            "total_return": amount + total_profit
        }

    def display_profit_report(self, plan_name: str, amount: float):
        """
        Display a formatted profit report for the investment.
        
        Args:
            plan_name: Name of the investment plan
            amount: Investment amount
        """
        try:
            result = self.calculate_profits(plan_name, amount)
            print("\n" + "="*50)
            print(f"Investment Plan: {result['plan']}")
            print(f"Investment Amount: ${result['investment']:,.2f}")
            print(f"Duration: {result['duration_days']} days")
            print("-"*50)
            print(f"Total Profit: ${result['total_profit']:,.2f}")
            print(f"ROI: {result['roi_percentage']:.2f}%")
            print(f"Total Return: ${result['total_return']:,.2f}")
            print("="*50 + "\n")
        except ValueError as e:
            print(f"\nError: {str(e)}\n", file=sys.stderr)

def main():
    """Main function to run the investment calculator."""
    calculator = ApexDigitalInvestmentCalculator()
    
    print("Apex Digital Limited - Investment Calculator")
    print("Available Plans:")
    for i, plan in enumerate(calculator.get_available_plans(), 1):
        print(f"{i}. {plan}")
    
    try:
        plan_choice = int(input("\nSelect plan (1-5): "))
        if not 1 <= plan_choice <= 5:
            raise ValueError("Please enter a number between 1 and 5")
            
        plan_name = calculator.get_available_plans()[plan_choice - 1]
        amount = float(input("Enter investment amount: $"))
        
        calculator.display_profit_report(plan_name, amount)
    except ValueError as e:
        print(f"\nError: {str(e)}\n", file=sys.stderr)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")

if __name__ == "__main__":
    main()
```
