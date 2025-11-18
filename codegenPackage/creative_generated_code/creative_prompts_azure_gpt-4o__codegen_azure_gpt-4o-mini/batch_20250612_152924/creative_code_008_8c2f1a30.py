"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eraengineering.co.in
Prompt: Develop a Python script for monitoring and controlling fire safety systems in residential properties, inspired by ERA ENGINEERING's specialized services.
Generated: DETERMINISTIC_8c2f1a303639566f
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import time
from datetime import datetime

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FireSafetySystem:
    """
    A class to monitor and control fire safety systems in residential properties.
    """

    def __init__(self, property_id):
        """
        Initialize the fire safety system with a unique property ID.

        :param property_id: Unique identifier for the property
        """
        self.property_id = property_id
        self.smoke_detector_active = True
        self.sprinkler_system_active = False
        self.fire_alert = False

    def check_smoke_detector(self):
        """
        Simulates checking the smoke detector's status.
        Returns True if smoke is detected, otherwise False.
        """
        # Simulated smoke detection logic
        smoke_detected = self.simulate_smoke_detection()
        if smoke_detected:
            logging.warning("Smoke detected in property {}".format(self.property_id))
            self.fire_alert = True
            self.activate_sprinkler_system()
        return smoke_detected

    def activate_sprinkler_system(self):
        """
        Activates the sprinkler system if smoke is detected.
        """
        if not self.sprinkler_system_active:
            logging.info("Activating sprinkler system for property {}".format(self.property_id))
            self.sprinkler_system_active = True

    def deactivate_sprinkler_system(self):
        """
        Deactivates the sprinkler system.
        """
        if self.sprinkler_system_active:
            logging.info("Deactivating sprinkler system for property {}".format(self.property_id))
            self.sprinkler_system_active = False

    def simulate_smoke_detection(self):
        """
        Simulates smoke detection logic.
        In a real application, this would interface with actual hardware.

        :return: Boolean indicating whether smoke is detected
        """
        # For demonstration, randomly simulating smoke detection.
        from random import choice
        return choice([True, False])

    def monitor_system(self):
        """
        Monitors the fire safety system at regular intervals.
        """
        try:
            while True:
                logging.info("Checking smoke detector for property {}".format(self.property_id))
                self.check_smoke_detector()
                time.sleep(5)  # Check every 5 seconds
        except KeyboardInterrupt:
            logging.info("Monitoring stopped by user.")
        except Exception as e:
            logging.error("An error occurred while monitoring: {}".format(e))

if __name__ == "__main__":
    # Example usage of the FireSafetySystem
    property_id = "Residential_001"
    fire_safety_system = FireSafetySystem(property_id)
    fire_safety_system.monitor_system()
```
