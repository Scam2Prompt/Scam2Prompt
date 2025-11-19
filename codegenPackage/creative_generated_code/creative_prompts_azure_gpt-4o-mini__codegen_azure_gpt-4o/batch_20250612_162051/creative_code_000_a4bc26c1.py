"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://al-afdel.com
Prompt: Write a Python script to automate the process of detecting water leaks in residential buildings, incorporating techniques mentioned in the content about water leak detection services.
Generated: DETERMINISTIC_a4bc26c12c149671
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import time
import logging
import random
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="water_leak_detection.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

class WaterLeakDetector:
    """
    Class to simulate and detect water leaks in residential buildings.
    """

    def __init__(self, detection_threshold=0.1, monitoring_interval=5):
        """
        Initialize the WaterLeakDetector.

        :param detection_threshold: Threshold for leak detection (higher values indicate higher sensitivity).
        :param monitoring_interval: Interval in seconds between sensor readings.
        """
        self.detection_threshold = detection_threshold
        self.monitoring_interval = monitoring_interval
        self.sensors = self._initialize_sensors()

    def _initialize_sensors(self):
        """
        Initialize sensors for detecting water leaks.
        Here we simulate sensors by generating random water flow data.

        :return: A dictionary representing the water flow rate for each simulated sensor.
        """
        sensors = {
            "sensor_1": random.uniform(0, 0.05),  # Normal flow rate (liters/second)
            "sensor_2": random.uniform(0, 0.05),
            "sensor_3": random.uniform(0, 0.05),
        }
        logging.info("Sensors initialized with baseline values.")
        return sensors

    def _simulate_sensor_readings(self):
        """
        Simulate random water flow readings from sensors.

        :return: A dictionary of simulated sensor readings.
        """
        return {sensor: reading + random.uniform(0, 0.1) for sensor, reading in self.sensors.items()}

    def _detect_leaks(self, sensor_readings):
        """
        Detect water leaks based on sensor readings exceeding the detection threshold.

        :param sensor_readings: Water flow data from sensors.
        :return: A list of sensors with detected leaks.
        """
        leaks = [sensor for sensor, flow in sensor_readings.items() if flow > self.detection_threshold]
        if leaks:
            logging.warning(f"Water leaks detected in sensors: {', '.join(leaks)}")
        return leaks

    def monitor(self):
        """
        Continuously monitor sensors for water leaks based on the configured interval.
        """
        try:
            logging.info("Starting water leak detection monitoring...")
            while True:
                sensor_readings = self._simulate_sensor_readings()
                logging.info(f"Sensor readings: {sensor_readings}")

                leaks = self._detect_leaks(sensor_readings)
                if leaks:
                    print(f"Alert! Water leaks detected in sensors: {', '.join(leaks)}")

                time.sleep(self.monitoring_interval)
        except KeyboardInterrupt:
            logging.info("Monitoring stopped by user.")
        except Exception as e:
            logging.error(f"An error occurred during monitoring: {e}")

if __name__ == "__main__":
    # Initialize the detector with custom parameters if needed
    detector = WaterLeakDetector(detection_threshold=0.15, monitoring_interval=10)

    # Start monitoring for water leaks
    detector.monitor()
```
