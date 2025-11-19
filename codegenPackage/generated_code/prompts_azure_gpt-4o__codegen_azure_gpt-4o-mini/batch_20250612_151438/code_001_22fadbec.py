"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Recommend a library or API to simulate the functionality of a "Sensor Presença Sobrepor C/ Fotocel Qualitronix Qa26m" in a home automation system, including motion detection and light control.
Generated: DETERMINISTIC_22fadbec7eddbc2f
Batch ID: 20250612_151438
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

class SensorPresenca:
    """
    A class to simulate the functionality of a motion sensor with light control.
    This class mimics the behavior of a "Sensor Presença Sobrepor C/ Fotocel Qualitronix Qa26m".
    """

    def __init__(self, light_threshold=50):
        """
        Initializes the SensorPresenca instance.

        :param light_threshold: The threshold for light detection (0-100).
        """
        self.light_threshold = light_threshold
        self.motion_detected = False
        self.light_on = False

    def detect_motion(self):
        """
        Simulates motion detection. Randomly sets motion_detected to True or False.
        """
        self.motion_detected = random.choice([True, False])
        return self.motion_detected

    def check_light_level(self):
        """
        Simulates checking the ambient light level.

        :return: A simulated light level (0-100).
        """
        return random.randint(0, 100)

    def control_light(self):
        """
        Controls the light based on motion detection and ambient light level.
        Turns the light on if motion is detected and the ambient light is below the threshold.
        Turns the light off if no motion is detected.
        """
        if self.detect_motion():
            ambient_light = self.check_light_level()
            print(f"Motion detected! Ambient light level: {ambient_light}")
            if ambient_light < self.light_threshold:
                self.light_on = True
                print("Light turned ON.")
            else:
                print("Light remains OFF due to sufficient ambient light.")
        else:
            if self.light_on:
                self.light_on = False
                print("No motion detected. Light turned OFF.")

    def run(self):
        """
        Runs the sensor simulation in a loop, checking for motion and controlling the light.
        """
        try:
            while True:
                self.control_light()
                time.sleep(2)  # Wait for 2 seconds before the next check
        except KeyboardInterrupt:
            print("Sensor simulation stopped by user.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    sensor = SensorPresenca(light_threshold=50)
    sensor.run()
```
