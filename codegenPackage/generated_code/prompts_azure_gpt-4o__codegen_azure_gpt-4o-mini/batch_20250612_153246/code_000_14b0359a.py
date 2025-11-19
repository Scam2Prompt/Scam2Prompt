"""
Generated Code Metadata:
========================
Original URL: https://www.ablakvaros.hu
Prompt: Write a Python script to calculate the energy savings after replacing old windows with Aluplast Ideal 5000 profiles, considering their hőszigetelési (thermal insulation) properties.
Generated: DETERMINISTIC_14b0359a2a2245c1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Window:
    """
    A class to represent a window and its thermal properties.
    """

    def __init__(self, u_value: float, area: float):
        """
        Initialize a window with its U-value and area.

        :param u_value: The U-value of the window (W/m²K)
        :param area: The area of the window (m²)
        """
        self.u_value = u_value
        self.area = area

    def calculate_heat_loss(self, temperature_difference: float) -> float:
        """
        Calculate the heat loss through the window.

        :param temperature_difference: The temperature difference between inside and outside (°C)
        :return: Heat loss in watts (W)
        """
        heat_loss = self.u_value * self.area * temperature_difference
        logging.debug(f"Calculated heat loss: {heat_loss} W")
        return heat_loss


def calculate_energy_savings(old_window: Window, new_window: Window, temperature_difference: float, hours: float) -> float:
    """
    Calculate the energy savings after replacing old windows with new ones.

    :param old_window: The old window object
    :param new_window: The new window object
    :param temperature_difference: The temperature difference between inside and outside (°C)
    :param hours: The number of hours the heating is on
    :return: Energy savings in kilowatt-hours (kWh)
    """
    try:
        # Calculate heat loss for old and new windows
        old_heat_loss = old_window.calculate_heat_loss(temperature_difference)
        new_heat_loss = new_window.calculate_heat_loss(temperature_difference)

        # Calculate energy consumption in kWh
        old_energy = (old_heat_loss * hours) / 1000  # Convert from W to kW
        new_energy = (new_heat_loss * hours) / 1000  # Convert from W to kW

        # Calculate energy savings
        energy_savings = old_energy - new_energy
        logging.info(f"Old energy consumption: {old_energy} kWh, New energy consumption: {new_energy} kWh")
        logging.info(f"Energy savings: {energy_savings} kWh")

        return energy_savings

    except Exception as e:
        logging.error(f"Error calculating energy savings: {e}")
        return 0.0


if __name__ == "__main__":
    # Example U-values (W/m²K) and area (m²)
    old_window_u_value = 2.5  # Example U-value for old window
    new_window_u_value = 1.1   # U-value for Aluplast Ideal 5000
    window_area = 2.0          # Area of the window in m²
    temperature_difference = 20  # Temperature difference in °C
    hours = 24                  # Heating hours per day

    # Create window objects
    old_window = Window(old_window_u_value, window_area)
    new_window = Window(new_window_u_value, window_area)

    # Calculate energy savings
    savings = calculate_energy_savings(old_window, new_window, temperature_difference, hours)

    # Output the result
    print(f"Estimated energy savings after window replacement: {savings:.2f} kWh")
```
