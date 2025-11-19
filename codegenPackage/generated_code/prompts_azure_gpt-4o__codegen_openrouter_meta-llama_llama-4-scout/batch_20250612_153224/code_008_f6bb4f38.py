"""
Generated Code Metadata:
========================
Original URL: https://unisonplus.vn
Prompt: Provide a Python implementation for monitoring and maintaining infrastructure systems, ensuring stability and efficiency as described by Unison Plus.
Generated: DETERMINISTIC_f6bb4f38f39ad71d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# infrastructure_monitor.py

import logging
import os
import psutil
import platform
import time
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InfrastructureMonitor:
    """
    A class used to monitor and maintain infrastructure systems.

    Attributes:
    ----------
    hostname : str
        The hostname of the machine being monitored.
    interval : int
        The interval in seconds between each monitoring check.

    Methods:
    -------
    get_system_info()
        Retrieves information about the system, including CPU, memory, and disk usage.
    check_cpu_usage()
        Checks the current CPU usage and logs a warning if it exceeds 80%.
    check_memory_usage()
        Checks the current memory usage and logs a warning if it exceeds 80%.
    check_disk_usage()
        Checks the current disk usage and logs a warning if it exceeds 80%.
    """

    def __init__(self, interval=60):
        """
        Initializes the InfrastructureMonitor class.

        Parameters:
        ----------
        interval : int, optional
            The interval in seconds between each monitoring check (default is 60).
        """
        self.hostname = platform.node()
        self.interval = interval

    def get_system_info(self):
        """
        Retrieves information about the system, including CPU, memory, and disk usage.

        Returns:
        -------
        dict
            A dictionary containing system information.
        """
        system_info = {
            'hostname': self.hostname,
            'platform': platform.system(),
            'platform-version': platform.version(),
            'architecture': platform.machine(),
            'processor': platform.processor(),
            'cpu-count': psutil.cpu_count(),
            'memory-total': psutil.virtual_memory().total / (1024.0 ** 3),
            'disk-total': psutil.disk_usage('/').total / (1024.0 ** 3),
        }
        return system_info

    def check_cpu_usage(self):
        """
        Checks the current CPU usage and logs a warning if it exceeds 80%.
        """
        cpu_usage = psutil.cpu_percent()
        if cpu_usage > 80:
            logging.warning(f'CPU usage is high: {cpu_usage}%')
        else:
            logging.info(f'CPU usage is normal: {cpu_usage}%')

    def check_memory_usage(self):
        """
        Checks the current memory usage and logs a warning if it exceeds 80%.
        """
        memory_usage = psutil.virtual_memory().percent
        if memory_usage > 80:
            logging.warning(f'Memory usage is high: {memory_usage}%')
        else:
            logging.info(f'Memory usage is normal: {memory_usage}%')

    def check_disk_usage(self):
        """
        Checks the current disk usage and logs a warning if it exceeds 80%.
        """
        disk_usage = psutil.disk_usage('/').percent
        if disk_usage > 80:
            logging.warning(f'Disk usage is high: {disk_usage}%')
        else:
            logging.info(f'Disk usage is normal: {disk_usage}%')

    def start_monitoring(self):
        """
        Starts the monitoring process.
        """
        try:
            logging.info('Starting infrastructure monitoring...')
            while True:
                system_info = self.get_system_info()
                logging.info(f'System Info: {system_info}')
                self.check_cpu_usage()
                self.check_memory_usage()
                self.check_disk_usage()
                time.sleep(self.interval)
        except KeyboardInterrupt:
            logging.info('Stopping infrastructure monitoring...')
        except Exception as e:
            logging.error(f'An error occurred: {e}')

if __name__ == '__main__':
    monitor = InfrastructureMonitor(interval=30)
    monitor.start_monitoring()
```
