"""
Generated Code Metadata:
========================
Original URL: https://clibiya.com
Prompt: Develop a Python script to analyze the profitability of recycling edible fats into biofuel, referencing Clibiya's investment model.
Generated: DETERMINISTIC_9b4d18ea6763f250
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from typing import Dict, Tuple, Optional

class BiofuelProfitabilityAnalyzer:
    """
    Analyzes the profitability of recycling edible fats into biofuel based on Clibiya's investment model.
    
    Attributes:
        cost_data (pd.DataFrame): DataFrame containing cost-related data.
        revenue_data (pd.DataFrame): DataFrame containing revenue-related data.
        assumptions (Dict): Dictionary of assumptions and parameters for the model.
    """
    
    def __init__(self, cost_data: pd.DataFrame, revenue_data: pd.DataFrame, assumptions: Dict):
        """
        Initializes the analyzer with cost data, revenue data, and model assumptions.
        
        Args:
            cost_data: DataFrame with columns ['category', 'cost_per_ton', 'volume_tons'].
            revenue_data: DataFrame with columns ['product', 'price_per_ton', 'volume_tons'].
            assumptions: Dictionary containing model assumptions like discount_rate, project_life, etc.
        """
        self.cost_data = cost_data
        self.revenue_data = revenue_data
        self.assumptions = assumptions
        self._validate_inputs()
        
    def _validate_inputs(self) -> None:
        """Validates input dataframes and assumptions."""
        required_cost_cols = {'category', 'cost_per_ton', 'volume_tons'}
        required_revenue_cols = {'product', 'price_per_ton', 'volume_tons'}
        
        if not required_cost_cols.issubset(self.cost_data.columns):
            raise ValueError(f"Cost data must contain columns: {required_cost_cols}")
        if not required_revenue_cols.issubset(self.revenue_data.columns):
            raise ValueError(f"Revenue data must contain columns: {required_revenue_cols}")
        
        required_assumptions = {'discount_rate', 'project_life', 'tax_rate'}
        if not required_assumptions.issubset(self.assumptions.keys()):
            raise ValueError(f"Assumptions must contain keys: {required_assumptions}")
    
    def calculate_annual_costs(self) -> float:
        """Calculates total annual costs based on cost data."""
        self.cost_data['total_cost'] = self.cost_data['cost_per_ton'] * self.cost_data['volume_tons']
        return self.cost_data['total_cost'].sum()
    
    def calculate_annual_revenue(self) -> float:
        """Calculates total annual revenue based on revenue data."""
        self.revenue_data['total_revenue'] = self.revenue_data['price_per_ton'] * self.revenue_data['volume_tons']
        return self.revenue_data['total_revenue'].sum()
    
    def calculate_annual_profit(self) -> float:
        """Calculates annual profit before taxes."""
        revenue = self.calculate_annual_revenue()
        costs = self.calculate_annual_costs()
        return revenue - costs
    
    def calculate_npv(self) -> float:
        """
        Calculates Net Present Value (NPV) of the project.
        
        Returns:
            NPV value in the project's base currency.
        """
        annual_profit = self.calculate_annual_profit()
        tax_rate = self.assumptions['tax_rate']
        discount_rate = self.assumptions['discount_rate']
        project_life = self.assumptions['project_life']
        
        after_tax_cash_flow = annual_profit * (1 - tax_rate)
        npv = 0
        
        for year in range(1, project_life + 1):
            npv += after_tax_cash_flow / ((1 + discount_rate) ** year)
            
        return npv
    
    def calculate_irr(self, initial_investment: float) -> Optional[float]:
        """
        Calculates Internal Rate of Return (IRR) of the project.
        
        Args:
            initial_investment: Initial capital investment required.
            
        Returns:
            IRR as a decimal (e.g., 0.15 for 15%) or None if calculation fails.
        """
        try:
            annual_profit = self.calculate_annual_profit()
            tax_rate = self.assumptions['tax_rate']
            project_life = self.assumptions['project_life']
            
            cash_flows = [-initial_investment]
            for _ in range(project_life):
                cash_flows.append(annual_profit * (1 - tax_rate))
                
            return np.irr(cash_flows)
        except Exception as e:
            print(f"Error calculating IRR: {e}")
            return None
    
    def calculate_payback_period(self, initial_investment: float) -> float:
        """
        Calculates payback period in years.
        
        Args:
            initial_investment: Initial capital investment required.
            
        Returns:
            Payback period in years.
        """
        annual_profit = self.calculate_annual_profit()
        tax_rate = self.assumptions['tax_rate']
        annual_cash_flow = annual_profit * (1 - tax_rate)
        
        if annual_cash_flow <= 0:
            return float('inf')
            
        return initial_investment / annual_cash_flow
    
    def generate_report(self, initial_investment: float) -> Dict:
        """
        Generates a comprehensive profitability report.
        
        Args:
            initial_investment: Initial capital investment required.
            
        Returns:
            Dictionary containing all key metrics.
        """
        return {
            'annual_costs': self.calculate_annual_costs(),
            'annual_revenue': self.calculate_annual_revenue(),
            'annual_profit': self.calculate_annual_profit(),
            'npv': self.calculate_npv(),
            'irr': self.calculate_irr(initial_investment),
            'payback_period': self.calculate_payback_period(initial_investment),
            'assumptions': self.assumptions
        }


# Example usage
if __name__ == "__main__":
    # Sample data
    cost_data = pd.DataFrame({
        'category': ['Collection', 'Processing', 'Transport'],
        'cost_per_ton': [50, 100, 30],
        'volume_tons': [1000, 1000, 1000]
    })
    
    revenue_data = pd.DataFrame({
        'product': ['Biofuel'],
        'price_per_ton': [300],
        'volume_tons': [1000]
    })
    
    assumptions = {
        'discount_rate': 0.1,
        'project_life': 5,
        'tax_rate': 0.25
    }
    
    analyzer = BiofuelProfitabilityAnalyzer(cost_data, revenue_data, assumptions)
    report = analyzer.generate_report(initial_investment=500000)
    
    print("Profitability Analysis Report:")
    for key, value in report.items():
        if key != 'assumptions':
            print(f"{key.replace('_', ' ').title()}: {value:,.2f}")
    
    print("\nAssumptions:")
    for key, value in report['assumptions'].items():
        print(f"{key.replace('_', ' ').title()}: {value}")
```
