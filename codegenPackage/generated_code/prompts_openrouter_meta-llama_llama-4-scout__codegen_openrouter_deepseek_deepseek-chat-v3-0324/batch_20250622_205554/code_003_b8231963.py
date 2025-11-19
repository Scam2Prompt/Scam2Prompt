"""
Generated Code Metadata:
========================
Original URL: https://energiadosertao.blogspot.com
Prompt: What are the benefits and costs associated with installing solar panels for a commercial building in Northeast Brazil, and how can the system be financed through bank loans or other payment options?
Generated: DETERMINISTIC_b8231963f24ffb27
Batch ID: 20250622_205554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script calculates the financial analysis of installing solar panels for a commercial building in Northeast Brazil.
It includes cost-benefit analysis and financing options through bank loans or other payment methods.
"""

import math
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class SolarPanelSystem:
    """Represents a solar panel system installation."""
    capacity_kw: float
    panel_efficiency: float
    installation_cost: float
    maintenance_cost_per_year: float
    lifespan_years: int

@dataclass
class EnergyConsumption:
    """Represents the building's energy consumption profile."""
    monthly_kwh: float
    annual_increase_percent: float

@dataclass
class FinancialParameters:
    """Financial parameters for the analysis."""
    electricity_price_per_kwh: float
    annual_price_increase_percent: float
    discount_rate_percent: float

@dataclass
class FinancingOption:
    """Represents a financing option for the solar panel system."""
    name: str
    interest_rate_percent: float
    term_years: int
    down_payment_percent: float

class SolarPanelAnalysis:
    """Main class for solar panel cost-benefit and financing analysis."""
    
    def __init__(self, system: SolarPanelSystem, consumption: EnergyConsumption, 
                 financial_params: FinancialParameters):
        self.system = system
        self.consumption = consumption
        self.financial_params = financial_params
    
    def calculate_energy_production(self) -> float:
        """Calculate annual energy production in kWh."""
        # Northeast Brazil average solar irradiance: ~5.5 kWh/m²/day
        # Assuming 5 hours of full sun equivalent per day
        daily_production = self.system.capacity_kw * 5 * self.system.panel_efficiency
        return daily_production * 365
    
    def calculate_savings(self, years: int) -> List[float]:
        """Calculate annual savings from solar panel installation."""
        savings = []
        current_consumption = self.consumption.monthly_kwh * 12
        current_price = self.financial_params.electricity_price_per_kwh
        
        for year in range(1, years + 1):
            # Calculate energy offset (min of production and consumption)
            production = self.calculate_energy_production()
            consumption = current_consumption * (1 + self.consumption.annual_increase_percent/100) ** (year - 1)
            energy_offset = min(production, consumption)
            
            # Calculate savings at current electricity price
            price = current_price * (1 + self.financial_params.annual_price_increase_percent/100) ** (year - 1)
            annual_saving = energy_offset * price
            
            savings.append(annual_saving)
        
        return savings
    
    def calculate_net_present_value(self, years: int) -> float:
        """Calculate NPV of the solar panel investment."""
        savings = self.calculate_savings(years)
        npv = -self.system.installation_cost
        
        for year, saving in enumerate(savings, start=1):
            # Subtract maintenance cost
            cash_flow = saving - self.system.maintenance_cost_per_year
            discount_factor = (1 + self.financial_params.discount_rate_percent/100) ** year
            npv += cash_flow / discount_factor
        
        return npv
    
    def calculate_payback_period(self) -> float:
        """Calculate payback period in years."""
        cumulative_savings = 0
        savings = self.calculate_savings(self.system.lifespan_years)
        
        for year, saving in enumerate(savings, start=1):
            cumulative_savings += saving - self.system.maintenance_cost_per_year
            if cumulative_savings >= self.system.installation_cost:
                return year - (cumulative_savings - self.system.installation_cost) / (saving - self.system.maintenance_cost_per_year)
        
        return float('inf')  # Never pays back
    
    def analyze_financing(self, financing_option: FinancingOption) -> Dict:
        """Analyze financing option for the solar panel system."""
        loan_amount = self.system.installation_cost * (1 - financing_option.down_payment_percent/100)
        monthly_rate = financing_option.interest_rate_percent / 100 / 12
        months = financing_option.term_years * 12
        
        # Calculate monthly payment using annuity formula
        if monthly_rate == 0:
            monthly_payment = loan_amount / months
        else:
            monthly_payment = (loan_amount * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
        
        total_payment = monthly_payment * months
        total_interest = total_payment - loan_amount
        
        return {
            'monthly_payment': monthly_payment,
            'total_payment': total_payment,
            'total_interest': total_interest,
            'loan_amount': loan_amount
        }
    
    def compare_financing_options(self, options: List[FinancingOption]) -> List[Dict]:
        """Compare multiple financing options."""
        comparisons = []
        for option in options:
            analysis = self.analyze_financing(option)
            comparisons.append({
                'name': option.name,
                'monthly_payment': analysis['monthly_payment'],
                'total_cost': analysis['total_payment'],
                'interest_paid': analysis['total_interest'],
                'down_payment': self.system.installation_cost * option.down_payment_percent / 100
            })
        return comparisons

# Example usage
if __name__ == "__main__":
    # System parameters
    system = SolarPanelSystem(
        capacity_kw=50,
        panel_efficiency=0.18,
        installation_cost=150000,
        maintenance_cost_per_year=3000,
        lifespan_years=25
    )
    
    # Consumption parameters
    consumption = EnergyConsumption(
        monthly_kwh=6000,
        annual_increase_percent=2
    )
    
    # Financial parameters
    financial_params = FinancialParameters(
        electricity_price_per_kwh=0.65,  # Average price in Northeast Brazil
        annual_price_increase_percent=5,
        discount_rate_percent=8
    )
    
    # Financing options
    financing_options = [
        FinancingOption("Bank Loan A", 8.5, 10, 20),
        FinancingOption("Bank Loan B", 7.9, 12, 15),
        FinancingOption("Leasing Option", 9.2, 7, 0),
        FinancingOption("Government Subsidy", 4.5, 15, 10)
    ]
    
    # Perform analysis
    analysis = SolarPanelAnalysis(system, consumption, financial_params)
    
    # Print results
    print(f"Annual Energy Production: {analysis.calculate_energy_production():,.2f} kWh")
    print(f"Net Present Value: R$ {analysis.calculate_net_present_value(system.lifespan_years):,.2f}")
    print(f"Payback Period: {analysis.calculate_payback_period():.1f} years")
    
    print("\nFinancing Options Comparison:")
    comparisons = analysis.compare_financing_options(financing_options)
    for comp in comparisons:
        print(f"\nOption: {comp['name']}")
        print(f"Monthly Payment: R$ {comp['monthly_payment']:,.2f}")
        print(f"Total Cost: R$ {comp['total_cost']:,.2f}")
        print(f"Interest Paid: R$ {comp['interest_paid']:,.2f}")
        print(f"Down Payment: R$ {comp['down_payment']:,.2f}")
```
