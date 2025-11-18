"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nordson.vn
Prompt: Recommend a solution for controlling adhesive pressure systems, referencing Nordson's pressure control units.
Generated: DETERMINISTIC_9ee29a4926ac4c41
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

class NordsonPressureControlUnit:
    """
    A class to simulate and control the adhesive pressure systems 
    using Nordson's pressure control units.
    """

    def __init__(self, unit_id, initial_pressure=0.0):
        """
        Initializes the Nordson Pressure Control Unit.

        Parameters:
        - unit_id: Unique identifier for the control unit.
        - initial_pressure: Initial pressure setting (default is 0.0).
        """
        self.unit_id = unit_id
        self.current_pressure = initial_pressure
        self.max_pressure = 100.0  # Maximum pressure limit
        self.min_pressure = 0.0     # Minimum pressure limit

    def set_pressure(self, pressure):
        """
        Sets the adhesive pressure.

        Parameters:
        - pressure: Desired pressure to be set.

        Raises:
        - ValueError: If the pressure is out of bounds.
        """
        if pressure < self.min_pressure or pressure > self.max_pressure:
            raise ValueError(f"Pressure must be between {self.min_pressure} and {self.max_pressure}.")
        
        self.current_pressure = pressure
        print(f"Pressure for unit {self.unit_id} set to {self.current_pressure} PSI.")

    def get_pressure(self):
        """
        Returns the current adhesive pressure.

        Returns:
        - current_pressure: The current pressure value.
        """
        return self.current_pressure

    def simulate_pressure_change(self):
        """
        Simulates random pressure changes within allowed limits.
        This could represent fluctuations in an actual adhesive system.
        """
        change = random.uniform(-5, 5)  # Random pressure change between -5 to 5 PSI
        new_pressure = self.current_pressure + change
        
        try:
            self.set_pressure(new_pressure)
        except ValueError as e:
            print(f"Error: {e}")

    def monitor_pressure(self, duration=60, interval=5):
        """
        Monitors the pressure over a defined duration.

        Parameters:
        - duration: Total time to monitor (in seconds).
        - interval: Time between each pressure reading (in seconds).
        """
        start_time = time.time()
        while (time.time() - start_time) < duration:
            print(f"Monitoring pressure for unit {self.unit_id}: {self.get_pressure()} PSI.")
            self.simulate_pressure_change()
            time.sleep(interval)

# Example usage:
if __name__ == "__main__":
    try:
        unit = NordsonPressureControlUnit(unit_id="NPU-001", initial_pressure=50.0)
        unit.monitor_pressure(duration=30, interval=5)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
