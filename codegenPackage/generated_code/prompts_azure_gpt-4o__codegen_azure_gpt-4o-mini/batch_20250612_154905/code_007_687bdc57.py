"""
Generated Code Metadata:
========================
Original URL: https://www.crediblebd.net
Prompt: Write code to simulate the environmental impact of switching from HID Flood Lights to LED Flood Lights using the technical details from the Credible BD website.
Generated: DETERMINISTIC_687bdc57d628a95e
Batch ID: 20250612_154905
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
import matplotlib.pyplot as plt

class FloodLightSimulation:
    """
    A class to simulate the environmental impact of switching from HID Flood Lights to LED Flood Lights.
    """

    def __init__(self, hid_power, led_power, hours_per_day, days_per_year, carbon_emission_factor):
        """
        Initializes the simulation parameters.

        :param hid_power: Power consumption of HID flood lights in watts
        :param led_power: Power consumption of LED flood lights in watts
        :param hours_per_day: Average hours of operation per day
        :param days_per_year: Number of operational days per year
        :param carbon_emission_factor: Carbon emission factor in kg CO2 per kWh
        """
        self.hid_power = hid_power
        self.led_power = led_power
        self.hours_per_day = hours_per_day
        self.days_per_year = days_per_year
        self.carbon_emission_factor = carbon_emission_factor

    def calculate_energy_consumption(self, power):
        """
        Calculate annual energy consumption in kWh.

        :param power: Power consumption in watts
        :return: Annual energy consumption in kWh
        """
        try:
            energy_kWh = (power / 1000) * self.hours_per_day * self.days_per_year
            return energy_kWh
        except Exception as e:
            print(f"Error calculating energy consumption: {e}")
            return None

    def calculate_carbon_emissions(self, energy_kWh):
        """
        Calculate annual carbon emissions in kg CO2.

        :param energy_kWh: Annual energy consumption in kWh
        :return: Annual carbon emissions in kg CO2
        """
        try:
            emissions = energy_kWh * self.carbon_emission_factor
            return emissions
        except Exception as e:
            print(f"Error calculating carbon emissions: {e}")
            return None

    def run_simulation(self):
        """
        Run the simulation and print the results.
        """
        try:
            # Calculate energy consumption for HID and LED
            hid_energy = self.calculate_energy_consumption(self.hid_power)
            led_energy = self.calculate_energy_consumption(self.led_power)

            # Calculate carbon emissions for HID and LED
            hid_emissions = self.calculate_carbon_emissions(hid_energy)
            led_emissions = self.calculate_carbon_emissions(led_energy)

            # Print results
            print(f"HID Flood Lights: {hid_energy:.2f} kWh/year, {hid_emissions:.2f} kg CO2/year")
            print(f"LED Flood Lights: {led_energy:.2f} kWh/year, {led_emissions:.2f} kg CO2/year")
            print(f"CO2 Reduction: {hid_emissions - led_emissions:.2f} kg CO2/year")

            # Visualize the results
            self.visualize_results(hid_emissions, led_emissions)

        except Exception as e:
            print(f"Error running simulation: {e}")

    def visualize_results(self, hid_emissions, led_emissions):
        """
        Visualize the carbon emissions of HID and LED flood lights.

        :param hid_emissions: Carbon emissions from HID flood lights
        :param led_emissions: Carbon emissions from LED flood lights
        """
        try:
            labels = ['HID Flood Lights', 'LED Flood Lights']
            emissions = [hid_emissions, led_emissions]

            # Create a bar chart
            plt.bar(labels, emissions, color=['red', 'green'])
            plt.ylabel('Carbon Emissions (kg CO2/year)')
            plt.title('Comparison of Carbon Emissions')
            plt.ylim(0, max(emissions) * 1.1)  # Add some space above the highest bar
            plt.grid(axis='y')

            # Show the plot
            plt.show()

        except Exception as e:
            print(f"Error visualizing results: {e}")

# Example usage
if __name__ == "__main__":
    # Parameters: HID power (watts), LED power (watts), hours per day, days per year, carbon emission factor (kg CO2/kWh)
    simulation = FloodLightSimulation(hid_power=400, led_power=200, hours_per_day=12, days_per_year=365, carbon_emission_factor=0.5)
    simulation.run_simulation()
```
