"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indexappl.rf.gd
Prompt: Develop a script to monitor bandwidth usage on a hosting platform with unlimited bandwidth, referencing iFastNet's hosting features.
Generated: DETERMINISTIC_e191cc786f1bf44f
Batch ID: 20250612_151553
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

# Configure logging for bandwidth monitoring
logging.basicConfig(
    filename='bandwidth_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_bandwidth_usage(previous_stats):
    """
    Get the current bandwidth usage since the last check.
    
    :param previous_stats: A tuple of previous network I/O stats
    :return: A tuple containing bytes sent and received
    """
    current_stats = psutil.net_io_counters()
    bytes_sent = current_stats.bytes_sent - previous_stats.bytes_sent
    bytes_recv = current_stats.bytes_recv - previous_stats.bytes_recv
    return bytes_sent, bytes_recv

def monitor_bandwidth(interval=60):
    """
    Monitor the bandwidth usage every specified interval.
    
    :param interval: Time in seconds to wait between checks
    """
    try:
        # Initial network I/O stats
        previous_stats = psutil.net_io_counters()
        logging.info("Starting bandwidth monitoring...")

        while True:
            time.sleep(interval)  # Wait for the specified interval
            bytes_sent, bytes_recv = get_bandwidth_usage(previous_stats)
            previous_stats = psutil.net_io_counters()  # Update previous stats

            # Log the bandwidth usage
            logging.info(f"Bandwidth Usage - Sent: {bytes_sent} bytes, Received: {bytes_recv} bytes")

    except KeyboardInterrupt:
        logging.info("Bandwidth monitoring stopped by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    monitor_bandwidth()
```
