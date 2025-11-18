"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea-nftclaim.free.nf
Prompt: Develop a Python-based monitoring tool for tracking bandwidth usage on a hosting service with unlimited bandwidth and no daily hit limits, such as iFastNet hosting.
Generated: DETERMINISTIC_c2e4d68a61eb7c92
Batch ID: 20250612_145213
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
logging.basicConfig(filename='bandwidth_monitor.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class BandwidthMonitor:
    """
    A class to monitor and log the bandwidth usage of the system.
    """

    def __init__(self, interval=10):
        """
        Initializes the BandwidthMonitor.

        :param interval: Time interval (in seconds) between bandwidth checks.
        """
        self.interval = interval
        self.previous_bytes = self.get_total_bytes()

    def get_total_bytes(self):
        """
        Returns the total number of bytes sent and received.

        :return: Tuple of (bytes_sent, bytes_received)
        """
        net_io = psutil.net_io_counters()
        return net_io.bytes_sent, net_io.bytes_recv

    def calculate_bandwidth_usage(self):
        """
        Calculates the bandwidth usage since the last check.

        :return: Tuple of (sent_bytes, received_bytes)
        """
        current_bytes = self.get_total_bytes()
        sent_bytes = current_bytes[0] - self.previous_bytes[0]
        received_bytes = current_bytes[1] - self.previous_bytes[1]
        self.previous_bytes = current_bytes
        return sent_bytes, received_bytes

    def log_usage(self):
        """
        Logs the current bandwidth usage to a file.
        """
        try:
            sent_bytes, received_bytes = self.calculate_bandwidth_usage()
            logging.info(f"Sent: {sent_bytes} bytes, Received: {received_bytes} bytes")
        except Exception as e:
            logging.error(f"Error logging bandwidth usage: {str(e)}")

    def start_monitoring(self):
        """
        Starts the bandwidth monitoring process.
        """
        logging.info("Starting bandwidth monitoring...")
        try:
            while True:
                self.log_usage()
                time.sleep(self.interval)
        except KeyboardInterrupt:
            logging.info("Bandwidth monitoring stopped by user.")
        except Exception as e:
            logging.error(f"Unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    # Create an instance of BandwidthMonitor and start monitoring
    monitor = BandwidthMonitor(interval=10)
    monitor.start_monitoring()
```
