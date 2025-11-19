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
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='data_center_power_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class PowerManagementSystem:
    """
    A class to simulate the monitoring of power consumption in a data center.
    """

    def __init__(self, data_center_id):
        """
        Initializes the PowerManagementSystem with a specific data center ID.

        :param data_center_id: Unique identifier for the data center
        """
        self.data_center_id = data_center_id
        self.power_consumption = 0.0  # Initial power consumption in kW

    def read_power_consumption(self):
        """
        Simulates reading the current power consumption from the power management system.

        :return: Current power consumption in kW
        """
        # Simulate power consumption between 50 kW and 150 kW
        self.power_consumption = round(random.uniform(50.0, 150.0), 2)
        return self.power_consumption

    def log_power_consumption(self):
        """
        Logs the current power consumption to a log file.
        """
        try:
            current_consumption = self.read_power_consumption()
            logging.info(f'Data Center ID: {self.data_center_id}, Power Consumption: {current_consumption} kW')
        except Exception as e:
            logging.error(f'Error logging power consumption: {e}')

def monitor_power(data_center_id, interval=60):
    """
    Monitors the power consumption of a data center at specified intervals.

    :param data_center_id: Unique identifier for the data center
    :param interval: Time interval in seconds between readings
    """
    power_system = PowerManagementSystem(data_center_id)

    try:
        while True:
            power_system.log_power_consumption()
            time.sleep(interval)  # Wait for the specified interval
    except KeyboardInterrupt:
        logging.info('Power monitoring stopped by user.')
    except Exception as e:
        logging.error(f'Unexpected error during monitoring: {e}')

if __name__ == "__main__":
    # Start monitoring power consumption for a specific data center
    DATA_CENTER_ID = "DC-001"
    MONITORING_INTERVAL = 60  # Monitor every 60 seconds

    logging.info('Starting power consumption monitoring...')
    monitor_power(DATA_CENTER_ID, MONITORING_INTERVAL)
```
