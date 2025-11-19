"""
Generated Code Metadata:
========================
Original URL: https://www.crediblebd.net
Prompt: Write Python code to calculate the energy savings for LED Flood Lights using the specifications provided on the Credible BD website, such as luminous flux, power factor, and service life.
Generated: DETERMINISTIC_ad378faff69f9b35
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LEDFloodLight:
    """
    A class to represent an LED flood light and calculate its energy savings.
    """

    def __init__(self, luminous_flux: float, power_factor: float, service_life: int, wattage: float):
        """
        Initializes the LEDFloodLight with the given specifications.

        :param luminous_flux: The luminous flux of the LED flood light in lumens.
        :param power_factor: The power factor of the LED flood light (between 0 and 1).
        :param service_life: The service life of the LED flood light in hours.
        :param wattage: The wattage of the LED flood light.
        """
        self.luminous_flux = luminous_flux
        self.power_factor = power_factor
        self.service_life = service_life
        self.wattage = wattage

    def calculate_energy_savings(self, traditional_wattage: float) -> float:
        """
        Calculates the energy savings when using the LED flood light compared to a traditional flood light.

        :param traditional_wattage: The wattage of the traditional flood light.
        :return: The energy savings in kilowatt-hours (kWh).
        """
        if traditional_wattage <= 0:
            raise ValueError("Traditional wattage must be greater than zero.")

        # Calculate the energy consumed by both lights over their service life
        led_energy_consumed = (self.wattage * self.service_life) / 1000  # Convert to kWh
        traditional_energy_consumed = (traditional_wattage * self.service_life) / 1000  # Convert to kWh

        # Calculate energy savings
        energy_savings = traditional_energy_consumed - led_energy_consumed
        return energy_savings

    def display_specifications(self):
        """
        Displays the specifications of the LED flood light.
        """
        print(f"LED Flood Light Specifications:")
        print(f"Luminous Flux: {self.luminous_flux} lumens")
        print(f"Power Factor: {self.power_factor}")
        print(f"Service Life: {self.service_life} hours")
        print(f"Wattage: {self.wattage} watts")


def main():
    """
    Main function to demonstrate the LED flood light energy savings calculation.
    """
    try:
        # Example specifications for an LED flood light
        led_flood_light = LEDFloodLight(luminous_flux=10000, power_factor=0.9, service_life=50000, wattage=100)

        # Display the specifications
        led_flood_light.display_specifications()

        # Calculate energy savings compared to a traditional flood light
        traditional_wattage = 400  # Example wattage for a traditional flood light
        savings = led_flood_light.calculate_energy_savings(traditional_wattage)

        print(f"Energy Savings: {savings:.2f} kWh over {led_flood_light.service_life} hours.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
