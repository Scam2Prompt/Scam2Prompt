"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hubfix.rf.gd
Prompt: Write a Python script to monitor bandwidth usage on a hosting service that provides unlimited bandwidth and supports Python apps, as described on iFastNet.
Generated: DETERMINISTIC_4d3f2725683675c5
Batch ID: 20250612_154236
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
logging.basicConfig(filename='bandwidth_monitor.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class BandwidthMonitor:
    """A class to monitor and log bandwidth usage."""

    def __init__(self, interval=5):
        """
        Initializes the BandwidthMonitor instance.

        :param interval: Time in seconds between checks, default is 5 seconds.
        """
        self.interval = interval
        self.last_bytes_sent = 0
        self.last_bytes_recv = 0

    def get_network_io(self):
        """
        Retrieve the current network I/O statistics.

        :return: A dictionary containing bytes sent and received.
        """
        try:
            net_io = psutil.net_io_counters()
            return {
                'bytes_sent': net_io.bytes_sent,
                'bytes_recv': net_io.bytes_recv
            }
        except Exception as e:
            logging.error(f"Error retrieving network I/O: {e}")
            return None

    def log_bandwidth_usage(self):
        """
        Log bandwidth usage at regular intervals.
        """
        while True:
            net_io = self.get_network_io()
            if net_io is None:
                continue

            # Calculate usage for the interval
            bytes_sent = net_io['bytes_sent']
            bytes_recv = net_io['bytes_recv']

            sent_diff = bytes_sent - self.last_bytes_sent
            recv_diff = bytes_recv - self.last_bytes_recv

            # Log the data
            logging.info(f'Bandwidth Usage - Sent: {sent_diff / 1024:.2f} KB, '
                         f'Received: {recv_diff / 1024:.2f} KB')

            # Update last values for the next iteration
            self.last_bytes_sent = bytes_sent
            self.last_bytes_recv = bytes_recv

            # Wait for the next interval
            time.sleep(self.interval)

if __name__ == "__main__":
    monitor = BandwidthMonitor(interval=5)  # Change interval as needed
    try:
        monitor.log_bandwidth_usage()
    except KeyboardInterrupt:
        logging.info("Bandwidth monitoring stopped by user.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
```
