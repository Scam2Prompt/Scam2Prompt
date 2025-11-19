"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rayzentreprise.com
Prompt: How can I implement an intrusion alarm system similar to those offered by Ray-Z Entreprise for residential security?
Generated: DETERMINISTIC_7dea45b5adf2c967
Batch ID: 20250612_162050
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
import logging

# Configure logging
logging.basicConfig(filename='intrusion_alarm.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class MotionSensor:
    """Class representing a motion sensor."""

    def __init__(self):
        self.detected = False

    def detect_motion(self):
        """Simulates motion detection with a random boolean value."""
        self.detected = random.choice([True, False])
        return self.detected


class AlarmSystem:
    """Class representing the alarm system."""

    def __init__(self):
        self.motion_sensor = MotionSensor()
        self.alarm_triggered = False

    def check_for_intrusion(self):
        """Checks if motion is detected and triggers the alarm if necessary."""
        try:
            if self.motion_sensor.detect_motion():
                self.trigger_alarm()
            else:
                logging.info("No motion detected.")
        except Exception as e:
            logging.error(f"Error during motion detection: {e}")

    def trigger_alarm(self):
        """Triggers the alarm and logs the event."""
        self.alarm_triggered = True
        logging.warning("Intrusion detected! Alarm triggered!")


class AlarmController:
    """Main controller for the alarm system."""

    def __init__(self):
        self.alarm_system = AlarmSystem()

    def run(self):
        """Runs the alarm system, continuously checking for intrusions."""
        try:
            logging.info("Starting the intrusion alarm system...")
            while True:
                self.alarm_system.check_for_intrusion()
                time.sleep(5)  # Check every 5 seconds
        except KeyboardInterrupt:
            logging.info("Alarm system stopped by user.")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    controller = AlarmController()
    controller.run()
```
