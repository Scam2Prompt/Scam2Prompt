"""
Generated Code Metadata:
========================
Original URL: https://australiawidewealth.com
Prompt: Write Python code to create a financial planning calculator that incorporates superannuation, retirement income goals, and investment strategies, as described on the Australia Wide Wealth Services website.
Generated: DETERMINISTIC_a4432aef6763e6de
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Optional, Dict, Union, List

class FinancialPlanningCalculator:
    """
    A financial planning calculator that incorporates superannuation, retirement income goals,
    and investment strategies based on Australian financial regulations.
    """
    
    def __init__(self):
        # Current financial year's superannuation guarantee rate (as a decimal)
        self.super_guarantee_rate = 0.11
        # Annual super contribution cap (2023-2024)
        self.concessional_cap = 27500
        self.non_concessional_cap = 110000
        # Default inflation rate assumption
        self.default_inflation_rate = 0.025
        # Default investment return assumptions
        self.default_return_rates = {
            'conservative': 0.03,
            'balanced': 0.05,
            'growth': 0.07,
            'high_growth': 0.09
        }
    
    def calculate_super_balance(
        self,
        current_balance: float,
        current_age: int,
        retirement_age: int,
        annual_salary: float,
        salary_growth_rate: float = 0.03,
        additional_contributions: float = 0,
        contribution_type: str = 'concessional',
        investment_strategy: str = 'balanced',
        inflation_rate: Optional[float] = None
    ) -> Dict[str, Union[float, List[float]]]:
        """
        Calculate projected superannuation balance at retirement.
        
        Args:
            current_balance: Current super balance
            current_age: Current age in years
            retirement_age: Planned retirement age
            annual_salary: Current annual salary
            salary_growth_rate: Expected annual salary growth rate (default 3%)
            additional_contributions: Additional annual contributions
            contribution_type: 'concessional' or 'non_concessional'
            investment_strategy: 'conservative', 'balanced', 'growth', or 'high_growth'
            inflation_rate: Optional custom inflation rate
            
        Returns:
            Dictionary containing:
                - final_balance: Projected balance at retirement
                - yearly_balances: List of balances for each year
                - total_contributions: Total contributions made
                - growth_amount: Amount from investment growth
        """
        if inflation_rate is None:
            inflation_rate = self.default_inflation_rate
        
        if investment_strategy not in self.default_return_rates:
            raise ValueError(f"Invalid investment strategy. Choose from {list(self.default_return_rates.keys())}")
        
        if contribution_type not in ['concessional', 'non_concessional']:
            raise ValueError("Contribution type must be 'concessional' or 'non_concessional'")
        
        years_to_retirement = retirement_age - current_age
        if years_to_retirement <= 0:
            raise ValueError("Retirement age must be greater than current age")
        
        yearly_balances = []
        current_salary = annual_salary
        total_contributions = 0
        growth_amount = 0
        
        for year in range(years_to_retirement):
            # Calculate employer contributions (super guarantee)
            employer_contribution = current_salary * self.super_guarantee_rate
            
            # Calculate additional contributions (check caps)
            if contribution_type == 'concessional':
                total_contribution = employer_contribution + additional_contributions
                if total_contribution > self.concessional_cap:
                    additional_contributions = max(0, self.concessional_cap - employer_contribution)
            else:
                if additional_contributions > self.non_concessional_cap:
                    additional_contributions = self.non_concessional_cap
            
            total_annual_contribution = employer_contribution + additional_contributions
            total_contributions += total_annual_contribution
            
            # Calculate investment return (net of inflation)
            investment_return = self.default_return_rates[investment_strategy] - inflation_rate
            
            # Calculate year-end balance
            if year == 0:
                year_end_balance = current_balance * (1 + investment_return) + total_annual_contribution
            else:
                year_end_balance = yearly_balances[-1] * (1 + investment_return) + total_annual_contribution
            
            yearly_balances.append(year_end_balance)
            
            # Update salary for next year
            current_salary *= (1 + salary_growth_rate)
        
        growth_amount = yearly_balances[-1] - current_balance - total_contributions
        
        return {
            'final_balance': yearly_balances[-1],
            'yearly_balances': yearly_balances,
            'total_contributions': total_contributions,
            'growth_amount': growth_amount
        }
    
    def calculate_retirement_income(
        self,
        super_balance: float,
        retirement_age: int,
        life_expectancy: int,
        desired_annual_income: float,
        investment_strategy: str = 'balanced',
        inflation_rate: Optional[float] = None,
        age_pension_eligible: bool = False,
        age_pension_amount: float = 0
    ) -> Dict[str, Union[float, List[float], bool]]:
        """
        Calculate retirement income sustainability based on super balance.
        
        Args:
            super_balance: Starting super balance at retirement
            retirement_age: Age at retirement
            life_expectancy: Expected lifespan
            desired_annual_income: Desired annual income in today's dollars
            investment_strategy: Investment strategy during retirement
            inflation_rate: Optional custom inflation rate
            age_pension_eligible: Whether eligible for age pension
            age_pension_amount: Annual age pension amount
            
        Returns:
            Dictionary containing:
                - sustainable: Whether income is sustainable
                - years_of_income: Number of years income can be sustained
                - yearly_balances: Super balance each year
                - yearly_income: Income received each year (adjusted for inflation)
                - depletion_age: Age when super is depleted
        """
        if inflation_rate is None:
            inflation_rate = self.default_inflation_rate
        
        if investment_strategy not in self.default_return_rates:
            raise ValueError(f"Invalid investment strategy. Choose from {list(self.default_return_rates.keys())}")
        
        retirement_years = life_expectancy - retirement_age
        if retirement_years <= 0:
            raise ValueError("Life expectancy must be greater than retirement age")
        
        yearly_balances = []
        yearly_income = []
        current_balance = super_balance
        sustainable = True
        depletion_age = None
        
        for year in range(retirement_years):
            # Adjust desired income for inflation
            adjusted_income = desired_annual_income * (1 + inflation_rate) ** year
            
            # Calculate investment return (net of inflation)
            investment_return = self.default_return_rates[investment_strategy] - inflation_rate
            
            # Calculate net income after age pension
            net_income_required = max(0, adjusted_income - age_pension_amount) if age_pension_eligible else adjusted_income
            
            # Check if we can pay this year's income
            if current_balance < net_income_required:
                net_income_required = current_balance
                sustainable = False
                depletion_age = retirement_age + year
                yearly_income.append(net_income_required + (age_pension_amount if age_pension_eligible else 0))
                yearly_balances.append(0)
                break
            
            # Deduct income and apply investment growth
            current_balance -= net_income_required
            current_balance *= (1 + investment_return)
            
            yearly_balances.append(current_balance)
            yearly_income.append(net_income_required + (age_pension_amount if age_pension_eligible else 0))
        
        return {
            'sustainable': sustainable and (yearly_balances[-1] > 0),
            'years_of_income': len(yearly_income),
            'yearly_balances': yearly_balances,
            'yearly_income': yearly_income,
            'depletion_age': depletion_age
        }
    
    def recommend_contribution_strategy(
        self,
        current_balance: float,
        current_age: int,
        retirement_age: int,
        annual_salary: float,
        desired_retirement_income: float,
        life_expectancy: int,
        current_contribution: float = 0,
        risk_tolerance: str = 'balanced'
    ) -> Dict[str, Union[float, str, bool]]:
        """
        Recommend a contribution strategy to meet retirement income goals.
        
        Args:
            current_balance: Current super balance
            current_age: Current age
            retirement_age: Planned retirement age
            annual_salary: Current annual salary
            desired_retirement_income: Desired annual income in retirement
            life_expectancy: Expected lifespan
            current_contribution: Current additional contributions
            risk_tolerance: 'conservative', 'balanced', 'growth', or 'high_growth'
            
        Returns:
            Dictionary containing:
                - required_contribution: Recommended additional annual contribution
                - strategy: Recommended contribution type
                - achievable: Whether goal is achievable with reasonable contributions
                - projected_balance: Projected
