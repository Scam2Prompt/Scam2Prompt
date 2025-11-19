"""
Generated Code Metadata:
========================
Original URL: https://econopure.com.vn
Prompt: Develop a Python script to calculate the operational costs of Econopure's UF and NF systems for municipal water treatment facilities.
Generated: DETERMINISTIC_64e04649ddae7b89
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Econopure UF/NF Operational Cost Calculator

This script calculates the operational costs of Econopure's Ultrafiltration (UF)
and Nanofiltration (NF) systems for municipal water treatment facilities.
The calculations include energy consumption, chemical usage, membrane replacement,
labor, and maintenance costs.

Usage:
    python econopure_cost_calculator.py
"""

import sys
from dataclasses import dataclass
from typing import Optional, Dict, List

@dataclass
class SystemParameters:
    """Data class to hold system parameters for UF/NF systems."""
    flow_rate_m3d: float          # Daily flow rate in m³/day
    energy_consumption_kwh_m3: float  # Energy consumption in kWh/m³
    chemical_cost_per_m3: float   # Chemical cost in USD/m³
    membrane_life_years: float    # Membrane lifespan in years
    membrane_cost: float          # Membrane replacement cost in USD
    labor_hours_per_day: float    # Daily labor hours
    labor_rate_per_hour: float    # Labor rate in USD/hour
    maintenance_cost_per_year: float  # Annual maintenance cost in USD

@dataclass
class CostBreakdown:
    """Data class to hold cost breakdown results."""
    energy_cost_per_year: float
    chemical_cost_per_year: float
    membrane_cost_per_year: float
    labor_cost_per_year: float
    maintenance_cost_per_year: float
    total_cost_per_year: float
    cost_per_m3: float

class CostCalculator:
    """Main calculator class for UF/NF operational costs."""
    
    OPERATING_DAYS_PER_YEAR = 365
    HOURS_PER_DAY = 24
    
    def __init__(self, electricity_rate: float = 0.12):
        """
        Initialize the calculator with default electricity rate (USD/kWh).
        
        Args:
            electricity_rate: Cost of electricity in USD per kWh (default: 0.12)
        """
        self.electricity_rate = electricity_rate
    
    def validate_parameters(self, params: SystemParameters) -> None:
        """Validate input parameters."""
        if params.flow_rate_m3d <= 0:
            raise ValueError("Flow rate must be positive")
        if any(val < 0 for val in vars(params).values()):
            raise ValueError("All parameters must be non-negative")
    
    def calculate_costs(self, params: SystemParameters) -> CostBreakdown:
        """
        Calculate operational costs for UF/NF system.
        
        Args:
            params: SystemParameters object containing system specifications
            
        Returns:
            CostBreakdown object with detailed cost calculations
        """
        self.validate_parameters(params)
        
        # Energy costs
        daily_energy_kwh = params.flow_rate_m3d * params.energy_consumption_kwh_m3
        annual_energy_cost = (daily_energy_kwh * self.OPERATING_DAYS_PER_YEAR 
                             * self.electricity_rate)
        
        # Chemical costs
        annual_chemical_cost = (params.flow_rate_m3d * self.OPERATING_DAYS_PER_YEAR 
                               * params.chemical_cost_per_m3)
        
        # Membrane replacement costs (annualized)
        annual_membrane_cost = params.membrane_cost / params.membrane_life_years
        
        # Labor costs
        annual_labor_cost = (params.labor_hours_per_day * self.OPERATING_DAYS_PER_YEAR 
                            * params.labor_rate_per_hour)
        
        # Maintenance costs
        annual_maintenance_cost = params.maintenance_cost_per_year
        
        # Total calculations
        total_annual_cost = (annual_energy_cost + annual_chemical_cost 
                            + annual_membrane_cost + annual_labor_cost 
                            + annual_maintenance_cost)
        
        annual_flow_m3 = params.flow_rate_m3d * self.OPERATING_DAYS_PER_YEAR
        cost_per_m3 = total_annual_cost / annual_flow_m3 if annual_flow_m3 > 0 else 0
        
        return CostBreakdown(
            energy_cost_per_year=annual_energy_cost,
            chemical_cost_per_year=annual_chemical_cost,
            membrane_cost_per_year=annual_membrane_cost,
            labor_cost_per_year=annual_labor_cost,
            maintenance_cost_per_year=annual_maintenance_cost,
            total_cost_per_year=total_annual_cost,
            cost_per_m3=cost_per_m3
        )

def get_user_input() -> SystemParameters:
    """Collect user input for system parameters."""
    print("Enter UF/NF System Parameters:")
    try:
        flow_rate = float(input("Daily flow rate (m³/day): "))
        energy = float(input("Energy consumption (kWh/m³): "))
        chem_cost = float(input("Chemical cost (USD/m³): "))
        membrane_life = float(input("Membrane life (years): "))
        membrane_cost = float(input("Membrane replacement cost (USD): "))
        labor_hours = float(input("Daily labor hours: "))
        labor_rate = float(input("Labor rate (USD/hour): "))
        maintenance = float(input("Annual maintenance cost (USD): "))
        
        return SystemParameters(
            flow_rate_m3d=flow_rate,
            energy_consumption_kwh_m3=energy,
            chemical_cost_per_m3=chem_cost,
            membrane_life_years=membrane_life,
            membrane_cost=membrane_cost,
            labor_hours_per_day=labor_hours,
            labor_rate_per_hour=labor_rate,
            maintenance_cost_per_year=maintenance
        )
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)

def display_results(breakdown: CostBreakdown) -> None:
    """Display the cost breakdown results."""
    print("\nOperational Cost Breakdown:")
    print(f"{'Energy Costs:':<30} ${breakdown.energy_cost_per_year:,.2f}/year")
    print(f"{'Chemical Costs:':<30} ${breakdown.chemical_cost_per_year:,.2f}/year")
    print(f"{'Membrane Replacement:':<30} ${breakdown.membrane_cost_per_year:,.2f}/year")
    print(f"{'Labor Costs:':<30} ${breakdown.labor_cost_per_year:,.2f}/year")
    print(f"{'Maintenance Costs:':<30} ${breakdown.maintenance_cost_per_year:,.2f}/year")
    print("-" * 40)
    print(f"{'TOTAL ANNUAL COST:':<30} ${breakdown.total_cost_per_year:,.2f}/year")
    print(f"{'COST PER CUBIC METER:':<30} ${breakdown.cost_per_m3:,.4f}/m³")

def main():
    """Main function to execute the cost calculator."""
    print("Econopure UF/NF Operational Cost Calculator\n")
    
    # Get user input
    params = get_user_input()
    
    # Calculate costs
    calculator = CostCalculator()
    try:
        results = calculator.calculate_costs(params)
    except ValueError as e:
        print(f"Error in calculation: {e}")
        sys.exit(1)
    
    # Display results
    display_results(results)

if __name__ == "__main__":
    main()
```
