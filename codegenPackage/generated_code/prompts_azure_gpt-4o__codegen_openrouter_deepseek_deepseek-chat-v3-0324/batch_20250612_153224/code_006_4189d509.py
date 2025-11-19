"""
Generated Code Metadata:
========================
Original URL: https://islaenergeticaautosuficiente.com
Prompt: Develop a simulation script to compare the energy efficiency of different renewable energy configurations (solar, wind, hydroelectric, geothermal) for "islas energéticas" as promoted by Digar Green.
Generated: DETERMINISTIC_4189d5092ccfe14b
Batch ID: 20250612_153224
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
from typing import Dict, List, Tuple
from dataclasses import dataclass
from enum import Enum, auto

class EnergyType(Enum):
    SOLAR = auto()
    WIND = auto()
    HYDRO = auto()
    GEOTHERMAL = auto()

@dataclass
class EnergyConfig:
    """Represents a renewable energy configuration."""
    energy_type: EnergyType
    capacity_kw: float
    efficiency: float  # 0-1
    maintenance_cost_per_kwh: float
    installation_cost: float
    lifespan_years: int

@dataclass
class SimulationResult:
    """Stores results for a single energy configuration simulation."""
    config: EnergyConfig
    total_energy_produced_kwh: float
    total_cost: float
    cost_per_kwh: float
    carbon_footprint_kg: float

class EnergySimulator:
    """Simulates and compares renewable energy configurations."""
    
    def __init__(self, demand_profile_kw: List[float], simulation_years: int = 20):
        """
        Args:
            demand_profile_kw: Hourly energy demand profile in kW for one year
            simulation_years: Number of years to simulate
        """
        self.demand_profile = demand_profile_kw
        self.simulation_years = simulation_years
        self.hours_per_year = 8760  # Non-leap year
        
    def _calculate_energy_produced(self, config: EnergyConfig) -> List[float]:
        """Calculates hourly energy production for a given configuration."""
        hourly_production = []
        
        for demand in self.demand_profile:
            # Simple model: production = capacity * efficiency * capacity factor
            if config.energy_type == EnergyType.SOLAR:
                capacity_factor = 0.15  # Typical for solar
            elif config.energy_type == EnergyType.WIND:
                capacity_factor = 0.35  # Typical for wind
            elif config.energy_type == EnergyType.HYDRO:
                capacity_factor = 0.50  # Typical for hydro
            elif config.energy_type == EnergyType.GEOTHERMAL:
                capacity_factor = 0.70  # Typical for geothermal
            
            production = config.capacity_kw * config.efficiency * capacity_factor
            hourly_production.append(min(production, demand))
        
        return hourly_production
    
    def _calculate_carbon_footprint(self, config: EnergyConfig, total_energy: float) -> float:
        """Calculates total carbon footprint in kg CO2 equivalent."""
        # Values in kg CO2 per kWh (source: IPCC)
        carbon_intensity = {
            EnergyType.SOLAR: 0.045,
            EnergyType.WIND: 0.011,
            EnergyType.HYDRO: 0.024,
            EnergyType.GEOTHERMAL: 0.038
        }
        return total_energy * carbon_intensity[config.energy_type]
    
    def simulate_configuration(self, config: EnergyConfig) -> SimulationResult:
        """Runs simulation for a single energy configuration."""
        try:
            # Calculate hourly production
            hourly_production = self._calculate_energy_produced(config)
            total_energy = sum(hourly_production) * self.simulation_years
            
            # Calculate costs
            maintenance_cost = total_energy * config.maintenance_cost_per_kwh
            installation_cost = config.installation_cost * (self.simulation_years / config.lifespan_years)
            total_cost = maintenance_cost + installation_cost
            
            # Calculate metrics
            cost_per_kwh = total_cost / total_energy if total_energy > 0 else float('inf')
            carbon_footprint = self._calculate_carbon_footprint(config, total_energy)
            
            return SimulationResult(
                config=config,
                total_energy_produced_kwh=total_energy,
                total_cost=total_cost,
                cost_per_kwh=cost_per_kwh,
                carbon_footprint_kg=carbon_footprint
            )
        except Exception as e:
            raise RuntimeError(f"Error simulating configuration {config}: {str(e)}")
    
    def compare_configurations(self, configs: List[EnergyConfig]) -> Dict[str, List[SimulationResult]]:
        """Compares multiple energy configurations."""
        results = []
        
        for config in configs:
            try:
                result = self.simulate_configuration(config)
                results.append(result)
            except RuntimeError as e:
                print(f"Skipping configuration due to error: {e}")
                continue
        
        # Sort by cost per kWh (most efficient first)
        results.sort(key=lambda x: x.cost_per_kwh)
        
        return {"results": results}
    
    def plot_comparison(self, results: List[SimulationResult], output_file: str = None) -> None:
        """Generates comparison plots."""
        if not results:
            raise ValueError("No results to plot")
        
        # Prepare data
        labels = [f"{result.config.energy_type.name}\n({result.config.capacity_kw:.0f} kW)" 
                 for result in results]
        costs = [result.cost_per_kwh for result in results]
        carbon = [result.carbon_footprint_kg / 1000 for result in results]  # Convert to tons
        
        # Create figure
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Cost plot
        ax1.bar(labels, costs, color='tab:blue')
        ax1.set_title('Cost per kWh Comparison')
        ax1.set_ylabel('Cost ($/kWh)')
        ax1.grid(axis='y', linestyle='--')
        
        # Carbon footprint plot
        ax2.bar(labels, carbon, color='tab:green')
        ax2.set_title('Carbon Footprint Comparison')
        ax2.set_ylabel('Carbon Footprint (tons CO2)')
        ax2.grid(axis='y', linestyle='--')
        
        plt.tight_layout()
        
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
        else:
            plt.show()

# Example usage
if __name__ == "__main__":
    # Sample demand profile (simplified: higher during day)
    demand_profile = [50 + 30 * np.sin(2 * np.pi * (i % 24) / 24) for i in range(8760)]
    
    # Define configurations to compare
    configurations = [
        EnergyConfig(
            energy_type=EnergyType.SOLAR,
            capacity_kw=100,
            efficiency=0.85,
            maintenance_cost_per_kwh=0.02,
            installation_cost=150000,
            lifespan_years=25
        ),
        EnergyConfig(
            energy_type=EnergyType.WIND,
            capacity_kw=100,
            efficiency=0.90,
            maintenance_cost_per_kwh=0.03,
            installation_cost=200000,
            lifespan_years=20
        ),
        EnergyConfig(
            energy_type=EnergyType.HYDRO,
            capacity_kw=100,
            efficiency=0.80,
            maintenance_cost_per_kwh=0.01,
            installation_cost=500000,
            lifespan_years=50
        ),
        EnergyConfig(
            energy_type=EnergyType.GEOTHERMAL,
            capacity_kw=100,
            efficiency=0.75,
            maintenance_cost_per_kwh=0.05,
            installation_cost=300000,
            lifespan_years=30
        )
    ]
    
    # Run simulation
    simulator = EnergySimulator(demand_profile)
    comparison = simulator.compare_configurations(configurations)
    
    # Display results
    print("\nEnergy Configuration Comparison:")
    print("=" * 50)
    for result in comparison["results"]:
        print(f"\n{result.config.energy_type.name}:")
        print(f"  Total Energy: {result.total_energy_produced_kwh:,.0f} kWh")
        print(f"  Total Cost: ${result.total_cost:,.0f}")
        print(f"  Cost per kWh: ${result.cost_per_kwh:.4f}")
        print(f"  Carbon Footprint: {result.carbon_footprint_kg:,.0f} kg CO2")
    
    # Generate plots
    simulator.plot_comparison(comparison["results"], "energy_comparison.png")
```
