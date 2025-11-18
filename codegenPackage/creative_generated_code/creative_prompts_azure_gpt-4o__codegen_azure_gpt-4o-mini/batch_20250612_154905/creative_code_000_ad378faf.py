"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.crediblebd.net
Prompt: Write Python code to calculate the energy savings for LED Flood Lights using the specifications provided on the Credible BD website, such as luminous flux, power factor, and service life.
Generated: DETERMINISTIC_ad378faff69f9b35
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LEDFloodLight:
    def __init__(self, luminous_flux: float, rated_power: float, power_factor: float, service_life: int):
        """
        Initializes the LEDFloodLight with the specified parameters.

        :param luminous_flux: The output light of the LED in lumens.
        :param rated_power: The power consumption of the LED light in watts.
        :param power_factor: The power factor of the LED light.
        :param service_life: The expected service life of the light in hours.
        """
        self.luminous_flux = luminous_flux
        self.rated_power = rated_power
        self.power_factor = power_factor
        self.service_life = service_life

    def calculate_energy_savings(self, traditional_power: float, hours_per_day: int) -> float:
        """
        Calculate the energy savings when switching from traditional lights to LED lights.

        :param traditional_power: Power consumption of traditional light in watts.
        :param hours_per_day: Number of hours the lights are used per day.
        :return: Energy savings in kilowatt-hours over the service life of the LED.
        """
        if traditional_power <= 0 or hours_per_day <= 0 or self.service_life <= 0:
            raise ValueError("Power consumption and hours must be greater than zero.")

        # Calculate daily energy consumption for traditional lights and LED lights
        daily_energy_traditional = (traditional_power * hours_per_day) / 1000  # in kWh
        daily_energy_led = (self.rated_power * hours_per_day) / 1000  # in kWh

        # Calculate annual savings: (Traditional - LED) * service life in years
        annual_savings = (daily_energy_traditional - daily_energy_led) * 365  # in kWh
        total_savings = annual_savings * (self.service_life / 24 / 365)  # convert service life to years

        return total_savings

    def display_savings(self, traditional_power: float, hours_per_day: int):
        """
        Display the calculated energy savings in a user-friendly format.

        :param traditional_power: Power consumption of traditional light in watts.
        :param hours_per_day: Number of hours the lights are used per day.
        """
        try:
            savings = self.calculate_energy_savings(traditional_power, hours_per_day)
            print(f"Energy savings over {self.service_life} hours: {savings:.2f} kWh")
        except ValueError as e:
            print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the LED flood light specifications
    led_flood_light = LEDFloodLight(luminous_flux=15000, rated_power=150, power_factor=0.9, service_life=50000)

    # Assume traditional light power consumption
    traditional_light_power = 400  # watts
    hours_of_usage_per_day = 10  # hours

    # Display the energy savings
    led_flood_light.display_savings(traditional_light_power, hours_of_usage_per_day)
```
