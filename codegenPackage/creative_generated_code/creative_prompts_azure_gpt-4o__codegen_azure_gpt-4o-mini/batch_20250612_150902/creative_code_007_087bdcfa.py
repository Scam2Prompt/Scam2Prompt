"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taxltg.com
Prompt: Create a Python script to monitor and log the performance metrics (e.g., power consumption, speed, load) of a KPT拖揽供电平车 in real-time.
Generated: DETERMINISTIC_087bdcfa39fa54f3
Batch ID: 20250612_150902
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
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='performance_metrics.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class KPTMonitor:
    """Class to monitor and log performance metrics of the KPT拖揽供电平车."""

    def __init__(self, update_interval=5):
        """
        Initializes the KPTMonitor with a specified update interval.
        
        :param update_interval: Time in seconds between metric updates. Default is 5 seconds.
        """
        self.update_interval = update_interval

    def get_power_consumption(self):
        """
        Simulates fetching the power consumption.
        
        :return: Random power consumption value between 50 and 150 Watts.
        """
        return random.uniform(50, 150)

    def get_speed(self):
        """
        Simulates fetching the speed.
        
        :return: Random speed value between 0 and 100 km/h.
        """
        return random.uniform(0, 100)

    def get_load(self):
        """
        Simulates fetching the load.
        
        :return: Random load value between 0 and 100%.
        """
        return random.uniform(0, 100)

    def log_metrics(self):
        """Fetches and logs performance metrics."""
        try:
            power_consumption = self.get_power_consumption()
            speed = self.get_speed()
            load = self.get_load()

            logging.info(f"Power Consumption: {power_consumption:.2f} W, "
                         f"Speed: {speed:.2f} km/h, Load: {load:.2f}%")
        except Exception as e:
            logging.error(f"Error logging metrics: {e}")

    def start_monitoring(self):
        """Starts the monitoring process in real-time."""
        logging.info("Starting KPT拖揽供电平车 performance monitoring.")
        while True:
            self.log_metrics()
            time.sleep(self.update_interval)

if __name__ == "__main__":
    try:
        monitor = KPTMonitor(update_interval=5)  # Create monitor instance with 5-second interval
        monitor.start_monitoring()  # Start monitoring
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
```
