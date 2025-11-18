"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indpfire.com
Prompt: Write Python code to simulate the activation of a fire sprinkler system based on temperature thresholds, as described by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_c23fe847ad249b3f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class FireSprinklerSystem:
    """
    A class to represent a fire sprinkler system that activates based on temperature thresholds.
    """

    def __init__(self, activation_temperature: float, check_interval: float):
        """
        Initializes the FireSprinklerSystem with the specified parameters.
        
        :param activation_temperature: The temperature threshold (in degrees Celsius) to activate the system.
        :param check_interval: The interval (in seconds) to check the temperature.
        """
        self.activation_temperature = activation_temperature
        self.check_interval = check_interval
        self.active = False

    def read_temperature(self) -> float:
        """
        Simulates reading the current temperature from a sensor.

        :return: A simulated temperature reading (in degrees Celsius).
        """
        # Simulate temperature reading (for demonstration purposes)
        return random.uniform(15.0, 100.0)  # Random temperature between 15 and 100 degrees Celsius

    def activate_system(self):
        """Activates the fire sprinkler system."""
        if not self.active:
            self.active = True
            print("Fire Sprinkler System Activated! Spraying water...")

    def deactivate_system(self):
        """Deactivates the fire sprinkler system."""
        if self.active:
            self.active = False
            print("Fire Sprinkler System Deactivated.")

    def monitor_temperature(self):
        """Continuously monitors the temperature and activates the system if the threshold is exceeded."""
        print("Starting temperature monitoring...")

        while True:
            try:
                current_temperature = self.read_temperature()
                print(f"Current Temperature: {current_temperature:.2f} °C")

                if current_temperature >= self.activation_temperature:
                    self.activate_system()
                else:
                    self.deactivate_system()

                time.sleep(self.check_interval)

            except Exception as e:
                print(f"Error occurred while monitoring temperature: {e}")
                break

def main():
    """
    Main function to run the fire sprinkler system simulation.
    """
    activation_temp = 75.0  # Activation temperature threshold in degrees Celsius
    check_interval = 5.0     # Temperature check interval in seconds

    sprinkler_system = FireSprinklerSystem(activation_temp, check_interval)
    sprinkler_system.monitor_temperature()

if __name__ == "__main__":
    main()
```
