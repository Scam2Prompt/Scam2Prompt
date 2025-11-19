"""
Generated Code Metadata:
========================
Original URL: https://deeper-net.works
Prompt: Generate code to monitor bandwidth utilization without throttling, inspired by Deeper Network's "Zero Speed Impact" feature.
Generated: DETERMINISTIC_f1569eca68dcfc46
Batch ID: 20250612_154049
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
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BandwidthMonitor:
    def __init__(self, interval=1):
        """
        Initializes the BandwidthMonitor with a specified interval.

        :param interval: Time in seconds between bandwidth checks (default is 1 second)
        """
        self.interval = interval
        self.previous_bytes_sent = 0
        self.previous_bytes_recv = 0

    def get_bandwidth_usage(self):
        """
        Retrieves the current bandwidth usage.

        :return: A tuple containing bytes sent and bytes received since the last check
        """
        net_io = psutil.net_io_counters()
        bytes_sent = net_io.bytes_sent
        bytes_recv = net_io.bytes_recv

        # Calculate the difference in bytes sent and received
        sent_diff = bytes_sent - self.previous_bytes_sent
        recv_diff = bytes_recv - self.previous_bytes_recv

        # Update previous values for the next check
        self.previous_bytes_sent = bytes_sent
        self.previous_bytes_recv = bytes_recv

        return sent_diff, recv_diff

    def monitor(self):
        """
        Continuously monitors bandwidth usage and logs the results.
        """
        logging.info("Starting bandwidth monitoring...")
        try:
            while True:
                sent, recv = self.get_bandwidth_usage()
                logging.info(f"Bandwidth Usage - Sent: {sent} bytes, Received: {recv} bytes")
                time.sleep(self.interval)
        except KeyboardInterrupt:
            logging.info("Bandwidth monitoring stopped by user.")
        except Exception as e:
            logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    # Create a BandwidthMonitor instance and start monitoring
    monitor = BandwidthMonitor(interval=1)
    monitor.monitor()
```
