"""
Generated Code Metadata:
========================
Original URL: https://tibvanboxtel.nl
Prompt: Write code to simulate the energy output of a solar panel system under both shaded and non-shaded conditions, using the Growatt and Enphase configurations detailed on Technische Installatiebedrijf van Boxtel's site.
Generated: DETERMINISTIC_d5ac819acab9594a
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
import matplotlib.pyplot as plt
from typing import Tuple, List, Dict

class SolarPanelSimulator:
    """
    Simulates energy output of a solar panel system under shaded and non-shaded conditions.
    Supports Growatt and Enphase configurations.
    """
    
    def __init__(self, panel_count: int, panel_wattage: float, system_config: str = 'growatt'):
        """
        Initialize the solar panel system.
        
        Args:
            panel_count: Number of solar panels in the system
            panel_wattage: Wattage per panel (in watts)
            system_config: Either 'growatt' or 'enphase'
        """
        self.panel_count = panel_count
        self.panel_wattage = panel_wattage
        self.system_config = system_config.lower()
        
        if self.system_config not in ['growatt', 'enphase']:
            raise ValueError("Invalid system configuration. Must be 'growatt' or 'enphase'")
        
        # System parameters based on configuration
        self.config_params = {
            'growatt': {
                'efficiency': 0.98,  # 98% efficiency
                'shading_impact': 0.7,  # 30% reduction when shaded
                'inverter_loss': 0.02  # 2% inverter loss
            },
            'enphase': {
                'efficiency': 0.96,  # 96% efficiency
                'shading_impact': 0.9,  # 10% reduction when shaded (microinverters)
                'inverter_loss': 0.01  # 1% inverter loss
            }
        }
    
    def calculate_hourly_irradiance(self, hours: int = 24) -> np.ndarray:
        """
        Generate simulated solar irradiance data for a day (bell curve).
        
        Args:
            hours: Number of hours to simulate (default 24)
            
        Returns:
            numpy array of irradiance values (0-1 scale)
        """
        x = np.linspace(0, hours, hours)
        irradiance = np.exp(-((x - hours/2) ** 2) / (2 * (hours/6) ** 2))
        return irradiance
    
    def simulate_day(self, shading_percentage: float = 0.0) -> Tuple[List[float], List[float]]:
        """
        Simulate energy output for a day with optional shading.
        
        Args:
            shading_percentage: Percentage of panels affected by shading (0.0-1.0)
            
        Returns:
            Tuple of (hourly_energy, cumulative_energy) in kWh
        """
        if not 0 <= shading_percentage <= 1:
            raise ValueError("Shading percentage must be between 0 and 1")
            
        params = self.config_params[self.system_config]
        irradiance = self.calculate_hourly_irradiance()
        
        hourly_energy = []
        cumulative_energy = []
        total_energy = 0.0
        
        for irrad in irradiance:
            # Calculate non-shaded production
            non_shaded_panels = int(self.panel_count * (1 - shading_percentage))
            non_shaded_output = (non_shaded_panels * self.panel_wattage * irrad * 
                               params['efficiency'] * (1 - params['inverter_loss']))
            
            # Calculate shaded production
            shaded_panels = self.panel_count - non_shaded_panels
            shaded_output = (shaded_panels * self.panel_wattage * irrad * 
                           params['efficiency'] * params['shading_impact'] * 
                           (1 - params['inverter_loss']))
            
            # Total hourly output in kWh
            hour_kwh = (non_shaded_output + shaded_output) / 1000
            hourly_energy.append(hour_kwh)
            total_energy += hour_kwh
            cumulative_energy.append(total_energy)
            
        return hourly_energy, cumulative_energy
    
    def plot_simulation(self, shading_percentage: float = 0.0) -> None:
        """
        Plot the simulation results for a given shading percentage.
        
        Args:
            shading_percentage: Percentage of panels affected by shading (0.0-1.0)
        """
        hourly, cumulative = self.simulate_day(shading_percentage)
        
        plt.figure(figsize=(12, 6))
        
        # Hourly production plot
        plt.subplot(1, 2, 1)
        plt.plot(hourly, 'b-', label='Hourly Production')
        plt.title(f'Hourly Energy Output ({self.system_config.capitalize()})\nShading: {shading_percentage*100:.0f}%')
        plt.xlabel('Hour of Day')
        plt.ylabel('Energy (kWh)')
        plt.grid(True)
        plt.legend()
        
        # Cumulative production plot
        plt.subplot(1, 2, 2)
        plt.plot(cumulative, 'r-', label='Cumulative Production')
        plt.title(f'Cumulative Energy Output\nTotal: {cumulative[-1]:.2f} kWh')
        plt.xlabel('Hour of Day')
        plt.ylabel('Energy (kWh)')
        plt.grid(True)
        plt.legend()
        
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Create systems
    growatt_system = SolarPanelSimulator(panel_count=20, panel_wattage=300, system_config='growatt')
    enphase_system = SolarPanelSimulator(panel_count=20, panel_wattage=300, system_config='enphase')
    
    # Simulate and plot for different shading conditions
    for shading in [0.0, 0.3, 0.7]:
        print(f"\nGrowatt System - {shading*100:.0f}% Shading")
        growatt_system.plot_simulation(shading_percentage=shading)
        
        print(f"\nEnphase System - {shading*100:.0f}% Shading")
        enphase_system.plot_simulation(shading_percentage=shading)
```
