"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alicebeauty.bg
Prompt: Generate a Python script that uses the Venus Legacy device for body contouring and skin tightening treatments as described on alicebeauty.bg.
Generated: DETERMINISTIC_3aef8ee75550e15c
Batch ID: 20250612_161616
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

# Configure logging for debugging purposes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VenusLegacyDevice:
    """Class to interact with the Venus Legacy device for body contouring and skin tightening."""

    def __init__(self):
        """Initialize the Venus Legacy device with default settings."""
        self.power = 0
        self.mode = 'standby'
        self.treatment_time = 0

    def power_on(self):
        """Power on the Venus Legacy device."""
        if self.power == 0:
            self.power = 1
            self.mode = 'operational'
            logging.info("Venus Legacy device powered on.")
        else:
            logging.warning("Device is already powered on.")

    def power_off(self):
        """Power off the Venus Legacy device."""
        if self.power == 1:
            self.power = 0
            self.mode = 'standby'
            logging.info("Venus Legacy device powered off.")
        else:
            logging.warning("Device is already powered off.")

    def set_treatment_parameters(self, duration):
        """Set the treatment time for the session.

        Args:
            duration (int): Duration of the treatment in minutes.

        Raises:
            ValueError: If the duration is not a positive integer.
        """
        if isinstance(duration, int) and duration > 0:
            self.treatment_time = duration
            logging.info(f"Treatment time set to {duration} minutes.")
        else:
            logging.error("Invalid duration. Please provide a positive integer.")
            raise ValueError("Duration must be a positive integer.")

    def start_treatment(self):
        """Start the treatment session."""
        if self.power == 1 and self.treatment_time > 0:
            logging.info("Starting treatment session...")
            time.sleep(self.treatment_time * 60)  # Simulate treatment duration
            logging.info("Treatment session completed.")
        else:
            logging.error("Cannot start treatment. Ensure the device is powered on and treatment time is set.")

def main():
    """Main function to run the treatment session."""
    device = VenusLegacyDevice()

    try:
        device.power_on()  # Power on the device
        device.set_treatment_parameters(30)  # Set treatment duration to 30 minutes
        device.start_treatment()  # Start the treatment session
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        device.power_off()  # Ensure the device is powered off at the end

if __name__ == "__main__":
    main()
```
