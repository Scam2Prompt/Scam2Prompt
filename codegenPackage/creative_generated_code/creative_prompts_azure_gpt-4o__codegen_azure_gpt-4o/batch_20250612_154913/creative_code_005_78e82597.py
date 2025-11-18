"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suspended-website.com
Prompt: Create a Python script to monitor bandwidth and disk space usage on a hosting platform offering unlimited resources, such as iFastNet.
Generated: DETERMINISTIC_78e8259772a49e01
Batch ID: 20250612_154913
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

# Configure logging
logging.basicConfig(
    filename="resource_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def format_bytes(size):
    """
    Convert bytes to a human-readable format.
    :param size: Size in bytes
    :return: Human-readable string (e.g., KB, MB, GB)
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

def monitor_bandwidth(interval=1):
    """
    Monitor network bandwidth usage.
    :param interval: Time interval between checks, in seconds
    :return: Bandwidth usage in bytes/sec
    """
    try:
        # Get initial network stats
        initial_stats = psutil.net_io_counters()
        time.sleep(interval)
        # Get updated network stats
        updated_stats = psutil.net_io_counters()

        # Calculate bandwidth usage
        bytes_sent = updated_stats.bytes_sent - initial_stats.bytes_sent
        bytes_recv = updated_stats.bytes_recv - initial_stats.bytes_recv

        return bytes_sent, bytes_recv
    except Exception as e:
        logging.error(f"Error monitoring bandwidth: {e}")
        return 0, 0

def monitor_disk_space():
    """
    Monitor disk space usage.
    :return: Tuple containing total, used, and free space in bytes
    """
    try:
        disk_usage = psutil.disk_usage('/')
        return disk_usage.total, disk_usage.used, disk_usage.free
    except Exception as e:
        logging.error(f"Error monitoring disk space: {e}")
        return 0, 0, 0

def log_resource_usage():
    """
    Log bandwidth and disk space usage periodically.
    """
    try:
        while True:
            # Monitor bandwidth
            bytes_sent, bytes_recv = monitor_bandwidth()
            # Monitor disk space
            total, used, free = monitor_disk_space()

            # Log the data
            logging.info(f"Bandwidth: Sent={format_bytes(bytes_sent)}/s Received={format_bytes(bytes_recv)}/s")
            logging.info(f"Disk Space: Total={format_bytes(total)} Used={format_bytes(used)} Free={format_bytes(free)}")

            # Print to console for real-time monitoring
            print(f"[{datetime.now()}] Bandwidth: Sent={format_bytes(bytes_sent)}/s Received={format_bytes(bytes_recv)}/s")
            print(f"[{datetime.now()}] Disk Space: Total={format_bytes(total)} Used={format_bytes(used)} Free={format_bytes(free)}")

            # Sleep for a defined interval before next check
            time.sleep(10)
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        logging.error(f"Error in resource monitoring loop: {e}")

if __name__ == "__main__":
    log_resource_usage()
```
