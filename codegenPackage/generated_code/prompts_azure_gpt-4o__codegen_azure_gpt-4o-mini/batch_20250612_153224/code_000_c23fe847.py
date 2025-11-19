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
import time
import random

class FireSprinklerSystem:
    def __init__(self, activation_temp=155):
        """
        Initializes the fire sprinkler system with a specified activation temperature.
        
        :param activation_temp: Temperature in Fahrenheit at which the sprinkler activates.
        """
        self.activation_temp = activation_temp
        self.is_activated = False

    def read_temperature(self):
        """
        Simulates reading the current temperature from a sensor.
        
        :return: A simulated temperature value in Fahrenheit.
        """
        # Simulate temperature reading (for demonstration purposes)
        return random.uniform(100, 200)

    def activate_sprinkler(self):
        """
        Activates the fire sprinkler system.
        """
        if not self.is_activated:
            self.is_activated = True
            print("Fire sprinkler system activated!")
        else:
            print("Fire sprinkler system is already activated.")

    def check_temperature(self):
        """
        Continuously checks the temperature and activates the sprinkler if the threshold is exceeded.
        """
        try:
            while not self.is_activated:
                current_temp = self.read_temperature()
                print(f"Current temperature: {current_temp:.2f}°F")

                if current_temp >= self.activation_temp:
                    self.activate_sprinkler()
                else:
                    print("Temperature is below activation threshold. Monitoring continues.")

                # Wait for a short period before checking again
                time.sleep(2)

        except Exception as e:
            print(f"An error occurred while checking the temperature: {e}")

if __name__ == "__main__":
    # Create an instance of the fire sprinkler system with a default activation temperature
    sprinkler_system = FireSprinklerSystem()

    # Start monitoring the temperature
    sprinkler_system.check_temperature()
```
