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
import psutil
import logging
import time
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='infrastructure_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class InfrastructureMonitor:
    def __init__(self, check_interval=60):
        """
        Initialize the InfrastructureMonitor with a specified check interval.
        
        :param check_interval: Time in seconds between checks.
        """
        self.check_interval = check_interval

    def log_system_metrics(self):
        """
        Log the system metrics such as CPU usage, memory usage, and disk usage.
        """
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()
            disk_info = psutil.disk_usage('/')

            logging.info(f'CPU Usage: {cpu_usage}%')
            logging.info(f'Memory Usage: {memory_info.percent}% (Total: {memory_info.total}, Available: {memory_info.available})')
            logging.info(f'Disk Usage: {disk_info.percent}% (Total: {disk_info.total}, Used: {disk_info.used})')
            
        except Exception as e:
            logging.error(f'Failed to log system metrics: {e}')

    def monitor(self):
        """
        Continuously monitor the system metrics at the defined interval.
        """
        logging.info("Starting infrastructure monitoring...")
        while True:
            self.log_system_metrics()
            time.sleep(self.check_interval)

if __name__ == "__main__":
    try:
        monitor = InfrastructureMonitor(check_interval=60)  # Set check interval to 60 seconds
        monitor.monitor()
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        logging.error(f'An error occurred: {e}')
```
