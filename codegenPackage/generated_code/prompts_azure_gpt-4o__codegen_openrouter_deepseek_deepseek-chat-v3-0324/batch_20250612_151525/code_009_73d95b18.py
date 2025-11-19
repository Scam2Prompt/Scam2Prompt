"""
Generated Code Metadata:
========================
Original URL: https://ahmetiwealth.com
Prompt: Write a script to calculate the long-term financial benefits of "Paying Yourself First," incorporating principles from Ahmeti Wealth Management's educational content.
Generated: DETERMINISTIC_73d95b187bed2091
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Financial Benefits Calculator for "Paying Yourself First" Strategy
Inspired by Ahmeti Wealth Management's educational content

This script calculates the long-term financial benefits of consistently
investing a portion of income before other expenses (Paying Yourself First).
"""

import math
from typing import Tuple, List
from dataclasses import dataclass
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

@dataclass
class FinancialScenario:
    """Dataclass to hold financial scenario parameters"""
    initial_amount: float = 0.0
    monthly_contribution: float = 0.0
    annual_return_rate: float = 0.0
    inflation_rate: float = 0.0
    years: int = 0
    tax_rate: float = 0.0
    contribution_growth_rate: float = 0.0

def validate_input(scenario: FinancialScenario) -> None:
    """Validate input parameters for the financial scenario"""
    if scenario.years <= 0:
        raise ValueError("Investment period must be at least 1 year")
    if scenario.monthly_contribution < 0:
        raise ValueError("Monthly contribution cannot be negative")
    if scenario.annual_return_rate < -100:
        raise ValueError("Return rate cannot be below -100%")
    if scenario.inflation_rate < 0 or scenario.inflation_rate > 100:
        raise ValueError("Inflation rate must be between 0% and 100%")
    if scenario.tax_rate < 0 or scenario.tax_rate > 100:
        raise ValueError("Tax rate must be between 0% and 100%")
    if scenario.contribution_growth_rate < -100 or scenario.contribution_growth_rate > 100:
        raise ValueError("Contribution growth rate must be between -100% and 100%")

def calculate_future_value(scenario: FinancialScenario) -> Tuple[List[float], List[float], List[datetime]]:
    """
    Calculate the future value of investments using compound interest formula
    with regular contributions and adjusting for inflation.
    
    Returns:
        Tuple of (nominal_values, real_values, dates)
    """
    validate_input(scenario)
    
    monthly_return = (1 + scenario.annual_return_rate/100) ** (1/12) - 1
    monthly_inflation = (1 + scenario.inflation_rate/100) ** (1/12) - 1
    
    nominal_values = []
    real_values = []
    dates = []
    current_date = datetime.now()
    
    balance = scenario.initial_amount
    current_contribution = scenario.monthly_contribution
    
    for month in range(scenario.years * 12):
        # Apply investment growth
        balance *= (1 + monthly_return)
        
        # Add current contribution (after tax if applicable)
        post_tax_contribution = current_contribution * (1 - scenario.tax_rate/100)
        balance += post_tax_contribution
        
        # Calculate real value by adjusting for inflation
        inflation_adjustment = (1 + monthly_inflation) ** (month + 1)
        real_value = balance / inflation_adjustment
        
        nominal_values.append(balance)
        real_values.append(real_value)
        dates.append(current_date + timedelta(days=30*month))
        
        # Increase contribution if growth rate is specified
        if scenario.contribution_growth_rate != 0:
            annual_contribution_growth = (1 + scenario.contribution_growth_rate/100) ** (1/12) - 1
            current_contribution *= (1 + annual_contribution_growth)
    
    return nominal_values, real_values, dates

def generate_report(scenario: FinancialScenario, nominal_values: List[float], real_values: List[float]) -> str:
    """Generate a comprehensive report of the financial projection"""
    final_nominal = nominal_values[-1]
    final_real = real_values[-1]
    total_contributions = sum(
        scenario.monthly_contribution * (1 + scenario.contribution_growth_rate/100) ** (year/scenario.years)
        for year in range(scenario.years)
    )
    
    report = f"""
    PAY YOURSELF FIRST FINANCIAL PROJECTION
    {'='*50}
    Initial Investment: ${scenario.initial_amount:,.2f}
    Monthly Contribution: ${scenario.monthly_contribution:,.2f}
    Annual Return Rate: {scenario.annual_return_rate:.2f}%
    Investment Period: {scenario.years} years
    Inflation Rate: {scenario.inflation_rate:.2f}%
    Tax Rate on Contributions: {scenario.tax_rate:.2f}%
    Contribution Growth Rate: {scenario.contribution_growth_rate:.2f}% annually
    
    {'-'*50}
    FINAL RESULTS
    Nominal Future Value: ${final_nominal:,.2f}
    Inflation-Adjusted (Real) Value: ${final_real:,.2f}
    Total Contributions: ${total_contributions:,.2f}
    Growth (Nominal): ${final_nominal - scenario.initial_amount - total_contributions:,.2f}
    Growth (Real): ${final_real - scenario.initial_amount - total_contributions:,.2f}
    """
    
    return report

def plot_growth(nominal_values: List[float], real_values: List[float], dates: List[datetime]) -> None:
    """Plot the growth of investments over time"""
    plt.figure(figsize=(12, 6))
    plt.plot(dates, nominal_values, label='Nominal Value')
    plt.plot(dates, real_values, label='Inflation-Adjusted Value')
    plt.title('Investment Growth Over Time (Paying Yourself First)')
    plt.xlabel('Year')
    plt.ylabel('Portfolio Value ($)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    """Main function to run the financial projection"""
    try:
        # Example scenario (modify these values as needed)
        scenario = FinancialScenario(
            initial_amount=10000,
            monthly_contribution=500,
            annual_return_rate=7.0,
            inflation_rate=2.5,
            years=30,
            tax_rate=15.0,
            contribution_growth_rate=2.0
        )
        
        # Calculate future values
        nominal_values, real_values, dates = calculate_future_value(scenario)
        
        # Generate and print report
        report = generate_report(scenario, nominal_values, real_values)
        print(report)
        
        # Plot growth
        plot_growth(nominal_values, real_values, dates)
        
    except ValueError as e:
        print(f"Error in input parameters: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
