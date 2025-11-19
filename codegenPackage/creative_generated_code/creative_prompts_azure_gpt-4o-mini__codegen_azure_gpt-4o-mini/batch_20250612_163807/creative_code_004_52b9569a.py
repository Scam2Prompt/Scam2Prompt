"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantaxbonk.network
Prompt: How can I implement monitoring for bandwidth usage to avoid exceeding limits on my server?
Generated: DETERMINISTIC_52b9569aaaeebe2e
Batch ID: 20250612_163807
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
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BandwidthMonitor:
    def __init__(self, limit_mb_per_sec, check_interval=1):
        """
        Initialize the bandwidth monitor.

        :param limit_mb_per_sec: Maximum allowed bandwidth in megabytes per second.
        :param check_interval: Time interval (in seconds) to check the bandwidth.
        """
        self.limit_bytes_per_sec = limit_mb_per_sec * 1024 * 1024  # Convert MB to bytes
        self.check_interval = check_interval
        self.prev_received = 0
        self.prev_sent = 0

    def get_bandwidth_usage(self):
        """
        Get the current bandwidth usage for the server.

        :return: A tuple of (incoming bandwidth, outgoing bandwidth) in bytes per second.
        """
        net_io = psutil.net_io_counters()
        received = net_io.bytes_recv
        sent = net_io.bytes_sent
        incoming_bandwidth = (received - self.prev_received) / self.check_interval
        outgoing_bandwidth = (sent - self.prev_sent) / self.check_interval
        
        # Update previous values
        self.prev_received = received
        self.prev_sent = sent

        return incoming_bandwidth, outgoing_bandwidth

    def check_bandwidth(self):
        """
        Continuously monitor the bandwidth and log if it exceeds the limit.
        """
        try:
            while True:
                incoming, outgoing = self.get_bandwidth_usage()
                logging.info(f'Incoming: {incoming / (1024 * 1024):.2f} MB/s, Outgoing: {outgoing / (1024 * 1024):.2f} MB/s')

                if incoming > self.limit_bytes_per_sec:
                    logging.warning(f'Incoming bandwidth limit exceeded: {incoming / (1024 * 1024):.2f} MB/s')

                if outgoing > self.limit_bytes_per_sec:
                    logging.warning(f'Outgoing bandwidth limit exceeded: {outgoing / (1024 * 1024):.2f} MB/s')

                time.sleep(self.check_interval)

        except Exception as e:
            logging.error(f'An error occurred: {e}')

if __name__ == "__main__":
    # Set bandwidth limit to 10 MB/s and check every second
    monitor = BandwidthMonitor(limit_mb_per_sec=10)
    monitor.check_bandwidth()
```
