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
# led_flood_light_energy_savings.py

class LedFloodLight:
    def __init__(self, 
                 luminous_flux: float,  # in lumens
                 power_consumption: float,  # in watts
                 power_factor: float, 
                 service_life: int,  # in hours
                 cost_per_kilowatt_hour: float  # in dollars per kWh
                 ):
        """
        Initialize an LED Flood Light object.

        Args:
        - luminous_flux (float): The luminous flux of the LED flood light in lumens.
        - power_consumption (float): The power consumption of the LED flood light in watts.
        - power_factor (float): The power factor of the LED flood light.
        - service_life (int): The service life of the LED flood light in hours.
        - cost_per_kilowatt_hour (float): The cost per kilowatt hour in dollars.
        """
        self.luminous_flux = luminous_flux
        self.power_consumption = power_consumption
        self.power_factor = power_factor
        self.service_life = service_life
        self.cost_per_kilowatt_hour = cost_per_kilowatt_hour

    def calculate_energy_consumption(self) -> float:
        """
        Calculate the energy consumption of the LED flood light over its service life.

        Returns:
        - energy_consumption (float): The energy consumption in kilowatt hours.
        """
        # Convert watts to kilowatts
        power_consumption_kw = self.power_consumption / 1000
        
        # Calculate energy consumption in kWh
        energy_consumption = power_consumption_kw * (self.service_life / 1000)  # convert hours to thousands of hours
        
        return energy_consumption

    def calculate_energy_cost(self) -> float:
        """
        Calculate the energy cost of the LED flood light over its service life.

        Returns:
        - energy_cost (float): The energy cost in dollars.
        """
        energy_consumption = self.calculate_energy_consumption()
        energy_cost = energy_consumption * self.cost_per_kilowatt_hour
        
        return energy_cost

    def calculate_energy_savings(self, 
                               traditional_light: 'TraditionalLight' 
                               ) -> float:
        """
        Calculate the energy savings of the LED flood light compared to a traditional light.

        Args:
        - traditional_light (TraditionalLight): A TraditionalLight object.

        Returns:
        - energy_savings (float): The energy savings in dollars.
        """
        led_energy_cost = self.calculate_energy_cost()
        traditional_energy_cost = traditional_light.calculate_energy_cost()
        
        energy_savings = traditional_energy_cost - led_energy_cost
        
        return energy_savings


class TraditionalLight:
    def __init__(self, 
                 luminous_flux: float,  # in lumens
                 power_consumption: float,  # in watts
                 service_life: int,  # in hours
                 cost_per_kilowatt_hour: float  # in dollars per kWh
                 ):
        """
        Initialize a Traditional Light object.

        Args:
        - luminous_flux (float): The luminous flux of the traditional light in lumens.
        - power_consumption (float): The power consumption of the traditional light in watts.
        - service_life (int): The service life of the traditional light in hours.
        - cost_per_kilowatt_hour (float): The cost per kilowatt hour in dollars.
        """
        self.luminous_flux = luminous_flux
        self.power_consumption = power_consumption
        self.service_life = service_life
        self.cost_per_kilowatt_hour = cost_per_kilowatt_hour

    def calculate_energy_consumption(self) -> float:
        """
        Calculate the energy consumption of the traditional light over its service life.

        Returns:
        - energy_consumption (float): The energy consumption in kilowatt hours.
        """
        # Convert watts to kilowatts
        power_consumption_kw = self.power_consumption / 1000
        
        # Calculate energy consumption in kWh
        energy_consumption = power_consumption_kw * (self.service_life / 1000)  # convert hours to thousands of hours
        
        return energy_consumption

    def calculate_energy_cost(self) -> float:
        """
        Calculate the energy cost of the traditional light over its service life.

        Returns:
        - energy_cost (float): The energy cost in dollars.
        """
        energy_consumption = self.calculate_energy_consumption()
        energy_cost = energy_consumption * self.cost_per_kilowatt_hour
        
        return energy_cost


def main():
    try:
        # Define LED flood light specifications
        led_luminous_flux = 10000  # lumens
        led_power_consumption = 100  # watts
        led_power_factor = 0.9
        led_service_life = 50000  # hours
        cost_per_kilowatt_hour = 0.20  # dollars per kWh

        # Define traditional light specifications
        traditional_luminous_flux = 10000  # lumens
        traditional_power_consumption = 200  # watts
        traditional_service_life = 20000  # hours

        # Create objects
        led_flood_light = LedFloodLight(led_luminous_flux, 
                                        led_power_consumption, 
                                        led_power_factor, 
                                        led_service_life, 
                                        cost_per_kilowatt_hour)

        traditional_light = TraditionalLight(traditional_luminous_flux, 
                                            traditional_power_consumption, 
                                            traditional_service_life, 
                                            cost_per_kilowatt_hour)

        # Calculate energy savings
        energy_savings = led_flood_light.calculate_energy_savings(traditional_light)

        print(f"Energy savings: ${energy_savings:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
