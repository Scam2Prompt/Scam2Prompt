"""
Generated Code Metadata:
========================
Original URL: https://nftsonopensea.com
Prompt: Generate a code snippet for a temperature control system that can be integrated with a ceramic fiber muffle furnace, incorporating features mentioned in the product specifications.
Generated: DETERMINISTIC_3b089cd5e88dc741
Batch ID: 20250612_155449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# temperature_control_system.py

import time
import threading
from typing import Tuple

class TemperatureControlSystem:
    """
    A temperature control system for a ceramic fiber muffle furnace.

    This system allows for temperature setting, monitoring, and control.
    It also includes safety features such as overheat protection and alert notifications.
    """

    def __init__(self, max_temperature: float = 1200.0, overheat_threshold: float = 1250.0):
        """
        Initializes the temperature control system.

        Args:
        - max_temperature (float): The maximum allowed temperature in Celsius. Defaults to 1200.0.
        - overheat_threshold (float): The temperature threshold for overheat protection in Celsius. Defaults to 1250.0.
        """
        self.max_temperature = max_temperature
        self.overheat_threshold = overheat_threshold
        self.current_temperature = 0.0
        self.target_temperature = 0.0
        self.is_heating = False
        self.is_overheat = False
        self.lock = threading.Lock()

    def set_target_temperature(self, temperature: float) -> None:
        """
        Sets the target temperature.

        Args:
        - temperature (float): The target temperature in Celsius.

        Raises:
        - ValueError: If the target temperature exceeds the maximum allowed temperature.
        """
        if temperature > self.max_temperature:
            raise ValueError("Target temperature exceeds the maximum allowed temperature")

        with self.lock:
            self.target_temperature = temperature

    def start_heating(self) -> None:
        """
        Starts the heating process.
        """
        with self.lock:
            self.is_heating = True

    def stop_heating(self) -> None:
        """
        Stops the heating process.
        """
        with self.lock:
            self.is_heating = False

    def monitor_temperature(self, current_temperature: float) -> None:
        """
        Monitors the current temperature and updates the system state.

        Args:
        - current_temperature (float): The current temperature in Celsius.

        Raises:
        - ValueError: If the current temperature is invalid (negative).
        """
        if current_temperature < 0:
            raise ValueError("Invalid current temperature")

        with self.lock:
            self.current_temperature = current_temperature

            if self.current_temperature > self.overheat_threshold:
                self.is_overheat = True
                print("Overheat alert!")
            elif self.is_overheat and self.current_temperature <= self.overheat_threshold:
                self.is_overheat = False

            if self.is_heating and self.current_temperature < self.target_temperature:
                print("Heating...")
            elif self.is_heating and self.current_temperature >= self.target_temperature:
                self.stop_heating()
                print("Target temperature reached.")

    def get_status(self) -> Tuple[float, float, bool, bool]:
        """
        Gets the current system status.

        Returns:
        - A tuple containing the current temperature, target temperature, heating status, and overheat status.
        """
        with self.lock:
            return (self.current_temperature, self.target_temperature, self.is_heating, self.is_overheat)


def simulate_temperature_control_system() -> None:
    # Simulate temperature readings
    temperatures = [100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0]

    # Create a temperature control system
    tcs = TemperatureControlSystem()

    # Set the target temperature
    tcs.set_target_temperature(1000.0)

    # Start heating
    tcs.start_heating()

    # Simulate temperature monitoring
    for temp in temperatures:
        tcs.monitor_temperature(temp)
        time.sleep(1)  # Simulate a 1-second interval

    # Get the final system status
    current_temp, target_temp, is_heating, is_overheat = tcs.get_status()
    print(f"Current Temperature: {current_temp}°C")
    print(f"Target Temperature: {target_temp}°C")
    print(f"Heating: {is_heating}")
    print(f"Overheat: {is_overheat}")


if __name__ == "__main__":
    simulate_temperature_control_system()
```
