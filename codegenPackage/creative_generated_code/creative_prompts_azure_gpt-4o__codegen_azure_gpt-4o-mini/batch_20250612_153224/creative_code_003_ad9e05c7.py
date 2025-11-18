"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://donturesystems.co.ke
Prompt: Write a script to configure an alarm system with intruder detection capabilities, optimized for residential or commercial spaces, inspired by Donture Systems Ltd's services.
Generated: DETERMINISTIC_ad9e05c7b16065a1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import threading
import random

class AlarmSystem:
    def __init__(self):
        self.sensors = []
        self.is_armed = False
        self.intruder_detected = False

    def add_sensor(self, sensor):
        """Add a sensor to the alarm system."""
        self.sensors.append(sensor)

    def arm_system(self):
        """Arm the alarm system, enabling detection."""
        self.is_armed = True
        print("Alarm system is now armed.")

    def disarm_system(self):
        """Disarm the alarm system, disabling detection."""
        self.is_armed = False
        print("Alarm system is now disarmed.")

    def monitor_sensors(self):
        """Continuously monitor the sensors for intruder detection."""
        print("Monitoring sensors...")
        while True:
            if self.is_armed:
                for sensor in self.sensors:
                    if sensor.detect_intruder():
                        self.intruder_detected = True
                        self.trigger_alarm()
                        break
            time.sleep(1)  # Sleep to prevent excessive CPU usage

    def trigger_alarm(self):
        """Trigger the alarm notification."""
        print("Intruder detected! Alarm is triggered!")
        # Here, you could integrate with an external notification system,
        # such as sending alerts to a phone or notifying authorities.


class Sensor:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id

    def detect_intruder(self):
        """
        Simulate intruder detection.
        This method randomly decides if an intruder is detected for demonstration purposes.
        """
        # Randomly return True or False to mimic detection
        return random.choice([True, False])


def main():
    """Main function to configure and run the alarm system."""
    alarm_system = AlarmSystem()

    # Adding sensors to the alarm system
    for i in range(5):
        sensor = Sensor(sensor_id=i)
        alarm_system.add_sensor(sensor)

    # Start the sensor monitoring in a separate thread
    monitoring_thread = threading.Thread(target=alarm_system.monitor_sensors)
    monitoring_thread.daemon = True
    monitoring_thread.start()

    try:
        # User controls to arm or disarm the system
        while True:
            command = input("Enter 'arm' to arm the system or 'disarm' to disarm it (type 'exit' to quit): ").strip().lower()
            if command == 'arm':
                alarm_system.arm_system()
            elif command == 'disarm':
                alarm_system.disarm_system()
            elif command == 'exit':
                print("Exiting the system.")
                break
            else:
                print("Invalid command. Please enter 'arm', 'disarm', or 'exit'.")
    except KeyboardInterrupt:
        print("\nSystem interrupted. Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the thread is properly cleaned up
        monitoring_thread.join(timeout=1)


if __name__ == "__main__":
    main()
```
