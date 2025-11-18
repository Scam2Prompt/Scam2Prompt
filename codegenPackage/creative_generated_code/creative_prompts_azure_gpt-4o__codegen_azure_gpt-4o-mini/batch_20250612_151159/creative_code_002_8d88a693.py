"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogem.life
Prompt: Provide an example of using the `psutil` library in Python to monitor server bandwidth usage and detect if it exceeds a specified limit.
Generated: DETERMINISTIC_8d88a693e13db953
Batch ID: 20250612_151159
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

# Set up logging for monitoring output
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BandwidthMonitor:
    def __init__(self, limit: float):
        """
        Initialize the BandwidthMonitor with a specified limit.

        :param limit: The bandwidth usage limit in bytes per second.
        """
        self.limit = limit

    def get_bandwidth_usage(self):
        """
        Retrieve the current bandwidth usage.

        :return: The current bandwidth usage in bytes per second.
        """
        net_io = psutil.net_io_counters()
        return net_io.bytes_sent + net_io.bytes_recv

    def monitor(self):
        """
        Continuously monitor the bandwidth usage and check if it exceeds the specified limit.
        """
        # Record the initial bandwidth usage
        initial_usage = self.get_bandwidth_usage()
        time.sleep(1)  # Wait for a second to get a more accurate reading
        current_usage = self.get_bandwidth_usage()

        # Calculate the bandwidth usage over the last second
        bandwidth_usage = current_usage - initial_usage

        if bandwidth_usage > self.limit:
            logging.warning(f"Bandwidth usage exceeded limit! Current usage: {bandwidth_usage} bytes/s, Limit: {self.limit} bytes/s")
        else:
            logging.info(f"Bandwidth usage: {bandwidth_usage} bytes/s, within limit.")

def main():
    # Set the bandwidth limit (e.g., 1 MB/s = 1024 * 1024 bytes/s)
    bandwidth_limit = 1024 * 1024  # 1 MB/s

    # Create an instance of BandwidthMonitor
    monitor = BandwidthMonitor(bandwidth_limit)

    try:
        while True:
            monitor.monitor()
            time.sleep(1)  # Check every second
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
