"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberconnectit.com
Prompt: Write a Python script to monitor system health and perform basic troubleshooting for a small business, as described in CyberConnect's IT services.
Generated: DETERMINISTIC_a4dcc22370784a17
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import psutil
import platform
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class SystemHealthMonitor:
    """Class to monitor system health and perform basic troubleshooting."""

    def __init__(self):
        """Initialize the system health monitor."""
        self.system_info = self.get_system_info()

    def get_system_info(self):
        """Retrieve basic system information."""
        try:
            info = {
                "OS": platform.system(),
                "OS Version": platform.version(),
                "Architecture": platform.architecture(),
                "CPU Count": psutil.cpu_count(logical=True),
                "Memory": psutil.virtual_memory(),
                "Disk Usage": psutil.disk_usage('/'),
                "Network Stats": psutil.net_if_stats(),
            }
            logging.info("System info retrieved successfully.")
            return info
        except Exception as e:
            logging.error(f"Error retrieving system info: {e}")
            return {}

    def check_cpu_usage(self, threshold=80):
        """Check CPU usage percentage against a threshold."""
        usage = psutil.cpu_percent(interval=1)
        if usage > threshold:
            logging.warning(f"High CPU usage detected: {usage}%")
            return False
        logging.info(f"CPU usage is normal: {usage}%")
        return True

    def check_memory_usage(self, threshold=80):
        """Check memory usage percentage against a threshold."""
        usage = self.system_info['Memory'].percent
        if usage > threshold:
            logging.warning(f"High memory usage detected: {usage}%")
            return False
        logging.info(f"Memory usage is normal: {usage}%")
        return True

    def check_disk_usage(self, threshold=80):
        """Check disk usage percentage against a threshold."""
        usage = self.system_info['Disk Usage'].percent
        if usage > threshold:
            logging.warning(f"High disk usage detected: {usage}%")
            return False
        logging.info(f"Disk usage is normal: {usage}%")
        return True

    def perform_health_check(self):
        """Perform a complete health check of the system."""
        logging.info("Performing system health check...")
        cpu_check = self.check_cpu_usage()
        memory_check = self.check_memory_usage()
        disk_check = self.check_disk_usage()

        if cpu_check and memory_check and disk_check:
            logging.info("System health check passed.")
            return True
        else:
            logging.error("System health check failed.")
            return False

if __name__ == "__main__":
    monitor = SystemHealthMonitor()
    if not monitor.perform_health_check():
        logging.error("Troubleshooting may be required.")
    else:
        logging.info("System is operating normally.")
```
