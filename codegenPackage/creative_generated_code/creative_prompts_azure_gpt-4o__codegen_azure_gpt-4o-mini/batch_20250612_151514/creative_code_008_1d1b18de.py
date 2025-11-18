"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallets-update.rf.gd
Prompt: Recommend tools or libraries for monitoring server performance on a hosting platform with unlimited bandwidth and no daily hit limits.
Generated: DETERMINISTIC_1d1b18de2b9abf9d
Batch ID: 20250612_151514
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
from datetime import datetime

# Configure logging to record server performance data
logging.basicConfig(
    filename='server_performance.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_server_performance():
    """
    Logs the server performance metrics including CPU usage,
    memory usage, disk usage, and network stats.
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
            # Get network statistics
            network_info = psutil.net_io_counters()
            bytes_sent = network_info.bytes_sent
            bytes_recv = network_info.bytes_recv

            # Log the collected metrics
            logging.info(
                f"CPU Usage: {cpu_usage}%, "
                f"Memory Usage: {memory_usage}%, "
                f"Disk Usage: {disk_usage}%, "
                f"Bytes Sent: {bytes_sent}, "
                f"Bytes Received: {bytes_recv}"
            )

            # Sleep for 5 seconds before the next log
            time.sleep(5)

    except Exception as e:
        logging.error(f"An error occurred while logging server performance: {e}")

if __name__ == "__main__":
    log_server_performance()
```
