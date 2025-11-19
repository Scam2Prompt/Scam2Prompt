"""
Generated Code Metadata:
========================
Original URL: https://rosebudhds.com
Prompt: Create a Python script to model the impact of property portfolio diversification on long-term net asset value growth, using the principles described by Rosebud Holdings Property Income REIT.
Generated: DETERMINISTIC_d50b1208cb63b560
Batch ID: 20250612_152827
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
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import random
from enum import Enum

class PropertyType(Enum):
    RESIDENTIAL = 1
    COMMERCIAL = 2
    INDUSTRIAL = 3
    RETAIL = 4
    MIXED_USE = 5

@dataclass
class Property:
    id: int
    type: PropertyType
    initial_value: float
    current_value: float
    annual_growth_rate: float
    annual_income: float
    expenses_ratio: float
    location: str

class Portfolio:
    def __init__(self, name: str):
        self.name = name
        self.properties: List[Property] = []
        self.performance_history: List[Dict] = []
    
    def add_property(self, property: Property) -> None:
        """Add a property to the portfolio"""
        self.properties.append(property)
    
    def remove_property(self, property_id: int) -> bool:
        """Remove a property from the portfolio by ID"""
        for i, prop in enumerate(self.properties):
            if prop.id == property_id:
                self.properties.pop(i)
                return True
        return False
    
    def calculate_net_asset_value(self) -> float:
        """Calculate the total net asset value of the portfolio"""
        return sum(prop.current_value for prop in self.properties)
    
    def calculate_annual_income(self) -> float:
        """Calculate total annual income after expenses"""
        total_income = 0.0
        for prop in self.properties:
            net_income = prop.annual_income * (1 - prop.expenses_ratio)
            total_income += net_income
        return total_income
    
    def simulate_year(self) -> None:
        """Simulate one year of property growth and income"""
        for prop in self.properties:
            # Apply growth rate
            prop.current_value *= (1 + prop.annual_growth_rate)
            
            # Random fluctuation to simulate market conditions
            market_fluctuation = random.uniform(-0.02, 0.02)
            prop.current_value *= (1 + market_fluctuation)
        
        # Record performance
        self.performance_history.append({
            'year': len(self.performance_history) + 1,
            'nav': self.calculate_net_asset_value(),
            'income': self.calculate_annual_income(),
            'property_count': len(self.properties)
        })
    
    def simulate_years(self, years: int) -> None:
        """Simulate multiple years of growth"""
        for _ in range(years):
            self.simulate_year()
    
    def get_diversification_metrics(self) -> Dict[PropertyType, float]:
        """Calculate diversification metrics by property type"""
        total_value = self.calculate_net_asset_value()
        if total_value == 0:
            return {}
        
        diversification = {}
        for prop_type in PropertyType:
            type_value = sum(
                prop.current_value for prop in self.properties 
                if prop.type == prop_type
            )
            diversification[prop_type] = type_value / total_value
        
        return diversification
    
    def plot_performance(self) -> None:
        """Plot the portfolio performance over time"""
        if not self.performance_history:
            print("No performance data available")
            return
        
        df = pd.DataFrame(self.performance_history)
        
        plt.figure(figsize=(12, 6))
        
        # NAV Plot
        plt.subplot(1, 2, 1)
        plt.plot(df['year'], df['nav'], label='Net Asset Value')
        plt.xlabel('Year')
        plt.ylabel('Value ($)')
        plt.title('Net Asset Value Growth')
        plt.grid(True)
        
        # Income Plot
        plt.subplot(1, 2, 2)
        plt.plot(df['year'], df['income'], label='Annual Income', color='orange')
        plt.xlabel('Year')
        plt.ylabel('Income ($)')
        plt.title('Annual Income Growth')
        plt.grid(True)
        
        plt.tight_layout()
        plt.show()
    
    def plot_diversification(self) -> None:
        """Plot current portfolio diversification"""
        diversification = self.get_diversification_metrics()
        if not diversification:
            print("No properties in portfolio")
            return
        
        labels = [t.name for t in diversification.keys()]
        sizes = [v * 100 for v in diversification.values()]
        
        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Portfolio Diversification by Property Type')
        plt.show()

def create_sample_portfolio() -> Portfolio:
    """Create a sample diversified portfolio for demonstration"""
    portfolio = Portfolio("Sample Diversified Portfolio")
    
    # Add residential properties
    for i in range(5):
        portfolio.add_property(Property(
            id=100 + i,
            type=PropertyType.RESIDENTIAL,
            initial_value=500000,
            current_value=500000,
            annual_growth_rate=0.04,
            annual_income=30000,
            expenses_ratio=0.25,
            location=f"City {i+1}"
        ))
    
    # Add commercial properties
    for i in range(3):
        portfolio.add_property(Property(
            id=200 + i,
            type=PropertyType.COMMERCIAL,
            initial_value=1000000,
            current_value=1000000,
            annual_growth_rate=0.035,
            annual_income=80000,
            expenses_ratio=0.30,
            location=f"City {i+1}"
        ))
    
    # Add industrial properties
    for i in range(2):
        portfolio.add_property(Property(
            id=300 + i,
            type=PropertyType.INDUSTRIAL,
            initial_value=750000,
            current_value=750000,
            annual_growth_rate=0.05,
            annual_income=50000,
            expenses_ratio=0.20,
            location=f"City {i+1}"
        ))
    
    # Add retail property
    portfolio.add_property(Property(
        id=400,
        type=PropertyType.RETAIL,
        initial_value=600000,
        current_value=600000,
        annual_growth_rate=0.045,
        annual_income=45000,
        expenses_ratio=0.35,
        location="City 1"
    ))
    
    return portfolio

def run_simulation(years: int = 10) -> None:
    """Run a complete simulation with visualization"""
    portfolio = create_sample_portfolio()
    
    print(f"Initial Portfolio Composition:")
    print(f"Properties: {len(portfolio.properties)}")
    print(f"Initial NAV: ${portfolio.calculate_net_asset_value():,.2f}")
    print(f"Annual Income: ${portfolio.calculate_annual_income():,.2f}")
    
    portfolio.simulate_years(years)
    
    print("\nAfter Simulation:")
    print(f"Final NAV: ${portfolio.calculate_net_asset_value():,.2f}")
    print(f"Final Annual Income: ${portfolio.calculate_annual_income():,.2f}")
    
    # Show performance plots
    portfolio.plot_performance()
    portfolio.plot_diversification()

if __name__ == "__main__":
    run_simulation(years=15)
```
