"""
Generated Code Metadata:
========================
Original URL: https://www.chicoelectric.com
Prompt: Write Python code to simulate the energy savings of installing microturbines, referencing Chico Electric's use of microturbines for distributed power applications.
Generated: DETERMINISTIC_403d228f35d4d72b
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Microturbine Energy Savings Simulation

This script simulates the energy savings from installing microturbines for distributed power applications,
inspired by Chico Electric's implementation. It calculates potential cost savings, energy generation,
and environmental impact based on user inputs.

Key Features:
- Energy generation calculation based on microturbine specifications
- Cost savings estimation compared to grid power
- Environmental impact (CO2 reduction) calculation
- Simple financial analysis with payback period
"""

import math
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class MicroturbineSpec:
    """Dataclass to store microturbine specifications"""
    model: str
    capacity_kw: float  # Rated capacity in kW
    efficiency: float   # Conversion efficiency (0-1)
    cost: float         # Installation cost in USD
    lifespan_years: int # Expected lifespan
    maintenance_rate: float  # Annual maintenance cost as % of installation cost

@dataclass
class EnergyProfile:
    """Dataclass to store energy usage profile"""
    avg_daily_usage_kwh: float
    peak_demand_kw: float
    utility_rate_per_kwh: float
    demand_charge_per_kw: float  # Monthly demand charge
    carbon_intensity: float      # kg CO2 per kWh from grid

class MicroturbineSimulator:
    """Simulates energy savings from microturbine installation"""
    
    def __init__(self, turbine_spec: MicroturbineSpec, energy_profile: EnergyProfile):
        self.turbine = turbine_spec
        self.profile = energy_profile
        self.validate_inputs()
        
    def validate_inputs(self):
        """Validate input parameters"""
        if not (0 < self.turbine.efficiency <= 1):
            raise ValueError("Efficiency must be between 0 and 1")
        if self.turbine.capacity_kw <= 0:
            raise ValueError("Capacity must be positive")
        if self.profile.avg_daily_usage_kwh <= 0:
            raise ValueError("Energy usage must be positive")
    
    def calculate_annual_energy_generation(self, capacity_factor: float = 0.85) -> float:
        """
        Calculate annual energy generation in kWh
        Args:
            capacity_factor: Utilization factor (0-1)
        Returns:
            Annual energy generation in kWh
        """
        if not (0 <= capacity_factor <= 1):
            raise ValueError("Capacity factor must be between 0 and 1")
            
        annual_hours = 8760
        return (self.turbine.capacity_kw * 
                capacity_factor * 
                annual_hours * 
                self.turbine.efficiency)
    
    def calculate_annual_cost_savings(self) -> dict:
        """Calculate annual cost savings from microturbine installation"""
        energy_generated = self.calculate_annual_energy_generation()
        energy_cost_savings = energy_generated * self.profile.utility_rate_per_kwh
        
        # Estimate demand charge savings (assuming 50% peak shaving)
        demand_savings = (self.turbine.capacity_kw * 0.5 * 
                          self.profile.demand_charge_per_kw * 12)
        
        total_savings = energy_cost_savings + demand_savings
        maintenance_cost = self.turbine.cost * self.turbine.maintenance_rate
        
        return {
            'energy_savings': energy_cost_savings,
            'demand_savings': demand_savings,
            'maintenance_cost': maintenance_cost,
            'net_savings': total_savings - maintenance_cost
        }
    
    def calculate_environmental_impact(self) -> dict:
        """Calculate annual CO2 emissions reduction"""
        energy_generated = self.calculate_annual_energy_generation()
        co2_reduction = energy_generated * self.profile.carbon_intensity
        
        return {
            'co2_reduction_kg': co2_reduction,
            'equivalent_trees': co2_reduction / 21.77  # kg CO2 absorbed per tree annually
        }
    
    def calculate_payback_period(self) -> float:
        """Calculate simple payback period in years"""
        annual_savings = self.calculate_annual_cost_savings()['net_savings']
        if annual_savings <= 0:
            return float('inf')
        return self.turbine.cost / annual_savings
    
    def generate_report(self) -> dict:
        """Generate comprehensive simulation report"""
        energy_gen = self.calculate_annual_energy_generation()
        cost_savings = self.calculate_annual_cost_savings()
        environmental = self.calculate_environmental_impact()
        payback = self.calculate_payback_period()
        
        return {
            'timestamp': datetime.now().isoformat(),
            'turbine_spec': {
                'model': self.turbine.model,
                'capacity_kw': self.turbine.capacity_kw,
                'efficiency': self.turbine.efficiency,
                'cost': self.turbine.cost,
                'lifespan_years': self.turbine.lifespan_years
            },
            'energy_profile': {
                'avg_daily_usage_kwh': self.profile.avg_daily_usage_kwh,
                'peak_demand_kw': self.profile.peak_demand_kw,
                'utility_rate': self.profile.utility_rate_per_kwh
            },
            'annual_energy_generation_kwh': energy_gen,
            'annual_cost_savings': cost_savings,
            'annual_environmental_impact': environmental,
            'financial_metrics': {
                'payback_period_years': payback,
                'roi_percentage': (cost_savings['net_savings'] * self.turbine.lifespan_years / 
                                  self.turbine.cost * 100) if payback != float('inf') else 0
            }
        }

def run_simulation_example():
    """Example simulation with sample data"""
    try:
        # Sample microturbine specification (similar to Capstone C65)
        turbine = MicroturbineSpec(
            model="C65",
            capacity_kw=65,
            efficiency=0.33,
            cost=150000,
            lifespan_years=15,
            maintenance_rate=0.02
        )
        
        # Sample energy profile (commercial building)
        profile = EnergyProfile(
            avg_daily_usage_kwh=1200,
            peak_demand_kw=150,
            utility_rate_per_kwh=0.15,
            demand_charge_per_kw=15,
            carbon_intensity=0.5  # kg CO2 per kWh
        )
        
        simulator = MicroturbineSimulator(turbine, profile)
        report = simulator.generate_report()
        
        # Print summary of results
        print("\nMicroturbine Energy Savings Simulation Results")
        print("="*50)
        print(f"Turbine Model: {report['turbine_spec']['model']}")
        print(f"Annual Generation: {report['annual_energy_generation_kwh']:,.0f} kWh")
        print(f"Annual Cost Savings: ${report['annual_cost_savings']['net_savings']:,.2f}")
        print(f"CO2 Reduction: {report['annual_environmental_impact']['co2_reduction_kg']:,.0f} kg/year")
        print(f"Equivalent Trees Planted: {report['annual_environmental_impact']['equivalent_trees']:,.0f}")
        print(f"Payback Period: {report['financial_metrics']['payback_period_years']:.1f} years")
        print(f"ROI over Lifespan: {report['financial_metrics']['roi_percentage']:.1f}%")
        
    except ValueError as e:
        print(f"Error in simulation: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    run_simulation_example()
```
