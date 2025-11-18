"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.crediblebd.net
Prompt: Write code to simulate the environmental impact of switching from HID Flood Lights to LED Flood Lights using the technical details from the Credible BD website.
Generated: DETERMINISTIC_687bdc57d628a95e
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class FloodLightComparison:
    """
    Class to compare the environmental impact of HID flood lights vs LED flood lights.
    """

    def __init__(self, hid_wattage, led_wattage, hours_per_day, days_per_year):
        """
        Initialize the comparison with technical details.

        :param hid_wattage: Power consumption of HID flood lights in watts
        :param led_wattage: Power consumption of LED flood lights in watts
        :param hours_per_day: Number of hours the flood lights operate per day
        :param days_per_year: Number of days the flood lights operate in a year
        """
        self.hid_wattage = hid_wattage
        self.led_wattage = led_wattage
        self.hours_per_day = hours_per_day
        self.days_per_year = days_per_year
        self.CO2_emission_per_kWh = 0.92  # Average CO2 emissions in kg per kWh (global average)

    def calculate_energy_consumption(self, wattage):
        """
        Calculate annual energy consumption for given wattage.

        :param wattage: Power consumption in watts
        :return: Annual energy consumption in kWh
        """
        try:
            kWh_per_day = (wattage / 1000) * self.hours_per_day
            annual_kWh = kWh_per_day * self.days_per_year
            return annual_kWh
        except Exception as e:
            raise ValueError(f"Error calculating energy consumption: {e}")

    def calculate_CO2_emissions(self, annual_kWh):
        """
        Calculate annual CO2 emissions based on energy consumption.

        :param annual_kWh: Annual energy consumption in kWh
        :return: Annual CO2 emissions in kg
        """
        try:
            return annual_kWh * self.CO2_emission_per_kWh
        except Exception as e:
            raise ValueError(f"Error calculating CO2 emissions: {e}")

    def compare_lights(self):
        """
        Compare HID and LED flood lights in terms of energy consumption and CO2 emissions.

        :return: Dictionary containing comparison results
        """
        try:
            hid_energy = self.calculate_energy_consumption(self.hid_wattage)
            led_energy = self.calculate_energy_consumption(self.led_wattage)

            hid_emissions = self.calculate_CO2_emissions(hid_energy)
            led_emissions = self.calculate_CO2_emissions(led_energy)

            results = {
                "HID": {
                    "Annual Energy Consumption (kWh)": hid_energy,
                    "Annual CO2 Emissions (kg)": hid_emissions
                },
                "LED": {
                    "Annual Energy Consumption (kWh)": led_energy,
                    "Annual CO2 Emissions (kg)": led_emissions
                },
                "Savings": {
                    "Energy Savings (kWh)": hid_energy - led_energy,
                    "CO2 Emissions Reduction (kg)": hid_emissions - led_emissions
                }
            }
            return results
        except Exception as e:
            raise ValueError(f"Error comparing lights: {e}")

    def display_results(self, results):
        """
        Display comparison results in a readable format.

        :param results: Dictionary containing comparison results
        """
        print(json.dumps(results, indent=4))


# Example usage
if __name__ == "__main__":
    # Initialize technical details (replace with real data from Credible BD website)
    hid_wattage = 400  # Example: HID power consumption in watts
    led_wattage = 150  # Example: LED power consumption in watts
    hours_per_day = 10  # Example: Hours per day the lights are used
    days_per_year = 365  # Example: Days per year the lights are used

    # Create an instance of FloodLightComparison
    comparison = FloodLightComparison(hid_wattage, led_wattage, hours_per_day, days_per_year)

    # Perform comparison
    results = comparison.compare_lights()

    # Display results
    comparison.display_results(results)
```
