"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deeper-net.works
Prompt: Generate code to monitor bandwidth utilization without throttling, inspired by Deeper Network's "Zero Speed Impact" feature.
Generated: DETERMINISTIC_f1569eca68dcfc46
Batch ID: 20250612_154049
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
from datetime import datetime

class BandwidthMonitor:
    """
    A class to monitor bandwidth utilization without throttling.
    Inspired by "Zero Speed Impact" feature of Deeper Network.
    """

    def __init__(self, interval=1):
        """
        Initializes the BandwidthMonitor.

        :param interval: Time interval (in seconds) to check bandwidth usage.
        """
        self.interval = interval
        self.last_sent = 0
        self.last_received = 0

    def get_network_stats(self):
        """
        Retrieves current network utilization stats.

        :return: A tuple (bytes_sent, bytes_recv)
        """
        network_io = psutil.net_io_counters()
        return network_io.bytes_sent, network_io.bytes_recv

    def calculate_bandwidth_usage(self):
        """
        Calculates bandwidth usage based on the difference in sent/received bytes.

        :return: A dictionary containing bandwidth usage in bytes per second.
        """
        current_sent, current_recv = self.get_network_stats()

        # Calculate differences
        sent_diff = current_sent - self.last_sent
        recv_diff = current_recv - self.last_received

        # Update last values
        self.last_sent = current_sent
        self.last_received = current_recv

        # Bandwidth usage per second
        return {
            "upload_speed": sent_diff / self.interval,
            "download_speed": recv_diff / self.interval
        }

    def monitor_bandwidth(self):
        """
        Continuously monitors bandwidth utilization.
        """
        print("Monitoring bandwidth usage. Press Ctrl+C to stop.")
        try:
            # Initialize last values
            self.last_sent, self.last_received = self.get_network_stats()
            while True:
                time.sleep(self.interval)
                bandwidth_usage = self.calculate_bandwidth_usage()
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - "
                      f"Upload: {bandwidth_usage['upload_speed']:.2f} bytes/s, "
                      f"Download: {bandwidth_usage['download_speed']:.2f} bytes/s")
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Create an instance of BandwidthMonitor with a 1-second interval
    monitor = BandwidthMonitor(interval=1)
    monitor.monitor_bandwidth()
```
