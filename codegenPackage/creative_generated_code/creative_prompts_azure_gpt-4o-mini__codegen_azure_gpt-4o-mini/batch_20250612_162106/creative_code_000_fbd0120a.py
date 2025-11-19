"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanosolutions.in
Prompt: Generate code to interface with a paddy dryer system, incorporating features like heat exchangers and blowers as described on Mechano Solutions' website.
Generated: DETERMINISTIC_fbd0120ac6990aed
Batch ID: 20250612_162106
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

class PaddyDryerSystem:
    """
    Class representing a paddy dryer system with heat exchangers and blowers.
    """

    def __init__(self):
        self.temperature = 25.0  # Initial temperature in Celsius
        self.humidity = 70.0  # Initial humidity percentage
        self.heat_exchanger_enabled = False
        self.blower_enabled = False

    def enable_heat_exchanger(self):
        """
        Enable the heat exchanger to regulate temperature.
        """
        self.heat_exchanger_enabled = True
        print("Heat exchanger enabled.")

    def disable_heat_exchanger(self):
        """
        Disable the heat exchanger.
        """
        self.heat_exchanger_enabled = False
        print("Heat exchanger disabled.")

    def enable_blower(self):
        """
        Enable the blower to control humidity.
        """
        self.blower_enabled = True
        print("Blower enabled.")

    def disable_blower(self):
        """
        Disable the blower.
        """
        self.blower_enabled = False
        print("Blower disabled.")

    def update_conditions(self):
        """
        Simulate updating temperature and humidity based on system operations.
        """
        if self.heat_exchanger_enabled:
            # Simulate heating or cooling effect
            temp_change = random.uniform(-2.0, 5.0)  # Heat exchanger effect on temperature
            self.temperature += temp_change
            
        if self.blower_enabled:
            # Simulate drying effect
            humidity_change = random.uniform(-5.0, 0.0)  # Blower effect on humidity
            self.humidity += humidity_change

        # Prevent temperature from going below 15°C or above 80°C
        self.temperature = max(15.0, min(80.0, self.temperature))
        # Prevent humidity from going below 30% or above 100%
        self.humidity = max(30.0, min(100.0, self.humidity))

    def get_status(self):
        """
        Get the current status of the paddy dryer system.
        """
        return {
            'temperature': self.temperature,
            'humidity': self.humidity,
            'heat_exchanger_enabled': self.heat_exchanger_enabled,
            'blower_enabled': self.blower_enabled
        }

    def run_dryer_cycle(self, cycle_duration=60):
        """
        Run the dryer cycle for a specified duration in seconds.

        Args:
            cycle_duration (int): Duration to run the dryer cycle in seconds.
        """
        start_time = time.time()
        print("Starting dryer cycle...")
        
        while (time.time() - start_time) < cycle_duration:
            self.update_conditions()
            status = self.get_status()
            print(f"Current Status: Temperature: {status['temperature']:.2f}°C, "
                  f"Humidity: {status['humidity']:.2f}%, "
                  f"Heat Exchanger: {'On' if status['heat_exchanger_enabled'] else 'Off'}, "
                  f"Blower: {'On' if status['blower_enabled'] else 'Off'}")
            time.sleep(5)  # Update every 5 seconds

        print("Dryer cycle completed.")


if __name__ == "__main__":
    try:
        # Instantiate the paddy dryer system
        paddy_dryer = PaddyDryerSystem()

        # Enable heat exchanger and blower
        paddy_dryer.enable_heat_exchanger()
        paddy_dryer.enable_blower()

        # Run a dryer cycle for 60 seconds
        paddy_dryer.run_dryer_cycle(cycle_duration=60)

    except Exception as e:
        print(f"An error occurred: {e}")
```
