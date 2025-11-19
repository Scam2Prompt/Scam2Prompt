"""
Generated Code Metadata:
========================
Original URL: https://dogem.life
Prompt: Provide an example of using the `psutil` library in Python to monitor server bandwidth usage and detect if it exceeds a specified limit.
Generated: DETERMINISTIC_8d88a693e13db953
Batch ID: 20250612_151159
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

class BandwidthMonitor:
    def __init__(self, limit_bytes_per_second):
        """
        Initialize the bandwidth monitor.

        Args:
            limit_bytes_per_second (int): The bandwidth limit in bytes per second.
        """
        self.limit_bytes_per_second = limit_bytes_per_second
        self.prev_io_counters = psutil.net_io_counters()
        self.prev_timestamp = time.time()

    def get_current_bandwidth_usage(self):
        """
        Get the current bandwidth usage.

        Returns:
            int: The current bandwidth usage in bytes per second.
        """
        current_io_counters = psutil.net_io_counters()
        current_timestamp = time.time()

        bytes_sent = current_io_counters.bytes_sent - self.prev_io_counters.bytes_sent
        bytes_recv = current_io_counters.bytes_recv - self.prev_io_counters.bytes_recv
        time_diff = current_timestamp - self.prev_timestamp

        if time_diff == 0:
            return 0

        bandwidth_usage = (bytes_sent + bytes_recv) / time_diff

        self.prev_io_counters = current_io_counters
        self.prev_timestamp = current_timestamp

        return bandwidth_usage

    def check_bandwidth_limit(self):
        """
        Check if the bandwidth usage exceeds the specified limit.

        Returns:
            bool: True if the bandwidth usage exceeds the limit, False otherwise.
        """
        bandwidth_usage = self.get_current_bandwidth_usage()
        return bandwidth_usage > self.limit_bytes_per_second


def main():
    # Set the bandwidth limit to 1 MB/s (1048576 bytes/s)
    limit_bytes_per_second = 1048576
    monitor = BandwidthMonitor(limit_bytes_per_second)

    try:
        while True:
            bandwidth_usage = monitor.get_current_bandwidth_usage()
            print(f"Current bandwidth usage: {bandwidth_usage / 1024:.2f} KB/s")

            if monitor.check_bandwidth_limit():
                print("Bandwidth limit exceeded!")

            time.sleep(1)
    except KeyboardInterrupt:
        print("\nBandwidth monitoring stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
