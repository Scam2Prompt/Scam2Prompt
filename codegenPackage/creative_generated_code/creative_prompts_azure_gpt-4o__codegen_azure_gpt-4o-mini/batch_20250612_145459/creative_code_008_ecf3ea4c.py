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
import psutil
import time
import logging

# Configure logging
logging.basicConfig(
    filename='hosting_performance_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_bandwidth_usage():
    """
    Get the current bandwidth usage (bytes sent and received).
    
    Returns:
        dict: A dictionary containing bytes sent and received.
    """
    net_io = psutil.net_io_counters()
    return {
        'bytes_sent': net_io.bytes_sent,
        'bytes_recv': net_io.bytes_recv
    }

def get_disk_space_usage():
    """
    Get the current disk space usage.
    
    Returns:
        dict: A dictionary containing total, used, and free disk space in bytes.
    """
    disk_usage = psutil.disk_usage('/')
    return {
        'total': disk_usage.total,
        'used': disk_usage.used,
        'free': disk_usage.free
    }

def log_performance_metrics():
    """
    Log the hosting performance metrics for bandwidth and disk space usage.
    """
    try:
        bandwidth = get_bandwidth_usage()
        disk_space = get_disk_space_usage()

        logging.info('Bandwidth Usage: %s', bandwidth)
        logging.info('Disk Space Usage: %s', disk_space)

    except Exception as e:
        logging.error('Error while logging performance metrics: %s', e)

def main():
    """
    Main function to monitor and log performance metrics at a defined interval.
    """
    monitoring_interval = 60  # Interval in seconds

    try:
        while True:
            log_performance_metrics()
            time.sleep(monitoring_interval)

    except KeyboardInterrupt:
        logging.info('Monitoring stopped by user.')

if __name__ == '__main__':
    main()
```
