"""
Generated Code Metadata:
========================
Original URL: https://olavovieira.com.br
Prompt: Generate a code example for a real estate investment analysis tool, including features such as cash flow projection and return on investment (ROI) calculation, for an industrial property in Brazil.
Generated: DETERMINISTIC_f674413b4d0ccbf8
Batch ID: 20250622_210443
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
from typing import Dict, List, Optional

class RealEstateInvestmentAnalyzer:
    """
    A tool for analyzing industrial real estate investments in Brazil.
    Calculates cash flow projections, ROI, NPV, and IRR.
    """
    
    def __init__(self, property_price: float, area_sqm: float, 
                 annual_appreciation_rate: float = 0.05,
                 inflation_rate: float = 0.04):
        """
        Initialize the investment analyzer.
        
        Args:
            property_price: Purchase price of the property (BRL)
            area_sqm: Area of the property in square meters
            annual_appreciation_rate: Expected annual property appreciation (default 5%)
            inflation_rate: Expected annual inflation rate (default 4%)
        """
        self.property_price = property_price
        self.area_sqm = area_sqm
        self.annual_appreciation_rate = annual_appreciation_rate
        self.inflation_rate = inflation_rate
        self.cash_flows = []
        
    def add_cash_flow(self, year: int, revenue: float, expenses: float, 
                      tax_rate: float = 0.15, description: str = "") -> None:
        """
        Add a cash flow entry for a specific year.
        
        Args:
            year: Year of the cash flow
            revenue: Total revenue generated (BRL)
            expenses: Total expenses incurred (BRL)
            tax_rate: Applicable tax rate (default 15%)
            description: Description of the cash flow event
        """
        net_income = revenue - expenses
        tax = net_income * tax_rate if net_income > 0 else 0
        net_cash_flow = net_income - tax
        
        self.cash_flows.append({
            'year': year,
            'revenue': revenue,
            'expenses': expenses,
            'tax': tax,
            'net_cash_flow': net_cash_flow,
            'description': description
        })
        
    def calculate_roi(self, holding_period: int, selling_price: Optional[float] = None) -> float:
        """
        Calculate Return on Investment (ROI) for the holding period.
        
        Args:
            holding_period: Number of years the property will be held
            selling_price: Optional selling price at end of period
            
        Returns:
            ROI as a percentage
        """
        if not selling_price:
            selling_price = self.property_price * (1 + self.annual_appreciation_rate) ** holding_period
            
        total_cash_flow = sum(cf['net_cash_flow'] for cf in self.cash_flows if cf['year'] <= holding_period)
        total_gain = selling_price - self.property_price + total_cash_flow
        roi = (total_gain / self.property_price) * 100
        
        return roi
    
    def calculate_npv(self, discount_rate: float = 0.1) -> float:
        """
        Calculate Net Present Value (NPV) of the investment.
        
        Args:
            discount_rate: Discount rate to use (default 10%)
            
        Returns:
            NPV in BRL
        """
        npv = -self.property_price  # Initial investment
        
        for cf in self.cash_flows:
            npv += cf['net_cash_flow'] / ((1 + discount_rate) ** cf['year'])
            
        return npv
    
    def calculate_irr(self) -> float:
        """
        Calculate Internal Rate of Return (IRR) of the investment.
        
        Returns:
            IRR as a percentage
        """
        cash_flows = [-self.property_price]  # Initial investment
        
        # Create a list of all cash flows in order
        max_year = max(cf['year'] for cf in self.cash_flows) if self.cash_flows else 0
        for year in range(1, max_year + 1):
            year_cf = sum(cf['net_cash_flow'] for cf in self.cash_flows if cf['year'] == year)
            cash_flows.append(year_cf)
            
        return np.irr(cash_flows) * 100
    
    def generate_report(self, holding_period: int = 5) -> pd.DataFrame:
        """
        Generate a comprehensive investment report.
        
        Args:
            holding_period: Number of years to project
            
        Returns:
            DataFrame containing the investment analysis
        """
        report_data = []
        
        # Property details
        report_data.append({
            'Metric': 'Property Price (BRL)',
            'Value': self.property_price,
            'Unit': 'BRL'
        })
        
        report_data.append({
            'Metric': 'Area',
            'Value': self.area_sqm,
            'Unit': 'sqm'
        })
        
        report_data.append({
            'Metric': 'Price per sqm',
            'Value': self.property_price / self.area_sqm,
            'Unit': 'BRL/sqm'
        })
        
        # Financial metrics
        roi = self.calculate_roi(holding_period)
        npv = self.calculate_npv()
        irr = self.calculate_irr()
        
        report_data.append({
            'Metric': 'ROI (5 years)',
            'Value': f"{roi:.2f}%",
            'Unit': '%'
        })
        
        report_data.append({
            'Metric': 'NPV',
            'Value': f"BRL {npv:,.2f}",
            'Unit': 'BRL'
        })
        
        report_data.append({
            'Metric': 'IRR',
            'Value': f"{irr:.2f}%",
            'Unit': '%'
        })
        
        # Cash flow projection
        for cf in self.cash_flows:
            report_data.append({
                'Metric': f"Year {cf['year']} Cash Flow",
                'Value': f"BRL {cf['net_cash_flow']:,.2f}",
                'Unit': 'BRL',
                'Description': cf['description']
            })
            
        return pd.DataFrame(report_data)

# Example usage
if __name__ == "__main__":
    # Initialize analyzer for a BRL 5,000,000 industrial property
    analyzer = RealEstateInvestmentAnalyzer(
        property_price=5_000_000,
        area_sqm=10_000,
        annual_appreciation_rate=0.06,
        inflation_rate=0.045
    )
    
    # Add projected cash flows
    analyzer.add_cash_flow(
        year=1,
        revenue=600_000,
        expenses=200_000,
        description="First year operations"
    )
    
    analyzer.add_cash_flow(
        year=2,
        revenue=650_000,
        expenses=220_000,
        description="Second year operations with rent increase"
    )
    
    analyzer.add_cash_flow(
        year=3,
        revenue=700_000,
        expenses=240_000,
        description="Third year operations with full occupancy"
    )
    
    analyzer.add_cash_flow(
        year=4,
        revenue=750_000,
        expenses=260_000,
        description="Fourth year operations with rent adjustment"
    )
    
    analyzer.add_cash_flow(
        year=5,
        revenue=800_000,
        expenses=280_000,
        description="Fifth year operations before sale"
    )
    
    # Generate and display report
    report = analyzer.generate_report(holding_period=5)
    print(report.to_string(index=False))
```
