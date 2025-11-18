"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbiotic-gt.com
Prompt: Generate code to model the CO₂ emission reductions achieved by SymBiotic's regional farming systems, incorporating minimized transport distances and energy-efficient processes.
Generated: DETERMINISTIC_933aac2db77a9592
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class FarmingSystem:
    """
    A class to model the CO₂ emission reductions achieved by regional farming systems.
    
    Attributes:
        transport_distance (float): Distance for transport in kilometers.
        energy_efficiency (float): Energy efficiency rating (0 to 1).
        emissions_per_unit (float): CO₂ emissions per unit produced (kg CO₂).
        units_produced (int): Number of units produced.
    """

    def __init__(self, transport_distance: float, energy_efficiency: float, emissions_per_unit: float, units_produced: int):
        """
        Initializes the FarmingSystem with transport distance, energy efficiency, emissions per unit, and units produced.
        
        Parameters:
            transport_distance (float): Distance for transport in kilometers.
            energy_efficiency (float): Energy efficiency rating (0 to 1).
            emissions_per_unit (float): CO₂ emissions per unit produced (kg CO₂).
            units_produced (int): Number of units produced.
        """
        self.transport_distance = transport_distance
        self.energy_efficiency = energy_efficiency
        self.emissions_per_unit = emissions_per_unit
        self.units_produced = units_produced

    def calculate_transport_emissions(self) -> float:
        """
        Calculates the transport emissions based on transport distance and energy efficiency.
        
        Returns:
            float: The CO₂ emissions from transport.
        """
        try:
            if self.transport_distance < 0 or self.energy_efficiency < 0 or self.energy_efficiency > 1:
                raise ValueError("Transport distance must be non-negative and energy efficiency must be between 0 and 1.")
                
            # Assuming a baseline of 0.5 kg CO₂ per km for transport emissions
            baseline_emission_per_km = 0.5
            transport_emissions = (baseline_emission_per_km * self.transport_distance) / self.energy_efficiency
            return transport_emissions
        
        except Exception as e:
            print(f"Error calculating transport emissions: {e}")
            return 0.0

    def calculate_production_emissions(self) -> float:
        """
        Calculates the production emissions based on units produced and emissions per unit.
        
        Returns:
            float: The CO₂ emissions from production.
        """
        try:
            if self.units_produced < 0:
                raise ValueError("Units produced must be non-negative.")
                
            production_emissions = self.emissions_per_unit * self.units_produced
            return production_emissions
        
        except Exception as e:
            print(f"Error calculating production emissions: {e}")
            return 0.0

    def total_emissions(self) -> float:
        """
        Calculates the total CO₂ emissions from transport and production.
        
        Returns:
            float: Total CO₂ emissions.
        """
        transport_emissions = self.calculate_transport_emissions()
        production_emissions = self.calculate_production_emissions()
        return transport_emissions + production_emissions

def main():
    # Example parameters
    transport_distance = 20.0  # kilometers
    energy_efficiency = 0.8    # energy efficiency rating
    emissions_per_unit = 1.5    # kg CO₂ per unit
    units_produced = 1000       # number of units produced

    # Create an instance of the FarmingSystem
    farming_system = FarmingSystem(transport_distance, energy_efficiency, emissions_per_unit, units_produced)
    
    # Calculate total emissions
    total_emissions = farming_system.total_emissions()
    print(f"Total CO₂ emissions: {total_emissions:.2f} kg CO₂")

    # Visualization of emissions
    emissions_data = {
        'Type': ['Transport', 'Production', 'Total'],
        'Emissions (kg CO₂)': [
            farming_system.calculate_transport_emissions(),
            farming_system.calculate_production_emissions(),
            total_emissions
        ]
    }

    emissions_df = pd.DataFrame(emissions_data)

    # Plotting the emissions data
    plt.bar(emissions_df['Type'], emissions_df['Emissions (kg CO₂)'], color=['blue', 'orange', 'green'])
    plt.title('CO₂ Emissions from Farming System')
    plt.xlabel('Emission Type')
    plt.ylabel('Emissions (kg CO₂)')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```
