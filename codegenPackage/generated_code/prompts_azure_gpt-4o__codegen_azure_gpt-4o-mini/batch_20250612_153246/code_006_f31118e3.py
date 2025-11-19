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

```python
class ElectricCalorifier:
    """
    A class to simulate the operation of electric calorifiers.
    
    Attributes:
        capacity (float): The maximum capacity of the calorifier in liters.
        current_temperature (float): The current temperature of the water in degrees Celsius.
        target_temperature (float): The desired temperature of the water in degrees Celsius.
        power (float): The power rating of the electric heater in kilowatts.
        heating_rate (float): The rate at which the water heats up in degrees Celsius per minute.
        is_heating (bool): Indicates whether the heater is currently on.
    """

    def __init__(self, capacity, power, heating_rate):
        """
        Initializes the ElectricCalorifier with specified capacity, power, and heating rate.
        
        Args:
            capacity (float): Maximum capacity of the calorifier in liters.
            power (float): Power rating of the electric heater in kilowatts.
            heating_rate (float): Heating rate in degrees Celsius per minute.
        """
        if capacity <= 0 or power <= 0 or heating_rate <= 0:
            raise ValueError("Capacity, power, and heating rate must be positive values.")
        
        self.capacity = capacity
        self.current_temperature = 20.0  # Default starting temperature in Celsius
        self.target_temperature = 60.0  # Default target temperature in Celsius
        self.power = power
        self.heating_rate = heating_rate
        self.is_heating = False

    def set_target_temperature(self, temperature):
        """
        Sets the target temperature for the calorifier.
        
        Args:
            temperature (float): Desired temperature in degrees Celsius.
        """
        if temperature < 20.0 or temperature > 100.0:
            raise ValueError("Target temperature must be between 20 and 100 degrees Celsius.")
        self.target_temperature = temperature

    def start_heating(self):
        """Starts the heating process."""
        if self.current_temperature >= self.target_temperature:
            print("Current temperature is already at or above the target temperature.")
            return
        
        self.is_heating = True
        print("Heating started...")

    def stop_heating(self):
        """Stops the heating process."""
        self.is_heating = False
        print("Heating stopped.")

    def update_temperature(self, minutes):
        """
        Updates the current temperature based on the heating rate and time elapsed.
        
        Args:
            minutes (int): The number of minutes to simulate heating.
        """
        if not self.is_heating:
            print("Heater is off. Please start heating first.")
            return
        
        if minutes < 0:
            raise ValueError("Minutes must be a non-negative value.")
        
        temperature_increase = self.heating_rate * minutes
        self.current_temperature += temperature_increase
        
        # Ensure the temperature does not exceed the target temperature
        if self.current_temperature > self.target_temperature:
            self.current_temperature = self.target_temperature
            self.stop_heating()
        
        print(f"Current temperature after {minutes} minutes: {self.current_temperature:.2f} °C")

    def get_status(self):
        """Returns the current status of the calorifier."""
        return {
            "current_temperature": self.current_temperature,
            "target_temperature": self.target_temperature,
            "is_heating": self.is_heating
        }


# Example usage
if __name__ == "__main__":
    try:
        calorifier = ElectricCalorifier(capacity=100, power=3.0, heating_rate=5.0)
        calorifier.set_target_temperature(60)
        calorifier.start_heating()
        calorifier.update_temperature(10)  # Simulate heating for 10 minutes
        status = calorifier.get_status()
        print(status)
    except ValueError as e:
        print(f"Error: {e}")
```
