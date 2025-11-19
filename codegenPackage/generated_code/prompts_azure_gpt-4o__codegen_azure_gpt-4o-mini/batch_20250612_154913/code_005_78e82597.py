"""
Generated Code Metadata:
========================
Original URL: https://suspended-website.com
Prompt: Create a Python script to monitor bandwidth and disk space usage on a hosting platform offering unlimited resources, such as iFastNet.
Generated: DETERMINISTIC_78e8259772a49e01
Batch ID: 20250612_154913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import psutil
import time
import logging

# Configure logging
logging.basicConfig(
    filename='resource_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_bandwidth():
    """
    Check the current bandwidth usage.
    Returns the bytes sent and received since the last check.
    """
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

def check_disk_space():
    """
    Check the disk space usage.
    Returns the total, used, and free disk space in bytes.
    """
    disk_usage = psutil.disk_usage('/')
    return disk_usage.total, disk_usage.used, disk_usage.free

def log_resource_usage():
    """
    Log the current bandwidth and disk space usage.
    """
    try:
        # Get bandwidth usage
        bytes_sent, bytes_recv = check_bandwidth()
        logging.info(f'Bandwidth - Sent: {bytes_sent} bytes, Received: {bytes_recv} bytes')

        # Get disk space usage
        total, used, free = check_disk_space()
        logging.info(f'Disk Space - Total: {total} bytes, Used: {used} bytes, Free: {free} bytes')

    except Exception as e:
        logging.error(f'Error while logging resource usage: {e}')

def main():
    """
    Main function to monitor resources at regular intervals.
    """
    logging.info('Starting resource monitoring...')
    try:
        while True:
            log_resource_usage()
            time.sleep(60)  # Log every 60 seconds
    except KeyboardInterrupt:
        logging.info('Resource monitoring stopped by user.')
    except Exception as e:
        logging.error(f'Unexpected error: {e}')

if __name__ == '__main__':
    main()
```
