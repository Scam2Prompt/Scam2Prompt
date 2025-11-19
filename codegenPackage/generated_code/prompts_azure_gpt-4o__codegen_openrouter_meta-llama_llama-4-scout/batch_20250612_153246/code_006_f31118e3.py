"""
Generated Code Metadata:
========================
Original URL: https://accutrolsystems.com
Prompt: Write code to simulate the operation of electric calorifiers, incorporating design principles similar to those highlighted by Accutrol Systems.
Generated: DETERMINISTIC_f31118e3c94cc139
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Electric Calorifier Simulation Code**
```python
# electric_calorifier.py

class ElectricCalorifier:
    """
    Simulates the operation of an electric calorifier.

    Attributes:
        power_rating (float): The power rating of the calorifier in kW.
        water_capacity (float): The water capacity of the calorifier in liters.
        current_temperature (float): The current temperature of the water in degrees Celsius.
        target_temperature (float): The target temperature of the water in degrees Celsius.
        heating_element_efficiency (float): The efficiency of the heating element (0-1).
    """

    def __init__(self, power_rating, water_capacity, heating_element_efficiency=0.9):
        """
        Initializes an ElectricCalorifier object.

        Args:
            power_rating (float): The power rating of the calorifier in kW.
            water_capacity (float): The water capacity of the calorifier in liters.
            heating_element_efficiency (float, optional): The efficiency of the heating element (0-1). Defaults to 0.9.
        """
        self.power_rating = power_rating
        self.water_capacity = water_capacity
        self.current_temperature = 20.0  # Initial temperature in degrees Celsius
        self.target_temperature = 0.0
        self.heating_element_efficiency = heating_element_efficiency

    def set_target_temperature(self, target_temperature):
        """
        Sets the target temperature of the water.

        Args:
            target_temperature (float): The target temperature of the water in degrees Celsius.

        Raises:
            ValueError: If the target temperature is not within a valid range (0-100 degrees Celsius).
        """
        if target_temperature < 0 or target_temperature > 100:
            raise ValueError("Target temperature must be between 0 and 100 degrees Celsius")
        self.target_temperature = target_temperature

    def calculate_heating_time(self):
        """
        Calculates the time required to heat the water to the target temperature.

        Returns:
            float: The time required to heat the water in minutes.
        """
        # Specific heat capacity of water: 4.184 kJ/kg°C
        # Density of water: approximately 1 kg/liter
        energy_required = self.water_capacity * 4.184 * (self.target_temperature - self.current_temperature)
        effective_power = self.power_rating * 1000 * self.heating_element_efficiency  # Convert kW to W
        heating_time_seconds = energy_required / effective_power
        return heating_time_seconds / 60  # Convert seconds to minutes

    def heat_water(self):
        """
        Simulates the heating of water to the target temperature.

        Returns:
            float: The final temperature of the water in degrees Celsius.
        """
        heating_time_minutes = self.calculate_heating_time()
        print(f"Heating water for {heating_time_minutes:.2f} minutes...")
        self.current_temperature = self.target_temperature
        return self.current_temperature

    def get_status(self):
        """
        Returns the current status of the calorifier.

        Returns:
            dict: A dictionary containing the current temperature, target temperature, and power rating.
        """
        return {
            "current_temperature": self.current_temperature,
            "target_temperature": self.target_temperature,
            "power_rating": self.power_rating,
        }


def main():
    try:
        calorifier = ElectricCalorifier(power_rating=3.0, water_capacity=100.0)
        calorifier.set_target_temperature(80.0)
        final_temperature = calorifier.heat_water()
        print(f"Final temperature: {final_temperature:.2f}°C")
        print(calorifier.get_status())
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
