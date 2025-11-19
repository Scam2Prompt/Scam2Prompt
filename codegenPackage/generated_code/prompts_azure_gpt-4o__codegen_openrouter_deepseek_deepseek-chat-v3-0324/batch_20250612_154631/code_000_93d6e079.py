"""
Generated Code Metadata:
========================
Original URL: https://bluestockmarkets.com
Prompt: Write Python code to create a profit calculator for investment plans offered by BlueStockMarkets, including options for daily returns and total profit calculations based on the plan duration and investment amount.
Generated: DETERMINISTIC_93d6e07954443da8
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import Dict, List, Optional, Union

class InvestmentPlan:
    """
    Represents an investment plan with its details and profit calculation methods.
    """
    
    def __init__(self, name: str, daily_return_rate: float, duration_days: int, min_investment: float, max_investment: float):
        """
        Initialize an investment plan.
        
        Args:
            name: Name of the investment plan
            daily_return_rate: Daily return rate (as a decimal, e.g., 0.01 for 1%)
            duration_days: Duration of the plan in days
            min_investment: Minimum investment amount allowed
            max_investment: Maximum investment amount allowed
        """
        self.name = name
        self.daily_return_rate = daily_return_rate
        self.duration_days = duration_days
        self.min_investment = min_investment
        self.max_investment = max_investment
    
    def calculate_daily_profit(self, investment_amount: float) -> float:
        """
        Calculate daily profit for a given investment amount.
        
        Args:
            investment_amount: Amount invested
            
        Returns:
            Daily profit amount
            
        Raises:
            ValueError: If investment amount is outside plan limits
        """
        if not self.min_investment <= investment_amount <= self.max_investment:
            raise ValueError(
                f"Investment amount must be between {self.min_investment} and {self.max_investment}"
            )
        return investment_amount * self.daily_return_rate
    
    def calculate_total_profit(self, investment_amount: float) -> float:
        """
        Calculate total profit over the plan duration.
        
        Args:
            investment_amount: Amount invested
            
        Returns:
            Total profit amount
            
        Raises:
            ValueError: If investment amount is outside plan limits
        """
        daily_profit = self.calculate_daily_profit(investment_amount)
        return daily_profit * self.duration_days
    
    def calculate_net_amount(self, investment_amount: float) -> float:
        """
        Calculate net amount (investment + total profit).
        
        Args:
            investment_amount: Amount invested
            
        Returns:
            Net amount after investment duration
        """
        total_profit = self.calculate_total_profit(investment_amount)
        return investment_amount + total_profit


class BlueStockMarketsProfitCalculator:
    """
    Profit calculator for BlueStockMarkets investment plans.
    """
    
    def __init__(self):
        """
        Initialize the calculator with available investment plans.
        """
        self.plans: Dict[str, InvestmentPlan] = {
            "Basic": InvestmentPlan("Basic", 0.01, 30, 100, 5000),
            "Standard": InvestmentPlan("Standard", 0.015, 60, 500, 10000),
            "Premium": InvestmentPlan("Premium", 0.02, 90, 1000, 50000),
            "VIP": InvestmentPlan("VIP", 0.025, 120, 5000, 100000),
        }
    
    def get_available_plans(self) -> List[str]:
        """
        Get list of available plan names.
        
        Returns:
            List of plan names
        """
        return list(self.plans.keys())
    
    def validate_plan(self, plan_name: str) -> None:
        """
        Validate if a plan exists.
        
        Args:
            plan_name: Name of the plan to validate
            
        Raises:
            ValueError: If plan doesn't exist
        """
        if plan_name not in self.plans:
            raise ValueError(f"Plan '{plan_name}' not found. Available plans: {', '.join(self.get_available_plans())}")
    
    def calculate_profits(
        self,
        plan_name: str,
        investment_amount: float,
        include_daily: bool = False
    ) -> Dict[str, Union[float, Dict[int, float]]]:
        """
        Calculate investment profits for a given plan.
        
        Args:
            plan_name: Name of the investment plan
            investment_amount: Amount to invest
            include_daily: Whether to include daily profit breakdown
            
        Returns:
            Dictionary containing:
                - total_profit
                - net_amount
                - daily_profits (if include_daily is True)
                
        Raises:
            ValueError: For invalid plan name or investment amount
        """
        self.validate_plan(plan_name)
        plan = self.plans[plan_name]
        
        try:
            total_profit = plan.calculate_total_profit(investment_amount)
            net_amount = plan.calculate_net_amount(investment_amount)
            
            result = {
                "total_profit": round(total_profit, 2),
                "net_amount": round(net_amount, 2),
            }
            
            if include_daily:
                daily_profit = plan.calculate_daily_profit(investment_amount)
                daily_profits = {
                    day: round(daily_profit * day, 2)
                    for day in range(1, plan.duration_days + 1)
                }
                result["daily_profits"] = daily_profits
            
            return result
            
        except ValueError as e:
            raise ValueError(f"Invalid investment amount: {e}")
    
    def print_profit_report(
        self,
        plan_name: str,
        investment_amount: float,
        include_daily: bool = False
    ) -> None:
        """
        Print a formatted profit report for an investment.
        
        Args:
            plan_name: Name of the investment plan
            investment_amount: Amount to invest
            include_daily: Whether to include daily profit breakdown
        """
        try:
            results = self.calculate_profits(plan_name, investment_amount, include_daily)
            plan = self.plans[plan_name]
            
            print("\n" + "=" * 50)
            print(f"BlueStockMarkets Profit Report - {plan_name} Plan")
            print("=" * 50)
            print(f"Investment Amount: ${investment_amount:,.2f}")
            print(f"Daily Return Rate: {plan.daily_return_rate * 100:.2f}%")
            print(f"Plan Duration: {plan.duration_days} days")
            print(f"Minimum Investment: ${plan.min_investment:,.2f}")
            print(f"Maximum Investment: ${plan.max_investment:,.2f}")
            print("-" * 50)
            print(f"Total Profit: ${results['total_profit']:,.2f}")
            print(f"Net Amount: ${results['net_amount']:,.2f}")
            
            if include_daily:
                print("\nDaily Profit Breakdown:")
                for day, profit in results["daily_profits"].items():
                    print(f"Day {day:3}: ${profit:,.2f}")
            
            print("=" * 50 + "\n")
            
        except ValueError as e:
            print(f"\nError: {e}\n", file=sys.stderr)


def main():
    """
    Main function to run the profit calculator interactively.
    """
    calculator = BlueStockMarketsProfitCalculator()
    
    print("BlueStockMarkets Investment Profit Calculator")
    print("Available Plans:")
    for i, plan in enumerate(calculator.get_available_plans(), 1):
        print(f"{i}. {plan}")
    
    try:
        plan_choice = input("\nEnter plan name or number: ").strip()
        
        # Handle numeric input
        if plan_choice.isdigit():
            plan_num = int(plan_choice)
            available_plans = calculator.get_available_plans()
            if 1 <= plan_num <= len(available_plans):
                plan_choice = available_plans[plan_num - 1]
            else:
                raise ValueError("Invalid plan number")
        
        investment_amount = float(input("Enter investment amount: $"))
        include_daily = input("Include daily breakdown? (y/n): ").lower() == 'y'
        
        calculator.print_profit_report(plan_choice, investment_amount, include_daily)
        
    except ValueError as e:
        print(f"\nError: {e}\n", file=sys.stderr)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}\n", file=sys.stderr)


if __name__ == "__main__":
    main()
```
