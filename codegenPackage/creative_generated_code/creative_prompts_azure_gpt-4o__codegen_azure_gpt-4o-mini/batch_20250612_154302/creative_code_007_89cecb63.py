"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbxtools.in
Prompt: Write code to simulate the operation of a pneumatic vacuum leak detector, referencing the specifications provided on the DBX Tools website.
Generated: DETERMINISTIC_89cecb63201dbf5c
Batch ID: 20250612_154302
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

class PneumaticVacuumLeakDetector:
    """
    A class to simulate the operation of a pneumatic vacuum leak detector.

    Attributes:
        pressure_threshold (float): The pressure threshold below which a leak is detected.
        current_pressure (float): The current pressure measured by the detector.
    """

    def __init__(self, pressure_threshold=15.0):
        """
        Initializes the vacuum leak detector with a specified pressure threshold.

        Args:
            pressure_threshold (float): The pressure threshold for leak detection.
        """
        self.pressure_threshold = pressure_threshold
        self.current_pressure = self.measure_pressure()

    def measure_pressure(self):
        """
        Simulates measuring the current pressure in the system.

        Returns:
            float: A simulated pressure value between 10 and 30 psi.
        """
        return round(random.uniform(10.0, 30.0), 2)

    def detect_leak(self):
        """
        Checks if there is a leak based on the current pressure.

        Returns:
            bool: True if a leak is detected, False otherwise.
        """
        self.current_pressure = self.measure_pressure()
        if self.current_pressure < self.pressure_threshold:
            return True
        return False

    def run_detection_cycle(self, cycles=5, delay=2):
        """
        Runs a series of leak detection cycles.

        Args:
            cycles (int): The number of detection cycles to perform.
            delay (int): The delay in seconds between cycles.
        """
        for cycle in range(cycles):
            try:
                leak_detected = self.detect_leak()
                status_message = "Leak detected!" if leak_detected else "No leak detected."
                print(f"Cycle {cycle + 1}: Current Pressure: {self.current_pressure} psi - {status_message}")

                # Delay between readings
                time.sleep(delay)

            except Exception as e:
                print(f"An error occurred during detection: {str(e)}")
                break

if __name__ == "__main__":
    # Create an instance of the pneumatic vacuum leak detector
    detector = PneumaticVacuumLeakDetector(pressure_threshold=15.0)

    # Run the detection cycle
    detector.run_detection_cycle(cycles=5, delay=2)
```
