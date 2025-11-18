"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claytonventuresnew.free.nf
Prompt: Create a Python script to monitor bandwidth usage on a hosting platform that advertises unlimited bandwidth and no daily hit limits.
Generated: DETERMINISTIC_679c2c05d1287fed
Batch ID: 20250612_151414
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
logging.basicConfig(filename='bandwidth_monitor.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class BandwidthMonitor:
    """Class to monitor and log bandwidth usage."""

    def __init__(self, interval=60):
        """
        Initialize the BandwidthMonitor.

        :param interval: Time interval in seconds between bandwidth checks.
        """
        self.interval = interval
        self.previous_bytes_sent = 0
        self.previous_bytes_recv = 0

    def get_bandwidth_usage(self):
        """
        Get the current bandwidth usage.

        :return: A tuple containing bytes sent and bytes received during the last interval.
        """
        # Get network I/O statistics
        net_io = psutil.net_io_counters()
        bytes_sent = net_io.bytes_sent
        bytes_recv = net_io.bytes_recv

        # Calculate bandwidth usage
        sent_usage = bytes_sent - self.previous_bytes_sent
        recv_usage = bytes_recv - self.previous_bytes_recv

        # Update previous values for the next check
        self.previous_bytes_sent = bytes_sent
        self.previous_bytes_recv = bytes_recv

        return sent_usage, recv_usage

    def log_usage(self):
        """Log the current bandwidth usage."""
        try:
            sent, recv = self.get_bandwidth_usage()
            logging.info(f"Bytes Sent: {sent}, Bytes Received: {recv}")
        except Exception as e:
            logging.error(f"Error retrieving bandwidth usage: {e}")

    def start_monitoring(self):
        """Start monitoring bandwidth usage at the specified interval."""
        logging.info("Starting bandwidth monitoring...")
        try:
            while True:
                self.log_usage()
                time.sleep(self.interval)
        except KeyboardInterrupt:
            logging.info("Bandwidth monitoring stopped by user.")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Main execution block
    monitor = BandwidthMonitor(interval=60)  # Set the monitoring interval to 60 seconds
    monitor.start_monitoring()
```
