"""
Generated Code Metadata:
========================
Original URL: https://nordson.vn
Prompt: Generate code to simulate temperature control for adhesive systems using Nordson's temperature control units.
Generated: DETERMINISTIC_b4101a6280aa0afb
Batch ID: 20250612_151525
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

class TemperatureControlUnit:
    """
    A class to simulate a temperature control unit for adhesive systems.
    """

    def __init__(self, target_temperature: float, tolerance: float = 2.0):
        """
        Initializes the temperature control unit with a target temperature and tolerance.

        :param target_temperature: The desired temperature to maintain (in Celsius).
        :param tolerance: The acceptable range of deviation from the target temperature (in Celsius).
        """
        self.target_temperature = target_temperature
        self.tolerance = tolerance
        self.current_temperature = self._simulate_initial_temperature()

    def _simulate_initial_temperature(self) -> float:
        """
        Simulates an initial temperature reading.

        :return: A float representing the initial temperature.
        """
        return random.uniform(self.target_temperature - 10, self.target_temperature + 10)

    def read_temperature(self) -> float:
        """
        Simulates reading the current temperature from the control unit.

        :return: The current temperature (in Celsius).
        """
        # Simulate temperature fluctuations
        fluctuation = random.uniform(-1.0, 1.0)
        self.current_temperature += fluctuation
        return self.current_temperature

    def adjust_temperature(self) -> None:
        """
        Adjusts the temperature of the unit to reach the target temperature.
        """
        current_temp = self.read_temperature()
        print(f"Current Temperature: {current_temp:.2f} °C")

        if current_temp < self.target_temperature - self.tolerance:
            self._increase_temperature()
        elif current_temp > self.target_temperature + self.tolerance:
            self._decrease_temperature()
        else:
            print("Temperature is within the acceptable range.")

    def _increase_temperature(self) -> None:
        """
        Increases the temperature of the unit.
        """
        print("Increasing temperature...")
        self.current_temperature += 1.0  # Simulate heating
        time.sleep(1)  # Simulate time delay for heating

    def _decrease_temperature(self) -> None:
        """
        Decreases the temperature of the unit.
        """
        print("Decreasing temperature...")
        self.current_temperature -= 1.0  # Simulate cooling
        time.sleep(1)  # Simulate time delay for cooling

    def run(self, duration: int) -> None:
        """
        Runs the temperature control simulation for a specified duration.

        :param duration: The total time to run the simulation (in seconds).
        """
        start_time = time.time()
        while time.time() - start_time < duration:
            self.adjust_temperature()
            time.sleep(2)  # Wait before the next adjustment

if __name__ == "__main__":
    try:
        # Initialize the temperature control unit with a target temperature of 100 °C
        tc_unit = TemperatureControlUnit(target_temperature=100.0)
        # Run the temperature control simulation for 30 seconds
        tc_unit.run(duration=30)
    except Exception as e:
        print(f"An error occurred: {e}")
```
