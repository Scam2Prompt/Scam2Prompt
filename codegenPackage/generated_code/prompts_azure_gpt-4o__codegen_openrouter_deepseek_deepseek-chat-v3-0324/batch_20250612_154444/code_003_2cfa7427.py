"""
Generated Code Metadata:
========================
Original URL: https://beboldproperties.com
Prompt: Create a program that uses modern technology to analyze property acquisition strategies and simulate long-term wealth creation, inspired by Bebold Properties' investment-focused approach.
Generated: DETERMINISTIC_2cfa7427debb6e77
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Property Investment Strategy Simulator

This program analyzes property acquisition strategies and simulates long-term wealth creation
based on various investment parameters. It includes features for cash flow analysis,
appreciation projections, and portfolio growth visualization.

Inspired by Bebold Properties' investment-focused approach.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime, timedelta
from enum import Enum, auto
import logging
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PropertyType(Enum):
    """Enumeration of property types"""
    SINGLE_FAMILY = auto()
    MULTI_FAMILY = auto()
    COMMERCIAL = auto()
    LAND = auto()

@dataclass
class Property:
    """Dataclass representing a property investment"""
    purchase_price: float
    down_payment: float
    interest_rate: float
    loan_term: int  # in years
    property_type: PropertyType
    monthly_rent: float
    annual_appreciation_rate: float
    annual_expenses: float  # as percentage of property value
    purchase_date: datetime
    name: str = "Unnamed Property"

    def __post_init__(self):
        if self.down_payment >= self.purchase_price:
            raise ValueError("Down payment must be less than purchase price")
        if not 0 <= self.annual_expenses <= 1:
            raise ValueError("Annual expenses must be between 0 and 1")

@dataclass
class InvestmentScenario:
    """Dataclass representing an investment scenario with multiple properties"""
    properties: List[Property]
    investment_horizon: int  # in years
    annual_inflation_rate: float = 0.02
    tax_rate: float = 0.25
    additional_yearly_investment: float = 0

class InvestmentSimulator:
    """Main class for simulating property investment strategies"""
    
    def __init__(self, scenario: InvestmentScenario):
        self.scenario = scenario
        self.results = None
    
    def calculate_monthly_mortgage(self, property: Property) -> float:
        """Calculate monthly mortgage payment using the standard formula"""
        principal = property.purchase_price - property.down_payment
        monthly_rate = property.interest_rate / 12
        num_payments = property.loan_term * 12
        
        if monthly_rate == 0:
            return principal / num_payments
        
        mortgage_payment = principal * (
            monthly_rate * (1 + monthly_rate) ** num_payments
        ) / ((1 + monthly_rate) ** num_payments - 1)
        
        return mortgage_payment
    
    def simulate(self) -> pd.DataFrame:
        """Run the simulation and return detailed results"""
        results = []
        current_date = datetime.now()
        end_date = current_date + timedelta(days=365 * self.scenario.investment_horizon)
        
        while current_date <= end_date:
            yearly_result = {
                'year': current_date.year,
                'total_value': 0,
                'total_equity': 0,
                'total_cash_flow': 0,
                'total_net_worth': 0,
                'properties': []
            }
            
            for prop in self.scenario.properties:
                # Calculate years since purchase
                years_held = (current_date - prop.purchase_date).days / 365
                
                if years_held < 0:
                    continue  # Property not purchased yet
                
                # Property value with appreciation
                current_value = prop.purchase_price * (1 + prop.annual_appreciation_rate) ** years_held
                
                # Mortgage calculations
                monthly_payment = self.calculate_monthly_mortgage(prop)
                total_paid = monthly_payment * 12 * min(years_held, prop.loan_term)
                
                # Equity calculation (simplified)
                if years_held < prop.loan_term:
                    remaining_principal = (prop.purchase_price - prop.down_payment) * (
                        (1 + prop.interest_rate) ** prop.loan_term - (1 + prop.interest_rate) ** years_held
                    ) / ((1 + prop.interest_rate) ** prop.loan_term - 1)
                else:
                    remaining_principal = 0
                
                equity = current_value - remaining_principal
                
                # Cash flow calculation
                annual_expenses = current_value * prop.annual_expenses
                annual_rent = prop.monthly_rent * 12 * (1 + self.scenario.annual_inflation_rate) ** years_held
                annual_mortgage = monthly_payment * 12 if years_held < prop.loan_term else 0
                
                cash_flow = annual_rent - annual_expenses - annual_mortgage
                cash_flow_after_tax = cash_flow * (1 - self.scenario.tax_rate)
                
                # Store property results
                prop_result = {
                    'name': prop.name,
                    'value': current_value,
                    'equity': equity,
                    'cash_flow': cash_flow_after_tax,
                    'rent': annual_rent,
                    'expenses': annual_expenses,
                    'mortgage': annual_mortgage
                }
                
                yearly_result['properties'].append(prop_result)
                yearly_result['total_value'] += current_value
                yearly_result['total_equity'] += equity
                yearly_result['total_cash_flow'] += cash_flow_after_tax
            
            # Add additional investments
            yearly_result['total_net_worth'] = (
                yearly_result['total_equity'] + 
                yearly_result['total_cash_flow'] +
                self.scenario.additional_yearly_investment * (current_date.year - datetime.now().year)
            )
            
            results.append(yearly_result)
            current_date = current_date + timedelta(days=365)
        
        self.results = pd.DataFrame(results)
        return self.results
    
    def visualize_results(self):
        """Generate visualization of the simulation results"""
        if self.results is None:
            raise ValueError("Run simulation first before visualizing results")
        
        plt.figure(figsize=(12, 8))
        
        # Net worth over time
        plt.subplot(2, 2, 1)
        plt.plot(self.results['year'], self.results['total_net_worth'])
        plt.title('Total Net Worth Over Time')
        plt.xlabel('Year')
        plt.ylabel('Net Worth ($)')
        plt.grid(True)
        
        # Property values over time
        plt.subplot(2, 2, 2)
        for prop in self.scenario.properties:
            prop_values = [p['value'] for p in self.results['properties'] if p['name'] == prop.name]
            if prop_values:
                plt.plot(self.results['year'], prop_values, label=prop.name)
        plt.title('Property Values Over Time')
        plt.xlabel('Year')
        plt.ylabel('Value ($)')
        plt.legend()
        plt.grid(True)
        
        # Cash flow over time
        plt.subplot(2, 2, 3)
        plt.plot(self.results['year'], self.results['total_cash_flow'])
        plt.title('Annual Cash Flow Over Time')
        plt.xlabel('Year')
        plt.ylabel('Cash Flow ($)')
        plt.grid(True)
        
        # Equity over time
        plt.subplot(2, 2, 4)
        plt.plot(self.results['year'], self.results['total_equity'])
        plt.title('Total Equity Over Time')
        plt.xlabel('Year')
        plt.ylabel('Equity ($)')
        plt.grid(True)
        
        plt.tight_layout()
        plt.show()
    
    def generate_report(self, filename: str = None) -> str:
        """Generate a JSON report of the simulation results"""
        if self.results is None:
            raise ValueError("Run simulation first before generating report")
        
        report = {
            'scenario': {
                'investment_horizon': self.scenario.investment_horizon,
                'inflation_rate': self.scenario.annual_inflation_rate,
                'tax_rate': self.scenario.tax_rate,
                'additional_investment': self.scenario.additional_yearly_investment,
                'property_count': len(self.scenario.properties)
            },
            'final_results': {
                'final_net_worth': self.results['total_net_worth'].iloc[-1],
                'final_equity': self.results['total_equity'].iloc[-1],
                'final_cash_flow': self.results['total_cash_flow'].iloc[-1],
                'final_property_value': self.results['total_value'].iloc[-1]
            },
            'annual_results': json.loads(self.results.to_json(orient='records'))
        }
        
        if filename:
            with open(filename, 'w') as f:
                json.dump(report, f, indent=2)
        
        return json
