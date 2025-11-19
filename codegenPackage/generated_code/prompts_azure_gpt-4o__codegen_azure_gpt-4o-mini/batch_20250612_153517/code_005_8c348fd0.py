"""
Generated Code Metadata:
========================
Original URL: https://thinktech.com.pk
Prompt: Create a program to monitor and analyze electrical safety compliance in real-time, inspired by Think Tech Engineering's services.
Generated: DETERMINISTIC_8c348fd04ad463de
Batch ID: 20250612_153517
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
import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ElectricalSafetyMonitor:
    def __init__(self, threshold: float):
        """
        Initializes the ElectricalSafetyMonitor with a specified compliance threshold.

        :param threshold: The maximum allowable electrical reading for compliance.
        """
        self.threshold = threshold
        self.readings: List[Dict[str, float]] = []

    def simulate_reading(self) -> float:
        """
        Simulates an electrical reading. In a real application, this would interface with hardware.

        :return: A simulated electrical reading.
        """
        return random.uniform(0, self.threshold * 2)  # Simulate readings up to twice the threshold

    def check_compliance(self, reading: float) -> bool:
        """
        Checks if the given reading is within compliance.

        :param reading: The electrical reading to check.
        :return: True if compliant, False otherwise.
        """
        return reading <= self.threshold

    def log_reading(self, reading: float):
        """
        Logs the reading and its compliance status.

        :param reading: The electrical reading to log.
        """
        compliant = self.check_compliance(reading)
        status = "Compliant" if compliant else "Non-Compliant"
        logging.info(f"Reading: {reading:.2f} - Status: {status}")
        self.readings.append({"reading": reading, "compliant": compliant})

    def monitor(self, duration: int, interval: int):
        """
        Monitors electrical readings for a specified duration at regular intervals.

        :param duration: Total time to monitor in seconds.
        :param interval: Time between readings in seconds.
        """
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                reading = self.simulate_reading()
                self.log_reading(reading)
                time.sleep(interval)
            except Exception as e:
                logging.error(f"An error occurred while monitoring: {e}")

if __name__ == "__main__":
    # Set the compliance threshold (example: 50.0 volts)
    compliance_threshold = 50.0
    monitor_duration = 60  # Monitor for 60 seconds
    reading_interval = 5    # Read every 5 seconds

    # Create an instance of the ElectricalSafetyMonitor
    safety_monitor = ElectricalSafetyMonitor(threshold=compliance_threshold)

    # Start monitoring
    logging.info("Starting electrical safety compliance monitoring...")
    safety_monitor.monitor(duration=monitor_duration, interval=reading_interval)
    logging.info("Monitoring completed.")
```
