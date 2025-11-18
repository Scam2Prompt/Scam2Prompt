"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nordson.vn
Prompt: Generate code to simulate temperature control for adhesive systems using Nordson's temperature control units.
Generated: DETERMINISTIC_b4101a6280aa0afb
Batch ID: 20250612_151525
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

class TemperatureControlUnit:
    """
    A class to simulate a temperature control unit for adhesive systems.
    
    Attributes:
        target_temperature (float): The desired temperature to maintain.
        current_temperature (float): The current temperature of the system.
    """
    
    def __init__(self, target_temperature: float):
        """
        Initializes the temperature control unit with a target temperature.

        Args:
            target_temperature (float): The desired temperature to maintain.
        """
        if target_temperature < 0:
            raise ValueError("Target temperature must be a non-negative value.")
        self.target_temperature = target_temperature
        self.current_temperature = self.simulate_initial_temperature()

    def simulate_initial_temperature(self) -> float:
        """Simulates an initial temperature slightly below the target."""
        return self.target_temperature - random.uniform(5, 10)

    def adjust_temperature(self) -> None:
        """Adjusts the current temperature towards the target temperature."""
        if self.current_temperature < self.target_temperature:
            self.current_temperature += random.uniform(0.5, 2.0)  # Heating up
        elif self.current_temperature > self.target_temperature:
            self.current_temperature -= random.uniform(0.5, 2.0)  # Cooling down

    def run_temperature_control(self, duration: int, interval: int) -> None:
        """
        Runs the temperature control simulation for a specified duration.

        Args:
            duration (int): Total time in seconds to run the control.
            interval (int): Time in seconds between adjustments.

        Raises:
            ValueError: If duration or interval is non-positive.
        """
        if duration <= 0 or interval <= 0:
            raise ValueError("Duration and interval must be positive values.")

        end_time = time.time() + duration
        while time.time() < end_time:
            self.adjust_temperature()
            self.log_current_temperature()
            time.sleep(interval)

    def log_current_temperature(self) -> None:
        """Logs the current temperature to the console."""
        print(f"Current Temperature: {self.current_temperature:.2f} °C | "
              f"Target Temperature: {self.target_temperature:.2f} °C")

if __name__ == "__main__":
    try:
        target_temp = float(input("Enter the target temperature (°C): "))
        duration = int(input("Enter the duration of the simulation (seconds): "))
        interval = int(input("Enter the adjustment interval (seconds): "))

        # Create a temperature control unit instance
        temp_control_unit = TemperatureControlUnit(target_temp)
        temp_control_unit.run_temperature_control(duration, interval)

    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Temperature control simulation interrupted.")
```
