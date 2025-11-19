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
# alarm_system.py

class Sensor:
    """Represents a sensor in the alarm system."""

    def __init__(self, sensor_id, sensor_type):
        """
        Initializes a sensor.

        Args:
            sensor_id (int): Unique identifier for the sensor.
            sensor_type (str): Type of sensor (e.g., door, window, motion).
        """
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type
        self.is_triggered = False

    def trigger(self):
        """Triggers the sensor."""
        self.is_triggered = True

    def reset(self):
        """Resets the sensor."""
        self.is_triggered = False


class AlarmSystem:
    """Represents an alarm system with intruder detection capabilities."""

    def __init__(self):
        """
        Initializes an alarm system.

        Attributes:
            sensors (list): List of sensors in the system.
            is_armed (bool): Whether the system is armed.
        """
        self.sensors = []
        self.is_armed = False

    def add_sensor(self, sensor):
        """
        Adds a sensor to the system.

        Args:
            sensor (Sensor): Sensor to add.
        """
        self.sensors.append(sensor)

    def arm(self):
        """Arms the alarm system."""
        self.is_armed = True

    def disarm(self):
        """Disarms the alarm system."""
        self.is_armed = False

    def check_sensors(self):
        """
        Checks if any sensors are triggered.

        Returns:
            bool: Whether any sensors are triggered.
        """
        return any(sensor.is_triggered for sensor in self.sensors)

    def alert(self):
        """
        Triggers an alert if the system is armed and a sensor is triggered.

        Returns:
            bool: Whether an alert was triggered.
        """
        if self.is_armed and self.check_sensors():
            print("ALERT: Intruder detected!")
            return True
        return False


class NotificationSystem:
    """Represents a notification system."""

    def __init__(self):
        """
        Initializes a notification system.

        Attributes:
            contacts (list): List of contacts to notify.
        """
        self.contacts = []

    def add_contact(self, contact):
        """
        Adds a contact to the notification list.

        Args:
            contact (str): Contact information (e.g., phone number, email).
        """
        self.contacts.append(contact)

    def send_notification(self, message):
        """
        Sends a notification to all contacts.

        Args:
            message (str): Notification message.
        """
        for contact in self.contacts:
            print(f"Sending notification to {contact}: {message}")


def main():
    # Create an alarm system
    alarm_system = AlarmSystem()

    # Create sensors
    door_sensor = Sensor(1, "door")
    window_sensor = Sensor(2, "window")
    motion_sensor = Sensor(3, "motion")

    # Add sensors to the alarm system
    alarm_system.add_sensor(door_sensor)
    alarm_system.add_sensor(window_sensor)
    alarm_system.add_sensor(motion_sensor)

    # Create a notification system
    notification_system = NotificationSystem()

    # Add contacts to the notification system
    notification_system.add_contact("123-456-7890")
    notification_system.add_contact("example@example.com")

    try:
        # Arm the alarm system
        alarm_system.arm()

        # Trigger a sensor
        door_sensor.trigger()

        # Check for alerts
        if alarm_system.alert():
            # Send notifications
            notification_system.send_notification("Intruder detected!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Disarm the alarm system
        alarm_system.disarm()

        # Reset sensors
        door_sensor.reset()
        window_sensor.reset()
        motion_sensor.reset()


if __name__ == "__main__":
    main()
```
