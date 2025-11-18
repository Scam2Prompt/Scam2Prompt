"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.dexodoor.com
Prompt: Write a Python script to simulate the energy efficiency benefits of UPVC windows and doors, referencing the features described on the Dexodoor website.
Generated: DETERMINISTIC_541c29339af63ca5
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import math


class WindowDoorEfficiencySimulator:
    """
    A class to simulate the energy efficiency benefits of UPVC windows and doors.
    """

    def __init__(self, area, u_value, hours_of_use):
        """
        Initializes the simulator with the given parameters.

        :param area: The area of the window/door in square meters.
        :param u_value: The U-value of the window/door (W/m²K).
        :param hours_of_use: The number of hours the window/door is exposed to temperature difference.
        """
        self.area = area
        self.u_value = u_value
        self.hours_of_use = hours_of_use

    def calculate_heat_loss(self, temperature_inside, temperature_outside):
        """
        Calculates the heat loss through the window/door.

        :param temperature_inside: The indoor temperature in degrees Celsius.
        :param temperature_outside: The outdoor temperature in degrees Celsius.
        :return: Heat loss in watts.
        """
        if not self._validate_temperatures(temperature_inside, temperature_outside):
            raise ValueError("Temperatures must be numeric values")
        
        temperature_difference = temperature_inside - temperature_outside
        heat_loss = self.u_value * self.area * temperature_difference
        return heat_loss

    def _validate_temperatures(self, inside, outside):
        """
        Validates the temperature inputs.

        :param inside: Indoor temperature.
        :param outside: Outdoor temperature.
        :return: True if valid, False otherwise.
        """
        return isinstance(inside, (int, float)) and isinstance(outside, (int, float))

    def calculate_energy_cost(self, heat_loss, energy_cost_per_kWh):
        """
        Calculates the energy cost based on heat loss.

        :param heat_loss: The heat loss in watts.
        :param energy_cost_per_kWh: The cost of energy per kilowatt-hour.
        :return: Total energy cost for the specified hours of use.
        """
        if energy_cost_per_kWh <= 0:
            raise ValueError("Energy cost per kWh must be greater than zero")

        # Convert watts to kilowatts
        heat_loss_kW = heat_loss / 1000
        total_energy_used = heat_loss_kW * self.hours_of_use  # energy used in kWh
        total_cost = total_energy_used * energy_cost_per_kWh
        return total_cost

    def simulate(self, temperature_inside, temperature_outside, energy_cost_per_kWh):
        """
        Simulates the overall energy efficiency benefit.

        :param temperature_inside: The indoor temperature in degrees Celsius.
        :param temperature_outside: The outdoor temperature in degrees Celsius.
        :param energy_cost_per_kWh: The cost of energy per kilowatt-hour.
        :return: A dictionary with heat loss and total energy cost.
        """
        heat_loss = self.calculate_heat_loss(temperature_inside, temperature_outside)
        total_cost = self.calculate_energy_cost(heat_loss, energy_cost_per_kWh)

        return {
            "heat_loss_W": heat_loss,
            "energy_cost_total": total_cost
        }


if __name__ == "__main__":
    # Example usage of the simulator
    try:
        area = 2.5  # Area in square meters
        u_value = 1.5  # U-value in W/m²K
        hours_of_use = 24  # Number of hours used
        temperature_inside = 21  # Indoor temperature in Celsius
        temperature_outside = 5  # Outdoor temperature in Celsius
        energy_cost_per_kWh = 0.2  # Cost of energy in currency per kWh

        simulator = WindowDoorEfficiencySimulator(area, u_value, hours_of_use)
        result = simulator.simulate(temperature_inside, temperature_outside, energy_cost_per_kWh)

        print(json.dumps(result, indent=4))

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
