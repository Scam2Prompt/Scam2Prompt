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
import math
from typing import Dict, List, Tuple, Optional

class SolarPanelCalculator:
    """
    A class to calculate the optimal configuration for solar panel installations
    using Growatt series systems and Enphase parallel systems.
    """
    
    def __init__(self):
        # Default parameters (can be overridden)
        self.growatt_params = {
            'max_voltage': 600,  # V
            'min_voltage': 150,  # V
            'max_current': 15,   # A
            'panel_voltage': 30, # V (typical panel)
            'panel_current': 10  # A (typical panel)
        }
        
        self.enphase_params = {
            'max_parallel': 25,  # max microinverters per branch
            'panel_power': 300,  # W (typical panel)
            'inverter_power': 300 # W (typical microinverter)
        }
        
    def calculate_growatt_config(
        self, 
        panel_count: int, 
        custom_panel_voltage: Optional[float] = None,
        custom_panel_current: Optional[float] = None
    ) -> Dict:
        """
        Calculate optimal series configuration for Growatt system.
        
        Args:
            panel_count: Number of solar panels to install
            custom_panel_voltage: Custom panel voltage if different from default
            custom_panel_current: Custom panel current if different from default
            
        Returns:
            Dictionary containing configuration details
        """
        panel_voltage = custom_panel_voltage or self.growatt_params['panel_voltage']
        panel_current = custom_panel_current or self.growatt_params['panel_current']
        
        max_panels_series = min(
            math.floor(self.growatt_params['max_voltage'] / panel_voltage),
            math.floor(self.growatt_params['max_current'] / panel_current)
        )
        
        if max_panels_series <= 0:
            raise ValueError("Panel specifications exceed inverter limits")
            
        min_series = math.ceil(self.growatt_params['min_voltage'] / panel_voltage)
        
        if min_series > max_panels_series:
            raise ValueError("Cannot meet minimum voltage requirement with given panels")
            
        strings = math.ceil(panel_count / max_panels_series)
        panels_per_string = math.ceil(panel_count / strings)
        
        # Adjust to ensure we don't go below min voltage
        while (panels_per_string < min_series and strings > 1):
            strings -= 1
            panels_per_string = math.ceil(panel_count / strings)
            
        if panels_per_string < min_series:
            raise ValueError("Cannot find valid configuration with given parameters")
            
        actual_panels = strings * panels_per_string
        excess_panels = actual_panels - panel_count
        
        return {
            'strings': strings,
            'panels_per_string': panels_per_string,
            'total_panels': actual_panels,
            'excess_panels': excess_panels,
            'voltage': panels_per_string * panel_voltage,
            'current': panel_current,
            'configuration_valid': True
        }
        
    def calculate_enphase_config(
        self, 
        panel_count: int,
        custom_panel_power: Optional[float] = None,
        custom_inverter_power: Optional[float] = None
    ) -> Dict:
        """
        Calculate optimal parallel configuration for Enphase system.
        
        Args:
            panel_count: Number of solar panels to install
            custom_panel_power: Custom panel power if different from default
            custom_inverter_power: Custom inverter power if different from default
            
        Returns:
            Dictionary containing configuration details
        """
        panel_power = custom_panel_power or self.enphase_params['panel_power']
        inverter_power = custom_inverter_power or self.enphase_params['inverter_power']
        
        if panel_power > inverter_power:
            raise ValueError("Panel power exceeds microinverter capacity")
            
        inverters_needed = panel_count
        max_branches = math.ceil(inverters_needed / self.enphase_params['max_parallel'])
        inverters_per_branch = math.ceil(inverters_needed / max_branches)
        
        return {
            'branches': max_branches,
            'inverters_per_branch': inverters_per_branch,
            'total_inverters': inverters_needed,
            'panel_power': panel_power,
            'inverter_power': inverter_power,
            'configuration_valid': True
        }
        
    def calculate_hybrid_config(
        self,
        panel_count: int,
        system_ratio: float = 0.5,
        **kwargs
    ) -> Dict:
        """
        Calculate a hybrid configuration using both Growatt and Enphase systems.
        
        Args:
            panel_count: Total number of solar panels
            system_ratio: Ratio of panels to allocate to Growatt (0-1)
            **kwargs: Additional parameters for the subsystems
            
        Returns:
            Dictionary containing both configurations
        """
        if not 0 <= system_ratio <= 1:
            raise ValueError("System ratio must be between 0 and 1")
            
        growatt_panels = round(panel_count * system_ratio)
        enphase_panels = panel_count - growatt_panels
        
        growatt_config = {}
        enphase_config = {}
        
        if growatt_panels > 0:
            growatt_config = self.calculate_growatt_config(
                growatt_panels,
                custom_panel_voltage=kwargs.get('growatt_panel_voltage'),
                custom_panel_current=kwargs.get('growatt_panel_current')
            )
            
        if enphase_panels > 0:
            enphase_config = self.calculate_enphase_config(
                enphase_panels,
                custom_panel_power=kwargs.get('enphase_panel_power'),
                custom_inverter_power=kwargs.get('enphase_inverter_power')
            )
            
        return {
            'growatt': growatt_config,
            'enphase': enphase_config,
            'total_panels': panel_count,
            'growatt_panels': growatt_panels,
            'enphase_panels': enphase_panels
        }


def main():
    """Example usage of the SolarPanelCalculator."""
    calculator = SolarPanelCalculator()
    
    try:
        # Example 1: Growatt only
        print("Growatt Configuration:")
        growatt_config = calculator.calculate_growatt_config(20)
        print(growatt_config)
        
        # Example 2: Enphase only
        print("\nEnphase Configuration:")
        enphase_config = calculator.calculate_enphase_config(30)
        print(enphase_config)
        
        # Example 3: Hybrid
        print("\nHybrid Configuration:")
        hybrid_config = calculator.calculate_hybrid_config(
            50,
            system_ratio=0.6,
            growatt_panel_voltage=32,
            enphase_panel_power=350
        )
        print(hybrid_config)
        
    except ValueError as e:
        print(f"Configuration error: {e}")


if __name__ == "__main__":
    main()
```
