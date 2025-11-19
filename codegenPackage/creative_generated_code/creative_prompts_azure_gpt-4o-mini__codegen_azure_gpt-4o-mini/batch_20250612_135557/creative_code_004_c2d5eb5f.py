"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osku.cl
Prompt: Illustrate how to implement a monitoring system for packaging performance in cold storage, inspired by Osku's post-sale service approach.
Generated: DETERMINISTIC_c2d5eb5f33562e43
Batch ID: 20250612_135557
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
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ColdStorageMonitor:
    """Class to monitor packaging performance in cold storage."""
    
    def __init__(self, threshold: float):
        """
        Initializes the ColdStorageMonitor with a specific performance threshold.
        
        Parameters:
        threshold (float): The maximum allowable temperature in the cold storage.
        """
        self.threshold = threshold
        self.performance_data: List[Dict[str, Any]] = []

    def simulate_packaging_performance(self) -> float:
        """Simulates the temperature during packaging.
        
        Returns:
        float: A simulated temperature value.
        """
        # Simulate a temperature between -10 and 5 degrees Celsius
        return random.uniform(-10.0, 5.0)

    def log_performance(self) -> None:
        """Logs the packaging performance and checks against the threshold."""
        try:
            temperature = self.simulate_packaging_performance()
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.performance_data.append({"timestamp": timestamp, "temperature": temperature})

            # Log performance data
            logging.info(f"Timestamp: {timestamp}, Temperature: {temperature:.2f} °C")

            # Check if the temperature exceeds the threshold
            if temperature > self.threshold:
                logging.warning(f"Temperature exceeded threshold: {temperature:.2f} °C > {self.threshold:.2f} °C")

        except Exception as e:
            logging.error(f"Error logging performance: {str(e)}")

    def run_monitoring(self, duration: int, interval: int) -> None:
        """
        Runs the monitoring system for a specified duration, logging performance at regular intervals.
        
        Parameters:
        duration (int): Total time to run the monitoring in seconds.
        interval (int): Time interval between performance logs in seconds.
        """
        end_time = time.time() + duration
        while time.time() < end_time:
            self.log_performance()
            time.sleep(interval)

if __name__ == "__main__":
    THRESHOLD_TEMP = 0.0  # Set the threshold temperature for monitoring
    MONITOR_DURATION = 60  # Total duration for monitoring in seconds
    LOG_INTERVAL = 5      # Interval between logs in seconds

    # Create an instance of the ColdStorageMonitor
    monitor = ColdStorageMonitor(threshold=THRESHOLD_TEMP)
    
    # Start monitoring the packaging performance
    logging.info("Starting cold storage monitoring...")
    monitor.run_monitoring(duration=MONITOR_DURATION, interval=LOG_INTERVAL)
    logging.info("Cold storage monitoring completed.")
```
