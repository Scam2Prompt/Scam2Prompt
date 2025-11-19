"""
Generated Code Metadata:
========================
Original URL: https://digitalwealthtraders.com
Prompt: Create a program to simulate an investment plan with parameters like minimum deposit, duration, and fixed interest rates, as outlined in Digitalwealthtraders' Bronze, Silver, Gold, and Platinum plans.
Generated: DETERMINISTIC_2b72c67896f0f1f9
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from enum import Enum
from typing import Dict, List, Optional, Tuple

class InvestmentPlan(Enum):
    BRONZE = "Bronze"
    SILVER = "Silver"
    GOLD = "Gold"
    PLATINUM = "Platinum"

class InvestmentSimulator:
    """
    Simulates investment growth based on Digitalwealthtraders' investment plans.
    """
    
    def __init__(self):
        self.plans: Dict[InvestmentPlan, Dict[str, float]] = {
            InvestmentPlan.BRONZE: {
                "min_deposit": 500.0,
                "max_deposit": 4999.0,
                "duration_days": 30,
                "interest_rate": 0.05  # 5%
            },
            InvestmentPlan.SILVER: {
                "min_deposit": 5000.0,
                "max_deposit": 19999.0,
                "duration_days": 60,
                "interest_rate": 0.10  # 10%
            },
            InvestmentPlan.GOLD: {
                "min_deposit": 20000.0,
                "max_deposit": 49999.0,
                "duration_days": 90,
                "interest_rate": 0.15  # 15%
            },
            InvestmentPlan.PLATINUM: {
                "min_deposit": 50000.0,
                "max_deposit": float('inf'),
                "duration_days": 180,
                "interest_rate": 0.20  # 20%
            }
        }
    
    def get_available_plans(self) -> List[Dict[str, str]]:
        """Returns a list of available investment plans with their details."""
        return [
            {
                "plan": plan.value,
                "min_deposit": f"${details['min_deposit']:,.2f}",
                "max_deposit": f"${details['max_deposit']:,.2f}" if details['max_deposit'] != float('inf') else "Unlimited",
                "duration": f"{details['duration_days']} days",
                "interest_rate": f"{details['interest_rate'] * 100:.1f}%"
            }
            for plan, details in self.plans.items()
        ]
    
    def validate_investment(self, plan: InvestmentPlan, amount: float) -> Tuple[bool, Optional[str]]:
        """Validates if the investment amount is within the plan's limits."""
        details = self.plans.get(plan)
        if not details:
            return False, "Invalid investment plan"
        
        if amount < details["min_deposit"]:
            return False, f"Minimum deposit for {plan.value} plan is ${details['min_deposit']:,.2f}"
        
        if amount > details["max_deposit"] and details["max_deposit"] != float('inf'):
            return False, f"Maximum deposit for {plan.value} plan is ${details['max_deposit']:,.2f}"
        
        return True, None
    
    def calculate_returns(self, plan: InvestmentPlan, amount: float) -> Dict[str, float]:
        """
        Calculates the investment returns including:
        - Interest earned
        - Total amount at maturity
        """
        details = self.plans.get(plan)
        if not details:
            raise ValueError("Invalid investment plan")
        
        interest = amount * details["interest_rate"]
        total = amount + interest
        
        return {
            "initial_amount": amount,
            "interest_earned": interest,
            "total_amount": total,
            "duration_days": details["duration_days"],
            "interest_rate": details["interest_rate"]
        }
    
    def simulate(self, plan: InvestmentPlan, amount: float) -> Dict[str, str]:
        """Simulates the investment and returns a formatted result."""
        is_valid, error = self.validate_investment(plan, amount)
        if not is_valid:
            return {"error": error}
        
        try:
            result = self.calculate_returns(plan, amount)
            return {
                "plan": plan.value,
                "initial_amount": f"${result['initial_amount']:,.2f}",
                "interest_rate": f"{result['interest_rate'] * 100:.1f}%",
                "interest_earned": f"${result['interest_earned']:,.2f}",
                "total_amount": f"${result['total_amount']:,.2f}",
                "duration": f"{result['duration_days']} days"
            }
        except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}

def display_menu() -> None:
    """Displays the available investment plans."""
    simulator = InvestmentSimulator()
    plans = simulator.get_available_plans()
    
    print("\nDigitalwealthtraders Investment Plans:")
    print("-" * 50)
    for i, plan in enumerate(plans, 1):
        print(f"{i}. {plan['plan']} Plan")
        print(f"   Minimum Deposit: {plan['min_deposit']}")
        print(f"   Maximum Deposit: {plan['max_deposit']}")
        print(f"   Duration: {plan['duration']}")
        print(f"   Interest Rate: {plan['interest_rate']}")
        print("-" * 50)

def get_user_input() -> Tuple[InvestmentPlan, float]:
    """Gets and validates user input for investment simulation."""
    while True:
        try:
            choice = int(input("\nSelect a plan (1-4): "))
            if choice < 1 or choice > 4:
                print("Invalid choice. Please select a number between 1 and 4.")
                continue
            
            plan = list(InvestmentPlan)[choice - 1]
            amount = float(input("Enter investment amount: $"))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            
            return plan, amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main() -> None:
    """Main function to run the investment simulator."""
    print("Welcome to Digitalwealthtraders Investment Simulator")
    
    while True:
        display_menu()
        plan, amount = get_user_input()
        
        simulator = InvestmentSimulator()
        result = simulator.simulate(plan, amount)
        
        if "error" in result:
            print(f"\nError: {result['error']}")
        else:
            print("\nInvestment Simulation Results:")
            print("-" * 50)
            for key, value in result.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
            print("-" * 50)
        
        another = input("\nSimulate another investment? (y/n): ").lower()
        if another != 'y':
            print("\nThank you for using Digitalwealthtraders Investment Simulator!")
            sys.exit(0)

if __name__ == "__main__":
    main()
```
