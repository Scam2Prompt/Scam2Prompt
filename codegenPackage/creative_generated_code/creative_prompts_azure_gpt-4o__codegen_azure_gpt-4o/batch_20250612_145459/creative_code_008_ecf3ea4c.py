"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethtransaction.ezyro.com
Prompt: Write a Python script to monitor hosting performance metrics (e.g., bandwidth usage and disk space) for a provider with no daily limits, like iFastNet.
Generated: DETERMINISTIC_ecf3ea4ce93bce57
Batch ID: 20250612_145459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import psutil
import logging
import time
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='hosting_performance.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_disk_usage(path="/"):
    """
    Get disk usage statistics for the specified path.
    :param path: Path to monitor (default is root "/").
    :return: A dictionary with total, used, and free space in bytes.
    """
    try:
        total, used, free = shutil.disk_usage(path)
        return {"total": total, "used": used, "free": free}
    except Exception as e:
        logging.error(f"Error getting disk usage: {e}")
        return None

def get_bandwidth_usage():
    """
    Get network bandwidth statistics.
    :return: A dictionary with bytes sent and received.
    """
    try:
        net_io = psutil.net_io_counters()
        return {"bytes_sent": net_io.bytes_sent, "bytes_received": net_io.bytes_recv}
    except Exception as e:
        logging.error(f"Error getting bandwidth usage: {e}")
        return None

def format_bytes(size):
    """
    Convert bytes into a human-readable format.
    :param size: Size in bytes.
    :return: Human-readable string representation (e.g., KB, MB, GB).
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

def log_metrics(disk_stats, bandwidth_stats):
    """
    Log performance metrics to a file.
    :param disk_stats: Disk usage statistics.
    :param bandwidth_stats: Bandwidth usage statistics.
    """
    try:
        if disk_stats:
            logging.info(
                f"Disk Usage -> Total: {format_bytes(disk_stats['total'])}, "
                f"Used: {format_bytes(disk_stats['used'])}, "
                f"Free: {format_bytes(disk_stats['free'])}"
            )
        if bandwidth_stats:
            logging.info(
                f"Bandwidth Usage -> Sent: {format_bytes(bandwidth_stats['bytes_sent'])}, "
                f"Received: {format_bytes(bandwidth_stats['bytes_received'])}"
            )
    except Exception as e:
        logging.error(f"Error logging metrics: {e}")

def monitor_hosting_performance(interval_seconds=60):
    """
    Monitor hosting performance metrics at regular intervals.
    :param interval_seconds: Time interval between metrics collection in seconds.
    """
    logging.info("Starting hosting performance monitoring...")
    try:
        while True:
            disk_stats = get_disk_usage()
            bandwidth_stats = get_bandwidth_usage()
            log_metrics(disk_stats, bandwidth_stats)
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        logging.info("Performance monitoring stopped by user.")
    except Exception as e:
        logging.error(f"Unexpected error during monitoring: {e}")

if __name__ == "__main__":
    # Run the monitoring function with a default interval of 60 seconds.
    monitor_hosting_performance(interval_seconds=60)
```
