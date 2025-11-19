"""
Generated Code Metadata:
========================
Original URL: https://vertiv.dns.cz
Prompt: "Write a Python script to simulate the monitoring of data center power consumption using Vertiv's power management systems."
Generated: DETERMINISTIC_aba5ff150f2fc3ed
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
import logging

# Configure logging to log power consumption data and errors
logging.basicConfig(
    filename='power_consumption.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DataCenterPowerMonitor:
    """
    A class to simulate monitoring of data center power consumption using Vertiv's power management systems.
    """

    def __init__(self, num_racks: int):
        """
        Initialize the power monitor with the number of racks in the data center.

        :param num_racks: Number of racks in the data center to monitor.
        """
        self.num_racks = num_racks
        self.rack_power_data = {f"Rack_{i+1}": 0.0 for i in range(num_racks)}

    def simulate_power_consumption(self):
        """
        Simulate power consumption for each rack in the data center.
        Randomly generates power consumption values between 100 and 500 watts.
        """
        for rack in self.rack_power_data:
            self.rack_power_data[rack] = round(random.uniform(100, 500), 2)

    def log_power_consumption(self):
        """
        Log the current power consumption data for all racks.
        """
        for rack, power in self.rack_power_data.items():
            logging.info(f"{rack} - Power Consumption: {power} watts")

    def monitor(self, interval: int = 5):
        """
        Start monitoring power consumption at regular intervals.

        :param interval: Time interval (in seconds) between power consumption updates.
        """
        try:
            logging.info("Starting power consumption monitoring...")
            while True:
                self.simulate_power_consumption()
                self.log_power_consumption()
                time.sleep(interval)
        except KeyboardInterrupt:
            logging.info("Power consumption monitoring stopped by user.")
        except Exception as e:
            logging.error(f"An error occurred during monitoring: {e}")

if __name__ == "__main__":
    # Number of racks in the data center
    NUM_RACKS = 10

    # Create an instance of the power monitor
    power_monitor = DataCenterPowerMonitor(num_racks=NUM_RACKS)

    # Start monitoring power consumption with a 5-second interval
    power_monitor.monitor(interval=5)
```
