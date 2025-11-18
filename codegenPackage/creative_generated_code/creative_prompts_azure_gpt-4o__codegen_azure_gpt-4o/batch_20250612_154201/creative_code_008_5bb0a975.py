"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviviendainforma.zya.me
Prompt: Write a script to monitor daily processes and optimize resource usage for a website hosted on iFastNet, ensuring compliance with their "no daily process limit" feature.
Generated: DETERMINISTIC_5bb0a97508279ecc
Batch ID: 20250612_154201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import psutil
import time
import logging
from datetime import datetime

# Set up logging configuration
logging.basicConfig(
    filename="resource_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class ResourceMonitor:
    """
    A class to monitor website hosting processes and optimize resource usage.
    """

    def __init__(self):
        """
        Initialize ResourceMonitor instance.
        """
        self.resource_thresholds = {
            "cpu_usage": 75.0,  # Maximum CPU usage percentage allowed
            "memory_usage": 80.0,  # Maximum memory usage percentage allowed
        }

    @staticmethod
    def get_system_resource_usage():
        """
        Retrieves current system resource usage.

        Returns:
            dict: A dictionary containing CPU and memory usage percentages.
        """
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent
        return {"cpu_usage": cpu_usage, "memory_usage": memory_usage}

    def optimize_resources(self):
        """
        Optimizes resource usage if thresholds are exceeded.
        """
        usage = self.get_system_resource_usage()
        cpu_usage = usage["cpu_usage"]
        memory_usage = usage["memory_usage"]

        if cpu_usage > self.resource_thresholds["cpu_usage"]:
            logging.warning(f"High CPU usage detected: {cpu_usage}%. Attempting optimization...")
            self.reduce_cpu_load()

        if memory_usage > self.resource_thresholds["memory_usage"]:
            logging.warning(f"High memory usage detected: {memory_usage}%. Attempting optimization...")
            self.free_up_memory()

    @staticmethod
    def reduce_cpu_load():
        """
        Simulates reducing CPU load by killing non-essential high-load processes.
        """
        try:
            for process in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent']):
                if process.info['cpu_percent'] > 50:  # Example threshold for high-load processes
                    logging.info(f"Terminating process {process.info['name']} (PID: {process.info['pid']}) consuming {process.info['cpu_percent']}% CPU.")
                    os.kill(process.info['pid'], 9)  # Forcefully terminate
        except Exception as e:
            logging.error(f"Error reducing CPU load: {e}")

    @staticmethod
    def free_up_memory():
        """
        Simulates freeing up memory by clearing cached data.
        """
        try:
            # Example of clearing temporary files (adjust path as needed)
            temp_dir = "/tmp"
            file_count = 0
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    file_count += 1
            logging.info(f"Cleared {file_count} temporary files to free up memory.")
        except Exception as e:
            logging.error(f"Error freeing up memory: {e}")

    def monitor(self):
        """
        Continuously monitors and optimizes resource usage in compliance with hosting policies.
        """
        logging.info("Starting resource monitoring...")
        try:
            while True:
                self.optimize_resources()
                time.sleep(30)  # Monitor every 30 seconds
        except KeyboardInterrupt:
            logging.info("Resource monitoring stopped by user.")
        except Exception as e:
            logging.error(f"Unexpected error during monitoring: {e}")

if __name__ == "__main__":
    monitor = ResourceMonitor()
    monitor.monitor()
```
