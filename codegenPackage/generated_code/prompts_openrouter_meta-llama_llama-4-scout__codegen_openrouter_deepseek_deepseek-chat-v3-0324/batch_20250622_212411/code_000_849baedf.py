"""
Generated Code Metadata:
========================
Original URL: https://dclinvest-sa.com
Prompt: Write a Python code to create a simple investment plan for a client using DCL Invest's wealth management services, considering factors such as risk tolerance and financial goals.
Generated: DETERMINISTIC_849baedf8f3fd181
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Dict, List, Optional, Tuple

class RiskTolerance(Enum):
    """Enum representing client's risk tolerance levels."""
    CONSERVATIVE = 1
    MODERATE = 2
    AGGRESSIVE = 3

class FinancialGoal(Enum):
    """Enum representing common financial goals."""
    RETIREMENT = 1
    EDUCATION = 2
    WEALTH_ACCUMULATION = 3
    HOME_PURCHASE = 4
    OTHER = 5

class InvestmentPlan:
    """Class representing an investment plan for a client."""
    
    def __init__(self, client_name: str, age: int, risk_tolerance: RiskTolerance, 
                 financial_goal: FinancialGoal, initial_investment: float, 
                 monthly_contribution: float, investment_horizon: int):
        """
        Initialize an investment plan.
        
        Args:
            client_name: Name of the client
            age: Current age of the client
            risk_tolerance: Risk tolerance level (CONSERVATIVE, MODERATE, AGGRESSIVE)
            financial_goal: Primary financial goal
            initial_investment: Initial investment amount
            monthly_contribution: Monthly contribution amount
            investment_horizon: Investment duration in years
        """
        self.client_name = client_name
        self.age = age
        self.risk_tolerance = risk_tolerance
        self.financial_goal = financial_goal
        self.initial_investment = initial_investment
        self.monthly_contribution = monthly_contribution
        self.investment_horizon = investment_horizon
        self.portfolio = self._create_portfolio()
        
    def _create_portfolio(self) -> Dict[str, float]:
        """Create a portfolio allocation based on risk tolerance and financial goal."""
        base_allocation = {
            'stocks': 0.0,
            'bonds': 0.0,
            'real_estate': 0.0,
            'commodities': 0.0,
            'cash': 0.0
        }
        
        if self.risk_tolerance == RiskTolerance.CONSERVATIVE:
            base_allocation.update({
                'stocks': 0.3,
                'bonds': 0.5,
                'real_estate': 0.1,
                'cash': 0.1
            })
        elif self.risk_tolerance == RiskTolerance.MODERATE:
            base_allocation.update({
                'stocks': 0.6,
                'bonds': 0.3,
                'real_estate': 0.1
            })
        elif self.risk_tolerance == RiskTolerance.AGGRESSIVE:
            base_allocation.update({
                'stocks': 0.8,
                'bonds': 0.1,
                'commodities': 0.1
            })
        
        return base_allocation
    
    def calculate_projection(self, annual_return_rate: float = 0.07) -> Tuple[List[float], float]:
        """
        Calculate investment projection over the horizon.
        
        Args:
            annual_return_rate: Expected annual return rate (default 7%)
            
        Returns:
            Tuple containing:
                - List of yearly balances
                - Total contributions
        """
        if annual_return_rate <= 0:
            raise ValueError("Annual return rate must be positive")
            
        monthly_rate = (1 + annual_return_rate) ** (1/12) - 1
        balance = self.initial_investment
        yearly_balances = [balance]
        total_contributions = self.initial_investment
        
        for year in range(1, self.investment_horizon + 1):
            for month in range(12):
                balance *= (1 + monthly_rate)
                balance += self.monthly_contribution
                total_contributions += self.monthly_contribution
            yearly_balances.append(balance)
            
        return yearly_balances, total_contributions
    
    def to_json(self) -> str:
        """Convert the investment plan to JSON format."""
        plan_dict = {
            'client_name': self.client_name,
            'age': self.age,
            'risk_tolerance': self.risk_tolerance.name,
            'financial_goal': self.financial_goal.name,
            'initial_investment': self.initial_investment,
            'monthly_contribution': self.monthly_contribution,
            'investment_horizon': self.investment_horizon,
            'portfolio_allocation': self.portfolio
        }
        return json.dumps(plan_dict, indent=2)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'InvestmentPlan':
        """Create an InvestmentPlan from JSON string."""
        data = json.loads(json_str)
        return cls(
            client_name=data['client_name'],
            age=data['age'],
            risk_tolerance=RiskTolerance[data['risk_tolerance']],
            financial_goal=FinancialGoal[data['financial_goal']],
            initial_investment=data['initial_investment'],
            monthly_contribution=data['monthly_contribution'],
            investment_horizon=data['investment_horizon']
        )

def create_investment_plan() -> InvestmentPlan:
    """Interactive function to create an investment plan."""
    print("Welcome to DCL Invest Wealth Management")
    print("Let's create your personalized investment plan\n")
    
    try:
        client_name = input("Enter your name: ").strip()
        age = int(input("Enter your age: "))
        
        print("\nSelect your risk tolerance:")
        for i, level in enumerate(RiskTolerance, 1):
            print(f"{i}. {level.name}")
        risk_choice = int(input("Enter choice (1-3): "))
        risk_tolerance = list(RiskTolerance)[risk_choice - 1]
        
        print("\nSelect your primary financial goal:")
        for i, goal in enumerate(FinancialGoal, 1):
            print(f"{i}. {goal.name.replace('_', ' ').title()}")
        goal_choice = int(input("Enter choice (1-5): "))
        financial_goal = list(FinancialGoal)[goal_choice - 1]
        
        initial_investment = float(input("\nEnter initial investment amount: $"))
        monthly_contribution = float(input("Enter monthly contribution amount: $"))
        investment_horizon = int(input("Enter investment horizon in years: "))
        
        if any(val < 0 for val in [age, initial_investment, monthly_contribution, investment_horizon]):
            raise ValueError("Negative values are not allowed")
            
        plan = InvestmentPlan(
            client_name=client_name,
            age=age,
            risk_tolerance=risk_tolerance,
            financial_goal=financial_goal,
            initial_investment=initial_investment,
            monthly_contribution=monthly_contribution,
            investment_horizon=investment_horizon
        )
        
        print("\nInvestment plan created successfully!")
        return plan
        
    except ValueError as e:
        print(f"\nError: {str(e)}")
        print("Please try again with valid inputs.")
        return None
    except (IndexError, KeyError):
        print("\nError: Invalid selection. Please try again.")
        return None

if __name__ == "__main__":
    plan = create_investment_plan()
    if plan:
        print("\nYour Portfolio Allocation:")
        for asset, allocation in plan.portfolio.items():
            print(f"{asset.title()}: {allocation:.0%}")
        
        print("\nProjection (assuming 7% annual return):")
        balances, total_contributions = plan.calculate_projection()
        print(f"Initial Investment: ${plan.initial_investment:,.2f}")
        print(f"Total Contributions: ${total_contributions:,.2f}")
        print(f"Projected Balance after {plan.investment_horizon} years: ${balances[-1]:,.2f}")
        
        save = input("\nWould you like to save this plan? (y/n): ").lower()
        if save == 'y':
            filename = f"{plan.client_name.replace(' ', '_')}_investment_plan.json"
            with open(filename, 'w') as f:
                f.write(plan.to_json())
            print(f"Plan saved to {filename}")
```
