"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftsonopensea.com
Prompt: Generate a code snippet for a temperature control system that can be integrated with a ceramic fiber muffle furnace, incorporating features mentioned in the product specifications.
Generated: DETERMINISTIC_3b089cd5e88dc741
Batch ID: 20250612_155449
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

class TemperatureControlSystem:
    """
    A temperature control system for a ceramic fiber muffle furnace.
    This system monitors and controls the temperature based on target settings.
    """
    
    def __init__(self, target_temp, tolerance=2.0):
        """
        Initialize the temperature control system.

        :param target_temp: The target temperature in Celsius.
        :param tolerance: The acceptable temperature deviation from target.
        """
        self.target_temp = target_temp
        self.tolerance = tolerance
        self.current_temp = self.read_temperature()
        self.is_heater_on = False
    
    def read_temperature(self):
        """
        Simulate reading the current temperature from the furnace.
        
        :return: A simulated current temperature value.
        """
        # In a real implementation, this would interface with a temperature sensor.
        return 20 + random.uniform(0, 50)  # Simulated temperature from 20 to 70°C

    def update_current_temp(self):
        """
        Update the current temperature reading.
        """
        self.current_temp = self.read_temperature()
        print(f"Current temperature: {self.current_temp:.2f} °C")

    def control_heater(self):
        """
        Control the heater based on the current temperature and target temperature.
        """
        if self.current_temp < (self.target_temp - self.tolerance):
            self.turn_heater_on()
        elif self.current_temp > (self.target_temp + self.tolerance):
            self.turn_heater_off()
        else:
            print("Temperature is within the acceptable range.")
    
    def turn_heater_on(self):
        """
        Turn the heater on.
        """
        if not self.is_heater_on:
            self.is_heater_on = True
            print("Heater is now ON.")
    
    def turn_heater_off(self):
        """
        Turn the heater off.
        """
        if self.is_heater_on:
            self.is_heater_on = False
            print("Heater is now OFF.")
    
    def run(self):
        """
        Main loop for controlling the temperature system.
        Continuously checks the temperature and adjusts the heater accordingly.
        """
        try:
            while True:
                self.update_current_temp()
                self.control_heater()
                time.sleep(5)  # Wait for 5 seconds before the next check
        except KeyboardInterrupt:
            print("Temperature control system has been stopped.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Specify the target temperature for the furnace
    target_temperature = 600.0  # Example target temperature in Celsius
    control_system = TemperatureControlSystem(target_temp=target_temperature)
    control_system.run()
```
