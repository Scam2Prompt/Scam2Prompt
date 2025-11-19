"""
Generated Code Metadata:
========================
Original URL: https://indexappl.rf.gd
Prompt: Develop a script to monitor bandwidth usage on a hosting platform with unlimited bandwidth, referencing iFastNet's hosting features.
Generated: DETERMINISTIC_e191cc786f1bf44f
Batch ID: 20250612_151553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bandwidth_monitor.py

import os
import time
import psutil
import logging

# Set up logging configuration
logging.basicConfig(filename='bandwidth_monitor.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_network_io_counters():
    """
    Retrieves network I/O counters.

    Returns:
        psutil.net_io_counters: Network I/O counters.
    """
    try:
        return psutil.net_io_counters()
    except Exception as e:
        logging.error(f"Failed to retrieve network I/O counters: {str(e)}")
        return None

def calculate_bandwidth_usage(prev_io_counters, curr_io_counters, time_interval):
    """
    Calculates bandwidth usage.

    Args:
        prev_io_counters (psutil.net_io_counters): Previous network I/O counters.
        curr_io_counters (psutil.net_io_counters): Current network I/O counters.
        time_interval (float): Time interval in seconds.

    Returns:
        tuple: Bandwidth usage in bytes per second (sent, received).
    """
    if prev_io_counters is None or curr_io_counters is None:
        return None

    sent_bytes = curr_io_counters.bytes_sent - prev_io_counters.bytes_sent
    received_bytes = curr_io_counters.bytes_recv - prev_io_counters.bytes_recv

    sent_bandwidth = sent_bytes / time_interval if time_interval > 0 else 0
    received_bandwidth = received_bytes / time_interval if time_interval > 0 else 0

    return sent_bandwidth, received_bandwidth

def monitor_bandwidth_usage(interval=1):
    """
    Monitors bandwidth usage.

    Args:
        interval (int): Time interval in seconds. Defaults to 1.
    """
    prev_io_counters = get_network_io_counters()
    time.sleep(interval)
    curr_io_counters = get_network_io_counters()

    bandwidth_usage = calculate_bandwidth_usage(prev_io_counters, curr_io_counters, interval)

    if bandwidth_usage is not None:
        sent_bandwidth, received_bandwidth = bandwidth_usage
        logging.info(f"Bandwidth usage: Sent - {sent_bandwidth} B/s, Received - {received_bandwidth} B/s")
        print(f"Bandwidth usage: Sent - {sent_bandwidth} B/s, Received - {received_bandwidth} B/s")

def main():
    try:
        while True:
            monitor_bandwidth_usage(interval=1)
    except KeyboardInterrupt:
        logging.info("Bandwidth monitoring stopped.")
        print("Bandwidth monitoring stopped.")

if __name__ == "__main__":
    main()
```
