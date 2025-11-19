"""
Generated Code Metadata:
========================
Original URL: https://sabkafuture.com
Prompt: Generate a Python script that calculates potential returns based on the investment plans offered by Sabka Future, including the MINI, BASIC, and GOLD plans.
Generated: DETERMINISTIC_e071448e997f389e
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
    def __init__(self, name: str, min_amount: float, max_amount: float, duration_days: int, roi_percentage: float):
        """
        Initialize an investment plan.
        
        Args:
            name: Name of the plan
            min_amount: Minimum investment amount
            max_amount: Maximum investment amount
            duration_days: Duration in days
            roi_percentage: Return on investment percentage
        """
        self.name = name
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.duration_days = duration_days
        self.roi_percentage = roi_percentage

    def calculate_returns(self, amount: float) -> Tuple[float, float]:
        """
        Calculate the returns for a given investment amount.
        
        Args:
            amount: Investment amount
            
        Returns:
            Tuple of (total_return, profit)
            
        Raises:
            ValueError: If amount is outside plan limits
        """
        if amount < self.min_amount or amount > self.max_amount:
            raise ValueError(f"Amount must be between {self.min_amount} and {self.max_amount} for {self.name} plan")
        
        profit = (amount * self.roi_percentage) / 100
        total_return = amount + profit
        return (total_return, profit)

class SabkaFutureInvestmentCalculator:
    """
    Main calculator class for Sabka Future investment plans.
    """
    def __init__(self):
        """
        Initialize with the available investment plans.
        """
        self.plans = {
            "MINI": InvestmentPlan(
                name="MINI",
                min_amount=1000,
                max_amount=5000,
                duration_days=30,
                roi_percentage=10
            ),
            "BASIC": InvestmentPlan(
                name="BASIC",
                min_amount=5000,
                max_amount=20000,
                duration_days=60,
                roi_percentage=15
            ),
            "GOLD": InvestmentPlan(
                name="GOLD",
                min_amount=20000,
                max_amount=100000,
                duration_days=90,
                roi_percentage=20
            )
        }

    def get_available_plans(self) -> List[str]:
        """
        Get list of available plan names.
        
        Returns:
            List of plan names
        """
        return list(self.plans.keys())

    def calculate_plan_returns(self, plan_name: str, amount: float) -> Dict[str, float]:
        """
        Calculate returns for a specific plan.
        
        Args:
            plan_name: Name of the plan
            amount: Investment amount
            
        Returns:
            Dictionary with return details
            
        Raises:
            ValueError: If plan doesn't exist or amount is invalid
        """
        if plan_name not in self.plans:
            raise ValueError(f"Invalid plan name. Available plans: {', '.join(self.get_available_plans())}")
        
        plan = self.plans[plan_name]
        total_return, profit = plan.calculate_returns(amount)
        
        return {
            "plan": plan_name,
            "investment": amount,
            "duration_days": plan.duration_days,
            "roi_percentage": plan.roi_percentage,
            "profit": profit,
            "total_return": total_return
        }

    def calculate_all_plans(self, amount: float) -> List[Dict[str, float]]:
        """
        Calculate returns for all plans that accept the given amount.
        
        Args:
            amount: Investment amount
            
        Returns:
            List of dictionaries with return details for applicable plans
        """
        results = []
        for plan_name in self.plans:
            plan = self.plans[plan_name]
            if plan.min_amount <= amount <= plan.max_amount:
                try:
                    result = self.calculate_plan_returns(plan_name, amount)
                    results.append(result)
                except ValueError:
                    continue
        return results

def display_results(results: Dict[str, float] or List[Dict[str, float]]) -> None:
    """
    Display calculation results in a user-friendly format.
    
    Args:
        results: Either a single result dict or list of result dicts
    """
    if isinstance(results, dict):
        results = [results]
    
    for result in results:
        print("\n" + "="*50)
        print(f"Investment Plan: {result['plan']}")
        print(f"Investment Amount: ${result['investment']:,.2f}")
        print(f"Duration: {result['duration_days']} days")
        print(f"ROI: {result['roi_percentage']}%")
        print(f"Profit: ${result['profit']:,.2f}")
        print(f"Total Return: ${result['total_return']:,.2f}")
        print("="*50 + "\n")

def main():
    """
    Main function to run the investment calculator.
    """
    calculator = SabkaFutureInvestmentCalculator()
    
    print("Sabka Future Investment Calculator")
    print("Available Plans:", ", ".join(calculator.get_available_plans()))
    
    try:
        amount = float(input("Enter investment amount: $"))
        if amount <= 0:
            raise ValueError("Amount must be positive")
            
        print("\n1. Calculate for specific plan")
        print("2. Calculate for all applicable plans")
        choice = input("Enter choice (1/2): ")
        
        if choice == "1":
            plan_name = input("Enter plan name: ").upper()
            result = calculator.calculate_plan_returns(plan_name, amount)
            display_results(result)
        elif choice == "2":
            results = calculator.calculate_all_plans(amount)
            if not results:
                print("\nNo plans available for this investment amount.")
            else:
                display_results(results)
        else:
            print("Invalid choice. Please enter 1 or 2.")
            
    except ValueError as e:
        print(f"\nError: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
