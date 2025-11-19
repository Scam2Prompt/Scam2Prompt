"""
Generated Code Metadata:
========================
Original URL: https://www.crediblebd.net
Prompt: Generate a Python script to calculate the energy savings when switching from traditional HID lights to LED flood lights from Credible BD, considering their specifications.
Generated: DETERMINISTIC_7e4d8d5cbecfa400
Batch ID: 20250612_161331
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

class LightFixture:
    """
    A class to represent a light fixture with its specifications.
    """

    def __init__(self, wattage: float, hours_per_day: float, days_per_year: int):
        """
        Initialize a LightFixture instance.

        :param wattage: Power consumption of the light fixture in watts.
        :param hours_per_day: Average hours the light is used per day.
        :param days_per_year: Number of days the light is used per year.
        """
        self.wattage = wattage
        self.hours_per_day = hours_per_day
        self.days_per_year = days_per_year

    def annual_energy_consumption(self) -> float:
        """
        Calculate the annual energy consumption in kilowatt-hours (kWh).

        :return: Annual energy consumption in kWh.
        """
        return (self.wattage / 1000) * self.hours_per_day * self.days_per_year


def calculate_energy_savings(hid: LightFixture, led: LightFixture) -> float:
    """
    Calculate the energy savings when switching from HID to LED lights.

    :param hid: LightFixture instance for HID lights.
    :param led: LightFixture instance for LED lights.
    :return: Energy savings in kWh.
    """
    try:
        hid_consumption = hid.annual_energy_consumption()
        led_consumption = led.annual_energy_consumption()
        savings = hid_consumption - led_consumption
        logging.info(f"HID Annual Consumption: {hid_consumption} kWh")
        logging.info(f"LED Annual Consumption: {led_consumption} kWh")
        logging.info(f"Energy Savings: {savings} kWh")
        return savings
    except Exception as e:
        logging.error("Error calculating energy savings: %s", e)
        return 0.0


def main():
    """
    Main function to execute the energy savings calculation.
    """
    # Specifications for HID and LED lights
    hid_wattage = 400  # Example wattage for HID light
    led_wattage = 200  # Example wattage for LED light
    hours_per_day = 10  # Average usage
    days_per_year = 365  # Days in a year

    # Create LightFixture instances for HID and LED
    hid_light = LightFixture(hid_wattage, hours_per_day, days_per_year)
    led_light = LightFixture(led_wattage, hours_per_day, days_per_year)

    # Calculate and print energy savings
    savings = calculate_energy_savings(hid_light, led_light)
    print(f"Annual Energy Savings: {savings} kWh")


if __name__ == "__main__":
    main()
```
