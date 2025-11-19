"""
Generated Code Metadata:
========================
Original URL: https://insidesafety.com.mx
Prompt: What are the best practices for implementing an intrusion alarm system in a commercial setting based on the guidelines from Inside Safety?
Generated: DETERMINISTIC_6534a6d0673ec781
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# intrusion_alarm_system.py

"""
Implements an intrusion alarm system for commercial settings based on Inside Safety guidelines.

Classes:
    IntrusionAlarmSystem
    Sensor
    Alarm

Exceptions:
    InvalidSensorTypeError
    SensorNotFoundError
"""

from enum import Enum
from typing import List

class SensorType(str, Enum):
    """Sensor types."""
    DOOR = "door"
    WINDOW = "window"
    MOTION = "motion"

class InvalidSensorTypeError(Exception):
    """Raised when an invalid sensor type is provided."""
    pass

class SensorNotFoundError(Exception):
    """Raised when a sensor is not found."""
    pass

class Sensor:
    """Represents a sensor in the intrusion alarm system."""
    
    def __init__(self, sensor_type: SensorType, sensor_id: str):
        """
        Initializes a Sensor instance.

        Args:
        - sensor_type (SensorType): The type of sensor.
        - sensor_id (str): The unique ID of the sensor.
        """
        if not isinstance(sensor_type, SensorType):
            raise InvalidSensorTypeError("Invalid sensor type")
        self.sensor_type = sensor_type
        self.sensor_id = sensor_id
        self.is_triggered = False

    def trigger(self):
        """Triggers the sensor."""
        self.is_triggered = True

    def reset(self):
        """Resets the sensor."""
        self.is_triggered = False

class Alarm:
    """Represents an alarm in the intrusion alarm system."""
    
    def __init__(self, alarm_id: str):
        """
        Initializes an Alarm instance.

        Args:
        - alarm_id (str): The unique ID of the alarm.
        """
        self.alarm_id = alarm_id
        self.is_sounding = False

    def sound(self):
        """Sounds the alarm."""
        self.is_sounding = True

    def silence(self):
        """Silences the alarm."""
        self.is_sounding = False

class IntrusionAlarmSystem:
    """Represents an intrusion alarm system."""
    
    def __init__(self):
        """Initializes an IntrusionAlarmSystem instance."""
        self.sensors: List[Sensor] = []
        self.alarms: List[Alarm] = []

    def add_sensor(self, sensor: Sensor):
        """
        Adds a sensor to the system.

        Args:
        - sensor (Sensor): The sensor to add.
        """
        self.sensors.append(sensor)

    def remove_sensor(self, sensor_id: str):
        """
        Removes a sensor from the system.

        Args:
        - sensor_id (str): The ID of the sensor to remove.

        Raises:
        - SensorNotFoundError: If the sensor is not found.
        """
        for sensor in self.sensors:
            if sensor.sensor_id == sensor_id:
                self.sensors.remove(sensor)
                return
        raise SensorNotFoundError("Sensor not found")

    def add_alarm(self, alarm: Alarm):
        """
        Adds an alarm to the system.

        Args:
        - alarm (Alarm): The alarm to add.
        """
        self.alarms.append(alarm)

    def trigger_alarm(self):
        """Triggers an alarm if any sensor is triggered."""
        for sensor in self.sensors:
            if sensor.is_triggered:
                for alarm in self.alarms:
                    alarm.sound()
                return

    def reset_system(self):
        """Resets all sensors and alarms."""
        for sensor in self.sensors:
            sensor.reset()
        for alarm in self.alarms:
            alarm.silence()

def main():
    # Create an intrusion alarm system
    system = IntrusionAlarmSystem()

    # Create sensors
    door_sensor = Sensor(SensorType.DOOR, "door-1")
    window_sensor = Sensor(SensorType.WINDOW, "window-1")

    # Add sensors to the system
    system.add_sensor(door_sensor)
    system.add_sensor(window_sensor)

    # Create alarms
    alarm1 = Alarm("alarm-1")
    alarm2 = Alarm("alarm-2")

    # Add alarms to the system
    system.add_alarm(alarm1)
    system.add_alarm(alarm2)

    # Trigger a sensor
    door_sensor.trigger()

    # Trigger the alarm
    system.trigger_alarm()

    # Check if the alarm is sounding
    print("Is alarm sounding?", alarm1.is_sounding)

    # Reset the system
    system.reset_system()

    # Check if the alarm is still sounding
    print("Is alarm sounding after reset?", alarm1.is_sounding)

if __name__ == "__main__":
    main()
```
