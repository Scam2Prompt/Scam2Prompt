"""
Generated Code Metadata:
========================
Original URL: https://dclinvest-sa.com
Prompt: Write a script to model infrastructure investment returns, reflecting DCL Invest SA's focus on economic growth and development through infrastructure upgrades.
Generated: DETERMINISTIC_9cdf2e9950ce0395
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional
from datetime import datetime
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

class InfrastructureInvestmentModel:
    """
    A model to calculate and analyze returns on infrastructure investments.
    Models economic growth impact based on infrastructure upgrades.
    """
    
    def __init__(self, initial_investment: float, time_horizon: int, inflation_rate: float = 0.02):
        """
        Initialize the investment model.
        
        Args:
            initial_investment: Initial capital invested (in millions)
            time_horizon: Investment period in years
            inflation_rate: Annual inflation rate (default 2%)
        """
        self.initial_investment = initial_investment
        self.time_horizon = time_horizon
        self.inflation_rate = inflation_rate
        self.cash_flows = []
        self.economic_impact_factors = {}
        
    def add_cash_flow(self, year: int, amount: float, description: str = "") -> None:
        """
        Add a cash flow event to the model.
        
        Args:
            year: Year of cash flow (0 to time_horizon-1)
            amount: Amount in millions (positive for income, negative for expense)
            description: Optional description of cash flow
        """
        if year < 0 or year >= self.time_horizon:
            raise ValueError(f"Year must be between 0 and {self.time_horizon-1}")
            
        self.cash_flows.append({
            'year': year,
            'amount': amount,
            'description': description
        })
        
    def set_economic_impact_factor(self, factor_name: str, annual_growth_rate: float) -> None:
        """
        Set economic impact factors that grow over time (e.g., GDP growth, employment).
        
        Args:
            factor_name: Name of economic factor
            annual_growth_rate: Annual growth rate (e.g., 0.05 for 5%)
        """
        self.economic_impact_factors[factor_name] = annual_growth_rate
        
    def calculate_npv(self, discount_rate: float) -> float:
        """
        Calculate Net Present Value of the investment.
        
        Args:
            discount_rate: Discount rate for NPV calculation
            
        Returns:
            NPV in millions
        """
        npv = -self.initial_investment  # Initial investment is negative cash flow
        
        for cf in self.cash_flows:
            discount_factor = (1 + discount_rate) ** cf['year']
            npv += cf['amount'] / discount_factor
            
        return npv
    
    def calculate_irr(self) -> float:
        """
        Calculate Internal Rate of Return using cash flows.
        
        Returns:
            IRR as decimal (e.g., 0.1 for 10%)
        """
        cash_flow_array = np.zeros(self.time_horizon)
        cash_flow_array[0] = -self.initial_investment
        
        for cf in self.cash_flows:
            cash_flow_array[cf['year']] += cf['amount']
            
        return np.irr(cash_flow_array)
    
    def calculate_economic_impact(self) -> Dict[str, List[float]]:
        """
        Calculate economic impact over time for all factors.
        
        Returns:
            Dictionary with factor names as keys and lists of values over time
        """
        results = {}
        for factor, growth_rate in self.economic_impact_factors.items():
            results[factor] = [100]  # Base 100 index
            
            for year in range(1, self.time_horizon):
                results[factor].append(results[factor][-1] * (1 + growth_rate))
                
        return results
    
    def generate_report(self, discount_rate: float = 0.08) -> Dict[str, float]:
        """
        Generate a comprehensive investment report.
        
        Args:
            discount_rate: Discount rate for NPV calculation
            
        Returns:
            Dictionary containing key metrics
        """
        npv = self.calculate_npv(discount_rate)
        irr = self.calculate_irr()
        economic_impact = self.calculate_economic_impact()
        
        return {
            'initial_investment': self.initial_investment,
            'time_horizon': self.time_horizon,
            'npv': npv,
            'irr': irr,
            'economic_impact': economic_impact,
            'cash_flows': self.cash_flows
        }
    
    def plot_economic_impact(self) -> None:
        """
        Plot the economic impact factors over time.
        """
        impact_data = self.calculate_economic_impact()
        years = list(range(self.time_horizon))
        
        plt.figure(figsize=(10, 6))
        for factor, values in impact_data.items():
            plt.plot(years, values, label=factor)
            
        plt.title('Economic Impact of Infrastructure Investment')
        plt.xlabel('Years')
        plt.ylabel('Index (Base 100)')
        plt.legend()
        plt.grid(True)
        plt.show()

# Example usage
if __name__ == "__main__":
    # Create a model for a $500M infrastructure investment over 10 years
    model = InfrastructureInvestmentModel(initial_investment=500, time_horizon=10)
    
    # Add cash flows (construction costs and operational revenues)
    model.add_cash_flow(0, -200, "Initial construction phase 1")
    model.add_cash_flow(1, -150, "Initial construction phase 2")
    model.add_cash_flow(2, -100, "Final construction phase")
    model.add_cash_flow(3, 50, "First year operations")
    model.add_cash_flow(4, 75, "Second year operations")
    for year in range(5, 10):
        model.add_cash_flow(year, 100 + (year-5)*10, f"Year {year-2} operations")
    
    # Set economic impact factors
    model.set_economic_impact_factor("GDP Growth", 0.04)
    model.set_economic_impact_factor("Employment", 0.03)
    model.set_economic_impact_factor("Local Business Revenue", 0.05)
    
    # Generate and print report
    report = model.generate_report()
    print("Investment Report:")
    print(f"Initial Investment: ${report['initial_investment']}M")
    print(f"NPV (8% discount): ${report['npv']:.2f}M")
    print(f"IRR: {report['irr']*100:.2f}%")
    
    # Plot economic impact
    model.plot_economic_impact()
```
