"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milarbrazw.blogspot.com
Prompt: Recommend a library or API to simulate the functionality of a "Sensor Presença Sobrepor C/ Fotocel Qualitronix Qa26m" in a home automation system, including motion detection and light control.
Generated: DETERMINISTIC_22fadbec7eddbc2f
Batch ID: 20250612_151438
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

class SensorPresenca:
    """
    A class to simulate a motion sensor with light control functionality.
    """

    def __init__(self, sensor_id):
        """
        Initializes the SensorPresenca object.

        :param sensor_id: Unique identifier for the sensor
        """
        self.sensor_id = sensor_id
        self.motion_detected = False
        self.light_on = False

    def detect_motion(self):
        """
        Simulates motion detection.
        
        This method randomly determines if motion is detected.
        """
        self.motion_detected = random.choice([True, False])
        return self.motion_detected

    def control_light(self):
        """
        Controls the light based on motion detection.

        If motion is detected, the light is turned on; otherwise, it's turned off.
        """
        if self.motion_detected:
            if not self.light_on:
                self.light_on = True
                print(f"Light ON - Motion detected by sensor {self.sensor_id}.")
            else:
                print(f"Light already ON - Motion detected by sensor {self.sensor_id}.")
        else:
            if self.light_on:
                self.light_on = False
                print(f"Light OFF - No motion detected by sensor {self.sensor_id}.")
            else:
                print(f"Light already OFF - No motion detected by sensor {self.sensor_id}.")

    def run(self):
        """
        Runs the sensor simulation in a loop, detecting motion and controlling light.
        
        This loop will run indefinitely unless interrupted.
        """
        try:
            while True:
                motion = self.detect_motion()
                self.control_light()
                time.sleep(2)  # Check for motion every 2 seconds
        except KeyboardInterrupt:
            print("Sensor simulation stopped.")

# Usage example
if __name__ == "__main__":
    sensor = SensorPresenca(sensor_id="QA26M-001")
    sensor.run()
```
