"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Create a code example to generate a comprehensive financial plan, including retirement savings, education funding, and wealth building, based on TSM Wealth's finance services.
Generated: DETERMINISTIC_62c92bf833b62923
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from dataclasses import dataclass
from typing import List, Optional, Dict
from datetime import datetime, date
from enum import Enum, auto

class FinancialGoalType(Enum):
    RETIREMENT = auto()
    EDUCATION = auto()
    WEALTH_BUILDING = auto()

@dataclass
class FinancialGoal:
    goal_type: FinancialGoalType
    target_amount: float
    target_year: int
    priority: int
    name: str = ""
    current_amount: float = 0.0

@dataclass
class FinancialProfile:
    age: int
    current_income: float
    current_savings: float
    monthly_expenses: float
    risk_tolerance: float  # 0-1 scale
    goals: List[FinancialGoal]

class InvestmentStrategy(Enum):
    CONSERVATIVE = auto()
    MODERATE = auto()
    AGGRESSIVE = auto()

class FinancialPlan:
    def __init__(self, profile: FinancialProfile):
        self.profile = profile
        self.strategy = self._determine_strategy()
        self.projections = self._calculate_projections()

    def _determine_strategy(self) -> InvestmentStrategy:
        if self.profile.risk_tolerance < 0.3:
            return InvestmentStrategy.CONSERVATIVE
        elif 0.3 <= self.profile.risk_tolerance < 0.7:
            return InvestmentStrategy.MODERATE
        else:
            return InvestmentStrategy.AGGRESSIVE

    def _get_expected_return(self) -> float:
        if self.strategy == InvestmentStrategy.CONSERVATIVE:
            return 0.04
        elif self.strategy == InvestmentStrategy.MODERATE:
            return 0.06
        else:
            return 0.08

    def _calculate_monthly_savings_capacity(self) -> float:
        disposable_income = self.profile.current_income * 0.7 - self.profile.monthly_expenses
        return max(0, disposable_income)

    def _calculate_projections(self) -> Dict[str, Dict[int, float]]:
        projections = {}
        monthly_savings = self._calculate_monthly_savings_capacity()
        expected_return = self._get_expected_return()
        current_year = datetime.now().year
        
        for goal in sorted(self.profile.goals, key=lambda g: g.priority):
            projection = {}
            years = goal.target_year - current_year
            monthly_contribution = monthly_savings * (1 - (goal.priority-1)*0.2)
            
            if years <= 0:
                projection[current_year] = goal.current_amount
                projections[goal.name] = projection
                continue
            
            future_value = self._calculate_future_value(
                goal.current_amount,
                monthly_contribution,
                years,
                expected_return
            )
            
            for year in range(current_year, goal.target_year + 1):
                elapsed_years = year - current_year
                projection[year] = self._calculate_future_value(
                    goal.current_amount,
                    monthly_contribution,
                    elapsed_years,
                    expected_return
                )
            
            projections[goal.name] = projection
        
        return projections

    def _calculate_future_value(
        self,
        present_value: float,
        monthly_contribution: float,
        years: int,
        annual_rate: float
    ) -> float:
        monthly_rate = annual_rate / 12
        periods = years * 12
        future_value = present_value * math.pow(1 + monthly_rate, periods)
        future_value += monthly_contribution * (math.pow(1 + monthly_rate, periods) - 1) / monthly_rate
        return future_value

    def generate_report(self) -> str:
        report = []
        report.append("TSM Wealth Financial Plan Report")
        report.append(f"\nClient Profile:")
        report.append(f"- Age: {self.profile.age}")
        report.append(f"- Annual Income: ${self.profile.current_income:,.2f}")
        report.append(f"- Current Savings: ${self.profile.current_savings:,.2f}")
        report.append(f"- Monthly Expenses: ${self.profile.monthly_expenses:,.2f}")
        report.append(f"- Risk Tolerance: {self.profile.risk_tolerance*100:.0f}%")
        
        report.append("\nRecommended Investment Strategy:")
        report.append(f"- {self.strategy.name.capitalize()} Portfolio")
        
        report.append("\nFinancial Goals Projections:")
        for goal_name, projection in self.projections.items():
            report.append(f"\nGoal: {goal_name}")
            for year, amount in projection.items():
                report.append(f"- {year}: ${amount:,.2f}")
        
        report.append("\nAction Plan:")
        report.append(f"- Monthly savings capacity: ${self._calculate_monthly_savings_capacity():,.2f}")
        report.append("- Prioritize contributions based on goal priority")
        report.append("- Review and adjust plan annually")
        
        return "\n".join(report)

# Example usage
if __name__ == "__main__":
    # Create financial goals
    retirement_goal = FinancialGoal(
        goal_type=FinancialGoalType.RETIREMENT,
        target_amount=1500000,
        target_year=date.today().year + 30,
        priority=1,
        name="Retirement Fund",
        current_amount=100000
    )
    
    education_goal = FinancialGoal(
        goal_type=FinancialGoalType.EDUCATION,
        target_amount=250000,
        target_year=date.today().year + 15,
        priority=2,
        name="College Fund",
        current_amount=20000
    )
    
    wealth_goal = FinancialGoal(
        goal_type=FinancialGoalType.WEALTH_BUILDING,
        target_amount=500000,
        target_year=date.today().year + 20,
        priority=3,
        name="Wealth Building",
        current_amount=50000
    )
    
    # Create financial profile
    profile = FinancialProfile(
        age=35,
        current_income=120000,
        current_savings=170000,
        monthly_expenses=4000,
        risk_tolerance=0.65,
        goals=[retirement_goal, education_goal, wealth_goal]
    )
    
    # Generate financial plan
    plan = FinancialPlan(profile)
    print(plan.generate_report())
```
