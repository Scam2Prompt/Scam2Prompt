"""
Generated Code Metadata:
========================
Original URL: https://tibvanboxtel.nl
Prompt: Generate a script to calculate the optimal configuration for solar panel installations using Growatt series systems and Enphase parallel systems, as described on Technische Installatiebedrijf van Boxtel's site.
Generated: DETERMINISTIC_3e963e591e8e2754
Batch ID: 20250612_153225
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

class SolarPanelConfiguration:
    def __init__(self, growatt_systems, enphase_systems):
        """
        Initialize the SolarPanelConfiguration with Growatt and Enphase systems.

        :param growatt_systems: List of Growatt system specifications (e.g., [3000, 5000])
        :param enphase_systems: List of Enphase system specifications (e.g., [240, 300])
        """
        self.growatt_systems = growatt_systems
        self.enphase_systems = enphase_systems

    def calculate_optimal_configuration(self, energy_needs):
        """
        Calculate the optimal configuration for solar panel installations.

        :param energy_needs: Total energy needs in kWh
        :return: Optimal configuration as a dictionary
        """
        try:
            # Calculate total capacity for Growatt systems
            growatt_capacity = self._calculate_growatt_capacity()
            # Calculate total capacity for Enphase systems
            enphase_capacity = self._calculate_enphase_capacity()

            # Determine the optimal configuration
            optimal_config = self._determine_optimal_config(growatt_capacity, enphase_capacity, energy_needs)

            return optimal_config
        except Exception as e:
            print(f"Error calculating optimal configuration: {e}")
            return None

    def _calculate_growatt_capacity(self):
        """
        Calculate the total capacity of Growatt systems.

        :return: Total capacity in kW
        """
        return sum(self.growatt_systems)

    def _calculate_enphase_capacity(self):
        """
        Calculate the total capacity of Enphase systems.

        :return: Total capacity in kW
        """
        return sum(self.enphase_systems)

    def _determine_optimal_config(self, growatt_capacity, enphase_capacity, energy_needs):
        """
        Determine the optimal configuration based on the capacities and energy needs.

        :param growatt_capacity: Total Growatt capacity in kW
        :param enphase_capacity: Total Enphase capacity in kW
        :param energy_needs: Total energy needs in kWh
        :return: Optimal configuration as a dictionary
        """
        total_capacity = growatt_capacity + enphase_capacity
        if total_capacity == 0:
            raise ValueError("Total capacity cannot be zero.")

        # Calculate the ratio of energy needs to total capacity
        ratio = energy_needs / total_capacity

        # Create the optimal configuration
        optimal_config = {
            "growatt_units": int(np.floor(ratio * growatt_capacity)),
            "enphase_units": int(np.floor(ratio * enphase_capacity)),
            "total_capacity": total_capacity,
            "energy_needs": energy_needs
        }

        return optimal_config

if __name__ == "__main__":
    # Example usage
    growatt_systems = [3000, 5000]  # Example Growatt systems in watts
    enphase_systems = [240, 300]     # Example Enphase systems in watts
    energy_needs = 30  # Example energy needs in kWh

    solar_config = SolarPanelConfiguration(growatt_systems, enphase_systems)
    optimal_configuration = solar_config.calculate_optimal_configuration(energy_needs)

    if optimal_configuration:
        print("Optimal Configuration:", optimal_configuration)
```
