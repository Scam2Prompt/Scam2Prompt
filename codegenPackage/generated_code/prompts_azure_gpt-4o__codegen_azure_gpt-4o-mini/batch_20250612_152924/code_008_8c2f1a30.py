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
import time
import random
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FireSafetySystem:
    def __init__(self):
        """Initialize the fire safety system with default parameters."""
        self.smoke_detector_active = True
        self.sprinkler_system_active = False
        self.alarm_active = False

    def check_smoke_detector(self):
        """Simulate checking the smoke detector status."""
        # Simulate smoke detection with a random boolean
        smoke_detected = random.choice([True, False])
        logging.info(f"Smoke detected: {smoke_detected}")
        return smoke_detected

    def activate_alarm(self):
        """Activate the fire alarm system."""
        if not self.alarm_active:
            self.alarm_active = True
            logging.warning("Fire alarm activated!")

    def deactivate_alarm(self):
        """Deactivate the fire alarm system."""
        if self.alarm_active:
            self.alarm_active = False
            logging.info("Fire alarm deactivated.")

    def activate_sprinkler_system(self):
        """Activate the sprinkler system."""
        if not self.sprinkler_system_active:
            self.sprinkler_system_active = True
            logging.warning("Sprinkler system activated!")

    def deactivate_sprinkler_system(self):
        """Deactivate the sprinkler system."""
        if self.sprinkler_system_active:
            self.sprinkler_system_active = False
            logging.info("Sprinkler system deactivated.")

    def monitor_system(self):
        """Monitor the fire safety system and respond to smoke detection."""
        try:
            while True:
                if self.smoke_detector_active:
                    if self.check_smoke_detector():
                        self.activate_alarm()
                        self.activate_sprinkler_system()
                    else:
                        self.deactivate_alarm()
                        self.deactivate_sprinkler_system()
                time.sleep(5)  # Check every 5 seconds
        except KeyboardInterrupt:
            logging.info("Monitoring stopped by user.")
        except Exception as e:
            logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    fire_safety_system = FireSafetySystem()
    logging.info("Starting fire safety system monitoring...")
    fire_safety_system.monitor_system()
```
