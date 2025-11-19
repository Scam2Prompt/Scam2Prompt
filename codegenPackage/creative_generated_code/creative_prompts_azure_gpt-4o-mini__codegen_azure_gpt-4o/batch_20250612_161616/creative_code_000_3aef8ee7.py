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
"""
Venus Legacy Device Simulation Script

This Python script simulates the Venus Legacy device for body contouring and 
skin tightening treatments. Note: This simulation does not control the actual 
hardware device and is meant for educational and illustrative purposes only.

Disclaimer: The Venus Legacy device is a medical-grade device. This script 
does not interact with the real device or its API. Consult the device 
manufacturer's documentation for proper usage.

Author: <Your Name>
"""

import time
import logging

# Setup logging to record events and errors
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

class VenusLegacyDevice:
    """
    A simulated Venus Legacy device class for body contouring and skin tightening.
    """
    def __init__(self):
        """Initialize the device."""
        self.is_on = False
        self.mode = None

    def power_on(self):
        """
        Power on the device.
        """
        if self.is_on:
            logging.warning("Device is already powered on.")
        else:
            self.is_on = True
            logging.info("Device powered on.")

    def power_off(self):
        """
        Power off the device.
        """
        if not self.is_on:
            logging.warning("Device is already powered off.")
        else:
            self.is_on = False
            self.mode = None
            logging.info("Device powered off.")

    def set_mode(self, mode):
        """
        Set the operation mode of the device.
        
        Modes:
        - 'contouring': Body contouring treatment
        - 'tightening': Skin tightening treatment
        
        Parameters:
        mode (str): The operation mode.
        """
        if not self.is_on:
            logging.error("Cannot set mode. The device is powered off.")
            raise RuntimeError("Device must be powered on to set mode.")
        
        if mode not in ['contouring', 'tightening']:
            logging.error(f"Invalid mode: {mode}")
            raise ValueError("Mode must be 'contouring' or 'tightening'.")
        
        self.mode = mode
        logging.info(f"Device set to {mode} mode.")

    def start_treatment(self):
        """
        Start the treatment based on the current mode.
        """
        if not self.is_on:
            logging.error("Cannot start treatment. The device is powered off.")
            raise RuntimeError("Device must be powered on to start treatment.")
        
        if self.mode is None:
            logging.error("Cannot start treatment. No mode is set.")
            raise RuntimeError("Mode must be set before starting treatment.")
        
        logging.info(f"Starting {self.mode} treatment...")
        try:
            # Simulate treatment duration
            for i in range(5):
                logging.info(f"Treatment in progress... {i+1}/5 minutes")
                time.sleep(1)  # Simulate 1 minute per iteration
            logging.info(f"{self.mode.capitalize()} treatment completed successfully.")
        except Exception as e:
            logging.error(f"An error occurred during treatment: {e}")
            raise RuntimeError("Treatment interrupted due to an error.")

    def device_status(self):
        """
        Print the current status of the device.
        """
        status = {
            'powered_on': self.is_on,
            'current_mode': self.mode if self.is_on else None
        }
        logging.info(f"Device Status: {status}")
        return status

# Example usage
if __name__ == "__main__":
    try:
        venus_device = VenusLegacyDevice()

        # Power on the device and configure mode
        venus_device.power_on()
        venus_device.set_mode('contouring')
        venus_device.device_status()

        # Start treatment
        venus_device.start_treatment()

        # Power off after treatment
        venus_device.power_off()
        venus_device.device_status()

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
