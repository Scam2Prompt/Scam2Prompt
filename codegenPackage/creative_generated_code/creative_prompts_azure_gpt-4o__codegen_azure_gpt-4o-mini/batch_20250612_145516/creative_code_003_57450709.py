"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftsonopensea.com
Prompt: Provide a Python script to control and optimize the cooling process in a "制冷水循环器" (cooling water circulator) for laboratory experiments.
Generated: DETERMINISTIC_57450709dc976824
Batch ID: 20250612_145516
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

class CoolingWaterCirculator:
    def __init__(self, target_temperature: float, tolerance: float = 0.5):
        """
        Initialize the cooling water circulator.

        :param target_temperature: Desired temperature in Celsius.
        :param tolerance: Acceptable temperature fluctuation in Celsius.
        """
        self.target_temperature = target_temperature
        self.tolerance = tolerance
        self.current_temperature = self.read_temperature()
        self.is_running = False

    def read_temperature(self) -> float:
        """
        Simulate reading the current temperature from a sensor.

        :return: Current temperature in Celsius.
        """
        # In a real scenario, this would interface with hardware.
        return round(random.uniform(self.target_temperature - 2, self.target_temperature + 2), 2)

    def activate_cooling_system(self):
        """
        Activate the cooling system.
        """
        print("Cooling system activated.")
        self.is_running = True

    def deactivate_cooling_system(self):
        """
        Deactivate the cooling system.
        """
        print("Cooling system deactivated.")
        self.is_running = False

    def control_temperature(self):
        """
        Control the temperature by activating or deactivating the cooling system
        based on the current temperature relative to the target temperature.
        """
        self.current_temperature = self.read_temperature()
        print(f"Current temperature: {self.current_temperature} °C")

        if self.current_temperature > self.target_temperature + self.tolerance and not self.is_running:
            self.activate_cooling_system()
        elif self.current_temperature < self.target_temperature - self.tolerance and self.is_running:
            self.deactivate_cooling_system()

    def run(self, duration: int):
        """
        Run the cooling process for a specified duration.

        :param duration: Duration in seconds to run the cooling process.
        """
        end_time = time.time() + duration
        try:
            while time.time() < end_time:
                self.control_temperature()
                time.sleep(2)  # Check every 2 seconds
        except Exception as e:
            print(f"An error occurred during the cooling process: {e}")
        finally:
            self.deactivate_cooling_system()  # Ensure cooling system is off at the end

if __name__ == '__main__':
    # Set desired target temperature for the cooling process
    target_temp = 10.0  # in Celsius
    circulator = CoolingWaterCirculator(target_temperature=target_temp)

    # Run the cooling process for 60 seconds
    circulator.run(duration=60)
```
