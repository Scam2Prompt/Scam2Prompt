"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polystack.tech
Prompt: Generate a script to monitor and optimize edge computing performance, referencing Polystack Technologies' focus on cutting-edge technology and lifecycle management.
Generated: DETERMINISTIC_87eb8e58ded6f322
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import psutil
import logging
from datetime import datetime

# Initialize logging
logging.basicConfig(
    filename='edge_performance_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class EdgePerformanceMonitor:
    """
    A class to monitor and optimize edge computing performance.
    This class fetches metrics related to CPU, memory usage,
    and disk I/O and logs them for lifecycle management.
    """

    def __init__(self, interval=5):
        """
        Initializes the performance monitor with a specified interval.

        Args:
            interval (int): Time interval (in seconds) for monitoring performance.
        """
        self.interval = interval

    def log_performance_metrics(self):
        """
        Logs the current performance metrics including CPU, memory,
        and disk usage.
        """
        try:
            cpu_usage = psutil.cpu_percent(interval=None)
            memory_info = psutil.virtual_memory()
            disk_info = psutil.disk_usage('/')

            logging.info(f"CPU Usage: {cpu_usage}%")
            logging.info(f"Memory Usage: {memory_info.percent}% (Total: {memory_info.total}, Available: {memory_info.available})")
            logging.info(f"Disk Usage: {disk_info.percent}% (Total: {disk_info.total}, Used: {disk_info.used})")

        except Exception as e:
            logging.error(f"Error logging performance metrics: {e}")

    def optimize_performance(self):
        """
        Placeholder method to optimize performance based on metrics.
        Extend this method with performance optimization logic as needed.
        """
        # Example optimization logic can be added here
        logging.info("Optimization process is not yet implemented.")

    def run_monitoring(self):
        """
        Runs the performance monitoring loop indefinitely.
        """
        logging.info("Starting edge performance monitoring.")
        try:
            while True:
                self.log_performance_metrics()
                self.optimize_performance()
                time.sleep(self.interval)

        except KeyboardInterrupt:
            logging.info("Monitoring stopped by user.")
        except Exception as e:
            logging.error(f"Unexpected error occurred: {e}")


if __name__ == "__main__":
    monitor = EdgePerformanceMonitor(interval=5)  # Monitor every 5 seconds
    monitor.run_monitoring()
```
