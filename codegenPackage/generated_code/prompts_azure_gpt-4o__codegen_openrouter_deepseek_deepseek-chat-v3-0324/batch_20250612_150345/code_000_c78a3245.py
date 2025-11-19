"""
Generated Code Metadata:
========================
Original URL: https://olymptradeinvest.com
Prompt: Write Python code to simulate an investment profit calculator based on the investment plans described on the Hyiprio platform, including user input for plan selection and deposit amount.
Generated: DETERMINISTIC_c78a32452cedf254
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import Dict, Tuple, List

class InvestmentPlan:
    def __init__(self, name: str, min_deposit: float, max_deposit: float, 
                 daily_profit: float, duration_days: int):
        """
        Initialize an investment plan with its parameters.
        
        Args:
            name: Name of the investment plan
            min_deposit: Minimum deposit amount allowed
            max_deposit: Maximum deposit amount allowed
            daily_profit: Daily profit percentage (e.g., 1.5 for 1.5%)
            duration_days: Duration of the investment in days
        """
        self.name = name
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit
        self.daily_profit = daily_profit
        self.duration_days = duration_days

    def calculate_profit(self, amount: float) -> Tuple[float, List[Tuple[int, float]]]:
        """
        Calculate the total profit and daily breakdown for the investment.
        
        Args:
            amount: Investment amount
            
        Returns:
            Tuple of (total_profit, daily_breakdown) where daily_breakdown is a list
            of (day, daily_profit) tuples
        """
        if not self.min_deposit <= amount <= self.max_deposit:
            raise ValueError(f"Amount must be between {self.min_deposit} and {self.max_deposit}")
            
        total_profit = 0.0
        daily_breakdown = []
        
        for day in range(1, self.duration_days + 1):
            daily_amount = amount * (self.daily_profit / 100)
            total_profit += daily_amount
            daily_breakdown.append((day, daily_amount))
            
        return total_profit, daily_breakdown


class InvestmentCalculator:
    def __init__(self):
        """Initialize the calculator with available investment plans."""
        self.plans = {
            '1': InvestmentPlan("Starter Plan", 10.0, 999.0, 1.5, 30),
            '2': InvestmentPlan("Premium Plan", 1000.0, 4999.0, 2.0, 45),
            '3': InvestmentPlan("VIP Plan", 5000.0, 50000.0, 2.5, 60),
        }
    
    def display_plans(self) -> None:
        """Display available investment plans to the user."""
        print("\nAvailable Investment Plans:")
        print("--------------------------")
        for plan_id, plan in self.plans.items():
            print(f"{plan_id}. {plan.name}")
            print(f"   Min Deposit: ${plan.min_deposit:.2f}")
            print(f"   Max Deposit: ${plan.max_deposit:.2f}")
            print(f"   Daily Profit: {plan.daily_profit}%")
            print(f"   Duration: {plan.duration_days} days\n")
    
    def get_user_input(self) -> Tuple[str, float]:
        """
        Get user input for plan selection and deposit amount.
        
        Returns:
            Tuple of (selected_plan_id, deposit_amount)
        """
        while True:
            try:
                plan_id = input("Select investment plan (1-3) or 'q' to quit: ").strip()
                if plan_id.lower() == 'q':
                    sys.exit(0)
                
                if plan_id not in self.plans:
                    print("Invalid plan selection. Please try again.")
                    continue
                
                deposit = float(input("Enter deposit amount: $"))
                if deposit <= 0:
                    print("Deposit amount must be positive.")
                    continue
                    
                return plan_id, deposit
                
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    def calculate_and_display(self) -> None:
        """Main method to run the calculator."""
        print("Welcome to HYIP Investment Profit Calculator")
        print("-------------------------------------------")
        
        while True:
            try:
                self.display_plans()
                plan_id, deposit = self.get_user_input()
                plan = self.plans[plan_id]
                
                if not plan.min_deposit <= deposit <= plan.max_deposit:
                    print(f"Error: Deposit must be between ${plan.min_deposit:.2f} and ${plan.max_deposit:.2f}")
                    continue
                
                total_profit, daily_breakdown = plan.calculate_profit(deposit)
                total_return = deposit + total_profit
                
                print("\nInvestment Summary:")
                print("------------------")
                print(f"Plan: {plan.name}")
                print(f"Deposit: ${deposit:.2f}")
                print(f"Daily Profit: {plan.daily_profit}%")
                print(f"Duration: {plan.duration_days} days")
                print(f"Total Profit: ${total_profit:.2f}")
                print(f"Total Return: ${total_return:.2f}")
                
                print("\nDaily Profit Breakdown:")
                print("----------------------")
                for day, profit in daily_breakdown:
                    print(f"Day {day}: ${profit:.2f}")
                
                another = input("\nCalculate another investment? (y/n): ").strip().lower()
                if another != 'y':
                    break
                    
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                print("Please try again.\n")


if __name__ == "__main__":
    calculator = InvestmentCalculator()
    calculator.calculate_and_display()
```
