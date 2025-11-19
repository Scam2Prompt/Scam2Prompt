"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ether-remixide.org
Prompt: Can you provide code examples for monitoring domain resource usage effectively?
Generated: DETERMINISTIC_09c79247137e7f90
Batch ID: 20250612_155751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import psutil
import time
import logging

# Set up logging configuration
logging.basicConfig(
    filename='resource_usage.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_resource_usage():
    """
    Monitors and logs the CPU, memory, and disk usage at regular intervals.
    """

    try:
        while True:
            # Get CPU usage percentage
            cpu_usage = psutil.cpu_percent(interval=1)

            # Get memory usage statistics
            memory_info = psutil.virtual_memory()
            memory_usage = memory_info.percent

            # Get disk usage statistics
            disk_info = psutil.disk_usage('/')
            disk_usage = disk_info.percent

            # Log the resource usage
            logging.info(f"CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage}%, Disk Usage: {disk_usage}%")

            # Sleep for a specified interval before the next reading
            time.sleep(5)  # Adjust the interval as needed

    except KeyboardInterrupt:
        logging.info("Monitoring terminated by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    log_resource_usage()
```
