"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-promo.net
Prompt: Recommend APIs or libraries for monitoring server performance on Xserver hosting platforms.
Generated: DETERMINISTIC_ed4ae6ca7340a87a
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Monitoring server performance on Xserver hosting platforms using Python.

This script demonstrates how to use the 'psutil' library to monitor server performance,
such as CPU usage, memory usage, disk I/O, and network statistics. psutil is a cross-platform
library for system monitoring and management.

Requirements:
- Python 3.x
- psutil library (install with `pip install psutil`)
"""

import psutil
import logging
from time import sleep

# Configure logging for monitoring output
logging.basicConfig(
    filename="server_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_cpu_usage():
    """Log the current CPU usage percentage."""
    try:
        cpu_percent = psutil.cpu_percent(interval=1)  # CPU usage percentage
        logging.info(f"CPU Usage: {cpu_percent}%")
    except Exception as e:
        logging.error(f"Failed to fetch CPU usage: {e}")

def log_memory_usage():
    """Log the current memory usage stats."""
    try:
        memory_info = psutil.virtual_memory()  # Memory usage stats
        logging.info(
            f"Memory Usage: {memory_info.percent}% (Used: {memory_info.used / (1024 ** 2):.2f} MB | Total: {memory_info.total / (1024 ** 2):.2f} MB)"
        )
    except Exception as e:
        logging.error(f"Failed to fetch memory usage: {e}")

def log_disk_usage():
    """Log the current disk usage stats."""
    try:
        disk_info = psutil.disk_usage('/')  # Disk usage stats for root directory
        logging.info(
            f"Disk Usage: {disk_info.percent}% (Used: {disk_info.used / (1024 ** 3):.2f} GB | Total: {disk_info.total / (1024 ** 3):.2f} GB)"
        )
    except Exception as e:
        logging.error(f"Failed to fetch disk usage: {e}")

def log_network_stats():
    """Log the current network I/O stats."""
    try:
        net_io = psutil.net_io_counters()  # Network I/O stats
        logging.info(
            f"Network I/O - Sent: {net_io.bytes_sent / (1024 ** 2):.2f} MB | Received: {net_io.bytes_recv / (1024 ** 2):.2f} MB"
        )
    except Exception as e:
        logging.error(f"Failed to fetch network stats: {e}")

def monitor_server(interval=5):
    """
    Continuously monitor server performance at specified intervals.

    Args:
        interval (int): Time interval (in seconds) between each monitoring cycle.
    """
    logging.info("Starting server performance monitoring...")
    try:
        while True:
            log_cpu_usage()
            log_memory_usage()
            log_disk_usage()
            log_network_stats()
            sleep(interval)  # Wait before the next monitoring cycle
    except KeyboardInterrupt:
        logging.info("Stopping server performance monitoring.")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    # Start monitoring with a 5-second interval
    monitor_server(interval=5)
```
