"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: Write Python code to simulate the ice preservation performance of Engel UltraLite coolers, incorporating features like closed-cell foam insulation and tapered drainage channels.
Generated: DETERMINISTIC_8049ed7acb47bd12
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Constants
class Constants:
    """Physical constants used in the simulation."""
    SPECIFIC_HEAT_CAPACITY_WATER = 4186  # J/kg°C
    DENSITY_WATER = 1000  # kg/m³
    LATENT_HEAT_FUSION_WATER = 334000  # J/kg
    THERMAL_CONDUCTIVITY_FOAM = 0.033  # W/m°C
    THERMAL_CONDUCTIVITY_WATER = 0.6  # W/m°C
    TEMPERATURE_AMBIENT = 25  # °C

class Cooler:
    """Simulates the Engel UltraLite cooler performance."""
    def __init__(self, 
                 insulation_thickness, 
                 cooler_volume, 
                 initial_temperature, 
                 ambient_temperature=Constants.TEMPERATURE_AMBIENT):
        """
        Initializes the cooler.

        Args:
        - insulation_thickness (float): Thickness of the insulation in meters.
        - cooler_volume (float): Volume of the cooler in cubic meters.
        - initial_temperature (float): Initial temperature of the contents in °C.
        - ambient_temperature (float): Ambient temperature in °C. Defaults to 25.
        """
        self.insulation_thickness = insulation_thickness
        self.cooler_volume = cooler_volume
        self.initial_temperature = initial_temperature
        self.ambient_temperature = ambient_temperature

    def model(self, temperature, time):
        """
        Model describing the temperature change over time.

        Args:
        - temperature (float): Current temperature in °C.
        - time (float): Current time in seconds.

        Returns:
        - dT/dt (float): Rate of temperature change.
        """
        # Heat transfer through insulation
        heat_transfer_coefficient = self.thermal_resistance()
        temperature_difference = temperature - self.ambient_temperature
        dT_dt = -heat_transfer_coefficient * temperature_difference / (self.cooler_volume * Constants.DENSITY_WATER * Constants.SPECIFIC_HEAT_CAPACITY_WATER)
        return dT_dt

    def thermal_resistance(self):
        """
        Calculates the thermal resistance of the insulation.

        Returns:
        - thermal_resistance (float): Thermal resistance in °C/W.
        """
        # Assuming A = 1 m² for simplicity
        thermal_resistance = self.insulation_thickness / (Constants.THERMAL_CONDUCTIVITY_FOAM * 1)
        return 1 / thermal_resistance

    def simulate(self, time_points):
        """
        Simulates the temperature change over time.

        Args:
        - time_points (numpy.array): Array of time points.

        Returns:
        - temperature_over_time (numpy.array): Temperature at each time point.
        """
        temperature_over_time = odeint(self.model, self.initial_temperature, time_points)
        return temperature_over_time

def tapered_drainage_channel_effectiveness(temperature, channel_angle):
    """
    Calculates the effectiveness of the tapered drainage channel.

    Args:
    - temperature (float): Current temperature in °C.
    - channel_angle (float): Angle of the channel in degrees.

    Returns:
    - effectiveness (float): Effectiveness of the channel (0-1).
    """
    # Simple model for demonstration; real model would require more data
    effectiveness = np.sin(np.radians(channel_angle)) * (1 - (temperature / 100))
    return effectiveness

def main():
    # Example usage
    cooler = Cooler(insulation_thickness=0.05, 
                    cooler_volume=0.1, 
                    initial_temperature=0)

    time_points = np.linspace(0, 86400, 100)  # 24 hours
    temperature_over_time = cooler.simulate(time_points)

    plt.plot(time_points / 3600, temperature_over_time)
    plt.xlabel('Time (hours)')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature over Time')
    plt.show()

    # Tapered drainage channel effectiveness
    channel_angle = 30  # degrees
    effectiveness = tapered_drainage_channel_effectiveness(cooler.initial_temperature, channel_angle)
    print(f"Effectiveness of tapered drainage channel: {effectiveness:.2f}")

if __name__ == "__main__":
    main()
```
