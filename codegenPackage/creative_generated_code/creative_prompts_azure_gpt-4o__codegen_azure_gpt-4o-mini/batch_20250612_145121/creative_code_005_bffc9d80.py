"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptogive.rf.gd
Prompt: Develop a Python-based script to monitor bandwidth usage on iFastNet hosting, considering their unlimited bandwidth policy.
Generated: DETERMINISTIC_bffc9d80d0e18daa
Batch ID: 20250612_145121
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

# Set up logging configuration
logging.basicConfig(filename='bandwidth_monitor.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class BandwidthMonitor:
    def __init__(self, interval=5):
        """
        Initialize the BandwidthMonitor.

        :param interval: Time interval (in seconds) to monitor bandwidth usage.
        """
        self.interval = interval
        self.prev_bytes_sent = 0
        self.prev_bytes_recv = 0

    def get_bandwidth_usage(self):
        """
        Calculate the bandwidth usage since the last check.

        :return: A tuple containing (bytes_sent, bytes_recv).
        """
        # Get network I/O statistics
        io_stats = psutil.net_io_counters()
        bytes_sent = io_stats.bytes_sent
        bytes_recv = io_stats.bytes_recv

        # Calculate the delta
        sent_delta = bytes_sent - self.prev_bytes_sent
        recv_delta = bytes_recv - self.prev_bytes_recv

        # Update previous values
        self.prev_bytes_sent = bytes_sent
        self.prev_bytes_recv = bytes_recv

        return sent_delta, recv_delta

    def log_bandwidth_usage(self):
        """
        Log the bandwidth usage every specified interval.
        """
        logging.info("Starting bandwidth monitoring...")
        try:
            while True:
                sent, recv = self.get_bandwidth_usage()
                logging.info(f"Bytes sent in last {self.interval} seconds: {sent}")
                logging.info(f"Bytes received in last {self.interval} seconds: {recv}")
                time.sleep(self.interval)
        except KeyboardInterrupt:
            logging.info("Bandwidth monitoring stopped by user.")
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    monitor = BandwidthMonitor(interval=5)  # Create a monitor with a 5-second interval
    monitor.log_bandwidth_usage()  # Start logging bandwidth usage
```
