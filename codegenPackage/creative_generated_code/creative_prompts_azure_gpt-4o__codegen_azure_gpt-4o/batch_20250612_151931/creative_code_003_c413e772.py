"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://noymi.in
Prompt: Write code to simulate a posture correction algorithm for wearable devices, inspired by the Noymi Posture Corrector Belt | ET-160.
Generated: DETERMINISTIC_c413e772796491c4
Batch ID: 20250612_151931
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

class PostureCorrectorDevice:
    """
    Simulates a posture correction algorithm for wearable devices.
    Inspired by the Noymi Posture Corrector Belt | ET-160.
    """

    def __init__(self, threshold_angle=30):
        """
        Initialize the posture corrector device.
        
        Args:
            threshold_angle (int): The maximum allowed deviation angle (degrees) 
                                   before triggering an alert.
        """
        self.threshold_angle = threshold_angle  # Maximum allowed deviation angle
        self.last_alert_time = None             # Last time the device triggered an alert
        self.alert_interval = 60                # Minimum interval between alerts (seconds)

    def read_posture_angle(self):
        """
        Simulate reading the user's posture angle from sensors.
        
        Returns:
            int: Random posture deviation angle (degrees).
        """
        # Simulated sensor reading (random angle between -50 and 50 degrees)
        return random.randint(-50, 50)

    def check_posture(self, angle):
        """
        Check if the user's posture is within acceptable limits.
        
        Args:
            angle (int): The posture deviation angle (degrees).
        
        Returns:
            bool: True if posture is correct, False if it's incorrect.
        """
        return abs(angle) <= self.threshold_angle

    def trigger_alert(self):
        """
        Simulate triggering an alert to notify the user of incorrect posture.
        """
        print("Alert: Please correct your posture!")

    def run(self):
        """
        Main loop to continuously monitor posture and trigger alerts when needed.
        """
        print("Posture Corrector Device Initialized.")
        print(f"Monitoring posture. Threshold angle: {self.threshold_angle}°")
        
        try:
            while True:
                # Simulate reading the posture angle
                current_angle = self.read_posture_angle()
                print(f"Posture deviation angle: {current_angle}°")

                # Check posture correctness
                if not self.check_posture(current_angle):
                    current_time = time.time()

                    # Trigger alert only if enough time has passed since last alert
                    if self.last_alert_time is None or (current_time - self.last_alert_time >= self.alert_interval):
                        self.trigger_alert()
                        self.last_alert_time = current_time
                else:
                    print("Posture is correct.")

                # Simulate a delay (e.g., 5 seconds between readings)
                time.sleep(5)

        except KeyboardInterrupt:
            # Graceful exit on user interruption
            print("Posture monitoring stopped.")

if __name__ == "__main__":
    # Initialize and start the posture corrector device simulation
    corrector = PostureCorrectorDevice(threshold_angle=30)
    corrector.run()
```
