"""
Generated Code Metadata:
========================
Original URL: https://rapidcointrades.org
Prompt: Generate a Python script to calculate potential profits based on the investment plans offered by RapidCoinTrades, including the Starter Plan (6%), Basic Plan (10%), Golden Plan (25%), and VIP Plan (50%).
Generated: DETERMINISTIC_6db9358c2c6e79bc
Batch ID: 20250612_160440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import Dict, List, Optional

class InvestmentPlan:
    """Represents an investment plan with its details."""
    
    def __init__(self, name: str, daily_interest: float, min_investment: float, max_investment: float):
        """
        Initialize an investment plan.
        
        Args:
            name: Name of the plan.
            daily_interest: Daily interest rate (in percentage).
            min_investment: Minimum investment amount.
            max_investment: Maximum investment amount.
        """
        self.name = name
        self.daily_interest = daily_interest
        self.min_investment = min_investment
        self.max_investment = max_investment

    def calculate_profit(self, amount: float, days: int) -> float:
        """
        Calculate the profit for a given investment amount and duration.
        
        Args:
            amount: Investment amount.
            days: Number of days to invest.
            
        Returns:
            Total profit earned.
            
        Raises:
            ValueError: If investment amount is outside plan limits.
        """
        if amount < self.min_investment or amount > self.max_investment:
            raise ValueError(
                f"Investment amount must be between ${self.min_investment:,.2f} "
                f"and ${self.max_investment:,.2f} for {self.name} plan."
            )
        return amount * (self.daily_interest / 100) * days

class RapidCoinTradesCalculator:
    """Calculator for RapidCoinTrades investment plans."""
    
    def __init__(self):
        """Initialize with predefined investment plans."""
        self.plans = {
            "starter": InvestmentPlan("Starter Plan", 6, 100, 1000),
            "basic": InvestmentPlan("Basic Plan", 10, 1000, 5000),
            "golden": InvestmentPlan("Golden Plan", 25, 5000, 15000),
            "vip": InvestmentPlan("VIP Plan", 50, 15000, 50000),
        }

    def get_plan_names(self) -> List[str]:
        """Return a list of available plan names."""
        return list(self.plans.keys())

    def calculate(
        self, plan_name: str, amount: float, days: int
    ) -> Dict[str, Optional[float]]:
        """
        Calculate profit for a given plan, amount, and duration.
        
        Args:
            plan_name: Name of the investment plan.
            amount: Investment amount.
            days: Number of days to invest.
            
        Returns:
            Dictionary containing 'profit' (float) if successful, or 'error' (str) if failed.
        """
        result = {"profit": None, "error": None}
        
        try:
            plan = self.plans.get(plan_name.lower())
            if not plan:
                raise ValueError(f"Invalid plan name. Available plans: {', '.join(self.get_plan_names())}")
            
            if days <= 0:
                raise ValueError("Investment duration must be at least 1 day.")
            
            profit = plan.calculate_profit(amount, days)
            result["profit"] = profit
            
        except ValueError as e:
            result["error"] = str(e)
            
        return result

def main():
    """Main function to interact with the user."""
    calculator = RapidCoinTradesCalculator()
    
    print("RapidCoinTrades Investment Profit Calculator")
    print("Available plans:")
    for name, plan in calculator.plans.items():
        print(f"- {plan.name}: {plan.daily_interest}% daily, "
              f"Min: ${plan.min_investment:,.2f}, Max: ${plan.max_investment:,.2f}")
    
    try:
        plan_name = input("\nEnter plan name (starter/basic/golden/vip): ").strip().lower()
        amount = float(input("Enter investment amount ($): "))
        days = int(input("Enter investment duration (days): "))
        
        result = calculator.calculate(plan_name, amount, days)
        
        if result["error"]:
            print(f"\nError: {result['error']}")
        else:
            print(f"\nExpected profit after {days} days: ${result['profit']:,.2f}")
            print(f"Total return: ${amount + result['profit']:,.2f}")
            
    except ValueError:
        print("\nError: Invalid input. Please enter numeric values for amount and days.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
