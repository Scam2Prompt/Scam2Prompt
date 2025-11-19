"""
Generated Code Metadata:
========================
Original URL: https://realtechearners.com
Prompt: Write a Python script to simulate the investment plans offered by realtechearners.com, including calculations for returns based on the specified percentages and durations (e.g., 30% after 24 hours, 100% after 48 hours).
Generated: DETERMINISTIC_4603ef6c8dfaf912
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from datetime import datetime, timedelta

class InvestmentPlan:
    """
    Represents an investment plan with its name, duration, and return percentage.
    """
    def __init__(self, name: str, duration_hours: int, return_percentage: float):
        self.name = name
        self.duration_hours = duration_hours
        self.return_percentage = return_percentage

    def calculate_return(self, amount: float) -> float:
        """
        Calculate the return on investment based on the plan's percentage.
        
        Args:
            amount: The initial investment amount
            
        Returns:
            The total return amount
        """
        return amount * (1 + self.return_percentage / 100)

    def get_maturity_date(self, investment_date: datetime) -> datetime:
        """
        Calculate the maturity date based on investment date and plan duration.
        
        Args:
            investment_date: The date when the investment was made
            
        Returns:
            The maturity date
        """
        return investment_date + timedelta(hours=self.duration_hours)

class InvestmentSimulator:
    """
    Simulates investment plans and calculates returns.
    """
    def __init__(self):
        self.plans = [
            InvestmentPlan("24-Hour Plan", 24, 30.0),
            InvestmentPlan("48-Hour Plan", 48, 100.0),
            InvestmentPlan("7-Day Plan", 168, 200.0)
        ]
    
    def display_plans(self):
        """Display available investment plans."""
        print("\nAvailable Investment Plans:")
        for i, plan in enumerate(self.plans, 1):
            print(f"{i}. {plan.name}: {plan.return_percentage}% after {plan.duration_hours//24} days")

    def get_valid_input(self, prompt: str, input_type: type, min_val=None, max_val=None):
        """
        Get validated user input.
        
        Args:
            prompt: The input prompt
            input_type: Expected data type
            min_val: Minimum allowed value
            max_val: Maximum allowed value
            
        Returns:
            Validated user input
        """
        while True:
            try:
                value = input_type(input(prompt))
                if min_val is not None and value < min_val:
                    print(f"Value must be at least {min_val}")
                    continue
                if max_val is not None and value > max_val:
                    print(f"Value must be at most {max_val}")
                    continue
                return value
            except ValueError:
                print("Invalid input. Please try again.")

    def simulate_investment(self):
        """Run the investment simulation."""
        print("Welcome to RealTechEarners Investment Simulator")
        
        while True:
            self.display_plans()
            
            try:
                plan_choice = self.get_valid_input(
                    "\nSelect a plan (1-3) or 0 to exit: ",
                    int, 0, len(self.plans)
                )
                
                if plan_choice == 0:
                    print("Exiting simulator. Goodbye!")
                    sys.exit(0)
                
                selected_plan = self.plans[plan_choice - 1]
                amount = self.get_valid_input(
                    "Enter investment amount ($10-$10000): $",
                    float, 10, 10000
                )
                
                investment_date = datetime.now()
                maturity_date = selected_plan.get_maturity_date(investment_date)
                return_amount = selected_plan.calculate_return(amount)
                
                print("\nInvestment Details:")
                print(f"Plan: {selected_plan.name}")
                print(f"Investment Amount: ${amount:.2f}")
                print(f"Investment Date: {investment_date.strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"Maturity Date: {maturity_date.strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"Total Return: ${return_amount:.2f}")
                print(f"Profit: ${(return_amount - amount):.2f}")
                
                another = input("\nSimulate another investment? (y/n): ").lower()
                if another != 'y':
                    print("Thank you for using the simulator. Goodbye!")
                    break
                    
            except IndexError:
                print("Invalid plan selection. Please try again.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                print("Please try again.")

if __name__ == "__main__":
    simulator = InvestmentSimulator()
    simulator.simulate_investment()
```
