"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Write Python code to simulate the ice preservation performance of Engel UltraLite coolers, incorporating features like closed-cell foam insulation and tapered drainage channels.
Generated: DETERMINISTIC_8049ed7acb47bd12
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class EngelUltraLiteCooler:
    """
    A class to simulate the ice preservation performance of Engel UltraLite coolers.
    Attributes:
        insulation_thickness (float): Thickness of the closed-cell foam insulation in meters.
        ambient_temperature (float): The external temperature in degrees Celsius.
        ice_mass (float): Mass of the ice in kilograms.
        drainage_channels (float): Effectiveness of the tapered drainage channels (0 to 1).
    """

    def __init__(self, insulation_thickness, ambient_temperature, ice_mass, drainage_channels):
        """
        Initializes the EngelUltraLiteCooler with the given parameters.

        Parameters:
            insulation_thickness (float): Thickness of closed-cell foam insulation.
            ambient_temperature (float): The external ambient temperature.
            ice_mass (float): Mass of the ice in kg.
            drainage_channels (float): Effectiveness of drainage channels (0 to 1).
        """
        self.insulation_thickness = insulation_thickness
        self.ambient_temperature = ambient_temperature
        self.ice_mass = ice_mass
        self.drainage_channels = drainage_channels

    def calculate_heat_transfer(self):
        """
        Calculate the rate of heat transfer through the cooler based on 
        insulation thickness and ambient temperature.

        Returns:
            float: The heat transfer rate in watts.
        """
        thermal_conductivity = 0.03  # W/mK for closed-cell foam insulation
        area = 1.0  # Assume 1m² surface area for simplification
        heat_transfer_rate = (thermal_conductivity * area * 
                              (self.ambient_temperature - 0)) / self.insulation_thickness
        return heat_transfer_rate

    def simulate_ice_melting(self, time_hours):
        """
        Simulate the melting of ice over a specified time period.

        Parameters:
            time_hours (float): The time duration for simulation in hours.

        Returns:
            float: Remaining mass of ice after the given time period.
        """
        try:
            # Convert time from hours to seconds
            time_seconds = time_hours * 3600
            heat_transfer_rate = self.calculate_heat_transfer()

            # Specific heat of ice (2.09 kJ/kgK) and latent heat of fusion (334 kJ/kg)
            specific_heat_ice = 2090  # J/kgK
            latent_heat_fusion = 334000  # J/kg

            # Total heat absorbed by the ice in Joules
            total_heat_absorbed = heat_transfer_rate * time_seconds

            # Calculate mass of ice melted
            mass_melted = total_heat_absorbed / latent_heat_fusion

            # Remaining mass of ice
            remaining_mass = self.ice_mass - mass_melted
            return max(remaining_mass, 0.0)

        except Exception as e:
            print(f"An error occurred during simulation: {e}")
            return self.ice_mass  # Return initial mass in case of error

    def plot_ice_melting(self, duration_hours):
        """
        Plot the ice melting over the specified duration.

        Parameters:
            duration_hours (float): The total duration for the simulation in hours.
        """
        time_steps = np.linspace(0, duration_hours, num=100)
        remaining_ice = [self.simulate_ice_melting(t) for t in time_steps]

        plt.figure(figsize=(10, 5))
        plt.plot(time_steps, remaining_ice, label='Remaining Ice Mass', color='blue')
        plt.xlabel('Time (hours)')
        plt.ylabel('Remaining Ice Mass (kg)')
        plt.title('Ice Preservation Performance of Engel UltraLite Cooler')
        plt.axhline(0, color='red', linestyle='--', label='No Ice Remaining')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage:
if __name__ == "__main__":
    try:
        cooler = EngelUltraLiteCooler(insulation_thickness=0.05, ambient_temperature=30, 
                                       ice_mass=5, drainage_channels=0.8)
        cooler.plot_ice_melting(duration_hours=24)
        
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
