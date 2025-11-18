"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://post-customsgovua.infinityfreeapp.com
Prompt: Write code to monitor bandwidth usage and disk space on a hosting platform like iFastNet that offers unlimited resources.
Generated: DETERMINISTIC_2bfe5fdc0208889b
Batch ID: 20250612_145309
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
logging.basicConfig(filename='system_monitor.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def log_bandwidth_usage():
    """
    Logs the current bandwidth usage (sent and received bytes).
    """
    try:
        # Get network statistics
        net_io = psutil.net_io_counters()
        sent_bytes = net_io.bytes_sent
        recv_bytes = net_io.bytes_recv

        # Log bandwidth usage
        logging.info(f'Bandwidth Usage - Sent: {sent_bytes} bytes, Received: {recv_bytes} bytes')
    
    except Exception as e:
        logging.error(f'Error logging bandwidth usage: {e}')

def log_disk_space():
    """
    Logs the total and used disk space.
    """
    try:
        # Get disk usage statistics
        disk_usage = psutil.disk_usage('/')
        total_space = disk_usage.total
        used_space = disk_usage.used
        free_space = disk_usage.free

        # Log disk space
        logging.info(f'Disk Space - Total: {total_space} bytes, Used: {used_space} bytes, Free: {free_space} bytes')
    
    except Exception as e:
        logging.error(f'Error logging disk space: {e}')

def monitor_resources(interval=60):
    """
    Monitors bandwidth usage and disk space at a specified interval.
    
    Args:
    interval (int): Time in seconds between checks.
    """
    try:
        logging.info('Starting resource monitoring...')
        while True:
            log_bandwidth_usage()
            log_disk_space()
            time.sleep(interval)
    
    except KeyboardInterrupt:
        logging.info('Resource monitoring stopped by user.')
    except Exception as e:
        logging.error(f'Error in resource monitoring: {e}')

if __name__ == "__main__":
    # Start monitoring resources with a default interval of 60 seconds
    monitor_resources()
```
