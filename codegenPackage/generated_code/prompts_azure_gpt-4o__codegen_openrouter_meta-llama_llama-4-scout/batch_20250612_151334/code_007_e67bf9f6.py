"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: Provide a Python script to simulate street lighting energy consumption, considering the services offered by E.C. Power & Lighting Ltd.
Generated: DETERMINISTIC_e67bf9f6a0135113
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# street_lighting_simulation.py

import random

class StreetLight:
    """Represents a street light with its characteristics and behavior."""

    def __init__(self, wattage, hours_of_operation):
        """
        Initializes a StreetLight object.

        Args:
            wattage (float): The wattage of the street light in Watts.
            hours_of_operation (float): The number of hours the street light operates per day.
        """
        self.wattage = wattage
        self.hours_of_operation = hours_of_operation

    def calculate_energy_consumption(self):
        """
        Calculates the daily energy consumption of the street light in kWh.

        Returns:
            float: The daily energy consumption in kWh.
        """
        return (self.wattage * self.hours_of_operation) / 1000


class EC_POWER_LightingLtd:
    """Simulates the services offered by E.C. Power & Lighting Ltd."""

    def __init__(self, street_lights):
        """
        Initializes an EC_POWER_LightingLtd object.

        Args:
            street_lights (list[StreetLight]): A list of StreetLight objects.
        """
        self.street_lights = street_lights

    def calculate_total_energy_consumption(self):
        """
        Calculates the total daily energy consumption of all street lights in kWh.

        Returns:
            float: The total daily energy consumption in kWh.
        """
        return sum(light.calculate_energy_consumption() for light in self.street_lights)

    def simulate_energy_consumption(self, days):
        """
        Simulates the energy consumption of all street lights over a specified number of days.

        Args:
            days (int): The number of days to simulate.

        Returns:
            list[float]: A list of daily energy consumptions in kWh.
        """
        energy_consumptions = []
        for _ in range(days):
            daily_energy_consumption = self.calculate_total_energy_consumption()
            energy_consumptions.append(daily_energy_consumption)
            # Introduce some randomness to simulate real-world variations
            for light in self.street_lights:
                light.hours_of_operation *= random.uniform(0.9, 1.1)
        return energy_consumptions


def main():
    try:
        # Create street lights with different characteristics
        street_light1 = StreetLight(wattage=100, hours_of_operation=12)
        street_light2 = StreetLight(wattage=150, hours_of_operation=10)
        street_light3 = StreetLight(wattage=200, hours_of_operation=8)

        # Create an EC_POWER_LightingLtd object with the street lights
        ec_power = EC_POWER_LightingLtd([street_light1, street_light2, street_light3])

        # Simulate energy consumption over 30 days
        days = 30
        energy_consumptions = ec_power.simulate_energy_consumption(days)

        # Print the daily energy consumptions
        for i, consumption in enumerate(energy_consumptions):
            print(f"Day {i+1}: {consumption:.2f} kWh")

        # Print the average daily energy consumption
        average_consumption = sum(energy_consumptions) / len(energy_consumptions)
        print(f"Average daily energy consumption: {average_consumption:.2f} kWh")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
