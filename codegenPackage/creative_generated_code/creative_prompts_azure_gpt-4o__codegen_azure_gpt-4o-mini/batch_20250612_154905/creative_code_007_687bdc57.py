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
import pandas as pd

class FloodLight:
    """
    A class to represent flood lights and calculate their environmental impact.
    """

    def __init__(self, wattage, hours_per_day, lifespan_years):
        """
        Initializes the FloodLight object with wattage, hours of operation per day, 
        and lifespan in years.

        Parameters:
            wattage (float): The wattage of the flood light.
            hours_per_day (float): The number of hours the light operates per day.
            lifespan_years (int): The expected lifespan of the light in years.
        """
        self.wattage = wattage
        self.hours_per_day = hours_per_day
        self.lifespan_years = lifespan_years
    
    def annual_energy_consumption(self):
        """
        Calculates the annual energy consumption in kWh.

        Returns:
            float: The annual energy consumption.
        """
        return (self.wattage * self.hours_per_day * 365) / 1000  # kWh

    def total_energy_consumption(self):
        """
        Calculates the total energy consumption over the lifespan.

        Returns:
            float: Total energy consumption over the lifespan in kWh.
        """
        return self.annual_energy_consumption() * self.lifespan_years

    def carbon_emission(self, emission_factor):
        """
        Calculates the carbon emission based on an emission factor.

        Parameters:
            emission_factor (float): The carbon emission factor in kg CO2/kWh.

        Returns:
            float: Total carbon emissions in kg CO2.
        """
        return self.total_energy_consumption() * emission_factor


def simulate_environmental_impact():
    """
    Simulates the environmental impact of switching from HID flood lights to LED flood lights.
    """

    # Technical details for HID Flood Lights (Example values)
    hid_wattage = 400  # Wattage of HID Flood Light
    hid_hours_per_day = 10  # Operating hours per day
    hid_lifespan_years = 5  # Lifespan in years

    # Technical details for LED Flood Lights (Example values)
    led_wattage = 150  # Wattage of LED Flood Light
    led_hours_per_day = 10  # Operating hours per day
    led_lifespan_years = 10  # Lifespan in years

    # Carbon emission factor (kg CO2/kWh) for electricity generation
    emission_factor = 0.5  # Example value

    try:
        # Create HID and LED flood light instances
        hid_light = FloodLight(hid_wattage, hid_hours_per_day, hid_lifespan_years)
        led_light = FloodLight(led_wattage, led_hours_per_day, led_lifespan_years)

        # Calculate energy consumption and emissions
        hid_energy = hid_light.total_energy_consumption()
        led_energy = led_light.total_energy_consumption()
        
        hid_emissions = hid_light.carbon_emission(emission_factor)
        led_emissions = led_light.carbon_emission(emission_factor)

        # Print results
        print(f"HID Flood Light - Total Energy Consumption: {hid_energy:.2f} kWh, "
              f"Total CO2 Emissions: {hid_emissions:.2f} kg CO2")
        print(f"LED Flood Light - Total Energy Consumption: {led_energy:.2f} kWh, "
              f"Total CO2 Emissions: {led_emissions:.2f} kg CO2")
        print(f"Energy Savings: {hid_energy - led_energy:.2f} kWh")
        print(f"CO2 Emissions Reduction: {hid_emissions - led_emissions:.2f} kg CO2")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    simulate_environmental_impact()
```
