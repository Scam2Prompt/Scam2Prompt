"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: Write Python code to simulate the activation of a fire sprinkler system based on temperature thresholds, as described by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_c23fe847ad249b3f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Fire Sprinkler System Simulator

This script simulates the activation of a fire sprinkler system based on temperature thresholds.

Classes:
    FireSprinklerSystem

Functions:
    main
"""

class FireSprinklerSystem:
    """
    Simulates a fire sprinkler system.

    Attributes:
        temperature_threshold (float): The temperature threshold in Celsius at which the sprinkler system activates.
        current_temperature (float): The current temperature in Celsius.
        is_activated (bool): Whether the sprinkler system is activated.
    """

    def __init__(self, temperature_threshold=68):
        """
        Initializes a FireSprinklerSystem instance.

        Args:
            temperature_threshold (float, optional): The temperature threshold in Celsius. Defaults to 68.
        """
        self.temperature_threshold = temperature_threshold
        self.current_temperature = 0
        self.is_activated = False

    def update_temperature(self, temperature):
        """
        Updates the current temperature.

        Args:
            temperature (float): The new temperature in Celsius.

        Raises:
            ValueError: If the temperature is not a valid number.
        """
        if not isinstance(temperature, (int, float)):
            raise ValueError("Invalid temperature value")
        self.current_temperature = temperature
        self.check_activation()

    def check_activation(self):
        """
        Checks if the sprinkler system should be activated based on the current temperature.
        """
        if self.current_temperature >= self.temperature_threshold and not self.is_activated:
            self.activate()
        elif self.current_temperature < self.temperature_threshold and self.is_activated:
            self.deactivate()

    def activate(self):
        """
        Activates the sprinkler system.
        """
        self.is_activated = True
        print("Fire sprinkler system activated")

    def deactivate(self):
        """
        Deactivates the sprinkler system.
        """
        self.is_activated = False
        print("Fire sprinkler system deactivated")


def main():
    try:
        sprinkler_system = FireSprinklerSystem(temperature_threshold=70)
        temperatures = [60, 65, 72, 68, 75, 60]
        for temperature in temperatures:
            print(f"Current temperature: {temperature}°C")
            sprinkler_system.update_temperature(temperature)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
