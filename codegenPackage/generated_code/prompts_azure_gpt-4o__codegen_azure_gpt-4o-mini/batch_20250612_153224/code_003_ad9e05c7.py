"""
Generated Code Metadata:
========================
Original URL: https://donturesystems.co.ke
Prompt: Write a script to configure an alarm system with intruder detection capabilities, optimized for residential or commercial spaces, inspired by Donture Systems Ltd's services.
Generated: DETERMINISTIC_ad9e05c7b16065a1
Batch ID: 20250612_153224
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

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AlarmSystem:
    def __init__(self):
        """Initialize the alarm system with default settings."""
        self.is_armed = False
        self.intruder_detected = False
        self.sensors = []
        self.alarm_triggered = False

    def add_sensor(self, sensor):
        """Add a sensor to the alarm system."""
        self.sensors.append(sensor)
        logging.info(f'Sensor {sensor.name} added to the system.')

    def arm_system(self):
        """Arm the alarm system."""
        self.is_armed = True
        logging.info('Alarm system armed.')

    def disarm_system(self):
        """Disarm the alarm system."""
        self.is_armed = False
        self.intruder_detected = False
        self.alarm_triggered = False
        logging.info('Alarm system disarmed.')

    def check_sensors(self):
        """Check all sensors for intruder detection."""
        if not self.is_armed:
            logging.warning('System is not armed. No detection will occur.')
            return

        for sensor in self.sensors:
            if sensor.detect_intruder():
                self.intruder_detected = True
                logging.info(f'Intruder detected by {sensor.name}.')
                self.trigger_alarm()
                break

    def trigger_alarm(self):
        """Trigger the alarm if an intruder is detected."""
        if not self.alarm_triggered:
            self.alarm_triggered = True
            logging.warning('Alarm triggered! Intruder detected!')
            self.notify_authorities()

    def notify_authorities(self):
        """Notify authorities about the intruder detection."""
        logging.info('Notifying authorities...')
        # Simulate notification delay
        time.sleep(2)
        logging.info('Authorities notified successfully.')

class Sensor:
    def __init__(self, name):
        """Initialize a sensor with a given name."""
        self.name = name

    def detect_intruder(self):
        """Simulate intruder detection with a random chance."""
        detection_chance = random.random()
        return detection_chance < 0.1  # 10% chance of detecting an intruder

def main():
    """Main function to configure and run the alarm system."""
    try:
        alarm_system = AlarmSystem()

        # Adding sensors to the alarm system
        alarm_system.add_sensor(Sensor("Front Door"))
        alarm_system.add_sensor(Sensor("Back Door"))
        alarm_system.add_sensor(Sensor("Window Sensor"))

        # Arm the system
        alarm_system.arm_system()

        # Simulate periodic checks for intruders
        while True:
            alarm_system.check_sensors()
            time.sleep(5)  # Check every 5 seconds

    except KeyboardInterrupt:
        logging.info('Alarm system shutting down.')
    except Exception as e:
        logging.error(f'An error occurred: {e}')

if __name__ == "__main__":
    main()
```
