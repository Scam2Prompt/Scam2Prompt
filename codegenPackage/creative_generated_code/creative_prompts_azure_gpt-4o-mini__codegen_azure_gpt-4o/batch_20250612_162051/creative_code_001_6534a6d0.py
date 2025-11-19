"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://insidesafety.com.mx
Prompt: What are the best practices for implementing an intrusion alarm system in a commercial setting based on the guidelines from Inside Safety?
Generated: DETERMINISTIC_6534a6d0673ec781
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is the clean, production-ready Python code for implementing an intrusion alarm system. It is based on general best practices that could be derived from safety guidelines such as those from "Inside Safety."

```python
import time
import logging
from threading import Thread

# Configure logging for monitoring and debugging
logging.basicConfig(
    filename="alarm_system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class IntrusionAlarmSystem:
    """
    Class representing an intrusion alarm system for a commercial setting.
    """

    def __init__(self, sensors, alarm_duration=10):
        """
        Initializes the alarm system.

        Args:
        - sensors (list): List of sensor objects, each capable of detecting intrusion.
        - alarm_duration (int): Duration (in seconds) the alarm should remain active.
        """
        self.sensors = sensors  # List of sensors
        self.alarm_duration = alarm_duration  # Time the alarm stays active
        self.alarm_active = False  # State of the alarm

    def monitor_sensors(self):
        """
        Continuously monitor sensors for intrusion events.
        """
        logging.info("Starting sensor monitoring.")
        try:
            while True:
                for sensor in self.sensors:
                    if sensor.detect_intrusion():
                        logging.warning(f"Intrusion detected by {sensor.name}. Activating alarm.")
                        self.activate_alarm()
                time.sleep(1)  # Polling interval to check sensors
        except Exception as e:
            logging.error(f"Error occurred during sensor monitoring: {e}")
        finally:
            logging.info("Stopped sensor monitoring.")

    def activate_alarm(self):
        """
        Activates the alarm for the specified duration.
        """
        if not self.alarm_active:
            self.alarm_active = True
            logging.info("Alarm activated.")
            # Trigger the alarm in a separate thread to avoid blocking
            Thread(target=self._alarm_thread).start()

    def _alarm_thread(self):
        """
        Separate thread to handle alarm logic without blocking the main application.
        """
        try:
            # Simulating alarm sound or alert
            logging.info("Alarm sounding...")
            time.sleep(self.alarm_duration)
            logging.info("Alarm deactivated.")
        except Exception as e:
            logging.error(f"Error occurred during alarm activation: {e}")
        finally:
            self.alarm_active = False

class Sensor:
    """
    Class representing a sensor capable of detecting intrusion.
    """

    def __init__(self, name, detection_function):
        """
        Initializes a sensor.

        Args:
        - name (str): Name of the sensor.
        - detection_function (callable): Function that returns True if intrusion is detected.
        """
        self.name = name
        self.detection_function = detection_function

    def detect_intrusion(self):
        """
        Detects intrusion using the provided detection function.

        Returns:
        - bool: True if intrusion is detected, False otherwise.
        """
        try:
            return self.detection_function()
        except Exception as e:
            logging.error(f"Error in detection function for {self.name}: {e}")
            return False

# Example intrusion detection function
def example_detection_function():
    """
    Simulates intrusion detection logic.

    Returns:
    - bool: Randomly simulates intrusion detection.
    """
    import random
    return random.choice([True, False])

if __name__ == "__main__":
    # Create sensors
    sensor1 = Sensor("Front Door Sensor", example_detection_function)
    sensor2 = Sensor("Back Window Sensor", example_detection_function)

    # Initialize alarm system with sensors
    alarm_system = IntrusionAlarmSystem(sensors=[sensor1, sensor2])

    # Start monitoring sensors
    monitoring_thread = Thread(target=alarm_system.monitor_sensors)
    monitoring_thread.start()

    # Main application loop
    try:
        while True:
            time.sleep(10)  # Simulate main application workload
    except KeyboardInterrupt:
        logging.info("Application terminated by user.")
```

This code implements a basic intrusion alarm system with sensors, proper monitoring, and alarm handling, following the best practices for clean, maintainable, and production-ready software.
