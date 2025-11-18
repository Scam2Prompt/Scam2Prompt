"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tibvanboxtel.nl
Prompt: Generate a script to calculate the optimal configuration for solar panel installations using Growatt series systems and Enphase parallel systems, as described on Technische Installatiebedrijf van Boxtel's site.
Generated: DETERMINISTIC_3e963e591e8e2754
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
from typing import List, Tuple, Dict

class SolarPanelConfiguration:
    """A class to calculate optimal configurations for solar panel installations."""
    
    def __init__(self, growatt_max_units: int, enphase_max_units: int):
        """
        Initializes the SolarPanelConfiguration with max units for Growatt and Enphase systems.
        
        :param growatt_max_units: Maximum number of Growatt units allowed.
        :param enphase_max_units: Maximum number of Enphase units allowed.
        """
        self.growatt_max_units = growatt_max_units
        self.enphase_max_units = enphase_max_units

    def calculate_optimal_configuration(self, load_demand: float) -> Dict[str, Tuple[int, float]]:
        """
        Calculates the optimal configuration for solar panel installations.
        
        :param load_demand: The total electrical load demand in kWh.
        :return: A dictionary with the optimal configuration for Growatt and Enphase systems.
        """
        try:
            # Assuming each Growatt unit provides 1.5 kWh and each Enphase unit provides 1.2 kWh
            growatt_capacity = 1.5
            enphase_capacity = 1.2
            
            # Calculate maximum possible units based on load demand
            max_growatt_units = math.ceil(load_demand / growatt_capacity)
            max_enphase_units = math.ceil(load_demand / enphase_capacity)

            # Constrain the maximum units to the specified limits
            optimal_growatt_units = min(max_growatt_units, self.growatt_max_units)
            optimal_enphase_units = min(max_enphase_units, self.enphase_max_units)

            # Calculate total energy produced
            total_energy_growatt = optimal_growatt_units * growatt_capacity
            total_energy_enphase = optimal_enphase_units * enphase_capacity
            
            return {
                "Growatt": (optimal_growatt_units, total_energy_growatt),
                "Enphase": (optimal_enphase_units, total_energy_enphase)
            }

        except Exception as e:
            print(f"Error calculating optimal configuration: {e}")
            return {}

def main():
    """Main function to execute the solar panel configuration calculation."""
    # Example usage with a specified load demand
    load_demand = 20.0  # in kWh
    growatt_max_units = 10  # Maximum Growatt units
    enphase_max_units = 15  # Maximum Enphase units

    # Create an instance of the SolarPanelConfiguration class
    config = SolarPanelConfiguration(growatt_max_units, enphase_max_units)

    # Calculate the optimal configuration
    optimal_config = config.calculate_optimal_configuration(load_demand)

    # Display the results
    if optimal_config:
        print("Optimal Solar Panel Configuration:")
        for system, (units, total_energy) in optimal_config.items():
            print(f"{system}: {units} units, Total Energy: {total_energy:.2f} kWh")

if __name__ == "__main__":
    main()
```
