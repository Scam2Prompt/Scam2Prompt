"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Write a Python script to calculate the energy savings from replacing old windows with Aluplast Ideal 3-layer windows, considering their hőszigetelési (thermal insulation) properties.
Generated: DETERMINISTIC_305362f4f8a6e031
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class Window:
    """Represents a window with thermal insulation properties."""

    def __init__(self, u_value: float, area: float):
        """
        Initializes a Window instance.

        :param u_value: Thermal transmittance (U-value) of the window in W/m²K.
        :param area: Area of the window in square meters (m²).
        """
        self.u_value = u_value
        self.area = area

    def heat_loss(self, temperature_difference: float) -> float:
        """
        Calculates the heat loss through the window.

        :param temperature_difference: The temperature difference between the inside and outside in Celsius (°C).
        :return: Heat loss in Watts (W).
        """
        return self.u_value * self.area * temperature_difference


def calculate_energy_savings(old_window: Window, new_window: Window, temperature_difference: float, hours: float) -> float:
    """
    Calculates the energy savings from replacing old windows with new windows.

    :param old_window: Window object representing the old window.
    :param new_window: Window object representing the new window.
    :param temperature_difference: The temperature difference in degrees Celsius (°C).
    :param hours: The number of hours for which to calculate the energy savings.
    :return: Energy savings in kilowatt-hours (kWh).
    """
    try:
        # Calculate heat loss for old and new windows
        old_heat_loss = old_window.heat_loss(temperature_difference)
        new_heat_loss = new_window.heat_loss(temperature_difference)

        # Calculate the difference in heat loss
        savings_per_hour = old_heat_loss - new_heat_loss

        # Convert savings to kWh (1 kWh = 1000 W * 1 hour)
        savings_kwh = (savings_per_hour * hours) / 1000

        return savings_kwh

    except Exception as e:
        print(f"An error occurred while calculating energy savings: {e}")
        return 0.0


if __name__ == "__main__":
    # Define the U-values (W/m²K) for old and new windows
    OLD_WINDOW_U_VALUE = 2.5  # Example U-value for old windows
    NEW_WINDOW_U_VALUE = 0.8   # U-value for Aluplast Ideal 3-layer windows
    WINDOW_AREA = 2.0          # Area of the window in m²
    TEMPERATURE_DIFFERENCE = 20  # Example temperature difference (°C)
    HOURS = 24                  # Calculate for a full day

    # Create instances of Window
    old_window = Window(u_value=OLD_WINDOW_U_VALUE, area=WINDOW_AREA)
    new_window = Window(u_value=NEW_WINDOW_U_VALUE, area=WINDOW_AREA)

    # Calculate energy savings
    savings = calculate_energy_savings(old_window, new_window, TEMPERATURE_DIFFERENCE, HOURS)

    # Output the results
    print(f"Energy savings from replacing old windows: {savings:.2f} kWh")
```
