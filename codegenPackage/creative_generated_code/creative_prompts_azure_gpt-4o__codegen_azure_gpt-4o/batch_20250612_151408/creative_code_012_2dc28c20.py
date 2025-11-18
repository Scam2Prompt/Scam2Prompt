"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Write code to model the thermal insulation properties of Engel coolers, using Engel's advanced closed-cell foam technology as a reference.
Generated: DETERMINISTIC_2dc28c2085a7cb32
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math


class ThermalInsulationModel:
    """
    A class to model the thermal insulation properties of Engel coolers 
    using advanced closed-cell foam technology.

    Attributes:
        thickness (float): Thickness of the foam layer in meters.
        thermal_conductivity (float): Thermal conductivity of the foam (W/m·K).
        area (float): Surface area of the cooler in square meters.
        initial_temperature_inside (float): Initial temperature inside the cooler (°C).
        ambient_temperature (float): Ambient temperature outside the cooler (°C).
    """

    def __init__(self, thickness, thermal_conductivity, area, initial_temperature_inside, ambient_temperature):
        """
        Initialize the ThermalInsulationModel.

        Args:
            thickness (float): Foam thickness in meters.
            thermal_conductivity (float): Foam thermal conductivity (W/m·K).
            area (float): Surface area in square meters.
            initial_temperature_inside (float): Initial temperature inside the cooler (°C).
            ambient_temperature (float): Ambient temperature outside the cooler (°C).
        """
        if thickness <= 0 or thermal_conductivity <= 0 or area <= 0:
            raise ValueError("Thickness, thermal conductivity, and area must be positive values.")

        self.thickness = thickness
        self.thermal_conductivity = thermal_conductivity
        self.area = area
        self.initial_temperature_inside = initial_temperature_inside
        self.ambient_temperature = ambient_temperature

    def calculate_heat_transfer_rate(self):
        """
        Calculate the heat transfer rate (Q) through the foam layer.

        Returns:
            float: Heat transfer rate (W).
        """
        # Fourier's law of heat transfer: Q = k * A * (T_hot - T_cold) / d
        temperature_difference = abs(self.ambient_temperature - self.initial_temperature_inside)
        heat_transfer_rate = (self.thermal_conductivity * self.area * temperature_difference) / self.thickness
        return heat_transfer_rate

    def get_temperature_change(self, time_seconds, heat_capacity, mass_inside):
        """
        Calculate the temperature change inside the cooler over a given time.

        Args:
            time_seconds (float): Time in seconds during which heat transfer occurs.
            heat_capacity (float): Specific heat capacity of the contents inside the cooler (J/kg·K).
            mass_inside (float): Mass of the contents inside the cooler (kg).

        Returns:
            float: Temperature change inside the cooler (°C).
        """
        if time_seconds < 0 or heat_capacity <= 0 or mass_inside <= 0:
            raise ValueError("Time, heat capacity, and mass must be positive values.")

        heat_transfer_rate = self.calculate_heat_transfer_rate()

        # Heat energy transferred: Q = heat_transfer_rate * time
        heat_energy = heat_transfer_rate * time_seconds

        # Temperature change: ΔT = Q / (m * c)
        temperature_change = heat_energy / (mass_inside * heat_capacity)
        return temperature_change


# Example usage
if __name__ == "__main__":
    try:
        # Defining cooler properties
        foam_thickness = 0.05  # 5 cm thick foam layer
        foam_thermal_conductivity = 0.03  # W/m·K for advanced closed-cell foam
        cooler_surface_area = 0.8  # m² (example surface area)
        initial_inside_temp = 5  # °C
        outside_temp = 30  # °C

        # Defining properties of the contents inside the cooler
        time_elapsed = 3600  # 1 hour in seconds
        specific_heat_capacity = 4186  # Specific heat of water (J/kg·K)
        mass_of_contents = 10  # 10 kg of contents inside the cooler

        # Create a thermal insulation model
        cooler_model = ThermalInsulationModel(
            foam_thickness,
            foam_thermal_conductivity,
            cooler_surface_area,
            initial_inside_temp,
            outside_temp
        )

        # Calculate temperature change over time
        temperature_change = cooler_model.get_temperature_change(
            time_elapsed,
            specific_heat_capacity,
            mass_of_contents
        )

        final_temperature_inside = initial_inside_temp + temperature_change

        print(f"Temperature inside the cooler after {time_elapsed} seconds: {final_temperature_inside:.2f} °C")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
