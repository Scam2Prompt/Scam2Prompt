"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisonplus.vn
Prompt: Provide a Python implementation for monitoring and maintaining infrastructure systems, ensuring stability and efficiency as described by Unison Plus.
Generated: DETERMINISTIC_f6bb4f38f39ad71d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Infrastructure Monitoring and Maintenance System

This Python script is designed to monitor and maintain infrastructure systems
ensuring stability and efficiency as described by Unison Plus. It includes
metrics collection, alerting, and automated maintenance tasks.
"""

import logging
import psutil
import time
from typing import List, Dict

# Configure logging for monitoring and maintenance activities
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="infra_monitoring.log"
)

class InfrastructureMonitor:
    """
    A class to monitor system health metrics and maintain infrastructure stability.
    """

    def __init__(self, check_interval: int = 10):
        """
        Initialize the infrastructure monitor with a check interval.

        Args:
            check_interval (int): Time interval (in seconds) between health checks.
        """
        self.check_interval = check_interval

    def get_system_metrics(self) -> Dict[str, float]:
        """
        Collect system health metrics using the psutil library.

        Returns:
            dict: A dictionary containing CPU usage, memory usage, and disk usage.
        """
        try:
            metrics = {
                "cpu_usage": psutil.cpu_percent(interval=1),
                "memory_usage": psutil.virtual_memory().percent,
                "disk_usage": psutil.disk_usage('/').percent
            }
            return metrics
        except Exception as e:
            logging.error(f"Error collecting system metrics: {e}")
            return {"cpu_usage": -1, "memory_usage": -1, "disk_usage": -1}

    def log_and_alert(self, metrics: Dict[str, float]):
        """
        Log system metrics and alert if any metric exceeds thresholds.

        Args:
            metrics (dict): A dictionary containing system health metrics.
        """
        try:
            logging.info(f"System Metrics: {metrics}")
            if metrics["cpu_usage"] > 80:
                logging.warning("High CPU usage detected! Take action.")
            if metrics["memory_usage"] > 85:
                logging.warning("High memory usage detected! Take action.")
            if metrics["disk_usage"] > 90:
                logging.warning("High disk usage detected! Take action.")
        except Exception as e:
            logging.error(f"Error during logging and alerting: {e}")

    def maintain_system_stability(self):
        """
        Perform automated maintenance tasks to ensure system stability.
        """
        try:
            # Example maintenance tasks
            logging.info("Performing system maintenance tasks...")
            # Placeholder for actual maintenance logic
            time.sleep(2)  # Simulate maintenance task duration
            logging.info("System maintenance tasks completed.")
        except Exception as e:
            logging.error(f"Error during maintenance tasks: {e}")

    def monitor(self):
        """
        Start monitoring infrastructure systems in intervals.
        """
        try:
            logging.info("Starting infrastructure monitoring...")
            while True:
                metrics = self.get_system_metrics()
                self.log_and_alert(metrics)
                self.maintain_system_stability()
                time.sleep(self.check_interval)
        except KeyboardInterrupt:
            logging.info("Monitoring stopped by user.")
        except Exception as e:
            logging.error(f"Unexpected error during monitoring: {e}")

if __name__ == "__main__":
    # Set up the monitoring system with a check interval of 10 seconds
    monitor = InfrastructureMonitor(check_interval=10)
    monitor.monitor()
```
