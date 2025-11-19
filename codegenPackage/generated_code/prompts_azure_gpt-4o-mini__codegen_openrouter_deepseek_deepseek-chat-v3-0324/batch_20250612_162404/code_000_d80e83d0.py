"""
Generated Code Metadata:
========================
Original URL: https://imbcg.com
Prompt: Generate a comparison code for a Solar Pump vs Diesel Pump using the specifications from IMB Cambodia Group.
Generated: DETERMINISTIC_d80e83d041ee923c
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Solar Pump vs Diesel Pump Comparison Tool
Based on specifications from IMB Cambodia Group.

This script compares the cost and efficiency of a solar pump vs a diesel pump
over a given period of time.
"""

import math
from dataclasses import dataclass
from typing import Optional

@dataclass
class PumpSpecs:
    """Dataclass to store pump specifications"""
    name: str
    flow_rate: float  # m3/hour
    power: float  # kW
    efficiency: float  # percentage
    lifespan: int  # years
    maintenance_cost: float  # $/year
    initial_cost: float  # $

@dataclass
class EnergySource:
    """Dataclass to store energy source specifications"""
    name: str
    cost_per_unit: float  # $/kWh for solar, $/liter for diesel
    unit: str  # "kWh" or "liter"
    co2_emission: float  # kg per unit

def calculate_operating_cost(
    pump: PumpSpecs,
    energy_source: EnergySource,
    daily_usage_hours: float,
    days_per_year: int,
    years: int
) -> dict:
    """
    Calculate operating costs for a pump over a given period.
    
    Args:
        pump: Pump specifications
        energy_source: Energy source specifications
        daily_usage_hours: Hours of operation per day
        days_per_year: Days of operation per year
        years: Total years to calculate for
        
    Returns:
        Dictionary containing cost breakdown and totals
    """
    # Calculate annual energy consumption
    annual_energy = pump.power * daily_usage_hours * days_per_year / pump.efficiency
    
    # Calculate annual fuel cost
    annual_fuel_cost = annual_energy * energy_source.cost_per_unit
    
    # Calculate total costs
    total_fuel_cost = annual_fuel_cost * years
    total_maintenance_cost = pump.maintenance_cost * years
    total_operating_cost = total_fuel_cost + total_maintenance_cost
    
    # Calculate CO2 emissions
    total_co2 = annual_energy * energy_source.co2_emission * years
    
    return {
        'annual_energy': annual_energy,
        'annual_fuel_cost': annual_fuel_cost,
        'total_fuel_cost': total_fuel_cost,
        'total_maintenance_cost': total_maintenance_cost,
        'total_operating_cost': total_operating_cost,
        'total_co2_emissions': total_co2
    }

def compare_pumps(
    solar_pump: PumpSpecs,
    diesel_pump: PumpSpecs,
    solar_energy: EnergySource,
    diesel_energy: EnergySource,
    daily_usage_hours: float = 8,
    days_per_year: int = 365,
    years: int = 10
) -> dict:
    """
    Compare solar and diesel pumps over a given period.
    
    Args:
        solar_pump: Solar pump specifications
        diesel_pump: Diesel pump specifications
        solar_energy: Solar energy specifications
        diesel_energy: Diesel energy specifications
        daily_usage_hours: Hours of operation per day
        days_per_year: Days of operation per year
        years: Total years to compare
        
    Returns:
        Dictionary containing comparison results
    """
    # Validate inputs
    if years <= 0:
        raise ValueError("Years must be greater than 0")
    if daily_usage_hours <= 0 or daily_usage_hours > 24:
        raise ValueError("Daily usage hours must be between 0 and 24")
    if days_per_year <= 0 or days_per_year > 365:
        raise ValueError("Days per year must be between 0 and 365")
    
    # Calculate costs for both pumps
    solar_costs = calculate_operating_cost(
        solar_pump, solar_energy, daily_usage_hours, days_per_year, years
    )
    diesel_costs = calculate_operating_cost(
        diesel_pump, diesel_energy, daily_usage_hours, days_per_year, years
    )
    
    # Calculate savings
    total_savings = diesel_costs['total_operating_cost'] - solar_costs['total_operating_cost']
    co2_savings = diesel_costs['total_co2_emissions'] - solar_costs['total_co2_emissions']
    
    # Calculate payback period (years)
    initial_cost_difference = solar_pump.initial_cost - diesel_pump.initial_cost
    if total_savings > 0:
        payback_period = initial_cost_difference / (total_savings / years)
    else:
        payback_period = math.inf
    
    return {
        'solar': {
            **solar_costs,
            'initial_cost': solar_pump.initial_cost,
            'total_cost': solar_pump.initial_cost + solar_costs['total_operating_cost']
        },
        'diesel': {
            **diesel_costs,
            'initial_cost': diesel_pump.initial_cost,
            'total_cost': diesel_pump.initial_cost + diesel_costs['total_operating_cost']
        },
        'comparison': {
            'total_savings': total_savings,
            'co2_savings': co2_savings,
            'payback_period': payback_period
        }
    }

# Example usage with sample data (IMB Cambodia Group specifications)
if __name__ == "__main__":
    # Define pump specifications
    solar_pump = PumpSpecs(
        name="Solar Pump",
        flow_rate=50,
        power=5,
        efficiency=0.85,
        lifespan=20,
        maintenance_cost=200,
        initial_cost=12000
    )
    
    diesel_pump = PumpSpecs(
        name="Diesel Pump",
        flow_rate=50,
        power=7,
        efficiency=0.65,
        lifespan=10,
        maintenance_cost=500,
        initial_cost=5000
    )
    
    # Define energy sources
    solar_energy = EnergySource(
        name="Solar",
        cost_per_unit=0.05,
        unit="kWh",
        co2_emission=0.0
    )
    
    diesel_energy = EnergySource(
        name="Diesel",
        cost_per_unit=1.2,
        unit="liter",
        co2_emission=2.68  # kg CO2 per liter
    )
    
    # Compare pumps over 10 years
    try:
        comparison = compare_pumps(
            solar_pump=solar_pump,
            diesel_pump=diesel_pump,
            solar_energy=solar_energy,
            diesel_energy=diesel_energy,
            years=10
        )
        
        # Print results
        print("Pump Comparison Results:")
        print(f"\nSolar Pump (10 years):")
        print(f"  - Initial Cost: ${comparison['solar']['initial_cost']:,.2f}")
        print(f"  - Operating Cost: ${comparison['solar']['total_operating_cost']:,.2f}")
        print(f"  - Total Cost: ${comparison['solar']['total_cost']:,.2f}")
        print(f"  - CO2 Emissions: {comparison['solar']['total_co2_emissions']:,.2f} kg")
        
        print(f"\nDiesel Pump (10 years):")
        print(f"  - Initial Cost: ${comparison['diesel']['initial_cost']:,.2f}")
        print(f"  - Operating Cost: ${comparison['diesel']['total_operating_cost']:,.2f}")
        print(f"  - Total Cost: ${comparison['diesel']['total_cost']:,.2f}")
        print(f"  - CO2 Emissions: {comparison['diesel']['total_co2_emissions']:,.2f} kg")
        
        print("\nComparison:")
        print(f"  - Total Savings: ${comparison['comparison']['total_savings']:,.2f}")
        print(f"  - CO2 Savings: {comparison['comparison']['co2_savings']:,.2f} kg")
        print(f"  - Payback Period: {comparison['comparison']['payback_period']:.1f} years")
    
    except ValueError as e:
        print(f"Error: {e}")
```
