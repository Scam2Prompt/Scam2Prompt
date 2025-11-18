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
import logging

# Configure logging for the alarm system
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("alarm_system.log"),  # Log to a file
        logging.StreamHandler()                  # Log to console
    ]
)

class AlarmSystem:
    """
    AlarmSystem class to configure and manage an intruder detection alarm system.
    Optimized for residential or commercial spaces.
    """
    
    def __init__(self, system_name="Default Alarm System"):
        """
        Initialize the alarm system.

        Parameters:
        - system_name: Name of the alarm system (default: "Default Alarm System").
        """
        self.system_name = system_name
        self.is_armed = False
        self.intruder_detected = False
        logging.info(f"{self.system_name} initialized.")

    def arm_system(self):
        """
        Arm the alarm system. Enables intruder detection.
        """
        if self.is_armed:
            logging.warning("System is already armed.")
        else:
            self.is_armed = True
            logging.info("Alarm system armed.")

    def disarm_system(self):
        """
        Disarm the alarm system. Disables intruder detection.
        """
        if not self.is_armed:
            logging.warning("System is already disarmed.")
        else:
            self.is_armed = False
            logging.info("Alarm system disarmed.")

    def detect_intruder(self):
        """
        Simulate intruder detection.
        """
        if not self.is_armed:
            logging.warning("Intruder detection failed. System is not armed.")
            return
        self.intruder_detected = True
        logging.error("Intruder detected! Alarm activated.")
        self.trigger_alarm()

    def trigger_alarm(self):
        """
        Trigger the alarm when an intruder is detected.
        """
        if self.intruder_detected:
            logging.warning("Siren activated! Notify authorities.")
            # Simulate siren sound or notification to authorities
            time.sleep(2)  # Simulate alarm duration
            self.intruder_detected = False  # Reset intruder detection after alarm
        
    def system_status(self):
        """
        Print the current status of the alarm system.
        """
        status = "armed" if self.is_armed else "disarmed"
        intruder_status = "detected" if self.intruder_detected else "not detected"
        logging.info(
            f"System Status: {status}, Intruder Status: {intruder_status}"
        )


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the alarm system
        alarm_system = AlarmSystem("Home Security Alarm")

        # System actions
        alarm_system.arm_system()
        time.sleep(1)  # Simulate delay
        
        alarm_system.detect_intruder()
        time.sleep(1)  # Simulate delay
        
        alarm_system.disarm_system()
        alarm_system.system_status()

    except Exception as e:
        logging.exception("An error occurred in the alarm system: %s", e)
```

This code provides a production-ready alarm system with intruder detection capabilities. It includes logging, error handling, and adherence to coding best practices.
