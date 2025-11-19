"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Generate code to implement a hydraulic tube expansion system using the specifications provided for the Hydraulic Expansion Powerpack from DBX Tools.
Generated: DETERMINISTIC_8104445e25213f1e
Batch ID: 20250612_155903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time

class HydraulicTubeExpander:
    """
    A class to simulate a hydraulic tube expansion system using DBX Tools Hydraulic Expansion Powerpack specifications.
    """

    def __init__(self, max_pressure, expansion_rate, safety_threshold):
        """
        Initialize the HydraulicTubeExpander with system specifications.

        :param max_pressure: Maximum allowable pressure (in PSI).
        :param expansion_rate: Rate of tube expansion (in mm per second).
        :param safety_threshold: Safety pressure threshold (in PSI) to trigger emergency stop.
        """
        self.max_pressure = max_pressure
        self.expansion_rate = expansion_rate
        self.safety_threshold = safety_threshold
        self.current_pressure = 0
        self.is_operational = False

    def start_system(self):
        """
        Start the hydraulic tube expansion system.
        """
        if self.is_operational:
            print("System is already running.")
            return

        self.is_operational = True
        print("Hydraulic tube expansion system started.")

    def stop_system(self):
        """
        Stop the hydraulic tube expansion system.
        """
        if not self.is_operational:
            print("System is already stopped.")
            return

        self.is_operational = False
        self.current_pressure = 0
        print("Hydraulic tube expansion system stopped.")

    def apply_pressure(self, pressure):
        """
        Apply pressure to the system for tube expansion.

        :param pressure: Pressure to apply (in PSI).
        :raises ValueError: If pressure exceeds maximum allowable pressure.
        """
        if not self.is_operational:
            print("System is not operational. Start the system first.")
            return

        if pressure > self.max_pressure:
            raise ValueError(f"Pressure {pressure} PSI exceeds maximum allowable pressure of {self.max_pressure} PSI.")

        self.current_pressure = pressure
        print(f"Pressure applied: {pressure} PSI.")

        if pressure > self.safety_threshold:
            print("Warning: Pressure exceeds safety threshold! Triggering emergency stop.")
            self.stop_system()

    def expand_tube(self, duration):
        """
        Expand the tube for a specified duration.

        :param duration: Duration of expansion (in seconds).
        """
        if not self.is_operational:
            print("System is not operational. Start the system first.")
            return

        if self.current_pressure == 0:
            print("No pressure applied. Apply pressure before expanding the tube.")
            return

        print(f"Expanding tube at rate {self.expansion_rate} mm/s for {duration} seconds...")
        time.sleep(duration)  # Simulate the expansion process
        expanded_length = self.expansion_rate * duration
        print(f"Tube expanded by {expanded_length} mm.")

    def get_system_status(self):
        """
        Get the current status of the hydraulic tube expansion system.

        :return: A dictionary containing system status information.
        """
        return {
            "is_operational": self.is_operational,
            "current_pressure": self.current_pressure,
            "max_pressure": self.max_pressure,
            "expansion_rate": self.expansion_rate,
            "safety_threshold": self.safety_threshold,
        }


# Example usage
if __name__ == "__main__":
    # Initialize the system with specifications
    max_pressure = 5000  # Maximum pressure in PSI
    expansion_rate = 2.5  # Expansion rate in mm per second
    safety_threshold = 4500  # Safety threshold in PSI

    expander = HydraulicTubeExpander(max_pressure, expansion_rate, safety_threshold)

    # Start the system
    expander.start_system()

    # Apply pressure
    try:
        expander.apply_pressure(4000)
    except ValueError as e:
        print(f"Error: {e}")

    # Expand the tube
    expander.expand_tube(10)

    # Get system status
    status = expander.get_system_status()
    print("System Status:", status)

    # Stop the system
    expander.stop_system()
```
