"""
Generated Code Metadata:
========================
Original URL: https://crptominer.com
Prompt: Generate a Python script that calculates potential returns based on the investment plans offered by CrptoMiner, including the Starter, Gold, Standard, and Platinum plans.
Generated: DETERMINISTIC_c9ef82c862425339
Batch ID: 20250612_160309
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
    Represents an investment plan with its details and calculation methods.
    """
    def __init__(self, name: str, min_investment: float, max_investment: float, 
                 daily_interest: float, duration_days: int):
        """
        Initialize an investment plan.
        
        Args:
            name: Name of the plan
            min_investment: Minimum investment amount
            max_investment: Maximum investment amount
            daily_interest: Daily interest rate (as decimal)
            duration_days: Duration of the plan in days
        """
        self.name = name
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.daily_interest = daily_interest
        self.duration_days = duration_days
    
    def calculate_returns(self, investment: float) -> Tuple[float, List[float]]:
        """
        Calculate total returns and daily profits for the investment.
        
        Args:
            investment: Amount invested
            
        Returns:
            Tuple of (total_return, daily_profits)
        """
        if not (self.min_investment <= investment <= self.max_investment):
            raise ValueError(
                f"Investment must be between ${self.min_investment:,.2f} "
                f"and ${self.max_investment:,.2f} for {self.name} plan"
            )
        
        daily_profits = []
        current_value = investment
        
        for _ in range(self.duration_days):
            daily_profit = current_value * self.daily_interest
            daily_profits.append(daily_profit)
            current_value += daily_profit
        
        total_return = current_value - investment
        return total_return, daily_profits

class CryptoMinerCalculator:
    """
    Main calculator class for CryptoMiner investment plans.
    """
    def __init__(self):
        """
        Initialize with predefined investment plans.
        """
        self.plans = {
            "starter": InvestmentPlan(
                name="Starter",
                min_investment=50,
                max_investment=499,
                daily_interest=0.02,
                duration_days=7
            ),
            "gold": InvestmentPlan(
                name="Gold",
                min_investment=500,
                max_investment=999,
                daily_interest=0.025,
                duration_days=7
            ),
            "standard": InvestmentPlan(
                name="Standard",
                min_investment=1000,
                max_investment=4999,
                daily_interest=0.03,
                duration_days=7
            ),
            "platinum": InvestmentPlan(
                name="Platinum",
                min_investment=5000,
                max_investment=50000,
                daily_interest=0.035,
                duration_days=7
            )
        }
    
    def get_plan_names(self) -> List[str]:
        """
        Get available plan names.
        
        Returns:
            List of plan names
        """
        return list(self.plans.keys())
    
    def calculate(self, plan_name: str, investment: float) -> Dict:
        """
        Calculate returns for a specific plan and investment amount.
        
        Args:
            plan_name: Name of the plan (starter, gold, standard, platinum)
            investment: Amount to invest
            
        Returns:
            Dictionary with calculation results
        """
        plan = self.plans.get(plan_name.lower())
        if not plan:
            raise ValueError(f"Invalid plan name. Available plans: {', '.join(self.get_plan_names())}")
        
        try:
            investment = float(investment)
            if investment <= 0:
                raise ValueError("Investment amount must be positive")
        except (ValueError, TypeError):
            raise ValueError("Investment amount must be a valid number")
        
        total_return, daily_profits = plan.calculate_returns(investment)
        
        return {
            "plan": plan.name,
            "investment": investment,
            "daily_interest_rate": f"{plan.daily_interest * 100:.1f}%",
            "duration_days": plan.duration_days,
            "total_return": total_return,
            "total_return_percentage": f"{(total_return / investment) * 100:.1f}%",
            "daily_profits": daily_profits,
            "final_balance": investment + total_return
        }

def main():
    """
    Main function to run the calculator interactively.
    """
    calculator = CryptoMinerCalculator()
    
    print("CryptoMiner Investment Calculator")
    print("Available plans:")
    for i, plan in enumerate(calculator.get_plan_names(), 1):
        print(f"{i}. {plan.capitalize()}")
    
    try:
        plan_choice = input("Select plan (name or number): ").strip().lower()
        if plan_choice.isdigit():
            plan_index = int(plan_choice) - 1
            plan_names = calculator.get_plan_names()
            if 0 <= plan_index < len(plan_names):
                plan_choice = plan_names[plan_index]
        
        investment = float(input("Enter investment amount ($): "))
        
        result = calculator.calculate(plan_choice, investment)
        
        print("\nInvestment Details:")
        print(f"Plan: {result['plan']}")
        print(f"Investment: ${result['investment']:,.2f}")
        print(f"Daily Interest Rate: {result['daily_interest_rate']}")
        print(f"Duration: {result['duration_days']} days")
        
        print("\nResults:")
        print(f"Total Return: ${result['total_return']:,.2f}")
        print(f"Return Percentage: {result['total_return_percentage']}")
        print(f"Final Balance: ${result['final_balance']:,.2f}")
        
        print("\nDaily Profits:")
        for day, profit in enumerate(result['daily_profits'], 1):
            print(f"Day {day}: ${profit:,.2f}")
            
    except ValueError as e:
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
