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
# Import required libraries
import math

class FloodLight:
    def __init__(self, wattage, lumens, lifespan):
        """
        Initialize a FloodLight object.

        Args:
            wattage (float): The wattage of the flood light in watts (W).
            lumens (float): The luminous flux of the flood light in lumens (lm).
            lifespan (float): The lifespan of the flood light in hours.
        """
        self.wattage = wattage
        self.lumens = lumens
        self.lifespan = lifespan

class HIDFloodLight(FloodLight):
    def __init__(self, wattage, lumens, lifespan=20000):
        """
        Initialize an HIDFloodLight object.

        Args:
            wattage (float): The wattage of the HID flood light in watts (W).
            lumens (float): The luminous flux of the HID flood light in lumens (lm).
        """
        super().__init__(wattage, lumens, lifespan)

class LEDFloodLight(FloodLight):
    def __init__(self, wattage, lumens, lifespan=50000):
        """
        Initialize an LEDFloodLight object.

        Args:
            wattage (float): The wattage of the LED flood light in watts (W).
            lumens (float): The luminous flux of the LED flood light in lumens (lm).
        """
        super().__init__(wattage, lumens, lifespan)

def calculate_energy_consumption(flood_light, operating_hours_per_year):
    """
    Calculate the energy consumption of a flood light.

    Args:
        flood_light (FloodLight): The flood light object.
        operating_hours_per_year (float): The number of operating hours per year.

    Returns:
        float: The energy consumption in kilowatt-hours (kWh).
    """
    energy_consumption = (flood_light.wattage / 1000) * operating_hours_per_year
    return energy_consumption

def calculate_co2_emissions(energy_consumption, co2_emission_factor):
    """
    Calculate the CO2 emissions.

    Args:
        energy_consumption (float): The energy consumption in kilowatt-hours (kWh).
        co2_emission_factor (float): The CO2 emission factor in kg CO2/kWh.

    Returns:
        float: The CO2 emissions in kilograms (kg).
    """
    co2_emissions = energy_consumption * co2_emission_factor
    return co2_emissions

def simulate_environmental_impact(
    hid_wattage, 
    hid_lumens, 
    led_wattage, 
    led_lumens, 
    operating_hours_per_year, 
    co2_emission_factor
):
    """
    Simulate the environmental impact of switching from HID Flood Lights to LED Flood Lights.

    Args:
        hid_wattage (float): The wattage of the HID flood light in watts (W).
        hid_lumens (float): The luminous flux of the HID flood light in lumens (lm).
        led_wattage (float): The wattage of the LED flood light in watts (W).
        led_lumens (float): The luminous flux of the LED flood light in lumens (lm).
        operating_hours_per_year (float): The number of operating hours per year.
        co2_emission_factor (float): The CO2 emission factor in kg CO2/kWh.

    Returns:
        dict: A dictionary containing the results of the simulation.
    """
    hid_flood_light = HIDFloodLight(hid_wattage, hid_lumens)
    led_flood_light = LEDFloodLight(led_wattage, led_lumens)

    hid_energy_consumption = calculate_energy_consumption(hid_flood_light, operating_hours_per_year)
    led_energy_consumption = calculate_energy_consumption(led_flood_light, operating_hours_per_year)

    hid_co2_emissions = calculate_co2_emissions(hid_energy_consumption, co2_emission_factor)
    led_co2_emissions = calculate_co2_emissions(led_energy_consumption, co2_emission_factor)

    results = {
        "HID Energy Consumption (kWh)": hid_energy_consumption,
        "LED Energy Consumption (kWh)": led_energy_consumption,
        "HID CO2 Emissions (kg)": hid_co2_emissions,
        "LED CO2 Emissions (kg)": led_co2_emissions,
        "Energy Savings (kWh)": hid_energy_consumption - led_energy_consumption,
        "CO2 Emissions Reduction (kg)": hid_co2_emissions - led_co2_emissions,
    }

    return results

def main():
    try:
        # Technical details from Credible BD website
        hid_wattage = 400  # watts (W)
        hid_lumens = 36000  # lumens (lm)
        led_wattage = 180  # watts (W)
        led_lumens = 36000  # lumens (lm)
        operating_hours_per_year = 8760  # hours
        co2_emission_factor = 0.682  # kg CO2/kWh

        results = simulate_environmental_impact(
            hid_wattage, 
            hid_lumens, 
            led_wattage, 
            led_lumens, 
            operating_hours_per_year, 
            co2_emission_factor
        )

        for key, value in results.items():
            print(f"{key}: {value:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
