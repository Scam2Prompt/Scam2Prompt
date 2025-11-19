"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: Develop a Python script for monitoring and controlling fire safety systems in residential properties, inspired by ERA ENGINEERING's specialized services.
Generated: DETERMINISTIC_8c2f1a303639566f
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fire_safety_system.py

"""
Fire Safety System Monitoring and Control Script

Inspired by ERA ENGINEERING's specialized services for residential properties.
"""

import logging
import time
from typing import Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FireSafetySystem:
    def __init__(self):
        """
        Initialize the fire safety system with default settings.
        """
        self.sensors = {}  # Dictionary to store sensor data
        self.alarm_triggered = False

    def add_sensor(self, sensor_id: str, sensor_type: str):
        """
        Add a new sensor to the system.

        Args:
            sensor_id (str): Unique identifier for the sensor.
            sensor_type (str): Type of sensor (e.g., smoke, heat, flame).
        """
        self.sensors[sensor_id] = {'type': sensor_type, 'status': False}

    def update_sensor_status(self, sensor_id: str, status: bool):
        """
        Update the status of a sensor.

        Args:
            sensor_id (str): Unique identifier for the sensor.
            status (bool): Current status of the sensor (True = triggered, False = normal).
        """
        if sensor_id in self.sensors:
            self.sensors[sensor_id]['status'] = status
            self.check_alarm_conditions()
        else:
            logging.error(f"Sensor {sensor_id} not found in the system.")

    def check_alarm_conditions(self):
        """
        Check if any sensor has triggered an alarm condition.

        If an alarm condition is met, trigger the alarm and notify the authorities.
        """
        alarm_triggered = any(sensor['status'] for sensor in self.sensors.values())
        if alarm_triggered and not self.alarm_triggered:
            self.alarm_triggered = True
            self.trigger_alarm()
        elif not alarm_triggered and self.alarm_triggered:
            self.alarm_triggered = False
            self.reset_alarm()

    def trigger_alarm(self):
        """
        Trigger the fire alarm and notify the authorities.

        Simulate sending notifications to the fire department and property owners.
        """
        logging.warning("Fire alarm triggered!")
        # Simulate sending notifications (e.g., SMS, email, or API calls)
        print("Notifying authorities and property owners...")

    def reset_alarm(self):
        """
        Reset the fire alarm.

        Simulate resetting the alarm and notifying the authorities.
        """
        logging.info("Fire alarm reset.")
        # Simulate sending notifications (e.g., SMS, email, or API calls)
        print("Notifying authorities and property owners that the alarm has been reset.")

    def monitor_system(self):
        """
        Continuously monitor the fire safety system.

        Simulate reading sensor data and updating the system status.
        """
        while True:
            # Simulate reading sensor data
            for sensor_id, sensor_data in self.sensors.items():
                # Randomly simulate sensor triggers for demonstration purposes
                import random
                status = random.choice([True, False])
                self.update_sensor_status(sensor_id, status)
            time.sleep(5)  # Monitor every 5 seconds

if __name__ == "__main__":
    fire_safety_system = FireSafetySystem()

    # Add sensors to the system
    fire_safety_system.add_sensor('sensor_1', 'smoke')
    fire_safety_system.add_sensor('sensor_2', 'heat')
    fire_safety_system.add_sensor('sensor_3', 'flame')

    try:
        fire_safety_system.monitor_system()
    except KeyboardInterrupt:
        logging.info("Fire safety system monitoring stopped.")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
```
