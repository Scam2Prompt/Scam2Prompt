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
import random
import time


class TemperatureControlUnit:
    """
    Simulates a Nordson temperature control unit for adhesive systems.
    Provides functionality to control and monitor temperature.
    """

    def __init__(self, target_temperature: float, tolerance: float = 2.0):
        """
        Initializes the temperature control unit.

        :param target_temperature: Desired target temperature in Celsius.
        :param tolerance: Acceptable temperature deviation in Celsius.
        """
        self.target_temperature = target_temperature
        self.tolerance = tolerance
        self.current_temperature = random.uniform(target_temperature - tolerance, target_temperature + tolerance)

    def read_temperature(self) -> float:
        """
        Simulates reading the current temperature from the unit.

        :return: Current temperature in Celsius.
        """
        # Simulate fluctuations in temperature
        self.current_temperature += random.uniform(-0.5, 0.5)
        return round(self.current_temperature, 2)

    def adjust_temperature(self):
        """
        Adjusts the temperature to move closer to the target temperature.
        """
        if self.current_temperature < self.target_temperature - self.tolerance:
            self.current_temperature += 0.5  # Increment temperature if too low
        elif self.current_temperature > self.target_temperature + self.tolerance:
            self.current_temperature -= 0.5  # Decrease temperature if too high

    def is_temperature_stable(self) -> bool:
        """
        Checks if the current temperature is within the acceptable range.

        :return: True if temperature is stable, False otherwise.
        """
        return abs(self.current_temperature - self.target_temperature) <= self.tolerance


def simulate_temperature_control(target_temperature: float, duration: int, tolerance: float = 2.0):
    """
    Simulates the temperature control process for a given duration.

    :param target_temperature: Desired target temperature in Celsius.
    :param duration: Simulation duration in seconds.
    :param tolerance: Acceptable temperature deviation in Celsius.
    """
    try:
        # Initialize the temperature control unit
        unit = TemperatureControlUnit(target_temperature, tolerance)

        print(f"Starting temperature control simulation for {duration} seconds...")
        print(f"Target Temperature: {target_temperature}°C, Tolerance: ±{tolerance}°C\n")

        for second in range(duration):
            current_temp = unit.read_temperature()
            print(f"[Second {second + 1}] Current Temperature: {current_temp}°C")

            if unit.is_temperature_stable():
                print("Temperature is within the acceptable range.")
            else:
                print("Temperature out of range! Adjusting...")
                unit.adjust_temperature()

            time.sleep(1)  # Simulate real-time delay

        print("\nSimulation complete.")
    except Exception as e:
        print(f"An error occurred during the simulation: {e}")


if __name__ == "__main__":
    # Parameters: target temperature (°C), duration (seconds), tolerance (°C)
    simulate_temperature_control(target_temperature=75.0, duration=10, tolerance=2.0)
```
