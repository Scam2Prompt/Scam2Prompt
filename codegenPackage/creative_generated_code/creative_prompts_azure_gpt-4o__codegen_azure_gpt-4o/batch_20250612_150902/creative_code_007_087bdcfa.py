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
    filename='kpt_performance.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class KPTPerformanceMonitor:
    """
    A class to monitor and log the performance metrics of a KPT拖揽供电平车 in real-time.
    """

    def __init__(self, polling_interval=5):
        """
        Initialize the performance monitor.

        Args:
            polling_interval (int): Time interval (in seconds) between metric readings.
        """
        self.polling_interval = polling_interval
        self.is_monitoring = False

    def get_power_consumption(self):
        """
        Simulate fetching the current power consumption of the KPT trolley.

        Returns:
            float: Power consumption in kilowatts (kW).
        """
        # Simulated value (replace with actual hardware API call in production)
        return round(random.uniform(1.0, 5.0), 2)

    def get_speed(self):
        """
        Simulate fetching the current speed of the KPT trolley.

        Returns:
            float: Speed in meters per second (m/s).
        """
        # Simulated value (replace with actual hardware API call in production)
        return round(random.uniform(0.5, 3.0), 2)

    def get_load(self):
        """
        Simulate fetching the current load of the KPT trolley.

        Returns:
            float: Load in tons (t).
        """
        # Simulated value (replace with actual hardware API call in production)
        return round(random.uniform(0.1, 10.0), 2)

    def log_metrics(self):
        """
        Fetch and log the performance metrics of the KPT trolley.
        """
        try:
            metrics = {
                "power_consumption_kW": self.get_power_consumption(),
                "speed_m_per_s": self.get_speed(),
                "load_tons": self.get_load(),
            }

            logging.info(
                "Power Consumption: %.2f kW, Speed: %.2f m/s, Load: %.2f tons",
                metrics["power_consumption_kW"],
                metrics["speed_m_per_s"],
                metrics["load_tons"]
            )
            print(f"[{datetime.now()}] Metrics logged: {metrics}")

        except Exception as e:
            # Log any exceptions that occur during metric collection
            logging.error("Error during metric logging: %s", str(e))
            print(f"Error occurred: {e}")

    def start_monitoring(self):
        """
        Start monitoring the performance metrics of the KPT trolley.
        """
        self.is_monitoring = True
        print("Started monitoring KPT trolley performance. Press Ctrl+C to stop.")

        try:
            while self.is_monitoring:
                self.log_metrics()
                time.sleep(self.polling_interval)
        except KeyboardInterrupt:
            # Gracefully handle the termination of monitoring
            print("\nMonitoring stopped.")
            logging.info("Monitoring stopped by user.")
            self.is_monitoring = False

if __name__ == "__main__":
    # Create an instance of the performance monitor with a 5-second interval
    monitor = KPTPerformanceMonitor(polling_interval=5)

    # Start monitoring
    monitor.start_monitoring()
```
