"""
Generated Code Metadata:
========================
Original URL: https://solucionestecnologicasbogota.com
Prompt: "Generate code for a simple alarm system using Python and Raspberry Pi, inspired by the security solutions offered by Space Tecnologies in Bogotá."
Generated: DETERMINISTIC_8c1f1bde911fbd94
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import RPi.GPIO as GPIO
import time
import datetime
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AlarmSystem:
    def __init__(self, buzzer_pin, sensor_pin):
        """
        Initialize the alarm system.

        Args:
            buzzer_pin (int): The GPIO pin connected to the buzzer.
            sensor_pin (int): The GPIO pin connected to the motion sensor.
        """
        self.buzzer_pin = buzzer_pin
        self.sensor_pin = sensor_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.buzzer_pin, GPIO.OUT)
        GPIO.setup(self.sensor_pin, GPIO.IN)

    def activate_alarm(self):
        """
        Activate the alarm by turning on the buzzer.
        """
        logging.warning("Alarm activated")
        GPIO.output(self.buzzer_pin, GPIO.HIGH)

    def deactivate_alarm(self):
        """
        Deactivate the alarm by turning off the buzzer.
        """
        logging.warning("Alarm deactivated")
        GPIO.output(self.buzzer_pin, GPIO.LOW)

    def check_motion(self):
        """
        Check for motion detected by the sensor.

        Returns:
            bool: True if motion is detected, False otherwise.
        """
        return GPIO.input(self.sensor_pin)

def main():
    try:
        # Define GPIO pins
        BUZZER_PIN = 17
        SENSOR_PIN = 23

        # Create an instance of the AlarmSystem class
        alarm_system = AlarmSystem(BUZZER_PIN, SENSOR_PIN)

        while True:
            # Check for motion
            if alarm_system.check_motion():
                # Activate the alarm
                alarm_system.activate_alarm()
                # Wait for 30 seconds before deactivating the alarm
                time.sleep(30)
                alarm_system.deactivate_alarm()
            else:
                # Deactivate the alarm if no motion is detected
                alarm_system.deactivate_alarm()
            # Wait for 1 second before checking again
            time.sleep(1)

    except KeyboardInterrupt:
        logging.info("Program stopped by user")
        GPIO.cleanup()

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        GPIO.cleanup()

if __name__ == "__main__":
    main()
```
