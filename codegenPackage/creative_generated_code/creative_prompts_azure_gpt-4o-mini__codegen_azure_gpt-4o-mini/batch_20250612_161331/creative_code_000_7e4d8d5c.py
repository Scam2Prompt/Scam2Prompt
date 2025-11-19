"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.crediblebd.net
Prompt: Generate a Python script to calculate the energy savings when switching from traditional HID lights to LED flood lights from Credible BD, considering their specifications.
Generated: DETERMINISTIC_7e4d8d5cbecfa400
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LightFixture:
    """
    Class to represent a light fixture with its specifications.
    """

    def __init__(self, wattage, hours_per_day, days_per_year):
        """
        Initialize a light fixture with wattage, usage hours, and usage days.

        Args:
            wattage (float): The wattage of the light fixture.
            hours_per_day (float): The number of hours the light is used per day.
            days_per_year (int): The number of days the light is used per year.
        """
        self.wattage = wattage
        self.hours_per_day = hours_per_day
        self.days_per_year = days_per_year

    def annual_energy_consumption(self):
        """
        Calculate the annual energy consumption of the light fixture in kWh.

        Returns:
            float: Annual energy consumption in kWh.
        """
        return (self.wattage / 1000) * self.hours_per_day * self.days_per_year


def calculate_energy_savings(hid_fixture, led_fixture, cost_per_kwh):
    """
    Calculate the annual energy savings when switching from HID to LED.

    Args:
        hid_fixture (LightFixture): The traditional HID light fixture.
        led_fixture (LightFixture): The new LED light fixture.
        cost_per_kwh (float): Cost of electricity per kWh.

    Returns:
        dict: A dictionary containing annual savings and total cost.
    """
    try:
        # Calculate annual energy consumption for both fixtures
        hid_consumption = hid_fixture.annual_energy_consumption()
        led_consumption = led_fixture.annual_energy_consumption()

        # Calculate cost for both fixtures
        hid_cost = hid_consumption * cost_per_kwh
        led_cost = led_consumption * cost_per_kwh

        # Calculate annual savings
        annual_savings = hid_cost - led_cost

        return {
            "annual_savings": annual_savings,
            "hid_cost": hid_cost,
            "led_cost": led_cost
        }
    except Exception as e:
        # Log the error and return None if an error occurs
        print(f"Error occurred during calculation: {e}")
        return None


def main():
    """
    Main function to execute the energy savings calculation.
    """
    # Specifications for the HID and LED fixtures
    hid_wattage = 400  # Example wattage for HID fixture
    led_wattage = 200  # Example wattage for LED fixture
    hours_per_day = 10  # Hours used per day
    days_per_year = 365  # Days used per year
    cost_per_kwh = 0.12  # Example cost of electricity per kWh

    # Create LightFixture instances
    hid_fixture = LightFixture(hid_wattage, hours_per_day, days_per_year)
    led_fixture = LightFixture(led_wattage, hours_per_day, days_per_year)

    # Calculate energy savings
    savings = calculate_energy_savings(hid_fixture, led_fixture, cost_per_kwh)

    # Output results
    if savings is not None:
        print(f"Annual Savings: ${savings['annual_savings']:.2f}")
        print(f"HID Annual Cost: ${savings['hid_cost']:.2f}")
        print(f"LED Annual Cost: ${savings['led_cost']:.2f}")


if __name__ == "__main__":
    main()
```
